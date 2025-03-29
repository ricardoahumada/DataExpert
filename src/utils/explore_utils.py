import pandas as pd
from tabulate import tabulate
from . import print_utils as pu

def explr(df):
    print(pu.headr('Columnas:'))
    print(df.columns.to_list())
    print(pu.headr('Numéricas'))
    pu.tabl(df.describe())
    print(pu.headr('Categóricas'))
    pu.tabl(df.describe(include=object))
