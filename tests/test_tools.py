import asyncio
from src.server.tools import add, subtract, multiply

async def test_add():
    assert await add(2,3) == {"result":5}

async def test_subtract():
    assert await subtract(5,3) == {"result":2}

async def test_multiply():
    assert await multiply(2,4) == {"result":8}

if __name__ == "__main__":
    asyncio.run(test_add())
    asyncio.run(test_subtract())
    asyncio.run(test_multiply())
