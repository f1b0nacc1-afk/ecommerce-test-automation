from typing import Any

import requests


class APIClient:
    def __init__(self, base_url: str, timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def _url(self, endpoint: str) -> str:
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.session.get(self._url(endpoint), timeout=self.timeout, **kwargs)

    def post(self, endpoint: str, json: dict | None = None, **kwargs: Any) -> requests.Response:
        return self.session.post(self._url(endpoint), json=json, timeout=self.timeout, **kwargs)

    def put(self, endpoint: str, json: dict | None = None, **kwargs: Any) -> requests.Response:
        return self.session.put(self._url(endpoint), json=json, timeout=self.timeout, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> requests.Response:
        return self.session.delete(self._url(endpoint), timeout=self.timeout, **kwargs)
