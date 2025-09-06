import asyncio
import subprocess
import httpx
import pytest

@pytest.mark.asyncio
async def test_integration():
    # Start server subprocess
    proc = subprocess.Popen(
        ["python", "-m", "src.server.main"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    async def wait_for_server(url="http://127.0.0.1:8000/tool/add", timeout=10):
        async with httpx.AsyncClient() as client:
            for _ in range(timeout * 2):
                try:
                    resp = await client.get(url, params={"a": 0, "b": 0})
                    if resp.status_code == 200:
                        return
                except httpx.ConnectError:
                    await asyncio.sleep(0.5)
            raise RuntimeError("Server did not start in time")

    await wait_for_server()

    # Test add tool
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000") as client:
        add_resp = (await client.get("/tool/add", params={"a": 2, "b": 3})).json()
        assert add_resp["result"] == 5

        greet_resp = (await client.get("/greeting/John")).text
        assert greet_resp == "Hello John!"

    # Stop server
    proc.terminate()
    proc.wait()
