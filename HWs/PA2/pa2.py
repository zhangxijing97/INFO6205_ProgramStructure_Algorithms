#!/usr/bin/env python3
"""
PA2: Dynamic Programming – All Construct Problem

Assignment Requirements:
--------------------------
(1) Subproblem Definition:
    - We want to determine all the different ways to construct a given target string using a list of words (wordbank).
    - Let F(target, wordbank) be the function that returns a 2D list of ways to build the target.
      For every word in the wordbank that is a prefix of the target, the problem reduces to solving for the suffix.
      The final result is assembled by prepending the matched word to every solution obtained for the suffix.
    - Base Case: When the target is empty (""), return [[]] representing one valid way (using no words).

(2) Decisions and Recursion:
    - Recursively check each word in the wordbank.
    - Use memoization (caching results in a dictionary) to speed up repeated subproblems.
    - As required by the assignment, print the solution for each subproblem as they are solved.
    
(3) Error Handling:
    - The program checks that the required command-line arguments are provided.
    - If arguments are missing or invalid, it prints a usage message and exits gracefully.

Usage:
------
Run the program from the command line:
    python pa2.py --target <target string> --wordbank <list of words>

Example:
    python pa2.py --target purple --wordbank purp p ur le purpl

(5) Example 1 execution output:

(base) zhangxijing@MacBook-Air PA2 % python pa2.py --target purple --wordbank purp p ur le purpl
Solving subproblem for target: 'purple'
Solving subproblem for target: 'le'
Completed subproblem for target: 'le' with solutions: [['le']]
Solving subproblem for target: 'urple'
Solving subproblem for target: 'ple'
Completed subproblem for target: 'ple' with solutions: [['p', 'le']]
Completed subproblem for target: 'urple' with solutions: [['ur', 'p', 'le']]
Solving subproblem for target: 'e'
Completed subproblem for target: 'e' with solutions: []
Completed subproblem for target: 'purple' with solutions: [['purp', 'le'], ['p', 'ur', 'p', 'le']]

--------------------------
Number of ways: 2
[
['purp', 'le']
['p', 'ur', 'p', 'le']
]
Runtime: 0.000040 seconds

"""

import sys
import time

def all_construct(target, wordbank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]

    # Print the subproblem being solved.
    print(f"Solving subproblem for target: '{target}'")

    ways = []
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, wordbank, memo)
            # Prepend the chosen word to the solutions for the suffix.
            target_ways = [[word] + way for way in suffix_ways]
            ways.extend(target_ways)

    memo[target] = ways
    # Print the solutions for this subproblem.
    print(f"Completed subproblem for target: '{target}' with solutions: {ways}")
    return ways

def main():
    # Check that the program received the required arguments.
    if len(sys.argv) < 3:
        print("Usage: pa2.py --target <target string> --wordbank <list of words>")
        sys.exit(1)

    try:
        target_index = sys.argv.index("--target") + 1
        wordbank_index = sys.argv.index("--wordbank") + 1
    except ValueError:
        print("Error: Arguments --target and --wordbank are required.")
        sys.exit(1)

    target = sys.argv[target_index]
    wordbank = sys.argv[wordbank_index:]

    start_time = time.time()
    result = all_construct(target, wordbank)
    end_time = time.time()
    runtime = end_time - start_time

    # Output the result in the required format.
    print("\n--------------------------")
    print(f"Number of ways: {len(result)}")
    print("[")
    for combination in result:
        print(combination)
    print("]")
    print(f"Runtime: {runtime:.6f} seconds")

if __name__ == "__main__":
    main()