#!/usr/bin/python
# -*- coding: utf-8 -*-

# Goes through all christmas movies in `xmas_films.txt` and
# generates all potential "House of Gamers versions", a test of validity
# is done by running a spellchecker over the title afterwords.

import itertools


def __appendchar(line, a, i):
    """
    Add character at position `i` in `line` with character `a`.
    E.g. Adding 'a' to "Hello" could produce "Ahello", "Haello", ...,  "Helloa".
    Attempts to add a character into a non alphabetic position results in an empty 
    string.

    If the character does not extend a word, but creates a new word, then a blank
    line is returned.
    """

    if i == len(line):
        if line[-1].isalpha():
            return line + a
        else:
            return ''

    if not line[i].isalpha():
        if i == 0:
            return ''
        elif not line[i - 1].isalpha():
            return ''

    if line[i].isupper():
        return line[:i] + a.upper() + line[i].lower() + line[i + 1:]
    else:
        return line[:i] + a + line[i:]


def __alts(line):
    """
    Given a movie title, returns the list of all potential candidate movie titles, replacing 
    each character in turn with all possible other  valid characters.
    E.g. `Hello` becomes "Ahello", "Haello", ..., "Helloy, "Helloz".
    """

    alts = itertools.product('abcdefghijklmnopqrstuvwxyz',
                             range(len(line) + 1))
    return filter(lambda s: s != '', (__appendchar(line, a, i) for (a,
                  i) in alts))


def house_of_gamers(line, spell_checker):
    """
    Takes a string and spell checker, generates all "House of Gamers" 
    possibilities on the string then filters these by the spellchecker.
    """

    words = line.split()
    candidate_words = map(__alts, words)
    candidate_words = list(map(lambda ws: filter(lambda w: \
                           len(spell_checker.unknown((w,))) == 0, ws),
                           candidate_words))

    for i in range(len(words)):
        for cw in candidate_words[i]:
            yield ' '.join(words[:i] + [cw] + words[i + 1:])