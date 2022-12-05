from byu_pytest_utils import max_score, with_import


@max_score(1)
@with_import
def test_last_letter_different(last_letter):
    observed = last_letter(["hi", "my", "name", "is", "Cosmo"])
    expected = {"i": ["hi"], "y": ["my"], "e": ["name"], "s": ["is"], "o": ["Cosmo"]}
    assert observed == expected


@max_score(2)
@with_import
def test_last_letter_same(last_letter):
    observed = last_letter(["stop", "tap", "mop", "chip", "loop"])
    expected = {"p": ["stop", "tap", "mop", "chip", "loop"]}
    assert observed == expected


@max_score(2)
@with_import
def test_last_letter_mixed(last_letter):
    observed = last_letter(
        ["What", "happens", "to", "an", "illegally", "parked", "frog?", "It", "gets", "toad", "away"])
    expected = {"t": ["What", "It"], "s": ["happens", "gets"], "o": ["to"], "n": ["an"], "y": ["illegally", "away"], "d": ["parked", "toad"], "?": ["frog?"]}
    assert observed == expected
