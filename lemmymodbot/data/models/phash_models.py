from dataclasses import dataclass


@dataclass
class PostInfo:
    post_id: int
    phash: str
