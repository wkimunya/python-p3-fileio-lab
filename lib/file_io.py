from pathlib import Path

def write_file(file_name, file_content):
    file_name = str(file_name)
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    try:
        with open(file_name, 'w') as file:
            file.write(file_content)
            print(f'File {file_name} has been successfully written.')
    except Exception as e:
        print(f'Error writing to {file_name}: {str(e)}')

def append_file(file_name, append_content):
    file_name = str(file_name)
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    try:
        with open(file_name, 'a') as file:
            file.write(append_content)
            print(f'Content has been successfully appended to {file_name}.')
    except Exception as e:
        print(f'Error appending to {file_name}: {str(e)}')

def read_file(file_name):
    file_name = str(file_name)
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except Exception as e:
        print(f'Error reading {file_name}: {str(e)}')
        return None
