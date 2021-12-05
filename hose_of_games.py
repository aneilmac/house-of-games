#!/usr/bin/python
# -*- coding: utf-8 -*-

# Goes through all christmas movies in `xmas_films.txt` and
# generates all potential "Hose of Gamers versions", a test of validity
# is done by running a spellchecker over the title afterwords.


def __removechar(line, i):
    """
    Given a string and an index, removes the character at that index. 
    Attempts to respect the capitalization of the removed character in the remaining characters.
    Returns a blank string if attempting to remove a non-alpha character.
    E.g. "Hello" can become "Ello, Hllo, Helo, Helo, Hell."
    """

    if not line[i].isalpha():
        return ''

    if i < len(line) - 1:
        c = line[i + 1]
        if line[i].isupper():
            c = c.upper()
    else:
        c = ''
    return line[:i] + c + line[i + 2:]


def __alts(line):
    """
    Given a movie title, returns the list of all potential candidate movie titles, removing 
    one character in turn.
    E.g. "Hello" can become "Ello, Hllo, Hlo, Hlo, Ho."
    """

    return filter(lambda w: w != '', (__removechar(line, i).strip()
                  for i in range(len(line))))


def hose_of_games(line, spell_checker):
    """
    Takes a string and spell checker, generates all "Hose of Games" 
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