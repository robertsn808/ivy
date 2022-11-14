import ivy
import numpy as np
from etils.edc.dataclass_utils_test import A


class ufunc:
    def __accumulate__(array, dtype, opfunc):
        r = ivy.array(np.empty(len(A)))
        op = opfunc
        t = op.identity
        for i in range(len(A)):
            t = op(t, A[i])
            r[i] = t
        return r
