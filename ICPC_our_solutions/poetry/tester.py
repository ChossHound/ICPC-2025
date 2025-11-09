#!/usr/bin/env python3

"""
Local testing tool for Poetic Tournament.

Note: This tool is intended to help with debugging interaction.
It is *not* the same code used to test your solution when it
is submitted. For example, the tool *does not* apply the time
and memory limits that are applied to submitted solutions,
and there may be other differences, especially if your solution
exhibits incorrect behavior. For this problem specifically, this
testing tool does not test whether your queries prove the identity
of the top k.

To run the testing tool, run::

    pypy3 testing_tool.py -v -f <filename> <n> <k> <program> <arguments>

where `arguments` are optional arguments to the program to run. The following
show examples for different languages:

    pypy3 testing_tool.py -v 100 4 ./myprogram
    pypy3 testing_tool.py -v 100 4 java -cp . MyProgram
    pypy3 testing_tool.py -v 100 4 pypy3 myprogram.py

When included, the optional argument '-v' prints the interaction to standard out.

When included, the optional argument '-f <filename>' uses preset skill levels
for all applicants. Otherwise, skill levels are determined randomly. filename
should contain a space-seperated list of n integers representing the skill
levels of all applicants. These integers should all be unique.

<n> should be the number of applicants.
<k> should be the number of applicants that get to advance.
"""

import argparse
import subprocess
import sys
from typing import TextIO
import random

class WrongAnswer(RuntimeError):
    """Raised whenever an incorrect answer is received."""
    pass

def vprint(*args, verbose: bool, file: TextIO, **kwargs) -> None:
    """Print to `file`, and also to stdout if `verbose is true."""
    if verbose:
        print('< ', end='')
        print(*args, **kwargs)
        sys.stdout.flush()
    print(*args, file=file, **kwargs)


def vreadline(data: TextIO, verbose: bool) -> str:
    """Read a line from `data`, and also log it to stdout if `verbose` is true."""
    line = data.readline()
    if verbose and line:
        print('>', line.rstrip('\n'))
    return line

count_queries = 0
def answer_query(process: subprocess.Popen, order: list[int], topk: set[int], verbose=True) -> None:
    """Handle one query."""
    global count_queries
    line = vreadline(process.stdout, verbose)
    if line == '':
        raise WrongAnswer('End of file received from team program')
    qtype, *params = line.split()
    if qtype == '!':
        try:
            if len(params) != len(topk):
                raise WrongAnswer("incorrect number of tokens in answer")
            params = set(map(int, params))
        except ValueError:
            raise WrongAnswer('Question contains non-integer tokens')
        
        if params == topk:
            print(f'Correct answer in {count_queries} queries')
            print('Your queries may or may not prove the identity of the top k')
        else:
            raise WrongAnswer('Incorrectly identified the top k')
        return True
    elif qtype == '?':
        count_queries += 1

        if not verbose and count_queries % 20_000 == 0:
            print(f'Processed {count_queries} queries...')

        if count_queries > 12 * len(order) + 1_000: # the limit number of queries
            raise WrongAnswer('Used too many queries')
    
        try:
            if len(params) != 2:
                raise WrongAnswer("incorrect number of tokens in query")
            a, b = map(int, params)
        except ValueError:
            raise WrongAnswer('Question contains non-integer tokens')
        
        if a == b: raise WrongAnswer('Query a and b must be distinct')

        if not (1 <= a <= len(order)): raise WrongAnswer(f'{a} out of range [1, {len(order)}]')
        if not (1 <= b <= len(order)): raise WrongAnswer(f'{b} out of range [1, {len(order)}]')

        vprint(a if order[a-1] > order[b-1] else b, file=process.stdin, flush=True, verbose=verbose)

        return False
        
    else:
        raise WrongAnswer(f'Unknown query type {qtype}')

def check_done(process: subprocess.Popen) -> None:
    """Check for extra output from program."""
    line = vreadline(process.stdout, True)
    if line != '':
        raise WrongAnswer('Program gave extra output')


def main() -> int:
    parser = argparse.ArgumentParser(usage='%(prog)s [-h] --file file.txt n k program [args...]')
    parser.add_argument('-v','--verbose', action='store_true', help='output interactions')
    parser.add_argument('-f','--file', type=str, help='filename containing skill levels')
    parser.add_argument('n', type=int, help='the number of applicants')
    parser.add_argument('k', type=int, help='the number of advancing applicants')
    parser.add_argument('program', nargs=argparse.REMAINDER)

    args = parser.parse_args()

    if not args.program:
        parser.error('Must specify program to run')

    if not args.n or not args.k:
        parser.error('Must specify the number of applicants and advancement slots')

    n = args.n
    k = args.k

    verbose = args.verbose

    print(f'n = {n}, k = {k}')

    if not args.file:
        print('Using random skill levels.')
        order = list(range(n))
        random.shuffle(order)
    else:
        print(f'Using skill levels from {args.file}')
        with open(args.file, 'r') as f:
            try:
                order = list(map(int,f.read().strip().split()))
                assert len(order) == n, f"{args.file} does not contain {n} skill levels"
                assert len(set(order)) == n, "all skill levels must be unique"
            except Exception as e:
                print("ERROR: %s" % e)
                return 1

    prog_exec = ' '.join(args.program)
    print(f'Running program "{prog_exec}"')

    if verbose: print('Printing interactions')
    else: print('Hiding interaction output')

    topk = sorted(range(1,n+1), key=lambda x: order[x-1])[-k:]
    topk = set(topk)

    process = subprocess.Popen(args.program, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               encoding='utf-8', errors='surrogateescape')
    
    try:
        vprint(n,k, file=process.stdin, flush=True, verbose=verbose)
        while True:
            if answer_query(process, order, topk, verbose=verbose):
                break
        check_done(process)
    except WrongAnswer as e:
        print('ERROR: %s' % e)
        vprint("-1", file=process.stdin, flush=True, verbose=verbose)
        return 1
    except BrokenPipeError:
        print('ERROR: error when communicating with program - exited prematurely?')
        return 2
    
    return 0


if __name__ == '__main__':
    sys.exit(main())