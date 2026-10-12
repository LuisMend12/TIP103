"""Tests for array_rank_transform (HackerRank: Rank Transform of an Array).

Run from this folder:  python -m pytest test_transformanarray.py -v
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from transformanarray import array_rank_transform

HERE = Path(__file__).parent
SCRIPT = HERE / "transformanarray.py"


# The three examples from the problem statement.
@pytest.mark.parametrize(
    "arr, expected",
    [
        ([40, 10, 20, 30], [4, 1, 2, 3]),
        ([100, 100, 100], [1, 1, 1]),
        ([37, 12, 28, 9, 100, 56, 80, 5, 12], [5, 3, 4, 2, 8, 6, 7, 1, 3]),
    ],
)
def test_problem_examples(arr, expected):
    assert array_rank_transform(arr) == expected


# Edge cases that follow straight from the definition of rank:
# smallest value gets 1, equal values share a rank, ranks have no gaps.
@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], []),                                   # empty input
        ([7], [1]),                                 # single element
        ([-5, 0, -5, 3], [1, 2, 1, 3]),             # negatives and a repeat
        ([1, 2, 3, 4], [1, 2, 3, 4]),               # already sorted
        ([4, 3, 2, 1], [4, 3, 2, 1]),               # reverse sorted
        ([10**9, -(10**9), 0], [3, 1, 2]),          # extreme values
    ],
)
def test_edge_cases(arr, expected):
    assert array_rank_transform(arr) == expected


def test_input_is_not_modified():
    arr = [40, 10, 20, 30]
    array_rank_transform(arr)
    assert arr == [40, 10, 20, 30]


def test_ranks_have_no_gaps():
    arr = [5, 50, 5, 500, 50]
    ranks = array_rank_transform(arr)
    assert sorted(set(ranks)) == list(range(1, len(set(arr)) + 1))


def test_large_input_runs_quickly():
    arr = list(range(100_000, 0, -1))
    assert array_rank_transform(arr)[0] == 100_000


def test_script_reads_stdin_like_hackerrank(tmp_path):
    """Runs the file the way HackerRank does: JSON arrays on stdin, results written to OUTPUT_PATH."""
    out_file = tmp_path / "out.txt"
    stdin = "\n".join(json.dumps(a) for a in ([40, 10, 20, 30], [100, 100, 100])) + "\n"
    subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=stdin,
        text=True,
        check=True,
        env={**os.environ, "OUTPUT_PATH": str(out_file)},
    )
    assert out_file.read_text().splitlines() == ["[4, 1, 2, 3]", "[1, 1, 1]"]
