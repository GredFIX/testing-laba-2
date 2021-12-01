import pytest
from calc_salary_bonus import calc_bonus


@pytest.mark.parametrize(
    "salary, pref_review, level, expected_error",
    [
        (60000, 1, 7, ValueError),
        (800000, 1, 7, ValueError),
        (150000, 6, 7, ValueError),
        (150000, 0.5, 7, ValueError),
        (150000, 1, 20, ValueError),
        (150000, 1, 5, ValueError),
        (150000.5, 1, 7, TypeError),
        ("foo", 1, 7, TypeError),
        (150000, "foo", 7, TypeError),
        (150000, 1, "foo", TypeError),
    ],
)
def test_calculate_salary_bonus_error(salary, pref_review, level, expected_error):
    with pytest.raises(expected_error):
        calc_bonus(salary, pref_review, level)


@pytest.mark.parametrize(
    "salary, pref_review, level, expected_result",
    [
        (100000, 1, 17, 0),
        (100000, 5, 14, 230000),
        (100000, 2, 7, 26250),
        (100000, 3, 17, 120000),
        (100000, 2.5, 11, 55000),
        (100000, 3.5, 11, 165000),
        (150000, 1, 11, 0),
        (150000, 5, 7, 315000),
        (150000, 3, 14, 172500),
        (150000, 2.5, 7, 78750),
        (150000, 3.5, 17, 270000),
        (400000, 5, 17, 960000),
        (400000, 2, 14, 115000),
        (400000, 3, 7, 420000),
        (400000, 2.5, 17, 240000),
        (750000, 1, 14, 0),
        (750000, 5, 11, 1650000),
        (750000, 2, 17, 225000),
        (750000, 3.5, 7, 1181250),
    ],
)
def test_calculate_salary_bonus(salary, pref_review, level, expected_result):
    assert expected_result == calc_bonus(salary, pref_review, level)
