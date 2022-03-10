import data
from half_division_method import get_root_by_half_division
from chord_method import get_root_by_chord_method
from sturm_method import get_number_of_roots_by_sturm_theorem
from newton_method import get_root_by_newton_method


def test_run() -> None:
    number_of_roots: int = get_number_of_roots_by_sturm_theorem(data.TEST_EQUATION, data.RANGE_FROM, data.RANGE_TO)

    print(f'According Sturm\'s theorem there are {number_of_roots} roots on range [{data.RANGE_FROM} .. {data.RANGE_TO}]\n')

    # The following values are taken from chart (Maple)
    look_for_from: float = 0
    look_for_to: float = 2

    root, iterations_count = get_root_by_half_division(data.TEST_EQUATION, look_for_from, look_for_to, data.ERROR)
    print(f'[Half-division-method]: Got x = {root} | Needed {iterations_count} iterations')

    root, iterations_count = get_root_by_chord_method(data.TEST_EQUATION, look_for_from, look_for_to, data.ERROR)
    print(f'[Chord-method]: Got x = {root} | Needed {iterations_count} iterations')

    root, iterations_count = get_root_by_newton_method(data.TEST_EQUATION, look_for_from, look_for_to, data.ERROR)
    print(f'[Newton-method]: Got x = {root} | Needed {iterations_count} iterations')
