import pytest
import calc_salary_bonus as calc
from allpairspy import AllPairs

salaries = list(range(68000, 751001, 1000))
levels = list(range(6, 19))
perf_results = list(round(x * 1.0, 1) for x in range(1, 5))
parameters = [salaries, levels, perf_results]

for parameter in parameters:
    parameter.extend(["foo", None])

pair_for_test = [pair for pair in AllPairs(parameters)]


@pytest.mark.parametrize(
    "salary, expected_error",
    [
        (50000, ValueError),
        (80000.5, TypeError),
        (800000, ValueError),
        ("foo", TypeError),
        (None, TypeError)
    ]
)
def test_validate_salary_error(salary, expected_error):
    with pytest.raises(expected_error):
        calc.validate_salary(salary)


@pytest.mark.parametrize(
    "salary, expected_result",
    [
        (75000, None),
        (500000, None),
        (750000, None),
    ]
)
def test_validate_salary_error(salary, expected_result):
    assert calc.validate_salary(salary) == expected_result


@pytest.mark.parametrize(
    "pref_review, expected_result",
    [
        (1, 0),
        (2, 0.25),
        (2.5, 0.5),
        (3, 1),
        (3.5, 1.5),
        (5, 2),
    ]
)
def test_pref_review(pref_review, expected_result):
    assert calc.calc_bonus_modifier(pref_review) == expected_result


@pytest.mark.parametrize(
    "pref_review, expected_error",
    [
        (0, ValueError),
        (6, ValueError),
        ("foo", TypeError),
        (None, TypeError)
    ]
)
def test_pref_review_error(pref_review, expected_error):
    with pytest.raises(expected_error):
        calc.calc_bonus_modifier(pref_review)


@pytest.mark.parametrize(
    "level, expected_result",
    [
        (7, 1.05),
        (10, 1.1),
        (13, 1.15),
        (17, 1.2)
    ]
)
def test_level(level, expected_result):
    assert calc.calc_level_bonus(level) == expected_result


@pytest.mark.parametrize(
    "level, expected_error",
    [
        (6, ValueError),
        (18, ValueError),
        ("foo", TypeError),
        (None, TypeError)
    ]
)
def test_level_error(level, expected_error):
    with pytest.raises(expected_error):
        calc.calc_level_bonus(level)


@pytest.mark.parametrize(
    "salary, pref_review, level",
    pair_for_test,
)
def test_calculate_salary_bonus(salary, pref_review, level):
    errors = (ValueError, TypeError)
    try:
        with pytest.raises(errors):
            calc.calc_bonus(salary, pref_review, level)
    except:
        assert calc_bonus(salary, pref_review, level) not in errors, "Бонус к зарплате расчитан без ошибок"
