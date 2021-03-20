import re
from requests import get, utils
response = get(('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'))
code = utils.get_encoding_from_headers(response.headers)
log = response.content.decode(encoding=code)
RE = re.compile(r'(?P<remote_addr>[\d.]+)[\s-]+\[(?P<request_datetime>\d{1,2}\/\w+\/\d{4}(?::\d{2}){3}\s+\+\d{4})\]\s+"(?P<request_type>\w+)\s+(?P<requested_resource>[^\s]+)\s[^"]+"\s+(?P<response_code>\d*)\s+(?P<response_size>\d*)')
for line in map(lambda x: x.groupdict(), RE.finditer(log)):
    print(line)
