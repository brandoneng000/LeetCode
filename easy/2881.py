import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.insert(2, "bonus", [salary * 2 for salary in employees['salary']])

    return employees