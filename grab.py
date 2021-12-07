#! /usr/bin/env python3
# Goes through `wiki_raw.txt` and extracts the names of
# Christmas films from the table, printing them to stdout.
import re

with open("in/wiki_raw.txt") as in_txt:
    contents = in_txt.read()
    r = re.compile(r"^\|\s{0,1}''\[\[(.+?)\]\]''", re.MULTILINE)
    m = re.findall(r, contents)
    for g in m:
        g = re.sub(r"^.*\|", "", g)
        print(g)
