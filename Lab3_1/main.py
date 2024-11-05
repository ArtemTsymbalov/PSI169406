# main.py
import asyncio
import json
from repositories.posts_repository import PostRepository
from services.posts_service import PostService

async def main():
    repository = PostRepository()
    service = PostService(repository)

    await service.load_posts()
    all_posts = repository.get_all_posts()
    print(json.dumps([post.__dict__ for post in all_posts], indent=4))

    query = "non"
    filtered_posts = service.filter_posts(query)

    print(json.dumps([post.__dict__ for post in filtered_posts], indent=4))

if __name__ == "__main__":
    asyncio.run(main())
