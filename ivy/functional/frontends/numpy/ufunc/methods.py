import numpy as np
import self as self
from etils.edc.dataclass_utils_test import A


class ufunc:
    def __init__(self, op):
        self.operator = op.identity()

    def accumulate(array, axis=0, dtype=None, out=None, op=None):
        self.operator = op
        r = np.empty(len(self.array.length))
        for i in range(len(self.array.length)):
            self.operator = op(self.operator, A[i])
            r[i] = self.operator
