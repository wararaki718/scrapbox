import sys

import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx


def main():
    options = {
        'c1': 0.5,
        'c2': 0.3,
        'w': 0.9
    }

    optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2, options=options)
    best_cost, best_pos = optimizer.optimize(fx.sphere, iters=100)
    print(best_cost)
    print(best_pos)

    return 0


if __name__ == '__main__':
    sys.exit(main())
