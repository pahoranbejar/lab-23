from byu_pytest_utils import max_score, with_import


@max_score(1)
@with_import
def test_first_vowel_same_first_vowel(first_vowel):
    observed = first_vowel(["hello", "see", "where", "cheese", "leap"])
    expected = ["hello", "see", "where", "cheese", "leap"]
    assert observed == expected


@max_score(2)
@with_import
def test_first_vowel_two_first_vowels(first_vowel):
    observed = first_vowel(["hello", "saw", "what", "cheese", "leap"])
    expected = ["hello", "cheese", "leap"]
    assert observed == expected


@max_score(2)
@with_import
def test_first_vowel_many_first_vowels(first_vowel):
    observed = first_vowel(["hello", "saw", "what", "cheese", "money", "mice", "leap"])
    expected = ["hello", "cheese", "leap"]
    assert observed == expected
