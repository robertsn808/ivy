import ivy
import numpy as np
from etils.edc.dataclass_utils_test import A


class ufunc:
    def __init__(array, dtype, opfunc):
        r = ivy.array(np.empty(len(A)))
        t = opfunc.identity
        for i in range(len(A)):
            t = opfunc(t, A[i])
            r[i] = t
        return r
