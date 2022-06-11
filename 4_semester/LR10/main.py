import data
from koshi_solution_by_adams import koshi_by_adams_explicit
from koshi_solution_by_adams_implicit import koshi_by_adams_implicit
from visualize import visualize_results, visualize_both


def main() -> None:
    # https://ru.wikipedia.org/wiki/Метод_Адамса
    explicit_solution = koshi_by_adams_explicit(data.function, data.INTERVAL, 0.01, data.START_CONDITION, data.A[6], data.M[6])
    implicit_solution = koshi_by_adams_implicit(data.function, data.INTERVAL, 0.01, data.START_CONDITION, data.A[6], data.M[6])

    visualize_results((implicit_solution[0], implicit_solution[1]), True)
    #visualize_both(explicit_solution, implicit_solution)




if __name__ == '__main__':
    main()
