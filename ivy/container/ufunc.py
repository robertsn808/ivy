from typing import Optional, Tuple, Union, List, Dict

# local
import ivy


def avg_pool3d(
        self: ivy.Container,
        kernel: Union[int, Tuple[int], Tuple[int, int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NDHWC",
        key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
        to_apply: bool = True,
        prune_unapplied: bool = False,
        map_sequences: bool = False,
        out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.avg_pool3d. This method simply
    wraps the function, and so the docstring for ivy.avg_pool3d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input volume *[batch_size,d,h,w,d_in]*.
    kernel
        Convolution filters *[d,h,w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        NDHWC" or "NCDHW". Defaults to "NDHWC".
    out
        optional output array, for writing the result to. It must
        have a shape that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((1, 2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 2, 2, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.max_pool3d(2, 1, "VALID"))
    {
        a: ivy.array([], shape=(1, 1, 0, 2, 2)),
        b: ivy.array([[[[[10., 11.],
                         [12., 13.]]]],
                   [[[[34., 35.],
                         [36., 37.]]]]])
    }
    :param out:
    :param map_sequences:
    :param prune_unapplied:
    :param to_apply:
    :param key_chains:
    :param data_format:
    :param padding:
    :param strides:
    :param kernel:
    :param self:
    """
    pass
