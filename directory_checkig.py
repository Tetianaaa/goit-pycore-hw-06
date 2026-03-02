from pathlib import Path
from colorama import Fore, Back, Style

def viz_directory_structure(path, indent=''):
    try:
        p = Path(path)
        # виключення для папок із великою кількістю файлів
        excluded_dirs = {'.venv', '__pycache__'}

        items = sorted(p.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        for i in items:
            if i.is_dir() and i.name in excluded_dirs:
                print(f'{indent}{Back.YELLOW}{i.name}/ (skipped){Back.RESET}')
                continue

            if i.is_dir():
                print(f'{indent}{Fore.BLUE}{Style.BRIGHT}{i.name}/{Style.RESET_ALL}')
                viz_directory_structure(i, indent + "    ")
            else:
                print(f'{indent}{Fore.GREEN}{i.name}')

    except PermissionError:
        print(f'{Fore.RED}Do not have Permission!')

    except Exception as e:
        print(f'{Fore.RED}(!) Error: {e}')

# checking:
path = '/Users/tetianakravchuk/Documents/Neoversity/Projects/python_programming/goit-pycore-hw-06'
print(viz_directory_structure(path))