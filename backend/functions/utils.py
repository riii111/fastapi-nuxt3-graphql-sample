import re
from datetime import datetime, timezone


def multi_space_to_single(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def get_now_utc() -> datetime:
    return datetime.now(timezone.utc)
