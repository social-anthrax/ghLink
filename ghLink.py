from os import error
import subprocess
from sys import argv
import json

line_url = ''
url = json.loads(
    subprocess.run(['gh', 'repo', 'view', '--json', 'url'], stdout=subprocess.PIPE).stdout.decode('utf-8')
).get('url')
commit = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE).stdout.decode('utf-8')

if len(argv) < 2:
    error("Please give file as url")
else:
    path = argv[1]
    if path.startswith('./'):
        relative = subprocess.run(
            ['git', 'rev-parse', '--show-prefix'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        relative = url[2:]  + path
    
    line_url = '{}/{}/{}'.format(url,commit,relative)
    if len(argv) > 2:
        line_url += '#L{}'.format(argv[2])


            
