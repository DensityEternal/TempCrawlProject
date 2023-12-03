import re

html_code = '<div data-itemtype="result" class="">To add insult to injury</div>'
pattern = r'<div[^>]*>(.*?)</div>'

match = re.search(pattern, html_code)
if match:
    text = match.group(1)
    print(text)