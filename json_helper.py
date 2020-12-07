from typing import Dict


def dict_eval(data: Dict, path: str) -> str:
    indexes = path.strip('/').split('/')
    sub_dict = data
    for idx_name in indexes:
        if idx_name.isnumeric():
            idx_name = int(idx_name)
        sub_dict = sub_dict[idx_name]
    return sub_dict


def __find_end_bracket_pos(text: str, start: int) -> int:
    depth = 0
    in_str = False
    while True:
        if text[start] == '"':
            in_str = not in_str
        if not in_str:
            if text[start] == '{':
                depth += 1
            if text[start] == '}':
                depth -= 1
        start += 1
        if depth == 0:
            return start


def get_json_data(data: str, beginning_str: str) -> str:
    start_pos = data.find(beginning_str)
    if start_pos == -1:
        raise Exception(f"Could not get json data\nBeginning not found")
    start_pos += len(beginning_str)
    end_pos = __find_end_bracket_pos(data, start_pos)
    return data[start_pos:end_pos]
