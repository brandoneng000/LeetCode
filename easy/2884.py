import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.salary *= 2

    return employees


# def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
#     employees.loc[:, 'salary'] = [s * 2 for s in employees.loc[:, 'salary']]

#     return employees