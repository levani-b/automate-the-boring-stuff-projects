import re

def regex_strip(text, chars=None):
    if chars is None:
        pattern = r'^\s+|\s+$'
    else:
        escaped_chars = re.escape(chars)
        pattern = rf'^[{escaped_chars}]+|[{escaped_chars}]+$'

    return re.sub(pattern, '', text)