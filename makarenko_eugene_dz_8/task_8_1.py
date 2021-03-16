import re
def email_parse(address):

    match = re.compile(r'^(?P<username>[A-Za-z\d._+-]+)@(?P<domain>[A-Za-z\d.-]+\b\.[a-z]+)$')
    try:
        return match.match(address).groupdict()
    except (AttributeError, TypeError):
        raise ValueError(f'wrong email: {address}')





print(email_parse('geekbrains@gmail.ry'))