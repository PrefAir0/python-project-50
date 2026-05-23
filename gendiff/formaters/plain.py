
def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
        
    if isinstance(value, str):
        return f"'{value}'"
        
    return str(value)

def walk(diff_tree, path=""):
    lines = []
    
    for node in diff_tree:
        key = node['key']
        type_ = node['type']
        
        current_path = f"{path}.{key}" if path else key
        
        if type_ == 'nested':
            lines.extend(walk(node['children'], current_path))
            
        elif type_ == 'added':
            val = format_value(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {val}")
            
        elif type_ == 'deleted':
            lines.append(f"Property '{current_path}' was removed")
            
        elif type_ == 'changed':
            old = format_value(node['old_value'])
            new = format_value(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. From {old} to {new}")
            

    return lines


def render(diff_tree):
    return '\n'.join(walk(diff_tree))