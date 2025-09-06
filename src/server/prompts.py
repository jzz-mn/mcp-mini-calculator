# src/server/prompts.py

def register_prompts(server):
    @server.resource("prompt://echo/{text}")
    def echo(text: str) -> str:
        return text

    @server.resource("prompt://shout/{text}")
    def shout(text: str) -> str:
        return text.upper()
