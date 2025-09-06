import asyncio
from src.server.prompts import generate_greeting

async def test_generate_greeting_friendly():
    response = await generate_greeting("Jazz", "friendly")
    assert response == {"result": "Hey Jazz! How’s it going?"}

async def test_generate_greeting_formal():
    response = await generate_greeting("Jazz", "formal")
    assert response == {"result": "Good day, Jazz."}

async def test_generate_greeting_casual():
    response = await generate_greeting("Jazz", "casual")
    assert response == {"result": "Hi Jazz!"}

async def test_generate_greeting_default():
    # If unknown style, fallback to default
    response = await generate_greeting("Jazz", "unknown")
    assert response == {"result": "Hello Jazz!"}

if __name__ == "__main__":
    asyncio.run(test_generate_greeting_friendly())
    asyncio.run(test_generate_greeting_formal())
    asyncio.run(test_generate_greeting_casual())
    asyncio.run(test_generate_greeting_default())