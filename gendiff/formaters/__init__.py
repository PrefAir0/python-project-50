from gendiff.formaters.stylish import format_stylish
from gendiff.formaters.plain import format_plain

def apply_format(diff_tree, format_name):
    if format_name == 'stylish':
        return format_stylish(diff_tree)
    elif format_name == 'plain':
        return format_plain(diff_tree)
