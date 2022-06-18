import re

sentence = 'hore fat'
regex = re.compile('(?P<animal>\w+)(?P<verb>\w+)(?P<adjective>\w+)')
matched = re.search(regex, sentence)
print(matched.group(2))