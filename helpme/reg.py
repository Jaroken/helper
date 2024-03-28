import numpy as np

def logform(df, x, y):
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
