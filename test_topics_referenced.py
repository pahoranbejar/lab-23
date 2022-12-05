from byu_pytest_utils import max_score, with_import, test_files


@max_score(5)
@with_import
def test_topics_referenced(topics_referenced):
    observed = topics_referenced(
        test_files / "fruit.txt",
        {"apple": "fruit", "banana": "fruit", "orange": "fruit", "pears": "fruit",
         "car": "vehicles", "truck": "vehicles",
         "tree": "plants", "grass": "plants", "flowers": "plants"
         })
    expected = {"fruit": 3, "vehicles": 1, "plants": 4}
    assert observed == expected
