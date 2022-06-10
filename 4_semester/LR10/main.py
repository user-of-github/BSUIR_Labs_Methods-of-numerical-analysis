import data

from koshi_solution_by_adams import koshi_by_adams


def main() -> None:
    koshi_by_adams(data.function, data.INTERVAL, 0.01, data.START_CONDITION, data.A[6], data.M[6])
    # koshi_problem_solution_by_runge_kutt(data.function, data.INTERVAL, 0.01, data.START_CONDITION, data.A[6], data.M[6])


if __name__ == '__main__':
    main()