
from datetime import datetime, timedelta

class PriceCache:
    def __init__(self):
        self.cache = {}

    def set(self, key, value, ttl_seconds):
        expiration_time = datetime.now().timestamp() + ttl_seconds
        self.cache[key] = {'value': value, 'expiration_time': expiration_time}

    def get(self, key):
        if key in self.cache:
            item = self.cache[key]
            if item['expiration_time'] > datetime.now().timestamp():
                return item['value']
            else:
                del self.cache[key]
        return None

    async def async_get_or_fetch(self, key, fetch_func, ttl_seconds):
        cached_value = self.get(key)
        if cached_value is not None:
            return cached_value
        value = await fetch_func()
        if value:
            self.set(key, value, ttl_seconds)
        return value
        