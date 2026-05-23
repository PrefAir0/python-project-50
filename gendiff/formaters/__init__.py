from gendiff.formaters import stylish
from gendiff.formaters import plain
from gendiff.formaters import json  

def apply_format(diff_tree, format_name):
    if format_name == 'stylish':
        return stylish.render(diff_tree)
    elif format_name == 'plain':
        return plain.render(diff_tree)
    elif format_name == 'json':
        return json.render(diff_tree)
    