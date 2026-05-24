from mcp.server.fastmcp import FastMCP

# Create your MCP server with SSE transport for deployment
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
    # SSE transport makes it work over the internet!
    mcp.run(transport="sse")