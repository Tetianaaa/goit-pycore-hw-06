# Task №1
def total_salary(path):
    try:
        total_salary = 0
        developers = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                developers += 1
        
        if developers == 0:
            return (0, 0)
        else:
            avg_salary = total_salary / developers
            return (total_salary, avg_salary)
    
    except FileNotFoundError:
        print(f'Error: do not find file throught this {path}')
        return (0, 0)

    except Exception as e:
        print(f'Error: {e}')
        return (0, 0)

# checking:
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



# Task №2
def get_cats_info(path):
    try:
        cat_list = []

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_dict = {
                    'id' : id,
                    'name': name,
                    'age' : age
                }
                cat_list.append(cat_dict)
        return cat_list
    
    except FileNotFoundError:
        print(f'Error: do not find file throught this {path}')
        return []

    except Exception as e:
        print(f'Error: {e}')
        return []

# checking:
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
