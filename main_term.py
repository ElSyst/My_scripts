from rutermextract import TermExtractor
import os
import sys
import csv

fn = sys.argv[1]
in_text = open(os.path.basename(fn), "r")
term_extractor = TermExtractor()
out_text=csv.writer(open("output.csv","w",newline=' '))

for line in in_text:
    for term in term_extractor(line):
		out_text.write(term.normalized)
out_text.close()
in_text.close()

