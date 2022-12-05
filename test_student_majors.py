from byu_pytest_utils import max_score, with_import


@max_score(1)
@with_import
def test_student_majors_same_major(student_majors):
    observed = student_majors({"Mark Zuckerberg": "Computer Science", "Larry Page": "Computer Science"})
    expected = {"Computer Science": ["Mark Zuckerberg", "Larry Page"]}
    assert observed == expected


@max_score(2)
@with_import
def test_student_majors_different_majors(student_majors):
    observed = student_majors({"Nik Day": "Music", "Jimmer Fredette": "American Studies", "Brandon Sanderson": "English", "Lindsey Stirling": "Recreation Management"})
    expected = {"Music": ["Nik Day"], "American Studies": ["Jimmer Fredette"], "English": ["Brandon Sanderson"], "Recreation Management": ["Lindsey Stirling"]}
    assert observed == expected


@max_score(2)
@with_import
def test_student_majors_mixed_majors(student_majors):
    observed = student_majors({"Nik Day": "Music", "Jimmer Fredette": "American Studies", "Brandon Sanderson": "English", "Lindsey Stirling": "Recreation Management", "Mark Zuckerberg": "Computer Science", "Larry Page": "Computer Science", "Katherine Johnson": "Mathmatics", "Elon Musk": "Physics", "Isaac Newton": "Mathmatics"})
    expected = {'Music': ['Nik Day'], 'American Studies': ['Jimmer Fredette'], 'English': ['Brandon Sanderson'], 'Recreation Management': ['Lindsey Stirling'], 'Computer Science': ['Mark Zuckerberg', 'Larry Page'], 'Mathmatics': ['Katherine Johnson', 'Isaac Newton'], 'Physics': ['Elon Musk']}
    assert observed == expected
