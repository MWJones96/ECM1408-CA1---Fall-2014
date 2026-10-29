# ECM1408 Assignment 1 - Fall 2014

Python solutions to the first continuous assessment for the University of Exeter module ECM1408 Programming for Science (autumn 2014).

## Overview

The assessment (see `Specification.pdf`) was an individual exercise covering functions, loops, lists and conditionals. This repository holds solutions redone six years on, in 2020, rather than the original 2014 submission. Each question's solution lives in its own file, `q1.py` to `q5.py`, instead of the file names the specification asks for.

## What's implemented

| File | Question | What it does |
| --- | --- | --- |
| `q1.txt`, `q1.py` | 1. Syntax errors | `q1.txt` lists the syntax errors in the specification's `find_first` snippet; `q1.py` is the corrected code, which prints the index of `'three'` in a sample list. |
| `q2.py` | 2. Diagonally | `diagonal(text, right_to_left=False)` prints a string diagonally without indexing, and prints `slantwise` in both directions. |
| `q3.py` | 3. Making change | `make_change(amount, coins)` gives change greedily from a descending list of denominations, or prints `Sorry. Change not available`. Runs the eight amount and denomination cases from the specification. |
| `q4.py` | 4. Ring of stars | `star(...)` draws an n-pointed star from its outer and inner radii; `ring(...)` draws a ring of filled stars. Draws an EU-style flag of 12 gold five-pointed stars on blue. |
| `q5.py` | 5. Train passengers | `is_train_possible(capacity, stations)` checks whether a train's recorded passenger counts are consistent. It reads `train1.txt` to `train4.txt` and prints `possible` or `impossible` for each. |

## Tech stack

Python 3, standard library only (`math` and `turtle`). The specification asks for the course's `exturtle` module in question 4; `q4.py` uses the standard `turtle` module instead.

## Getting started

You need Python 3, and Tk support for `q4.py`, which opens a turtle graphics window.

Run each question from the repository root:

```
python q#.py
```

Run it from the root because `q5.py` opens the train data files by relative path.

## Project structure

```
Specification.pdf         Assessment brief
q1.txt                    Question 1 answer: list of syntax errors
q1.py ... q5.py           Solutions to questions 1-5
train1.txt ... train4.txt Sample train data for question 5
```

Each train file starts with a line holding the capacity and the number of stations. Each following line holds the number of people who left, entered and had to wait at a station.

## Status

The repository is complete and archived. The row of 5-, 6-, 7- and 8-pointed stars that question 4 asks for is left in `q4.py` as a commented-out block. Only the ring is drawn.

## Acknowledgements

The assessment brief is from ECM1408 Programming for Science at the University of Exeter. The train passengers problem in question 5 is credited in the brief to the UK and Ireland Programming Contest.
