from mcp.server.fastmcp import FastMCP
import sqlite3

# Create your MCP server
mcp = FastMCP("Database")

# Database file location
DB_PATH = r"C:\Users\smita.suresh.masti\mcp-learning\mydata.db"

def get_connection():
    """Create a connection to the database"""
    return sqlite3.connect(DB_PATH)

@mcp.tool()
def create_table(table_name: str, columns: str) -> str:
    """Create a new table in the database. 
    columns should be like: 'name TEXT, age INTEGER, city TEXT'"""
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})")
        
        conn.commit()
        conn.close()
        
        return f"✅ Table '{table_name}' created successfully!"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"


@mcp.tool()
def insert_record(table_name: str, data: str) -> str:
    """Insert a record into a table.
    data should be like: 'Smita, 25, Pune'"""
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Split the data by comma
        values = [v.strip() for v in data.split(",")]
        placeholders = ", ".join(["?" for _ in values])
        
        cursor.execute(f"INSERT INTO {table_name} VALUES (NULL, {placeholders})", values)
        
        conn.commit()
        conn.close()
        
        return f"✅ Record inserted successfully into '{table_name}'!"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"


@mcp.tool()
def get_all_records(table_name: str) -> str:
    """Get all records from a table"""
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        
        # Get column names
        column_names = [description[0] for description in cursor.description]
        
        conn.close()
        
        if not rows:
            return f"📭 No records found in '{table_name}'"
        
        # Format the results nicely
        result = f"📋 Records in '{table_name}':\n\n"
        result += " | ".join(column_names) + "\n"
        result += "-" * 40 + "\n"
        
        for row in rows:
            result += " | ".join(str(v) for v in row) + "\n"
        
        return result
    
    except Exception as e:
        return f"❌ Error: {str(e)}"


@mcp.tool()
def delete_record(table_name: str, record_id: int) -> str:
    """Delete a record from a table by its ID"""
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
        
        conn.commit()
        conn.close()
        
        return f"✅ Record with ID {record_id} deleted from '{table_name}'!"
    
    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    mcp.run()