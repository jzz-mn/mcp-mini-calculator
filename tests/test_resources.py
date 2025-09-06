import asyncio
from src.server.resources import greeting

async def test_greeting():
    response = await greeting("Jazz")
    assert response == {"result": "Hello, Jazz!"}

if __name__ == "__main__":
    asyncio.run(test_greeting())
