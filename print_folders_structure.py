from pathlib import Path
from colorama import Fore, Style, init
import sys

init(autoreset=True)

FILE_ICONS = {
    ".py": "🐍",
    ".txt": "📄",
    ".json": "🧾",
    ".md": "📘",
    ".csv": "📊",
}

def file_icon(path: Path) -> str:
    '''
        Returns an emoji icon based on the file extension. If the extension is not recognized, it returns a default document icon (📄).

        @param path: A Path object representing a file.
        @output: String: An emoji icon corresponding to the file type based on its extension.
    '''
    
    return FILE_ICONS.get(path.suffix.lower(), "📄")

def print_folders_structure(path: Path, prefix=""):
    '''
        Recursively prints the folder structure of a given directory path, using indentation and icons to represent files and folders.
    
        @param path: A Path object representing the directory to print.
        @param prefix: A string used for indentation to visually represent the folder hierarchy (default is an empty string).
    '''

    try:
        def sort_key(p: Path):
            return (not p.is_dir(), p.name.lower())

        items = sorted(path.iterdir(), key=sort_key)

        for index, item in enumerate(items):
            is_last = index == len(items) - 1
            connector = "└── " if is_last else "├── "

            if item.is_dir():
                print(prefix + Fore.MAGENTA + connector + Fore.GREEN + "📁 " + Style.BRIGHT + item.name)

                new_prefix = prefix + ("    " if is_last else "│   ")
                print_folders_structure(item, new_prefix)
            else:
                print(prefix + Fore.MAGENTA + connector + Fore.YELLOW + f"{file_icon(item)} {item.name}")

    except Exception as e:
        print(Fore.RED + f"Error accessing {path}: {e}")

if __name__ == "__main__":
    '''
        Usage: python3 print_folders_structure.py /path/to/directory

        Example: python3 print_folders_structure.py .data
    '''

    if len(sys.argv) < 2:
        print(Fore.RED + "Usage: python print_folders_structure.py <path>")
        sys.exit(1)

    base_path = Path(sys.argv[1])
    print(Fore.GREEN + f"📂 {base_path.resolve()}")
    print_folders_structure(base_path)
