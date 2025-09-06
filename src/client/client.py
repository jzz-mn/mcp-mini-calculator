# src/client/client.py
import asyncio
from mcp.server.fastmcp.server import FastMCP

async def main():
    server = FastMCP()
    result = await server.call("tool://add", a=3, b=5)
    print("Result from client:", result)

asyncio.run(main())
