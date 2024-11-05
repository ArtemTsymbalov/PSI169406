from repositories.posts_repository import PostsRepository
from services.posts_service import PostsService


class Container:
    def __init__(self):
        self._repositories = {}
        self._services = {}

        self._repositories['posts_repository'] = PostsRepository()

        self._services['posts_service'] = PostsService(self._repositories['posts_repository'])

    def repository(self, repo_name: str):
        return self._repositories.get(repo_name)

    def service(self, service_name: str = 'posts_service'):
        return self._services.get(service_name)
