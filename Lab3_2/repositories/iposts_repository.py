from abc import ABC, abstractmethod
from typing import List
from domains.posts import Post

class IPostsRepository(ABC):
    @abstractmethod
    async def fetch_posts_and_comments(self) -> List[Post]:
        pass

    @abstractmethod
    async def filter_posts(self, query: str) -> List[Post]:
        pass

    @abstractmethod
    async def clear_inactive_records(self, threshold_seconds: int) -> None:
        pass

    @abstractmethod
    async def sort_posts_by_last_accessed(self) -> List[Post]:
        pass
