from mcp.server.fastmcp import FastMCP
import os

# Tell MCP which port to use via environment variable
os.environ["FASTMCP_PORT"] = os.environ.get("PORT", "8000")
os.environ["FASTMCP_HOST"] = "0.0.0.0"

# Create your MCP server
mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

if __name__ == "__main__":
    mcp.run(transport="sse")