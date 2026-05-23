

def stringify(value, depth):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'

    if not isinstance(value, dict):
        return str(value)

    space = " " * (depth * 4)
    lines = []
    
    for key, val in value.items():

        lines.append(f"{space}    {key}: {stringify(val, depth + 1)}")
        
    result = '\n'.join(lines)
    return f"{{\n{result}\n{space}}}"

def walk(diff_tree, depth):
    indent = " " * (depth * 4 - 2)

    bracket_indent = " " * ((depth - 1) * 4)
    
    lines = []
    for node in diff_tree:
        key = node['key']
        type_ = node['type']
        
        if type_ == 'nested':
            formatted_value = walk(node['children'], depth + 1)
            lines.append(f"{indent}  {key}: {formatted_value}")
            
        elif type_ == 'added':
            formatted_value = stringify(node['value'], depth)
            lines.append(f"{indent}+ {key}: {formatted_value}")
            
        elif type_ == 'deleted':
            formatted_value = stringify(node['value'], depth)
            lines.append(f"{indent}- {key}: {formatted_value}")
            
        elif type_ == 'unchanged':
            formatted_value = stringify(node['value'], depth)
            lines.append(f"{indent}  {key}: {formatted_value}")
            
        elif type_ == 'changed':
            value1 = stringify(node['old_value'], depth)
            value2 = stringify(node['new_value'], depth)
            lines.append(f"{indent}- {key}: {value1}")
            lines.append(f"{indent}+ {key}: {value2}")
            
    result = '\n'.join(lines)
    return f"{{\n{result}\n{bracket_indent}}}"

def render(diff_tree):
    return walk(diff_tree, 1)