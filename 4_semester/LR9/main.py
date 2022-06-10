import data
from get_koshi_solution_by_eiler import koshi_problem_solution_by_euler
from get_koshi_solution_by_runge_kutt import koshi_problem_solution_by_runge_kutt


def main() -> None:
    koshi_problem_solution_by_euler(data.function, data.INTERVAL, 0.01, data.START_CONDITION, data.A[6], data.M[6])
    # koshi_problem_solution_by_runge_kutt(data.function, data.INTERVAL, 0.01, data.START_CONDITION, data.A[6], data.M[6])


if __name__ == '__main__':
    main()
