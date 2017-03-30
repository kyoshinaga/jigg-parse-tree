#!/usr/bin/env bash

if [ ! $# -ge 2 ]; then
  echo Usage: `basename $0` 'input output'
  echo
  exit
fi

scriptdir=`dirname $0`

java -cp "$scriptdir/*" jigg.pipeline.Pipeline \
  -annotators "corenlp[tokenize,ssplit,pos,parse]" \
  -corenlp.ssplit.eolonly "true" \
  -outputFormat json \
  -nThreads 50 \
  -file $1 \
  -output $2 \
  > /dev/null 2>&1

python $scriptdir/generate_trees.py $2 --format "txt"
