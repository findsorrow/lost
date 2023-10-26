from io import BytesIO
from os import mkdir, path
from sys import getsizeof
from typing import Optional

from aiofiles import open as async_open
from pydantic import BaseModel
from xxhash import xxh32_hexdigest

from tools.managers.network import ClientSession

cache = path.join("/temp", "cache")
if not path.exists(cache):
    mkdir(cache)


class Asset(BaseModel):
    size: int
    name: str
    extension: str
    is_video: bool
    buffer: bytes

    @property
    def url(self: "Asset") -> str:
        return f"https://dev.wock.sh/cache/{self.name}.{self.extension}"

