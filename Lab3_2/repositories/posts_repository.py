import aiohttp
from datetime import datetime, timedelta
from typing import List
from domains.posts import Post, Comment
from repositories.iposts_repository import IPostsRepository
from utils import consts

class PostsRepository(IPostsRepository):
    def __init__(self):
        self.posts_db = []  # "baza danych" w pamięci

    async def fetch_posts_and_comments(self) -> List[Post]:
        async with aiohttp.ClientSession() as session:
            async with session.get(consts.API_POSTS_URL) as posts_response:
                posts_data = await posts_response.json()

            async with session.get(consts.API_COMMENTS_URL) as comments_response:
                comments_data = await comments_response.json()

        comments_dict = {}
        for comment in comments_data:
            post_id = comment['postId']
            if post_id not in comments_dict:
                comments_dict[post_id] = []
            comments_dict[post_id].append(Comment(**comment))

        self.posts_db = [
            Post(**post, comments=comments_dict.get(post['id'], []))
            for post in posts_data
        ]
        return self.posts_db

    async def filter_posts(self, query: str) -> List[Post]:
        filtered_posts = [
            post for post in self.posts_db
            if query.lower() in post.title.lower() or
               query.lower() in post.body.lower() or
               any(query.lower() in comment.body.lower() or query.lower() in comment.name.lower() for comment in post.comments)
        ]
        return filtered_posts

    async def clear_inactive_records(self, threshold_seconds: int) -> None:
        now = datetime.utcnow()
        threshold_time = now - timedelta(seconds=threshold_seconds)
        self.posts_db = [post for post in self.posts_db if post.last_accessed >= threshold_time]
        for post in self.posts_db:
            post.comments = [comment for comment in post.comments if comment.last_accessed >= threshold_time]

    async def sort_posts_by_last_accessed(self) -> List[Post]:
        return sorted(self.posts_db, key=lambda post: post.last_accessed, reverse=True)
