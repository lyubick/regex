# Invalid Double Quotes in JSON String
Regexp below will find all double quotes that require escape symbol to preserve valid JSON string.

## Regexp
```regexp
((?<!":)(?<!": )(?<!{)(?<!",)(?<!", )(?<!},)(?<!}, )(?<!\[)(?<!],)(?<!], )(?<!\d,)(?<!, )(?<!null,)(?<!null, ))"((?!:)(?!})(?!,")(?!, ")(?!]))
```

## Example in Python
```python
import re


def escape_double_quotes(invalid_json_string: str) -> str:
    return re.sub(
        r'((?<!":)(?<!": )(?<!{)(?<!",)(?<!", )(?<!},)(?<!}, )(?<!\[)(?<!],)(?<!], )(?<!\d,)(?<!, )(?<!null,)(?<!null, ))"((?!:)(?!})(?!,")(?!, ")(?!]))',  # noqa
        '\\"',
        invalid_json_string
    )
```

In case if an input string will be
```text
{"he"llo": "wor"ld!", "hel"lo": ["world", "aga"in!"]}
```

the output will be
```text
{"he\"llo": "wor\"ld!", "hel\"lo": ["world", "aga\"in!"]}
```

## Usage
Feel free to copy and paste. For the lazy people use a `pip install` command if using Python.

```bash
pip install git+ssh://git@github.com/lyubick/regex.git#subdirectory=funny_regex
```

then just
```python
import json

from funny_regex import json_string_escape_double_quotes as escape_double_quotes

if __name__ == '__main__':
    print(escape_double_quotes(invalid_json_string='{"he"llo": "wor"ld!", "hel"lo": ["world", "aga"in!"]}'))
    print(json.loads(escape_double_quotes(invalid_json_string='{"he"llo": "wor"ld!", "hel"lo": ["world", "aga"in!"]}')))
```
