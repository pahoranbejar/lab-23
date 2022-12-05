from byu_pytest_utils import max_score, with_import


@max_score(1)
@with_import
def test_letter_count_same_max_letter_frequency(letter_count):
    observed = letter_count(["wood", "book", "took", "odor", "sleep"])
    expected = {2: ["wood", "book", "took", "odor", "sleep"]}
    assert observed == expected


@max_score(2)
@with_import
def test_letter_count_two_different_max_letter_frequencies(letter_count):
    observed = letter_count(["spoke", "book", "odor", "lemur"])
    expected = {1: ["spoke", "lemur"], 2: ["book", "odor"]}
    assert observed == expected


@max_score(2)
@with_import
def test_letter_count_three_different_max_letter_frequencies(letter_count):
    observed = letter_count(["spoke", "book", "needle", "odor", "lemur", "cheese"])
    expected = {1: ["spoke", "lemur"], 2: ["book", "odor"], 3: ["needle", "cheese"]}
    assert observed == expected
