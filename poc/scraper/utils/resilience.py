import aiohttp
import pybreaker
from tenacity import retry, wait_exponential, stop_after_attempt

breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)

@breaker
@retry(wait=wait_exponential(min=1, max=10), stop=stop_after_attempt(3))
async def fetch_case(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
            response.raise_for_status()
            return await response.json()
