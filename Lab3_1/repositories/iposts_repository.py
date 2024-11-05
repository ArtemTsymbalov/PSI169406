from abc import ABC, abstractmethod
from typing import List
from domains.posts import Post

class IPostsRepository(ABC):
    @abstractmethod
    async def fetch_posts_and_comments(self) -> List[Post]:
        """Pobiera wszystkie posty i komentarze i zapisuje je w pamięci"""
        pass

    @abstractmethod
    async def filter_posts(self, query: str) -> List[Post]:
        """Filtruje posty po tytule, treści, nazwie autora lub komentarzach"""
        pass

    @abstractmethod
    async def clear_inactive_records(self, threshold_seconds: int) -> None:
        """Usuwa posty i komentarze, które nie były używane przez zadany czas"""
        pass

    @abstractmethod
    async def sort_posts_by_last_accessed(self) -> List[Post]:
        """Sortuje posty według czasu ostatniego użycia"""
        pass
