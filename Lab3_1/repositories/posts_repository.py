import aiohttp

from typing import List
from domains.posts import PostRecord
from utils.consts import API_SENSOR_URL

class PostRepository:
    def __init__(self):
        self._posts = []

    async def fetch_and_store_posts(self) -> None:
        async with aiohttp.ClientSession() as session:
            async with session.get(API_SENSOR_URL) as response:
                if response.status == 200:
                    posts_data = await response.json()
                    self._posts = [PostRecord(**post) for post in posts_data]

    def get_all_posts(self) -> List[PostRecord]:
        return self._posts