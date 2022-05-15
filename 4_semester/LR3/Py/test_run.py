from half_division_method import get_root_by_half_division
from chord_method import get_root_by_chord_method
from sturm_method import get_number_of_roots_by_sturm_theorem
from newton_method import get_root_by_newton_method


def test_run(equation: list, range_from: float, range_to: float, error: float) -> None:
    number_of_roots: int = get_number_of_roots_by_sturm_theorem(equation, range_from, range_to)

    print(f'According Sturm\'s theorem there are {number_of_roots} roots on range [{range_from} .. {range_to}]\n')

    # The following values are taken from chart (Maple)
    look_for_from: float = -1
    look_for_to: float = 1

    root, iterations_count = get_root_by_half_division(equation, look_for_from, look_for_to, error)
    print(f'[Half-division-method]: Got x = {root} | Needed {iterations_count} iterations')

    root, iterations_count = get_root_by_newton_method(equation, look_for_from, look_for_to, error)
    print(f'[Newton-method]: Got x = {root} | Needed {iterations_count} iterations')

    root, iterations_count = get_root_by_chord_method(equation, look_for_from, look_for_to, error)
    print(f'[Chord-method]: Got x = {root} | Needed {iterations_count} iterations')


