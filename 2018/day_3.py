#!/usr/bin/env python3
import sys


def problem_1(fname):
    cells = {}
    with open(fname, "r") as f:
        for line in f.readlines():
            order, _, loc, dim = line.strip().split(" ", 3)
            x, y = [int(x) for x in loc.strip(":").split(",", 1)]
            width, height = [int(x) for x in dim.split("x", 1)]
            for cell_y in range(y, y + height):
                for cell_x in range(x, x + width):
                    cell_loc = "{0},{1}".format(cell_x, cell_y)
                    cells[cell_loc] = cells.get(cell_loc, 0) + 1
    return len([x for x in cells.values() if x > 1])


def problem_2(fname):
    cells = {}
    non_duplicated_orders = set([])
    with open(fname, "r") as f:
        for line in f.readlines():
            order, _, loc, dim = line.strip().split(" ", 3)
            non_duplicated_orders.add(order)
            x, y = [int(x) for x in loc.strip(":").split(",", 1)]
            width, height = [int(x) for x in dim.split("x", 1)]
            for cell_y in range(y, y + height):
                for cell_x in range(x, x + width):
                    cell_loc = "{0},{1}".format(cell_x, cell_y)
                    orders = cells.get(cell_loc, set([]))
                    orders.add(order)
                    cells[cell_loc] = orders
                    if len(orders) == 1:
                        continue
                    to_remove = list(orders) if len(orders) == 2 else [order]
                    for o in list(to_remove):
                        if o in non_duplicated_orders:
                            non_duplicated_orders.remove(o)
    return non_duplicated_orders.pop()

if __name__ == "__main__":
    print("Problem 1: {0}".format(problem_1(sys.argv[1])))
    print("Problem 2: {0}".format(problem_2(sys.argv[1])))
