from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Comment:
    postId: int
    id: int
    name: str
    email: str
    body: str
    last_accessed: datetime = field(default_factory=datetime.utcnow)
