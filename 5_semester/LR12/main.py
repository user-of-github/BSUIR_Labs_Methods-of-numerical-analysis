import math
from task1 import get_1_task_solution
from task2 import get_2_task_solution
from task3 import get_3_task_solution


def solve_task1() -> None:
    k: int = 21
    a, b = math.sin(k), math.cos(k)
    interval: tuple[float, float] = (-1, 1)
    initials: tuple[float, float] = (0, 0)
    epsilon: float = 0.05
    get_1_task_solution(a, b, epsilon, interval, initials)


def solve_task2() -> None:
    Ua, Ub = 0, 5
    interval: tuple[float, float] = (-1, 1)
    epsilon: float = 0.001
    get_2_task_solution(epsilon, Ua, Ub, interval)


def solve_task3() -> None:
    epsilon: float = 0.01
    get_3_task_solution(epsilon)


def main() -> None:
    #solve_task1()
    #solve_task2()
    solve_task3()


if __name__ == '__main__':
    main()
