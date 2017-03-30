# jigg-parse-tree
Get parsing tree and represent it into sentence.

## Requirement
- jigg 0.6.2+
  - jigg-0.6.2.jar is must be stored on same directory.
  - You can download the jar file from:
    https://github.com/mynlp/jigg/releases/download/v-0.6.2/jigg-0.6.2.tar.gz
- Grammar file for Berkeley parser.
  - You can donwload the file from:
    https://github.com/slavpetrov/berkeleyparser/raw/master/eng_sm6.gr

## Usage
- For stanford case-sensitive
```bash
$./parse-stanford.sh INPUT_FILE OUTPUT_FILE
```

- For berkeley parser
```bash
$./parse-berkeley.sh INPUT_FILE OUTPUT_FILE
```

### For instance
- INPUT_FILE
```text
At what institutions was Marshall Hall a professor ?
What fuel does an internal combustion engine use ?
```

- OUTPUT_FILE
```
(ROOT (FRAG (PP (IN At) (SBAR (WHNP (WP what)) (S (NP (NNS institutions)) (VP (VBD was) (NP (NNP Marshall) (NNP Hall)))))) (NP (DT a) (NN professor)) (. ?)))
(ROOT (SBARQ (WHNP (WP What) (NN fuel)) (SQ (VBZ does) (NP (DT an) (JJ internal) (NN combustion) (NN engine)) (VP (VB use))) (. ?)))
```
