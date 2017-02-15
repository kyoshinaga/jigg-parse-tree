#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

args = parser.parse_args()

def recursive(root, tree, tokens):
  phrase = ''
  node = tree.get(root,'')
  if node == '':
    token = tokens.get(root,'')
    phrase += '(' + token['pos'] + ' ' + token['form'] + ')'
  else:
    children = node['children'].split()
    phrases = [recursive(l, tree, tokens) for l in children]
    phrase += '(' + node['symbol'] + ' ' + ' '.join(phrases) + ')'
  return phrase

def main():
  data = json.loads(args.infile.read())
  
  sentences = data['.child'][0]['.child'][0]

  parses = {}
  
  for s in sentences['.child']:
    sentence = s['text']
    childs = s['.child']
    tokens = {}
    tree = {}
    root = ''
    for c in childs:
      if c['.tag'] == 'tokens':
        for t in c['.child']:
          token = {}
          token['form'] = t['form']
          token['pos'] = t['pos']
          tokens[t['id']] = token
      elif c['.tag'] == 'parse':
        root = c['root']
        for span in c['.child']:
          elem = {}
          elem['symbol'] = span['symbol']
          elem['children'] = span['children']
          tree[span['id']] = elem

    if (len(tree) == 0):
      parses[sentence] = ''
    else:
      parses[sentence] = '(ROOT ' + recursive(root, tree, tokens) + ')'
  print(json.dumps(parses, indent=2))

main()
