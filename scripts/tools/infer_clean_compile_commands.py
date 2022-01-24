import json
import sys

commands = json.load(open(sys.argv[1]))
res = []
for command in commands:
    if command['file'].startswith('external/'):
        continue
    if command['file'].startswith('/'):
        continue
    if command['file'].startswith('bazel-out/'):
        continue
    command['command'] = command['command'].replace('-fno-canonical-system-headers ', '')
    res.append(command)
json.dump(res, open(sys.argv[2], 'w'), indent=1)