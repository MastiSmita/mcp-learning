from mcp.server.fastmcp import FastMCP

# Create your MCP server and give it a name
mcp = FastMCP("Calculator")

# Tool 1: Add two numbers
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b

# Tool 2: Subtract two numbers
@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a"""
    return a - b

# Tool 3: Multiply two numbers
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together"""
    return a * b

# Tool 4: Divide two numbers
@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Start the server
if __name__ == "__main__":
    mcp.run()
