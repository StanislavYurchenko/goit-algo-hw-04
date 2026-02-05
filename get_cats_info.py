from pathlib import Path

def get_cats_info(path):
    '''
        Reads a file containing cat information (ID, name, age), and returns a list of dictionaries with this information.

        @param path: A string representing the file path to read.
        @output: A list of dictionaries, where each dictionary contains the keys 'id', 'name', and 'age' corresponding to each cat's information.
    '''
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            for line in file:
                parts = line.strip().split(',')
                id = parts[0].strip()
                name = parts[1].strip()
                try:
                    age = parts[2].strip()
                    cats.append({'id': id, 'name': name, 'age': age})
                except ValueError:
                    continue

            return cats

    except FileNotFoundError:
        print(f"File {path} not found.")
        return []

 
# Example usage:
if __name__ == "__main__":
    cats_file = Path('data/cats.txt')
    cats_info = get_cats_info(cats_file)
    for cat in cats_info:
        print(f"Cat ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")