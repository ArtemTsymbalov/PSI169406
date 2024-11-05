from typing import List
from domains.posts import Post
from repositories.iposts_repository import IPostsRepository

class PostsService:
    def __init__(self, repository: IPostsRepository):
        self.repository = repository

    async def get_filtered_posts(self, query: str) -> List[Post]:
        return await self.repository.filter_posts(query)

    async def get_sorted_posts(self) -> List[Post]:
        return await self.repository.sort_posts_by_last_accessed()

    async def clear_old_records(self, threshold_seconds: int) -> None:
        await self.repository.clear_inactive_records(threshold_seconds)
