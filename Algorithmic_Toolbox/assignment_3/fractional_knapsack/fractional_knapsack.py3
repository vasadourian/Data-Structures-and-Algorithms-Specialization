import sys
from collections import namedtuple

pairs = namedtuple("Item", "value weight")


def get_optimal_value(capacity, weights, values):

    value = 0

    value_by_weight = sorted(
        [pairs(v, w) for v, w in zip(values, weights)],
        key=lambda i: i.value / i.weight,reverse=True)
    

    
    cap_left = int(capacity)
    for item in value_by_weight:

        # If the item fit into the knapsack, put it and recalculate space left.
        if cap_left - item.weight >= 0:
            value += item.value
            cap_left -= item.weight
        else:
            # Otherwise calculate weight of unit of the item and fill
            # the knapsack's left space.
            value += (item.value / item.weight) * cap_left
            cap_left = 0
        if not cap_left:
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
