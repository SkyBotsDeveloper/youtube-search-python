import asyncio
import time
from typing import Optional

import httpx

from youtubesearchpython.core.constants import userAgent


class RequestCore:
    RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}

    def __init__(
        self,
        timeout: Optional[int] = None,
        max_retries: int = 2,
        retry_backoff: float = 0.4,
    ):
        self.url = None
        self.data = None
        self.timeout = timeout if timeout is not None else 10
        self.max_retries = max(0, int(max_retries))
        self.retry_backoff = max(0.0, float(retry_backoff))
        self.headers = {}
        self.cookies = None

    def _merge_headers(self, base_headers: dict) -> dict:
        merged = dict(base_headers)
        if isinstance(self.headers, dict):
            merged.update(self.headers)
        return merged

    def _get_retry_delay(self, attempt: int) -> float:
        return self.retry_backoff * (2 ** attempt)

    def syncPostRequest(self) -> httpx.Response:
        timeout = self.timeout if self.timeout is not None else 10
        headers = self._merge_headers(
            {
                "User-Agent": userAgent,
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/json",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
            }
        )

        for attempt in range(self.max_retries + 1):
            try:
                response = httpx.post(
                    self.url,
                    headers=headers,
                    json=self.data,
                    timeout=timeout,
                    cookies=self.cookies,
                )
            except httpx.RequestError:
                if attempt < self.max_retries:
                    time.sleep(self._get_retry_delay(attempt))
                    continue
                raise
            if (
                response.status_code in self.RETRYABLE_STATUS_CODES
                and attempt < self.max_retries
            ):
                time.sleep(self._get_retry_delay(attempt))
                continue
            return response

    async def asyncPostRequest(self) -> httpx.Response:
        timeout = self.timeout if self.timeout is not None else 10
        headers = self._merge_headers(
            {
                "User-Agent": userAgent,
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/json",
                "Origin": "https://www.youtube.com",
                "Referer": "https://www.youtube.com/",
            }
        )
        async with httpx.AsyncClient() as client:
            for attempt in range(self.max_retries + 1):
                try:
                    response = await client.post(
                        self.url,
                        headers=headers,
                        json=self.data,
                        timeout=timeout,
                        cookies=self.cookies,
                    )
                except httpx.RequestError:
                    if attempt < self.max_retries:
                        await asyncio.sleep(self._get_retry_delay(attempt))
                        continue
                    raise
                if (
                    response.status_code in self.RETRYABLE_STATUS_CODES
                    and attempt < self.max_retries
                ):
                    await asyncio.sleep(self._get_retry_delay(attempt))
                    continue
                return response

    # a special thanks to https://github.com/CertifiedCoder For his work in requests.py

    def syncGetRequest(self) -> httpx.Response:
        timeout = self.timeout if self.timeout is not None else 10
        headers = self._merge_headers(
            {
                "User-Agent": userAgent,
                "Accept-Encoding": "gzip, deflate",
            }
        )
        cookies = {"CONSENT": "YES+1"}
        if isinstance(self.cookies, dict):
            cookies.update(self.cookies)

        for attempt in range(self.max_retries + 1):
            try:
                response = httpx.get(
                    self.url,
                    headers=headers,
                    timeout=timeout,
                    cookies=cookies,
                )
            except httpx.RequestError:
                if attempt < self.max_retries:
                    time.sleep(self._get_retry_delay(attempt))
                    continue
                raise
            if (
                response.status_code in self.RETRYABLE_STATUS_CODES
                and attempt < self.max_retries
            ):
                time.sleep(self._get_retry_delay(attempt))
                continue
            return response

    async def asyncGetRequest(self) -> httpx.Response:
        timeout = self.timeout if self.timeout is not None else 10
        headers = self._merge_headers(
            {
                "User-Agent": userAgent,
                "Accept-Encoding": "gzip, deflate",
            }
        )
        cookies = {"CONSENT": "YES+1"}
        if isinstance(self.cookies, dict):
            cookies.update(self.cookies)

        async with httpx.AsyncClient() as client:
            for attempt in range(self.max_retries + 1):
                try:
                    response = await client.get(
                        self.url,
                        headers=headers,
                        timeout=timeout,
                        cookies=cookies,
                    )
                except httpx.RequestError:
                    if attempt < self.max_retries:
                        await asyncio.sleep(self._get_retry_delay(attempt))
                        continue
                    raise
                if (
                    response.status_code in self.RETRYABLE_STATUS_CODES
                    and attempt < self.max_retries
                ):
                    await asyncio.sleep(self._get_retry_delay(attempt))
                    continue
                return response
