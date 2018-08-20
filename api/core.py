import json
import requests

from django.conf import settings

class APIClient:

    VALID_OPS = {
        "categories": "ls_c",
        "visors": "ls_v",
        "places": "ls_l",
        "tags": "ls_t"
    }

    def __init__(self, srv=None):
        self.srv = srv or settings.API_SRV

    def _make_request(self, op, data=None):
        payload = {
            "op": op,
            "payload": data or {}
        }
        return requests.post(self.srv, data={"data": json.dumps(payload)}).json()

    def _cache(self, item, func):
        cached = getattr(self, '_' + item, False)
        if not cached:
            cached = func(item)
            setattr(self, '_' + item, cached)
        return cached

    def __getattr__(self, item):
        if item not in self.VALID_OPS:
            return self.__getattribute__(item)
        return self._cache(self.VALID_OPS[item], self._make_request)
