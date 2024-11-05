from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from domains.comments import Comment


@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str
    comments: List[Comment] = field(default_factory=list)
    last_accessed: datetime = field(default_factory=datetime.utcnow)
