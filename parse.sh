#!/usr/bin/env bash

if [ ! $# -ge 1 ]; then
  echo Usage: `basename $0` 'file'
  echo
  exit
fi

scriptdir=`dirname $0`

java -cp "$scriptdir/*" jigg.pipeline.Pipeline \
  -annotators "corenlp[tokenize,ssplit,pos,lemma,ner],berkeleyparser" \
  -berkeleyparser.grFileName ./eng_sm6.gr \
  -outputFormat json \
  -nThreads 32 \
  -file $1
