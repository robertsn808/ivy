from lib2to3.pgen2.grammar import op

import ivy
import numpy as np
from etils.edc.dataclass_utils_test import A
import ivy
from self import self


class ufunc:

    def __accumulate__(array, axis, dtype, out):
        r = ivy.array(np.empty(len(A)))
        t = op.identity

        for i in range(len(A)):
            t = op(t, A[i])
            r[i] = t

        if ivy.exists(out):
            return ivy.any(self, dtype=dtype, out=out)

        return r


    # If out != None
    #def __out__(self, axis=None, dtype=None, out=ndarray):
     #   if ivy.exists(out):
      #      r = ufunc.__call__(out)
       #     return r

    # if axis > 1
    #def __axis__(self, axis, dtype=None, out=None):




