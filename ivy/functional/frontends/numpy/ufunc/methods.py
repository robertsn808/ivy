import numpy as np
from etils.edc.dataclass_utils_test import A


class ufunc:
    def __init__(array, dtype, opfunc):
        def accumulate(r=np.empty(len(A)), op=opfunc.identity):
            for i in range(len(A)):
                t = op(t, A[i])
                r[i] = t
            return r
