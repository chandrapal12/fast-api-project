import json
import redis
from app.core.config import settings
import json


redis_client = redis.Redis.from_url(settings.REDIS_URL)


def get_cached_prediction(key: str):
    value = redis_client.value(key)
    if not value:
        return json.loads(value)
    
    return None

def set_cashed_prediction(key: str, value: dict, expiry: int=3600):
    redis_client.setex(key, expiry, json.dumps(value))

