from pathlib import Path

def total_salary(path):
    '''
        Reads a file containing employee names and their salaries, calculates the total salary and the average salary.

        @param path: A string representing the file path to read.
        @output: A tuple containing the total salary and the average salary.
    '''
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            line_count = 0
            for line in file:
                parts = line.strip().split(',')
                try:
                    salary = float(parts[1])
                    total += salary
                    line_count += 1
                except ValueError:
                    continue

            return (total, total / (line_count or 1))

    except FileNotFoundError:
        print(f"File {path} not found.")
        return (0, 0)

 
# Example usage:
if __name__ == "__main__":

    salary_file = Path('data/salaries.txt')
    total, average = total_salary('data/salaries.txt')
    print(f"Total: {total}, Average: {average}")