#!/usr/bin/env python3
# Goes through all christmas movies in `xmas_films.txt` and
# generates all potential "Mouse of Games versions", a test of validity
# is done by running a spellchecker over the title afterwords.

import itertools


def _altrange(c):
    """
    Given a character, returns the range of characters excluding the passed 
    character. E.g. if given 'a', will return 'bcdefghijklmnopqrstyvwxyz'. If 
    given 'B', will return 'ACDEFGHIJKLMNOPRQRSTUVWXYZ'. This function respects 
    the case of the passed character. If given a non-alpha character returns an 
    empty iterator.
    """

    if not c.isalpha():
        return iter(())
    else:
        (c1, c2) = ("A", "Z") if c.isupper() else ("a", "z")
        return map(
            chr,
            itertools.chain(
                range(ord(c1), ord(c)), range(ord(c) + 1, ord(c2) + 1)
            ),
        )


def _alts(line):
    """
    Given a movie title, returns the list of all potential candidate movie 
    titles, replacing each character in turn with all possible other valid 
    characters. E.g. `Hello` becomes `[Aello, Bello, Cello, ..., Helly, Hellz]`.
    """

    it = iter(())
    for i in range(len(line)):
        alts = zip(_altrange(line[i]), itertools.cycle((i,)))
        it = itertools.chain(
            it, (line[:i] + a + line[i + 1 :] for (a, i) in alts)
        )
    return it


def mouse_of_games(line, spell_checker):
    """
    Takes a string and spell checker, generates all 'Mouse of Games'
    possibilities on the string then filters these by the spellchecker.
    """

    words = line.split()
    candidate_words = map(_alts, words)
    filtered_words = list(
        map(
            lambda ws: filter(
                lambda w: len(spell_checker.unknown((w,))) == 0, ws
            ),
            candidate_words,
        )
    )

    for i in range(len(words)):
        for cw in filtered_words[i]:
            yield " ".join(words[:i] + [cw] + words[i + 1 :])
