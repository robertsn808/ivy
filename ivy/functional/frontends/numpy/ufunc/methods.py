import ivy


def accumulate(array, dtype=None, out=None):
    return ivy.array(array, dtype=dtype, out=out)
