from gendiff.parser import parse, get_format
import json


def read_file(filepath):
    with open(filepath) as f:
        return f.read()


def format_value(value):
    if value is True:
        return 'true'

    if value is False:
        return 'false'

    if value is None:
        return 'null'

    return str(value)


def generate_diff(filepath1, filepath2):
    data1 = parse(read_file(filepath1), get_format(filepath1))
    data2 = parse(read_file(filepath2), get_format(filepath2))

    keys = sorted(data1.keys() | data2.keys())

    lines = ['{']

    for key in keys:
        if key not in data2:
            lines.append(
                f'  - {key}: {format_value(data1[key])}'
            )

        elif key not in data1:
            lines.append(
                f'  + {key}: {format_value(data2[key])}'
            )

        elif data1[key] == data2[key]:
            lines.append(
                f'    {key}: {format_value(data1[key])}'
            )

        else:
            lines.append(
                f'  - {key}: {format_value(data1[key])}'
            )

            lines.append(
                f'  + {key}: {format_value(data2[key])}'
            )

    lines.append('}')

    return '\n'.join(lines)