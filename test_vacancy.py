from vacancy import Vacancy

def test_Vacancy_eq():
    a1 = Vacancy("back", 10_000, 20_000)
    a2 = Vacancy("back", 10_000, 20_000)
    a3 = Vacancy("bac", 10_000, 20_000)
    assert a1 == a2
    assert a1 != a3
    assert a1 != 2


def test_Vacancy_lt():
    a1 = Vacancy("", 10_000, 20_000)
    a2 = Vacancy("", 20_000, 30_000)
    a3 = Vacancy("", 5_000, 6_000)
    a4 = Vacancy("", None, 5_000)
    a5 = Vacancy("", 5_000, None)
    assert a1 < a2
    assert a1 > a3
    assert a2 > a4
    assert a1 > a4
    assert a5 < a3


def test_Vacancy_le():
    a1 = Vacancy("", 10_000, 20_000)
    a2 = Vacancy("", 10_000, 20_000)
    a3 = Vacancy("", 5_000, 6_000)
    a4 = Vacancy("", None, 5_000)
    a5 = Vacancy("", 5_000, None)
    assert a1 <= a2
    assert a1 >= a3
    assert a2 >= a4
    assert a1 >= a4
    assert a5 <= a3