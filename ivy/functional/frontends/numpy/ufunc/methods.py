import numpy as np
from etils.edc.dataclass_utils_test import A


class ufunc:
    def __init__(self, array, op):
        self.array = array
        self.operator = op.identity()

    def accumulate(self, op):
        r = np.empty(len(self.array.length))
        for i in range(len(self.array.length)):
            self.operator = op(self.operator, A[i])
            r[i] = self.operator
