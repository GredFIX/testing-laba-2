def validate_salary(salary: int):
    if 70000 > salary or salary > 750000:
        raise ValueError('Salary must be [70000...750000]')
    elif type(salary) != int:
        raise TypeError('Salary must be integer')


def validate_pref_review(pref_review: float):
    if 1 > pref_review or pref_review > 5:
        raise ValueError('Pref_review must be [1...5]')


def validate_level(level: int):
    if 7 > level or level > 17:
        raise ValueError('Level must be [7...17]')


def calc_level_bonus(level: int) -> float:
    validate_level(level)
    if level < 10:
        return 1.05
    elif 10 <= level < 13:
        return 1.1
    elif 13 <= level < 15:
        return 1.15
    elif 15 <= level:
        return 1.2


def calc_bonus_modifier(pref_review: float) -> float:
    validate_pref_review(pref_review)
    if pref_review < 2:
        return 0
    elif 2 <= pref_review < 2.5:
        return 0.25
    elif 2.5 <= pref_review < 3:
        return 0.5
    elif 3 <= pref_review < 3.5:
        return 1
    elif 3.5 <= pref_review < 4:
        return 1.5
    elif 4 <= pref_review:
        return 2


def calc_bonus(salary: int, pref_review: float, level: int) -> float:
    validate_salary(salary)
    return round(calc_bonus_modifier(pref_review) * calc_level_bonus(level) * salary)


if __name__ == '__main__':
    assert calc_bonus(75000, 3, 20) == 90000
