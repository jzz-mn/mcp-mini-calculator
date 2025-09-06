# src/server/resources.py

def register_resources(server):
    @server.resource("greeting://hello/{name}")
    def hello(name: str) -> str:
        return f"Hello, {name}! Welcome to MCP server."

    @server.resource("greeting://goodbye/{name}")
    def goodbye(name: str) -> str:
        return f"Goodbye, {name}! See you next time."
