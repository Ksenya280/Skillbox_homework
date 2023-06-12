import os
import re

def count_code_lines(dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as file:
                    for line in file:
                        line = line.strip()
                        if line and not re.match(r'^\s*#', line):
                            yield line


dir_path = '/dpo_python_basic/Module25/'
code_lines_count = sum(1 for _ in count_code_lines(dir_path))
print(f'Общее количество строк кода: {code_lines_count}')
