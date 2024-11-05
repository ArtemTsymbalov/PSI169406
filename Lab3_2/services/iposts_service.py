from abc import ABC
from typing import List
from domains.posts import PostRecord

class IPostsService(ABC):
    async def get_all_posts(self) -> List[PostRecord]:
        pass

    async def filter_posts(self, query: str) -> List[PostRecord]:

        pass