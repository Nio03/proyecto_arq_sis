import pytest
import asyncio
from scraper.utils.resilience import fetch_case

@pytest.mark.asyncio
async def test_fetch_case_success(monkeypatch):
    class FakeResponse:
        async def json(self):
            return {"ok": True}
        def raise_for_status(self): pass
    class FakeSession:
        async def __aenter__(self): return self
        async def __aexit__(self, *args): pass
        async def get(self, url, timeout): return FakeResponse()
    monkeypatch.setattr("aiohttp.ClientSession", lambda: FakeSession())

    result = await fetch_case("http://fakeurl.com")
    assert result["ok"] is True
