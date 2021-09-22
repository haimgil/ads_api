from enum import Enum
from typing import Dict

from redis import Redis

ADS_KEY = 'ads'
IMPRESSIONS_KEY = 'impressions'


class StatsDimension(Enum):
    USER = 'user'
    SDK_VERSION = 'sdk_version'


class Repository:

    def __init__(self, redis: Redis):
        self.redis_con = redis

    def ad_increment(self, dimension: StatsDimension, dimension_value: str):
        self.redis_con.hincrby(ADS_KEY + ':' + dimension.value, dimension_value)

    def impression_increment(self, dimension: StatsDimension, dimension_value: str):
        self.redis_con.hincrby(IMPRESSIONS_KEY + ':' + dimension.value, dimension_value)

    def get_ad_requests_amount(self, dimension: StatsDimension) -> Dict[str, int]:
        ads: Dict[bytes, bytes] = self.redis_con.hgetall(ADS_KEY + ':' + dimension.value)
        return {k.decode('utf-8'): int(v) for k, v in ads.items()}

    def get_impressions_amount(self, dimension: StatsDimension) -> Dict[str, int]:
        impressions: Dict[bytes, bytes] = self.redis_con.hgetall(IMPRESSIONS_KEY + ':' + dimension.value)
        return {k.decode('utf-8'): int(v) for k, v in impressions.items()}
