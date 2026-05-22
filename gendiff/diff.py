from gendiff.parser import parse, get_format
from gendiff.formaters.stylish import format_stylish


def read_file(filepath):
    with open(filepath) as f:
        return f.read()


def build_diff(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    diff = []

    for key in keys:
        if key not in data2:
            diff.append({
                'key': key,
                'type': 'deleted',
                'value': data1[key]
            })
        elif key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
            })
        else:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })  
    return diff

def generate_diff(filepath1, filepath2, format_name='stylish'):
    data1 = parse(read_file(filepath1), get_format(filepath1))
    data2 = parse(read_file(filepath2), get_format(filepath2))
    diff_tree = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff_tree)

    raise ValueError(f"Unknown format: {format_name}")