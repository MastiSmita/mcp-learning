from mcp.server.fastmcp import FastMCP
import json
import os

mcp = FastMCP("NoteTaker")

# File where all notes will be saved
NOTES_FILE = r"C:\Users\smita.suresh.masti\mcp-learning\notes.json"

def load_notes():
    """Load all notes from the file"""
    if not os.path.exists(NOTES_FILE):
        return {}
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

def save_notes(notes):
    """Save all notes to the file"""
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


@mcp.tool()
def add_note(title: str, content: str) -> str:
    """Save a new note with a title and content"""
    try:
        notes = load_notes()
        notes[title] = content
        save_notes(notes)
        return f"✅ Note '{title}' saved successfully!"
    except Exception as e:
        return f"❌ Error: {str(e)}"


@mcp.tool()
def get_note(title: str) -> str:
    """Get a note by its title"""
    try:
        notes = load_notes()
        if title not in notes:
            return f"❌ Note '{title}' not found!"
        return f"📝 {title}:\n\n{notes[title]}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


@mcp.tool()
def list_notes() -> str:
    """List all saved notes"""
    try:
        notes = load_notes()
        if not notes:
            return "📭 No notes saved yet!"
        titles = "\n".join([f"• {title}" for title in notes.keys()])
        return f"📋 Your saved notes:\n\n{titles}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


@mcp.tool()
def delete_note(title: str) -> str:
    """Delete a note by its title"""
    try:
        notes = load_notes()
        if title not in notes:
            return f"❌ Note '{title}' not found!"
        del notes[title]
        save_notes(notes)
        return f"✅ Note '{title}' deleted successfully!"
    except Exception as e:
        return f"❌ Error: {str(e)}"


if __name__ == "__main__":
    mcp.run()