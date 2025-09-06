# src/server/tools.py

async def add(a: int, b: int) -> int:
    return a + b

async def subtract(a: int, b: int) -> int:
    return a - b

def register_tools(server):
    # HTTP-friendly registration
    server.resource("tool://add")(add)
    server.resource("tool://subtract")(subtract)
