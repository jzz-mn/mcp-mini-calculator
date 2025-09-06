# src/server/main.py
from mcp.server.fastmcp import FastMCP
from tools import register_tools

server = FastMCP()
register_tools(server)

# Start HTTP server
server.run_http(host="127.0.0.1", port=8000)
