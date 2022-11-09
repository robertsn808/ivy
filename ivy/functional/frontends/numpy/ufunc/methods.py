from lib2to3.pgen2.grammar import op

import ivy
import numpy as np
from etils.edc.dataclass_utils_test import A
import ivy
from self import self


class ufunc:

    def __accumulate__(array, dtype, op):
        r = ivy.array(np.empty(len(A)))
        t = op.identity

        for i in range(len(A)):
            t = op(t, A[i])
            r[i] = t
        return r




