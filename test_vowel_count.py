from byu_pytest_utils import max_score, with_import


@max_score(2)
@with_import
def test_vowel_count_mixed(vowel_count):
    observed = vowel_count(["Hey!", "How", "have", "you", "been?"])
    expected = {1: ["Hey!", "How"], 2: ["have", "you", "been?"]}
    assert observed == expected


@max_score(1)
@with_import
def test_vowel_count_same(vowel_count):
    observed = vowel_count(["Hi", "I'm", "well", "thanks"])
    expected = {1: ["Hi", "I'm", "well", "thanks"]}
    assert observed == expected


@max_score(2)
@with_import
def test_vowel_count_different(vowel_count):
    observed = vowel_count(["a", "book", "about", "treasure"])
    expected = {1: ["a"], 2: ["book"], 3: ["about"], 4: ["treasure"]}
    assert observed == expected
