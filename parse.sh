#!/usr/bin/env bash

if [ ! $# -ge 2 ]; then
  echo Usage: `basename $0` 'input output'
  echo
  exit
fi

scriptdir=`dirname $0`

java -cp "$scriptdir/*" jigg.pipeline.Pipeline \
  -annotators "corenlp[tokenize,ssplit,pos,lemma,ner],berkeleyparser" \
  -berkeleyparser.grFileName "$scriptdir/eng_sm6.gr" \
  -outputFormat json \
  -nThreads 32 \
  -file $1 \
  -output $2 \
  > /dev/null 2>&1

python $scriptdir/generate_berkeley_trees.py $2 --format "txt"
