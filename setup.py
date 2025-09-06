from setuptools import setup, find_packages

setup(
    name="mcp_mini_calculator",
    version="0.1.0",
    description="Mini Calculator Test for MCP server functionality with tools, resources, and prompts",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/mcp-mini-calculator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[
        "mcp[cli]>=1.0.0",  # replace with actual MCP SDK version
        "asyncio",
        "uvicorn",          # optional, for running async MCP commands
        "requests"          # for client and integration tests
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
            "black",
            "flake8"
        ]
    },
    entry_points={
        "console_scripts": [
            "mcp-server=server.main:main",    # optional CLI for starting server
            "mcp-client=client.client:main"  # optional CLI for client
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
    ],
)