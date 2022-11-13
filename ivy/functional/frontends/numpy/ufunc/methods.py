from lib2to3.pgen2.grammar import op
import ivy
import numpy as np
from etils.edc.dataclass_utils_test import A


class ufunc:
    def __accumulate__(array, axis, dtype, out):
        r = ivy.array(np.empty(len(A)))
        t = op.identity
        for i in range(len(A)):
            t = op(t, A[i])
            r[i] = t
        if ivy.exists(out):
            return ivy.any(self.A, dtype=dtype, out=out)
        return r
