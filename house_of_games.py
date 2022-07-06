#!/usr/bin/env python3
"""
House of Games
==============

Helper script to generate House of Games prompts.

Generates potential House of Games prompts from a given answer. 

Covers:

* Mouse of Games, replaces one letter in the input.

* House of Gamers, adds an additional letter to the input.

* Hose of Gamers, removes one letter from the input.
"""

import itertools
from hose_of_games import hose_of_games
from mouse_of_games import mouse_of_games
from house_of_gamers import house_of_gamers
import argparse
import sys
from spellchecker import SpellChecker


def generate_house_of_games(args):
    sp = SpellChecker(local_dictionary=args.dictionary)
    if args.blocked_words:
        words = list(map(lambda s: s.rstrip(), args.blocked_words.readlines()))
        sp.word_frequency.remove_words(words)

    if args.input:
        args.lines += args.input.readlines()

    it = iter(())
    for l in args.lines:
        if args.gamers:
            it = itertools.chain(it, house_of_gamers(l, sp))
        if args.mouse:
            it = itertools.chain(it, mouse_of_games(l, sp))
        if args.hose:
            it = itertools.chain(it, hose_of_games(l, sp))
    for i in it:
        print(i, file=sys.stdout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate House of Games from input"
    )
    parser.add_argument(
        "-r",
        "--gamers",
        help="Generates House of Gamers prompts",
        action="store_true",
    )
    parser.add_argument(
        "-m", "--mouse", help="Gernates Mouse of Games prompts", action="store_true"
    )
    parser.add_argument(
        "-s", "--hose", help="Generates Hose of Games prompts", action="store_true"
    )
    parser.add_argument(
        "-d", "--dictionary", help="Use a local dictionary file.", default=None
    )
    parser.add_argument(
        "-i", "--input", help="Use a local argument file.", type=open
    )
    parser.add_argument(
        "-b",
        "--blocked-words",
        help="File containing list of words to remove from dictionary",
        type=open,
        default="in/blocked_words.txt",
    )
    parser.add_argument("lines", nargs="*")

    parser.set_defaults(func=generate_house_of_games)

    args = parser.parse_args()
    if not vars(args):
        parser.print_help(sys.stderr)
    else:
        args.func(args)

