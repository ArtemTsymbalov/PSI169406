# services/posts_service.py
from typing import List
from repositories.posts_repository import PostRepository
from domains.posts import PostRecord

class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    async def load_posts(self) -> None:
        await self.repository.fetch_and_store_posts()

    def filter_posts(self, query: str) -> List[PostRecord]:
        all_posts = self.repository.get_all_posts()
        return [
            post for post in all_posts
            if query.lower() in post.title.lower() or query.lower() in post.body.lower()
        ]
