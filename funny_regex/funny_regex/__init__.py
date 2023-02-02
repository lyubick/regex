import re


def json_string_escape_double_quotes(invalid_json_string: str) -> str:
    return re.sub(
        r'((?<!":)(?<!": )(?<!{)(?<!",)(?<!", )(?<!},)(?<!}, )(?<!\[)(?<!],)(?<!], )(?<!\d,)(?<!, )(?<!null,)(?<!null, ))"((?!:)(?!})(?!,")(?!, ")(?!]))',  # noqa
        '\\"',
        invalid_json_string
    )
