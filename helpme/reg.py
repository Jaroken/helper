import numpy as np
import pandas as pd

def logform(df, x, y):
    """A function to create a plot line for the resulting formula and the formula itself for a univariate logistic regression
    params:
    df: Pandas DataFrame
    x: independent variable name (string)
    y: dependent variable name (string)"""
    ind = np.array(list(df[x])) 
    dep = np.array(list(df[y]))
    fit = np.polyfit(np.log(ind), dep, 1)
    fitted_line = fit[1]+fit[0]*np.log(list(range(1,int(round(np.max(ind))))))
    formula1 = 'y = '+str(round(fit[1],3)) 
    if fit[0] > 0:
        formula2 = ' + '+str(round(fit[0],3)) 
    if fit[0] < 0:
        formula2 = ' - '+str(abs(round(fit[0],3)))
    formula3 = ' * LN(x)'
    formula = formula1+formula2+formula3
    print(formula)

    return fitted_line, formula
