from mcp.server.fastmcp import FastMCP

# Create your MCP server
mcp = FastMCP("FileReader")

@mcp.tool()
def read_file(file_path: str) -> str:
    """Read the contents of a file and return it as text"""
    
    try:
        # Open the file and read it
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        return f"✅ File read successfully!\n\n{content}"
    
    except FileNotFoundError:
        return f"❌ File not found: {file_path}"
    
    except Exception as e:
        return f"❌ Error reading file: {str(e)}"


@mcp.tool()
def list_files(folder_path: str) -> str:
    """List all files inside a folder"""
    
    import os
    
    try:
        files = os.listdir(folder_path)
        
        if not files:
            return f"📂 Folder is empty: {folder_path}"
        
        file_list = "\n".join(files)
        return f"📂 Files in {folder_path}:\n\n{file_list}"
    
    except FileNotFoundError:
        return f"❌ Folder not found: {folder_path}"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    mcp.run()