'''
execute notebook via papermill
'''
import sys

import papermill as pm


def main():
    pm.execute_notebook(
        'notebooks/base.ipynb',
        'notebooks/output.ipynb',
        parameters = {'alpha': 10, 'beta': 20}
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
