from pathlib import Path 
import json
import yaml

def get_format(file_path: str):
    return Path(file_path).suffix[1:]

def parse(content: str, format_name: str):
    if format_name == "json":
        return json.loads(content)

    if format_name in ("yaml", "yml"):
        return yaml.safe_load(content)
