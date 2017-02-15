#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

args = parser.parse_args()

data = json.loads(args.infile.read())

sentences = data['.child'][0]['.child'][0]

ners = {}

for s in sentences['.child']:
  sentence = s['text']
  childs = s['.child']
  nes = []
  tokens = {}
  for c in childs:
    if c['.tag'] == 'NEs':
      for t in c.get('.child',''):
        nes.append(t['tokens'])
    elif c['.tag'] == 'tokens':
      for t in c['.child']:
        tokens[t['id']] = t['form']
    
  words = []
  for ne in nes:
    words.append(' '.join([tokens[tid] for tid in ne.split()]))
  ners[sentence] = words

print(json.dumps(ners,indent=2))
