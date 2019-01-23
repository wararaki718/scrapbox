import os

import papermill as pm


def hello_call(parameters):
    base_notebook_path = os.path.join(os.path.dirname(__file__), 'base.ipynb')

    nb = pm.execute_notebook(
        base_notebook_path,
        'out.ipynb',
        parameters=parameters,
        log_output=True
    )
    return nb

