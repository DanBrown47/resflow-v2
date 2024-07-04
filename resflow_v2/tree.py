import os

def print_tree(startpath, exclude=None):
    if exclude is None:
        exclude = ['__pycache__', '.git', '.venv', 'node_modules']

    for root, dirs, files in os.walk(startpath):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in exclude]

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not any(f.endswith(ext) for ext in ['.pyc', '.pyo', '.log']):
                print(f"{subindent}{f}")

if __name__ == "__main__":
    project_path = r"C:\Users\ASUS\ResFlow\new\resflow-v2\resflow_v2"
    print_tree(project_path)
