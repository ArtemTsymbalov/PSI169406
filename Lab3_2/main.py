import asyncio
import json
from container import Container
from services.posts_service import PostsService

async def main():
    container = Container()
    posts_service = container.service()

    await posts_service.repository.fetch_posts_and_comments()

    query = "sunt"
    filtered_posts = await posts_service.get_filtered_posts(query)
    filtered_posts_json = json.dumps([post.__dict__ for post in filtered_posts], default=str, indent=2)
    print(f"Filtered posts:\n{filtered_posts_json}")

    sorted_posts = await posts_service.get_sorted_posts()
    sorted_posts_json = json.dumps([post.__dict__ for post in sorted_posts], default=str, indent=2)
    print(f"Sorted posts by last accessed:\n{sorted_posts_json}")

    await posts_service.clear_old_records(threshold_seconds=60)

if __name__ == "__main__":
    asyncio.run(main())
