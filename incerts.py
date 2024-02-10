from sympy import *
import numpy as np


def incerts (f, var_list, var, svar):
    if len(var) != len(svar) or len(var_list) != len(var):
        s = 'Lists are not the same length'
    else:
        partials = []
        adi = []
        list_tpl = []
        for i in range(len(var)):
            list_tpl.append((var_list[i], var[i]))
        for i in range(len(var_list)):
            partials.append(diff(f, var_list[i]))
            partials[i] = partials[i].subs(list_tpl)
            adi.append(partials[i]**2*svar[i]**2)
        sum = np.sum(adi)
        s = sum**(0.5)
    return s