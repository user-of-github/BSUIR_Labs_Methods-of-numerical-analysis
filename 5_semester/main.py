import math

from task1 import get_1_task_solution


def main() -> None:
    # task 1
    k: int = 21
    a, b = math.sin(k), math.cos(k)
    interval: tuple[float, float] = (-1, 1)
    initials: tuple[float, float] = (0, 0)
    get_1_task_solution(a, b, 0.001, interval, initials)


if __name__ == '__main__':
    main()

