import numpy
import pandas
from matplotlib import pyplot as plt
from tabulate import tabulate


def visualize_results(data: tuple[list, list], print_table: bool = False) -> None:
    plt.plot(data[0], data[1], mew=2, ms=10)
    plt.show()

    if not print_table:
        return

    df = pandas.DataFrame({'x': data[0], 'y': data[1]})
    print(df)

    xx = numpy.array(data[0])
    yy = numpy.array(data[1])

    col_headers = ['x', 'y']

    merged_array = numpy.array([xx, yy]).T

    table = tabulate(merged_array, col_headers, tablefmt='fancy_grid', floatfmt='.4f')
    print(table)


def visualize_both(first: tuple[list, list], second: tuple[list, list]) -> None:
    fig, (ax1, ax2) = plt.subplots(2)

    fig.suptitle('Compare')
    ax1.plot(*first)
    ax2.plot(*second)

    plt.show()