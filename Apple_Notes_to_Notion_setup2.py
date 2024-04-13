from notion_client import Client

notion = Client(auth="your_notion_integration_token")

def add_to_notion(title, content):
    """Add notes to Notion."""
    notion.pages.create(
        parent={"database_id": database_id},
        properties={
            "Name": {"title": [{"text": {"content": title}}]},
            "Content": {"rich_text": [{"text": {"content": content}}]}
        }
    )

# assuming we have a way to get title and content from AppleScript
add_to_notion(note_title, note_content)
