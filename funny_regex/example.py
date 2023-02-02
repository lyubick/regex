import json

from funny_regex import json_string_escape_double_quotes as escape_double_quotes

if __name__ == '__main__':
    print(escape_double_quotes(invalid_json_string='{"he"llo": "wor"ld!", "hel"lo": ["world", "aga"in!"]}'))
    print(json.loads(escape_double_quotes(invalid_json_string='{"he"llo": "wor"ld!", "hel"lo": ["world", "aga"in!"]}')))
