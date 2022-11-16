#ivy.container.experimental.creation
# global
from typing import Optional, Tuple, Union, List, Dict

# local
import ivy
from ivy.container.base import ContainerBase


def static_triu_indices(
    n_rows: int,
    n_cols: Optional[int] = None,
    k: Optional[int] = 0,
    /,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    *,
    device: Optional[Union[ivy.Device, ivy.NativeDevice]] = None,
    out: Optional[Tuple[ivy.Array]] = None,
) -> ivy.Container:
    pass


def triu_indices(
    self: ivy.Container,
    n_rows: int,
    n_cols: Optional[int] = None,
    k: Optional[int] = 0,
    /,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    *,
    device: Optional[Union[ivy.Device, ivy.NativeDevice]] = None,
    out: Optional[Tuple[ivy.Array]] = None,
) -> ivy.Container:
    pass


def static_hann_window(
    window_length: Union[int, ivy.Container],
    periodic: Optional[bool] = True,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.hann_window. This method simply wraps
    the function, and so the docstring for ivy.hann_window also applies to this
    method with minimal changes.

    Parameters
    ----------
    window_length
        container including multiple window sizes.
    periodic
        If True, returns a window to be used as periodic function.
        If False, return a symmetric window.
    dtype
        The data type to produce. Must be a floating point type.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that contains the Hann windows.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_hann(x)
    {
        a: ivy.array([0.0000, 0.7500, 0.7500])
        b: ivy.array([0.0000, 0.3455, 0.9045, 0.9045, 0.3455])
    }
    """
    pass


def hann_window(
    self: ivy.Container,
    periodic: Optional[bool] = True,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.hann_window. This method simply
    wraps the function, and so the docstring for ivy.hann_window also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input container with window sizes.
    periodic
        If True, returns a window to be used as periodic function.
        If False, return a symmetric window.
    dtype
        The data type to produce. Must be a floating point type.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container containing the Hann windows.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.hann_window(x)
    {
        a: ivy.array([0.0000, 0.7500, 0.7500])
        b: ivy.array([0.0000, 0.3455, 0.9045, 0.9045, 0.3455])
    }
    """
    pass


def static_kaiser_window(
    window_length: Union[int, ivy.Container],
    periodic: bool = True,
    beta: float = 12.0,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.kaiser_window. This method
    simply wraps the function, and so the docstring for ivy.kaiser_window
    also applies to this method with minimal changes.

    Parameters
    ----------
    window_length
        input container including window lenghts.
    periodic
        If True, returns a periodic window suitable for use in spectral analysis.
        If False, returns a symmetric window suitable for use in filter design.
    beta
        a float used as shape parameter for the window.
    dtype
        data type of the returned array.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Kaiser windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_kaiser_window(x, True, 5)
    {
        a: ivy.array([0.2049, 0.8712, 0.8712]),
        a: ivy.array([0.0367, 0.7753, 0.7753]),
    }
    """
    pass


def kaiser_window(
    self: ivy.Container,
    periodic: bool = True,
    beta: float = 12.0,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.kaiser_window. This method
    simply wraps the function, and so the docstring for ivy.kaiser_window
    also applies to this method with minimal changes.

    Parameters
    ----------
    self
        input container including window lenghts.
    periodic
        If True, returns a periodic window suitable for use in spectral analysis.
        If False, returns a symmetric window suitable for use in filter design.
    beta
        a float used as shape parameter for the window.
    dtype
        data type of the returned array.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Kaiser windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_kaiser_window(x, True, 5)
    {
        a: ivy.array([0.2049, 0.8712, 0.8712]),
        a: ivy.array([0.0367, 0.7753, 0.7753]),
    }
    """
    pass


def static_kaiser_bessel_derived_window(
    x: Union[int, ivy.Array, ivy.NativeArray, ivy.Container],
    periodic: bool = True,
    beta: float = 12.0,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.kaiser_bessel_derived_window.
    This method simply wraps the function, and so the docstring for
    ivy.kaiser_bessel_derived_window also applies to this method with
    minimal changes.

    Parameters
    ----------
    x
        input container including window lenghts.
    periodic
        If True, returns a periodic window suitable for use in spectral analysis.
        If False, returns a symmetric window suitable for use in filter design.
    beta
        a float used as shape parameter for the window.
    dtype
        data type of the returned array.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Kaiser Bessel Derived windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_kaiser_bessel_derived_window(x, True, 5)
    {
        a: ivy.array([0.70710677, 0.70710677]),
        b: ivy.array([0.18493208, 0.9827513 , 0.9827513 , 0.18493208]),
    }
    """
    pass


def kaiser_bessel_derived_window(
    self: ivy.Container,
    periodic: bool = True,
    beta: float = 12.0,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.kaiser_bessel_derived_window.
    This method simply wraps the function, and so the docstring for
    ivy.kaiser_bessel_derived_window also applies to this method with
    minimal changes.

    Parameters
    ----------
    self
        input container including window lenghts.
    periodic
        If True, returns a periodic window suitable for use in spectral analysis.
        If False, returns a symmetric window suitable for use in filter design.
    beta
        a float used as shape parameter for the window.
    dtype
        data type of the returned array.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Kaiser Bessel Derived windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5))
    >>> x.kaiser_bessel_derived_window(True, 5)
    {
        a: ivy.array([0.70710677, 0.70710677]),
        b: ivy.array([0.18493208, 0.9827513 , 0.9827513 , 0.18493208]),
    }
    """
    pass


def static_hamming_window(
    x: Union[int, ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    periodic: Optional[bool] = True,
    alpha: Optional[float] = 0.54,
    beta: Optional[float] = 0.46,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.hamming_window.
    This method simply wraps the function, and so the docstring for
    ivy.hamming_window also applies to this method with
    minimal changes.

    Parameters
    ----------
    x
        input container including window lenghts.
    periodic
        If True, returns a window to be used as periodic function.
        If False, return a symmetric window.
    alpha
        The coefficient alpha in the hamming window equation
    beta
        The coefficient beta in the hamming window equation
    dtype
        data type of the returned arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Hamming windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_hamming_window(x, periodic=True, alpha=0.2, beta=2)
    {
        a: ivy.array([-1.8000,  1.2000,  1.2000]),
        b: ivy.array([-1.8000, -0.4180,  1.8180,  1.8180, -0.4180])
    }
    """
    pass


def hamming_window(
    self: ivy.Container,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    periodic: Optional[bool] = True,
    alpha: Optional[float] = 0.54,
    beta: Optional[float] = 0.46,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.hamming_window.
    This method simply wraps the function, and so the docstring for
    ivy.hamming_window also applies to this method with
    minimal changes.

    Parameters
    ----------
    self
        input container including window lenghts.
    periodic
        If True, returns a window to be used as periodic function.
        If False, return a symmetric window.
    alpha
        The coefficient alpha in the hamming window equation
    beta
        The coefficient beta in the hamming window equation
    dtype
        data type of the returned arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Hamming windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5))
    >>> x.hamming_window(periodic=True, alpha=0.2, beta=2)
    {
        a: ivy.array([-1.8000,  1.2000,  1.2000]),
        b: ivy.array([-1.8000, -0.4180,  1.8180,  1.8180, -0.4180])
    }
    """
    pass


#ivy.container.experimental.elementwise
# global
from typing import Optional, Union, List, Dict, Tuple

# local
import ivy
from ivy.container.base import ContainerBase


def static_sinc(
    x: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.sinc. This method simply
    wraps the function, and so the docstring for ivy.sinc also
    applies to this method with minimal changes.

    Parameters
    ----------
    x
        input container whose elements are each expressed in radians.
        Should have a floating-point data type.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        optional output container, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        a container containing the sinc of each element in ``x``. The returned
        container must have a floating-point data type determined by
        :ref:`type-promotion`.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([0.5, 1.5, 2.5]),
    ...                   b=ivy.array([3.5, 4.5, 5.5]))
    >>> y = ivy.Container.static_sinc(x)
    >>> print(y)
    {
        a: ivy.array([0.636, -0.212, 0.127]),
        b: ivy.array([-0.090, 0.070, -0.057])
    }
    """
    pass


def sinc(
    self: ivy.Container,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.sinc. This method simply
    wraps the function, and so the docstring for ivy.sinc also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        input container whose elements are each expressed in radians.
        Should have a floating-point data type.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        optional output container, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        a container containing the sinc of each element in ``self``.
        The returned container must have a floating-point data type
        determined by :ref:`type-promotion`.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([0.5, 1.5, 2.5]),
    ...                   b=ivy.array([3.5, 4.5, 5.5]))
    >>> y = x.sinc()
    >>> print(y)
    {
        a: ivy.array([0.637,-0.212,0.127]),
        b: ivy.array([-0.0909,0.0707,-0.0579])
    }
    """
    pass


def static_lcm(
    x1: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.lcm. This method simply wraps the
    function, and so the docstring for ivy.lcm also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        first input container.
    x2
        second input container.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        a container containing the element-wise least common multiples
        of the arrays contained in x1 and x2.

    Examples
    --------
    >>> x1=ivy.Container(a=ivy.array([2, 3, 4]),
    ...                  b=ivy.array([6, 54, 62, 10]))
    >>> x2=ivy.Container(a=ivy.array([5, 8, 15]),
    ...                  b=ivy.array([32, 40, 25, 13]))
    >>> ivy.Container.lcm(x1, x2)
    {
        a: ivy.array([10, 21, 60]),
        b: ivy.array([96, 1080, 1550, 130])
    }

    """
    pass


def lcm(
    self: ivy.Container,
    x2: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.lcm. This method simply wraps the
    function, and so the docstring for ivy.lcm also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        first input container.
    x2
        second input container.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        a container containing the the element-wise least common multiples
        of the arrays contained in x1 and x2.

    Examples
    --------
    >>> x1=ivy.Container(a=ivy.array([2, 3, 4]),
    ...                  b=ivy.array([6, 54, 62, 10]))
    >>> x2=ivy.Container(a=ivy.array([5, 8, 15]),
    ...                  b=ivy.array([32, 40, 25, 13]))
    >>> x1.lcm(x2)
    {
        a: ivy.array([10, 24, 60]),
        b: ivy.array([96, 1080, 1550, 130])
    }

    """
    pass


def static_fmod(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.fmod. This method simply wraps
    the function, and so the docstring for ivy.fmod also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        container with the first input arrays.
    x2
        container with the second input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise remainder of divisions.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([2, 3, 4]),\
                           b=ivy.array([ivy.nan, 0, ivy.nan]))
    >>> x2 = ivy.Container(a=ivy.array([1, 5, 2]),\
                           b=ivy.array([0, ivy.nan, ivy.nan]))
    >>> ivy.Container.static_fmod(x1, x2)
    {
        a: ivy.array([ 0,  3,  0])
        b: ivy.array([ nan,  nan,  nan])
    }
    """
    pass


def fmod(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.fmod. This method simply
    wraps the function, and so the docstring for ivy.fmod also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        container with the first input arrays.
    x2
        container with the second input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise remainder of divisions.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([2, 3, 4]),\
                           b=ivy.array([ivy.nan, 0, ivy.nan]))
    >>> x2 = ivy.Container(a=ivy.array([1, 5, 2]),\
                           b=ivy.array([0, ivy.nan, ivy.nan]))
    >>> x1.fmod(x2)
    {
        a: ivy.array([ 0,  3,  0])
        b: ivy.array([ nan,  nan,  nan])
    }
    """
    pass


def static_fmax(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.fmax. This method simply wraps
    the function, and so the docstring for ivy.fmax also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        container with the first input arrays.
    x2
        container with the second input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise maximums.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([2, 3, 4]),\
                           b=ivy.array([ivy.nan, 0, ivy.nan]))
    >>> x2 = ivy.Container(a=ivy.array([1, 5, 2]),\
                           b=ivy.array([0, ivy.nan, ivy.nan]))
    >>> ivy.Container.static_fmax(x1, x2)
    {
        a: ivy.array([ 2.,  5.,  4.])
        b: ivy.array([ 0,  0,  nan])
    }
    """
    pass


def fmax(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.fmax. This method simply
    wraps the function, and so the docstring for ivy.fmax also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        container with the first input arrays.
    x2
        container with the second input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise maximums.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([2, 3, 4]),\
                           b=ivy.array([ivy.nan, 0, ivy.nan]))
    >>> x2 = ivy.Container(a=ivy.array([1, 5, 2]),\
                           b=ivy.array([0, ivy.nan, ivy.nan]))
    >>> x1.fmax(x2)
    {
        a: ivy.array([ 2.,  5.,  4.])
        b: ivy.array([ 0,  0,  nan])
    }
    """
    pass


def static_float_power(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.float_power. This method simply wraps
    the function, and so the docstring for ivy.float_power also applies to this
    method with minimal changes.

    Parameters
    ----------
    x1
        container with the base input arrays.
    x2
        container with the exponent input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with base arrays raised to the powers
        of exponents arrays, element-wise .

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([2, 10]))
    >>> x2 = ivy.Container(a=ivy.array([1, 3, 1]), b=0)
    >>> ivy.Container.static_float_power(x1, x2)
    {
        a: ivy.array([1,  8,  3])
        b: ivy.array([1, 1])
    }
    """
    pass


def float_power(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.float_power. This method simply
    wraps the function, and so the docstring for ivy.float_power also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    x2
        container with the exponent input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with base arrays raised to the powers
        of exponents arrays, element-wise .

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([2, 10]))
    >>> x2 = ivy.Container(a=ivy.array([1, 3, 1]), b=0)
    >>> x1.float_power(x2)
    {
        a: ivy.array([1,  8,  3])
        b: ivy.array([1, 1])
    }
    """
    pass


def static_exp2(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.exp2. This method simply wraps
    the function, and so the docstring for ivy.exp2 also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise 2 to the power
        of input arrays elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=[5, 6, 7])
    >>> ivy.Container.static_exp2(x)
    {
        a: ivy.array([2.,  4.,  8.])
        b: ivy.array([32., 64., 128.])
    }
    """
    pass


def exp2(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.exp2. This method simply
    wraps the function, and so the docstring for ivy.exp2 also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise 2 to the power
        of input array elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=[5, 6, 7])
    >>> x.exp2()
    {
        a: ivy.array([2.,  4.,  8.])
        b: ivy.array([32., 64., 128.])
    }
    """
    pass


def static_count_nonzero(
    a: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: Optional[bool] = False,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.count_nonzero. This method simply
    wraps the function, and so the docstring for ivy.count_nonzero also applies
    to this method with minimal changes.

    Parameters
    ----------
    a
        container with the base input arrays.
    axis
        optional axis or tuple of axes along which to count non-zeros. Default is
        None, meaning that non-zeros will be counted along a flattened
        version of the input array.
    keepdims
        optional, if this is set to True, the axes that are counted are left in the
        result as dimensions with size one. With this option, the result
        will broadcast correctly against the input array.
    dtype
        optional output dtype. Default is of type integer.
    key_chains
        The key-chains to apply or not apply the method to. Default is None.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is True.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is False.
    map_sequences
        Whether to also map method to sequences (lists, tuples). Default is False.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including number of non-zero values in the array along a
        given axis. Otherwise, container with the total number of non-zero
        values in the array is returned.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> ivy.Container.static_count_nonzero(x)
    {
        a: ivy.array(7),
        b: ivy.array(7)
    }
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> ivy.Container.static_count_nonzero(x, axis=0)
    {
        a: ivy.array([1, 2, 2, 2]),
        b: ivy.array([[1, 2],
                      [2, 2]])
    }
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> ivy.Container.static_count_nonzero(x, axis=(0,1), keepdims=True)
    {
        a: ivy.array([[7]]),
        b: ivy.array([[[3, 4]]])
    }
    """
    pass


def count_nonzero(
    self: ivy.Container,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: Optional[bool] = False,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.count_nonzero. This method
    simply wraps the function, and so the docstring for ivy.count_nonzero also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    axis
        optional axis or tuple of axes along which to count non-zeros. Default is
        None, meaning that non-zeros will be counted along a flattened
        version of the input array.
    keepdims
        optional, if this is set to True, the axes that are counted are left in the
        result as dimensions with size one. With this option, the result
        will broadcast correctly against the input array.
    dtype
        optional output dtype. Default is of type integer.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including number of non-zero values in the array along a
        given axis. Otherwise, container with the total number of non-zero
        values in the array is returned.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> x.count_nonzero()
    {
        a: ivy.array(7),
        b: ivy.array(7)
    }
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> x.count_nonzero(axis=0)
    {
        a: ivy.array([1, 2, 2, 2]),
        b: ivy.array([[1, 2],
                      [2, 2]])
    }
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> x.count_nonzero(axis=(0,1), keepdims=True)
    {
        a: ivy.array([[7]]),
        b: ivy.array([[[3, 4]]])
    }
    """
    pass


def static_nansum(
    x: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    axis: Optional[Union[tuple, int]] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    keepdims: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.nansum. This method simply wraps
    the function, and so the docstring for ivy.nansum also applies to this method
    with minimal changes.
    
    Parameters
    ----------
    x
        Input array.
    axis
        Axis or axes along which the sum is computed.
        The default is to compute the sum of the flattened array.
    dtype
        The type of the returned array and of the accumulator in
        which the elements are summed. By default, the dtype of input is used.
    keepdims
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one.
    out
        Alternate output array in which to place the result.
        The default is None.
    
    Returns
    -------
    ret
        A new array holding the result is returned unless out is specified,
        in which it is returned.
    
    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([[10, 7, 4], [3, 2, 1]]),\
            b=ivy.array([[1, 4, 2], [ivy.nan, ivy.nan, 0]]))
    >>> ivy.Container.static_nansum(x)
    {
        a: 27,
        b: 7.0
    }
    >>> ivy.Container.static_nansum(x, axis=0)
    {
        a: ivy.array([13, 9, 5]),
        b: ivy.array([1., 4., 2.])
    }
    >>> ivy.Container.static_nansum(x, axis=1)
    {
        a: ivy.array([21, 6]),
        b: ivy.array([7., 0.])
    }
    """
    pass


def nansum(
    self: ivy.Container,
    /,
    *,
    axis: Optional[Union[tuple, int]] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    keepdims: Optional[bool] = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.nansum. This method simply
    wraps the function, and so the docstring for ivy.nansum also applies to this
    method with minimal changes.
    
    Parameters
    ----------
    self
        Input container including arrays.
    axis
        Axis or axes along which the sum is computed.
        The default is to compute the sum of the flattened array.
    dtype
        The type of the returned array and of the accumulator in
        which the elements are summed. By default, the dtype of input is used.
    keepdims
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one.
    out
        Alternate output array in which to place the result.
        The default is None.
    
    Returns
    -------
    ret
        A new array holding the result is returned unless out is specified,
        in which it is returned.
    
    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([[10, 7, 4], [3, 2, 1]]),\
            b=ivy.array([[1, 4, 2], [ivy.nan, ivy.nan, 0]]))
    >>> x.nansum(axis=0)
    {
        a: ivy.array([13, 9, 5]),
        b: ivy.array([1., 4., 2.])
    }
    >>> x.nansum(axis=1)
    {
        a: ivy.array([21, 6]),
        b: ivy.array([7., 0.])
    }
    """
    pass


def static_gcd(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container, int, list, tuple],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container, int, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.gcd. This method simply wraps
    the function, and so the docstring for ivy.gcd also applies to this
    method with minimal changes.

    Parameters
    ----------
    x1
        first input container with array-like items.
    x2
        second input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise gcd of input arrays.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([1, 2, 3]))
    >>> x2 = ivy.Container(a=ivy.array([5, 6, 7]),\
                           b=10)
    >>> ivy.Container.static_gcd(x1, x2)
    {
        a: ivy.array([1.,  1.,  3.])
        b: ivy.array([1., 2., 1.])
    }
    """
    pass


def gcd(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.gcd. This method simply
    wraps the function, and so the docstring for ivy.gcd also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        first input container with array-like items.
    x2
        second input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise gcd of input arrays.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([1, 2, 3]))
    >>> x2 = ivy.Container(a=ivy.array([5, 6, 7]),\
                           b=10)
    >>> x1.gcd(x2)
    {
        a: ivy.array([1.,  1.,  3.])
        b: ivy.array([1., 2., 1.])
    }
    """
    pass


def static_isclose(
    a: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    b: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    rtol: Optional[float] = 1e-05,
    atol: Optional[float] = 1e-08,
    equal_nan: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.isclose. This method simply wraps
    the function, and so the docstring for ivy.isclose also applies to this method
    with minimal changes.

    Parameters
    ----------
    a
        Input container containing first input array.
    b
        Input container containing second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in a will be
        considered equal to NaN's in b in the output array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        A new array holding the result is returned unless out is specified,
        in which it is returned.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([1.0, ivy.nan]),\
            b=ivy.array([1.0, ivy.nan]))
    >>> y = ivy.Container(a=ivy.array([1.0, ivy.nan]),\
            b=ivy.array([1.0, ivy.nan]))
    >>> ivy.Container.static_isclose(x, y)
    {
        a: ivy.array([True, False]),
        b: ivy.array([True, False])
    }
    >>> ivy.Container.static_isclose(x, y, equal_nan=True)
    {
        a: ivy.array([True, True]),
        b: ivy.array([True, True])
    }
    >>> x = ivy.Container(a=ivy.array([1.0, 2.0]),\
            b=ivy.array([1.0, 2.0]))
    >>> y = ivy.Container(a=ivy.array([1.0, 2.001]),\
            b=ivy.array([1.0, 2.0]))
    >>> ivy.Container.static_isclose(x, y, atol=0.0)
    {
        a: ivy.array([True, False]),
        b: ivy.array([True, True])
    }
    >>> ivy.Container.static_isclose(x, y, rtol=0.01, atol=0.0)
    {
        a: ivy.array([True, True]),
        b: ivy.array([True, True])
    }
    """
    pass


def isclose(
    self: ivy.Container,
    b: ivy.Container,
    /,
    *,
    rtol: Optional[float] = 1e-05,
    atol: Optional[float] = 1e-08,
    equal_nan: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.isclose. This method simply
    wraps the function, and so the docstring for ivy.isclose also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container containing first input array.
    b
        Input container containing second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in a will be
        considered equal to NaN's in b in the output array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        A new array holding the result is returned unless out is specified,
        in which it is returned.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([1.0, ivy.nan]),\
            b=ivy.array([1.0, ivy.nan]))
    >>> y = ivy.Container(a=ivy.array([1.0, ivy.nan]),\
            b=ivy.array([1.0, ivy.nan]))
    >>> x.isclose(y)
    {
        a: ivy.array([True, False]),
        b: ivy.array([True, False])
    }
    >>> x.isclose(y, equal_nan=True)
    {
        a: ivy.array([True, True]),
        b: ivy.array([True, True])
    }
    >>> x = ivy.Container(a=ivy.array([1.0, 2.0]),\
            b=ivy.array([1.0, 2.0]))
    >>> y = ivy.Container(a=ivy.array([1.0, 2.001]),\
            b=ivy.array([1.0, 2.0]))
    >>> x.isclose(y, atol=0.0)
    {
        a: ivy.array([True, False]),
        b: ivy.array([True, True])
    }
    >>> x.isclose(y, rtol=0.01, atol=0.0)
    {
        a: ivy.array([True, True]),
        b: ivy.array([True, True])
    }
    """
    pass


def static_isposinf(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.isposinf. This method simply wraps
    the function, and so the docstring for ivy.isposinf also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including a boolean array with values
        True where the corresponding element of the input
        is positive infinity and values False where the
        element of the input is not positive infinity.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, ivy.inf, -ivy.inf]),\
                            b=ivy.array([5, ivy.inf, ivy.inf]))
    >>> ivy.Container.static_isposinf(x)
    {
        a: ivy.array([False, True, False]),
        b: ivy.array([False, True, True])
    }
    """
    pass


def isposinf(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.isposinf. This method simply
    wraps the function, and so the docstring for ivy.isposinf also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Returns container including a boolean array with values
        True where the corresponding element of the input
        is positive infinity and values False where the
        element of the input is not positive infinity.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, ivy.inf, -ivy.inf]),\
                           b=ivy.array([5, ivy.inf, ivy.inf]))
    >>> x.isposinf()
    {
        a: ivy.array([False, True, False]),
        b: ivy.array([False, True, True])
    }
    """
    pass


def static_isneginf(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.isneginf. This method simply wraps
    the function, and so the docstring for ivy.isneginf also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including a boolean array with values
        True where the corresponding element of the input
        is negative infinity and values False where the
        element of the input is not negative infinity.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, ivy.inf, -ivy.inf]),\
                            b=ivy.array([5, -ivy.inf, -ivy.inf]))
    >>> ivy.Container.static_isneginf(x)
    {
        a: ivy.array([False, False, True]),
        b: ivy.array([False, True, True])
    }
    """
    pass


def isneginf(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.isneginf. This method simply
    wraps the function, and so the docstring for ivy.isneginf also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Returns container including a boolean array with values
        True where the corresponding element of the input
        is negative infinity and values False where the
        element of the input is not negative infinity.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, ivy.inf, -ivy.inf]),\
                           b=ivy.array([5, -ivy.inf, -ivy.inf]))
    >>> x.isneginf()
    {
        a: ivy.array([False, False, True]),
        b: ivy.array([False, True, True])
    }
    """
    pass


def static_nan_to_num(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    copy: Optional[bool] = True,
    nan: Optional[Union[float, int]] = 0.0,
    posinf: Optional[Union[float, int]] = None,
    neginf: Optional[Union[float, int]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.nan_to_num. This method simply wraps
    the function, and so the docstring for ivy.nan_to_num also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        Input container with array items.
    copy
        Whether to create a copy of x (True) or to replace values in-place (False).
        The in-place operation only occurs if casting to an array does not require
        a copy. Default is True.
    nan
        Value to be used to fill NaN values. If no value is passed then NaN values
        will be replaced with 0.0.
    posinf
        Value to be used to fill positive infinity values. If no value is passed
        then positive infinity values will be replaced with a very large number.
    neginf
        Value to be used to fill negative infinity values.
        If no value is passed then negative infinity values
        will be replaced with a very small (or negative) number.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with replaced non-finite elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, 2, 3, nan]),\
                           b=ivy.array([1, 2, 3, inf]))
    >>> ivy.Container.static_nan_to_num(x, posinf=5e+100)
    {
        a: ivy.array([1.,  1.,  3.,  0.0])
        b: ivy.array([1., 2., 1.,  5e+100])
    }
    """
    pass


def nan_to_num(
    self: ivy.Container,
    /,
    *,
    copy: Optional[bool] = True,
    nan: Optional[Union[float, int]] = 0.0,
    posinf: Optional[Union[float, int]] = None,
    neginf: Optional[Union[float, int]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.nan_to_num. This method simply
    wraps the function, and so the docstring for ivy.nan_to_num also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input container with array items.
    copy
        Whether to create a copy of x (True) or to replace values in-place (False).
        The in-place operation only occurs if casting to an array does not require
        a copy. Default is True.
    nan
        Value to be used to fill NaN values. If no value is passed then NaN values
        will be replaced with 0.0.
    posinf
        Value to be used to fill positive infinity values. If no value is passed
        then positive infinity values will be replaced with a very large number.
    neginf
        Value to be used to fill negative infinity values.
        If no value is passed then negative infinity values
        will be replaced with a very small (or negative) number.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with replaced non-finite elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, 2, 3, nan]),\
                           b=ivy.array([1, 2, 3, inf]))
    >>> x.nan_to_num(posinf=5e+100)
    {
        a: ivy.array([1.,  1.,  3.,  0.0])
        b: ivy.array([1., 2., 1.,  5e+100])
    }
    """
    pass


def static_logaddexp2(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.logaddexp2. This method simply wraps
    the function, and so the docstring for ivy.logaddexp2 also applies to this
    method with minimal changes.

    Parameters
    ----------
    x1
        first input container with array-like items.
    x2
        second input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise logaddexp2 of input arrays.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([1, 2, 3]))
    >>> x2 = ivy.Container(a=ivy.array([4, 5, 6]),\
                           b=5)
    >>> ivy.Container.static_logaddexp2(x1, x2)
    {
        a: ivy.array([4.169925, 5.169925, 6.169925])
        b: ivy.array([5.08746284, 5.169925  , 5.32192809])
    }
    """
    pass


def logaddexp2(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.logaddexp2. This method simply
    wraps the function, and so the docstring for ivy.logaddexp2 also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        first input container with array-like items.
    x2
        second input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise logaddexp2 of input arrays.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([1, 2, 3]))
    >>> x2 = ivy.Container(a=ivy.array([4, 5, 6]),\
                           b=5)
    >>> x1.logaddexp2(x2)
    {
        a: ivy.array([4.169925, 5.169925, 6.169925])
        b: ivy.array([5.08746284, 5.169925  , 5.32192809])
    }
    """
    pass


def static_signbit(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, int, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.signbit. This method simply wraps
    the function, and so the docstring for ivy.signbit also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise signbit of input arrays.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, -2, 3]),\
                           b=-5)
    >>> ivy.Container.static_signbit(x)
    {
        a: ivy.array([False, True, False])
        b: ivy.array([True])
    }
    """
    pass


def signbit(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.signbit. This method simply
    wraps the function, and so the docstring for ivy.signbit also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise signbit of input arrays.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, -2, 3]),\
                           b=-5)
    >>> x.signbit()
    {
        a: ivy.array([False, True, False])
        b: ivy.array([True])
    }
    """
    pass


def static_allclose(
    x1: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    rtol: Optional[float] = 1e-05,
    atol: Optional[float] = 1e-08,
    equal_nan: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.allclose. This method simply wraps
    the function, and so the docstring for ivy.allclose also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        Input container containing first input array.
    x2
        Input container containing second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in x1 will be
        considered equal to NaN's in x2 in the output array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        A new container holding the result is returned unless out is specified,
        in which it is returned.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> x2 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> y = ivy.Container.static_allclose(x1, x2)
    >>> print(y)
    {
        a: true,
        b: true
    }

    >>> x1 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> x2 = ivy.Container(a=ivy.array([1., 2., 3.0003]),\
    ...                         b=ivy.array([1.0006, 2., 3.]))
    >>> y = ivy.Container.static_allclose(x1, x2, rtol=1e-3)
    >>> print(y)
    {
        a: true,
        b: true
    }
    """
    pass


def allclose(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    rtol: Optional[float] = 1e-05,
    atol: Optional[float] = 1e-08,
    equal_nan: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.allclose. This method simply
    wraps the function, and so the docstring for ivy.allclose also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container containing first input array.
    x2
        Input container containing second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in x1 will be
        considered equal to NaN's in x2 in the output array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        A new container holding the result is returned unless out is specified,
        in which it is returned.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> x2 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> y = x1.allclose(x2)
    >>> print(y)
    {
        a: true,
        b: true
    }

    >>> x1 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> x2 = ivy.Container(a=ivy.array([1., 2., 3.0003]),\
    ...                         b=ivy.array([1.0006, 2., 3.]))
    >>> y = x1.allclose(x2, rtol=1e-3)
    >>> print(y)
    {
        a: true,
        b: true
    }
    """
    pass


def static_fix(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.fix. This method simply wraps
    the function, and so the docstring for ivy.fix also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        input container with array items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise rounding of
        input arrays elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([2.1, 2.9, -2.1]),\
                           b=ivy.array([3.14]))
    >>> ivy.Container.static_fix(x)
    {
        a: ivy.array([ 2.,  2., -2.])
        b: ivy.array([ 3.0 ])
    }
    """
    pass


def fix(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.fix. This method simply
    wraps the function, and so the docstring for ivy.fix also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input container with array items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise rounding of
        input arrays elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([2.1, 2.9, -2.1]),\
                           b=ivy.array([3.14]))
    >>> x.fix()
    {
        a: ivy.array([ 2.,  2., -2.])
        b: ivy.array([ 3.0 ])
    }
    """
    pass


def static_nextafter(
    x1: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.nextafter. This method simply wraps
    the function, and so the docstring for ivy.nextafter also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        Input container containing first input arrays.
    x2
        Input container containing second input arrays.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        container including the next representable values of
        input container's arrays, element-wise

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1.0e-50, 2.0e+50]),\
    ...                         b=ivy.array([2.0, 1.0])
    >>> x2 = ivy.Container(a=ivy.array([5.5e-30]),\
    ...                         b=ivy.array([-2.0]))
    >>> ivy.Container.static_nextafter(x1, x2)
    {
        a: ivy.array([1.4013e-45., 3.4028e+38]),
        b: ivy.array([5.5e-30])
    }
    """
    pass


def nextafter(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.nextafter. This method simply
    wraps the function, and so the docstring for ivy.nextafter also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container containing first input array.
    x2
        Input container containing second input array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        container including the next representable values of
        input container's arrays, element-wise

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1.0e-50, 2.0e+50]),\
    ...                         b=ivy.array([2.0, 1.0])
    >>> x2 = ivy.Container(a=ivy.array([5.5e-30]),\
    ...                         b=ivy.array([-2.0]))
    >>> x1.nextafter(x2)
    {
        a: ivy.array([1.4013e-45., 3.4028e+38]),
        b: ivy.array([5.5e-30])
    }
    """
    pass


#ivy.container.experimental.layers
# global
from typing import Optional, Union, List, Dict, Tuple, Literal

# local
import ivy
from ivy.container.base import ContainerBase


def static_max_pool1d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kernel: Union[int, Tuple[int]],
    strides: Union[int, Tuple[int]],
    padding: str,
    /,
    *,
    data_format: str = "NWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.max_pool1d. This method simply
    wraps the function, and so the docstring for ivy.max_pool1d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Container of input images *[batch_size, w, d_in]*.
    kernel
        Size of the kernel i.e., the sliding window for each
        dimension of input. *[w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list
        indicating the per-dimension paddings.
    data_format
        NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12.).reshape((2,2,3))
    >>> b = ivy.arange(24.).reshape((2,3,4))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(ivy.Container.static_max_pool1d(x,2, 2, "VALID"))
    {
        a: ivy.array([[[3., 4., 5.]],
                      [[9., 10., 11.]]]),
        b: ivy.array([[[4., 5., 6., 7.]],
                      [[16., 17., 18., 19.]]])
    }
    """
    pass


def max_pool1d(
    self: ivy.Container,
    kernel: Union[int, Tuple[int]],
    strides: Union[int, Tuple[int]],
    padding: str,
    /,
    *,
    data_format: str = "NWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of `ivy.max_pool1d`. This method simply
    wraps the function, and so the docstring for `ivy.max_pool1d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Container of input images *[batch_size, w, d_in]*.
    kernel
        Size of the kernel i.e., the sliding window for each
        dimension of input. *[w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list
        indicating the per-dimension paddings.
    data_format
        NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12.).reshape((2,2,3))
    >>> b = ivy.arange(24.).reshape((2,3,4))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.max_pool1d(2, 2, "VALID"))
    {
        a: ivy.array([[[3., 4., 5.]],
                      [[9., 10., 11.]]]),
        b: ivy.array([[[4., 5., 6., 7.]],
                      [[16., 17., 18., 19.]]])
    }
    """
    pass


def static_max_pool2d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kernel: Union[int, Tuple[int], Tuple[int, int]],
    strides: Union[int, Tuple[int], Tuple[int, int]],
    padding: str,
    /,
    *,
    data_format: str = "NHWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.max_pool2dd. This method simply
    wraps the function, and so the docstring for ivy.max_pool2d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window to take a max over.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(ivy.Container.static_max_pool2d(x, (2, 2), (1, 1), "SAME"))
    {
        a: (<class ivy.array.array.Array> shape=[2, 1, 3, 2]),
        b: (<class ivy.array.array.Array> shape=[2, 4, 3, 2])
    }
    """
    pass


def max_pool2d(
    self: ivy.Container,
    kernel: Union[int, Tuple[int], Tuple[int, int]],
    strides: Union[int, Tuple[int], Tuple[int, int]],
    padding: str,
    /,
    *,
    data_format: str = "NHWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of `ivy.max_pool2d`. This method simply
    wraps the function, and so the docstring for `ivy.max_pool2d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window to take a max over.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    dilations
        The dilation factor for each dimension of input. (Default value = 1)
    out
        optional output array, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.max_pool2d(2, 2), (1, 1), "SAME"))
    {
        a: (<class ivy.array.array.Array> shape=[2, 1, 3, 2]),
        b: (<class ivy.array.array.Array> shape=[2, 4, 3, 2])
    }
    """
    pass


def static_max_pool3d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
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
    """ivy.Container static method variant of ivy.max_pool3d. This method simply
    wraps the function, and so the docstring for ivy.max_pool3d also applies
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
    >>> print(ivy.Container.static_max_pool3d(x, 2, 1, "VALID"))
    {
        a: ivy.array([], shape=(1, 1, 0, 2, 2)),
        b: ivy.array([[[[[20, 21],
                         [22, 23]]]],
                   [[[[44, 45],
                         [46, 47]]]]])
    }
    """
    pass


def max_pool3d(
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
    """ivy.Container static method variant of ivy.max_pool3d. This method simply
    wraps the function, and so the docstring for ivy.max_pool3d also applies
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
        b: ivy.array([[[[[20, 21],
                         [22, 23]]]],
                   [[[[44, 45],
                         [46, 47]]]]])
    }
    """
    pass


def static_avg_pool1d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kernel: Union[int, Tuple[int]],
    strides: Union[int, Tuple[int]],
    padding: str,
    /,
    *,
    data_format: str = "NWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.avg_pool1d. This method simply
    wraps the function, and so the docstring for ivy.avg_pool1d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Container of input images *[batch_size, w, d_in]*.
    kernel
        Size of the kernel i.e., the sliding window for each
        dimension of input. *[w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list
        indicating the per-dimension paddings.
    data_format
        NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12.).reshape((2,2,3))
    >>> b = ivy.arange(24.).reshape((2,3,4))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(ivy.Container.static_avg_pool1d(x,2, 2, "VALID"))
    {
        a: ivy.array([[[1.5, 2.5, 3.5]],
                      [[7.5, 8.5, 9.5]]]),
        b: ivy.array([[[2., 3., 4., 5.]],
                      [[14., 15., 16., 17.]]])
    }
    """
    pass


def avg_pool1d(
    self: ivy.Container,
    kernel: Union[int, Tuple[int]],
    strides: Union[int, Tuple[int]],
    padding: str,
    /,
    *,
    data_format: str = "NWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of `ivy.avg_pool1d`. This method simply
    wraps the function, and so the docstring for `ivy.avg_pool1d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Container of input images *[batch_size, w, d_in]*.
    kernel
        Size of the kernel i.e., the sliding window for each
        dimension of input. *[w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list
        indicating the per-dimension paddings.
    data_format
        NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12.).reshape((2,2,3))
    >>> b = ivy.arange(24.).reshape((2,3,4))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.avg_pool1d(2, 2, "VALID"))
    {
        a: ivy.array([[[1.5, 2.5, 3.5]],
                      [[7.5, 8.5, 9.5]]]),
        b: ivy.array([[[2., 3., 4., 5.]],
                      [[14., 15., 16., 17.]]])
    }
    """
    pass


def static_avg_pool2d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kernel: Union[int, Tuple[int], Tuple[int, int]],
    strides: Union[int, Tuple[int], Tuple[int, int]],
    padding: str,
    /,
    *,
    data_format: str = "NHWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.avg_pool2d. This method simply
    wraps the function, and so the docstring for ivy.avg_pool2d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window to take a max over.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(ivy.Container.static_avg_pool2d(x, (2, 2), (1, 1), "SAME"))
    {
        a: ivy.array([], shape=(2, 0, 2, 2)),
        b: (<class ivy.array.array.Array> shape=[2, 3, 2, 2])
    }
    """
    pass


def avg_pool2d(
    self: ivy.Container,
    kernel: Union[int, Tuple[int], Tuple[int, int]],
    strides: Union[int, Tuple[int], Tuple[int, int]],
    padding: str,
    /,
    *,
    data_format: str = "NHWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of `ivy.avg_pool2d`. This method simply
    wraps the function, and so the docstring for `ivy.avg_pool2d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window to take a max over.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.avg_pool2d((2, 2), (1, 1), "SAME"))
    {
        a: ivy.array([], shape=(2, 0, 2, 2)),
        b: (<class ivy.array.array.Array> shape=[2, 3, 2, 2])
    }
    """
    pass


def static_avg_pool3d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
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
    >>> print(ivy.Container.static_avg_pool3d(x, 2, 1, "VALID"))
    {
        a: ivy.array([], shape=(1, 1, 0, 2, 2)),
        b: ivy.array([[[[[10., 11.],
                         [12., 13.]]]],
                   [[[[34., 35.],
                         [36., 37.]]]]])
    }
    """
    pass


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
    """
    pass


def static_dct(
    x: ivy.Container,
    /,
    *,
    type: Optional[Literal[1, 2, 3, 4]] = 2,
    n: Optional[int] = None,
    axis: Optional[int] = -1,
    norm: Optional[Literal["ortho"]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.dct. This method simply wraps
    the function, and so the docstring for ivy.dct also applies to this method
    with minimal changes.

    Parameters
    ----------
    x
        Container with the input signals.
    type
        The type of the dct. Must be 1, 2, 3 or 4.
    n
        The lenght of the transform. If n is less than the input signal lenght,
        then x is truncated, if n is larger than x is zero-padded.
    norm
        The type of normalization to be applied. Must be either None or "ortho".
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The transformed input.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([8, 16, 24, 32, 40, 48, 56, 64]),
    ...                   b=ivy.array([1,  2,  3,  4,  5,  6,  7,  8]))
    >>> ivy.Container.static_dct(x, type=2, norm='ortho')
    {
        a: ivy.array([102., -51.5, 0., -5.39, 0., -1.61, 0.,
                    -0.406]),
        b: ivy.array([12.7, -6.44, 0., -0.673, 0., -0.201, 0.,
                    -0.0507])
    }

    With multiple :class:`ivy.Container` inputs:

    >>> x = ivy.Container(a=ivy.array([  8, 16,  24,  32,   40,   48,   56,   64]),
    ...                   b=ivy.array([11., 54, 23., 13., 255., 255., 132., 182.]))
    >>> n = ivy.Container(a=9, b=5)
    >>> type = ivy.Container(a=2, b=4)
    >>> norm = ivy.Container(a="ortho", b=None)
    >>> ivy.Container.static_dct(x, type=type, n=n, norm=norm)
    {
        a: ivy.array([96., -28.2, -31.9, 22.9, -26., 19.8, -17., 10.9,
                    -5.89]),
        b: ivy.array([242., -253., 286., -515., 467.])
    }
    """
    pass


def dct(
    self: ivy.Container,
    /,
    *,
    type: Optional[Literal[1, 2, 3, 4]] = 2,
    n: Optional[int] = None,
    axis: Optional[int] = -1,
    norm: Optional[Literal["ortho"]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.dct. This method simply wraps
    the function, and so the docstring for ivy.dct also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        Container with the input signals.
    type
        The type of the dct. Must be 1, 2, 3 or 4.
    n
        The lenght of the transform. If n is less than the input signal lenght,
        then x is truncated, if n is larger then x is zero-padded.
    norm
        The type of normalization to be applied. Must be either None or "ortho".
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The transformed input.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([8, 16, 24, 32, 40, 48, 56, 64]),
    ...                   b=ivy.array([1,  2,  3,  4,  5,  6,  7,  8]))
    >>> x.dct(type=2, norm='ortho')
    {
        a: ivy.array([102., -51.5, 0., -5.39, 0., -1.61, 0.,
                    -0.406]),
        b: ivy.array([12.7, -6.44, 0., -0.673, 0., -0.201, 0.,
                    -0.0507])
    }
    """
    pass


#ivy.container.experimental.linear_algebra
# global
from typing import Union, Optional, List, Dict

# local
from ivy.container.base import ContainerBase
import ivy


def static_diagflat(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    offset: Optional[int] = 0,
    padding_value: Optional[float] = 0,
    align: Optional[str] = "RIGHT_LEFT",
    num_rows: Optional[int] = -1,
    num_cols: Optional[int] = -1,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    pass


def diagflat(
    self: ivy.Container,
    /,
    *,
    offset: Optional[int] = 0,
    padding_value: Optional[float] = 0,
    align: Optional[str] = "RIGHT_LEFT",
    num_rows: Optional[int] = -1,
    num_cols: Optional[int] = -1,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.diagflat.
    This method simply wraps the function, and so the docstring for
    ivy.diagflat also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.Container(a=[1,2])
    >>> ivy.diagflat(x, k=1)
    {
        a: ivy.array([[0, 1, 0],
                      [0, 0, 2],
                      [0, 0, 0]])
    }
    """
    pass


def static_kron(
    a: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    b: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.kron. This method simply wraps
    the function, and so the docstring for ivy.kron also applies to this method
    with minimal changes.

    Parameters
    ----------
    a
        first container with input arrays.
    b
        second container with input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the Kronecker product of
        the arrays in the input containers, computed element-wise

    Examples
    --------
    >>> a = ivy.Container(x=ivy.array([1,2]), y=ivy.array(50))
    >>> b = ivy.Container(x=ivy.array([3,4]), y=ivy.array(9))
    >>> ivy.Container.static_kron(a, b)
    {
        a: ivy.array([3, 4, 6, 8])
        b: ivy.array([450])
    }
    """
    pass


def kron(
    self: ivy.Container,
    b: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.kron.
    This method simply wraps the function, and so the docstring for
    ivy.kron also applies to this method with minimal changes.

    Examples
    --------
    >>> a = ivy.Container(x=ivy.array([1,2]), y=ivy.array([50]))
    >>> b = ivy.Container(x=ivy.array([3,4]), y=ivy.array(9))
    >>> a.kron(b)
    {
        a: ivy.array([3, 4, 6, 8])
        b: ivy.array([450])
    }
    """
    pass


#ivy.container.experimental.manipulation
# global
from typing import (
    Optional,
    Union,
    List,
    Dict,
    Sequence,
    Tuple,
    Literal,
    Any,
    Callable,
    Iterable,
)
from numbers import Number

# local
import ivy
from ivy.container.base import ContainerBase


def static_moveaxis(
    a: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    source: Union[int, Sequence[int]],
    destination: Union[int, Sequence[int]],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.moveaxis. This method simply wraps
    the function, and so the docstring for ivy.moveaxis also applies to this method
    with minimal changes.

    Parameters
    ----------
    a
        The container with the arrays whose axes should be reordered.
    source
        Original positions of the axes to move. These must be unique.
    destination
        Destination positions for each of the original axes.
        These must also be unique.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with moved axes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.zeros((3, 4, 5)), b=ivy.zeros((2,7,6)))
    >>> ivy.Container.static_moveaxis(x, 0, -1).shape
    {
        a: (4, 5, 3)
        b: (7, 6, 2)
    }
    """
    pass


def moveaxis(
    self: ivy.Container,
    source: Union[int, Sequence[int]],
    destination: Union[int, Sequence[int]],
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.moveaxis. This method simply
    wraps the function, and so the docstring for ivy.flatten also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        The container with the arrays whose axes should be reordered.
    source
        Original positions of the axes to move. These must be unique.
    destination
        Destination positions for each of the original axes.
        These must also be unique.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with moved axes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.zeros((3, 4, 5)), b=ivy.zeros((2,7,6)))
    >>> x.moveaxis(, 0, -1).shape
    {
        a: (4, 5, 3)
        b: (7, 6, 2)
    }
    """
    pass


def static_heaviside(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.heaviside. This method simply wraps
    the function, and so the docstring for ivy.heaviside also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        input container including the arrays.
    x2
        values to use where the array is zero.
    out
        optional output container array, for writing the result to.

    Returns
    -------
    ret
        output container with element-wise Heaviside step function of each array.

    Examples
    --------
    With :class:`ivy.Array` input:
    >>> x1 = ivy.Container(a=ivy.array([-1.5, 0, 2.0]), b=ivy.array([3.0, 5.0])
    >>> x2 = ivy.Container(a=0.5, b=[1.0, 2.0])
    >>> ivy.Container.static_heaviside(x1, x2)
    {
        a: ivy.array([ 0. ,  0.5,  1. ])
        b: ivy.array([1.0, 1.0])
    }
    """
    pass


def heaviside(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.heaviside. This method simply
    wraps the function, and so the docstring for ivy.heaviside also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        input container including the arrays.
    x2
        values to use where the array is zero.
    out
        optional output container array, for writing the result to.

    Returns
    -------
    ret
        output container with element-wise Heaviside step function of each array.

    Examples
    --------
    With :class:`ivy.Array` input:
    >>> x1 = ivy.Container(a=ivy.array([-1.5, 0, 2.0]), b=ivy.array([3.0, 5.0])
    >>> x2 = ivy.Container(a=0.5, b=[1.0, 2.0])
    >>> x1.heaviside(x2)
    {
        a: ivy.array([ 0. ,  0.5,  1. ])
        b: ivy.array([1.0, 1.0])
    }
    """
    pass


def static_flipud(
    m: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.flipud. This method simply wraps
    the function, and so the docstring for ivy.flipud also applies to this method
    with minimal changes.

    Parameters
    ----------
    m
        the container with arrays to be flipped.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the input container's array
        with elements order reversed along axis 0.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> m = ivy.Container(a=ivy.diag([1, 2, 3]), b=ivy.arange(4))
    >>> ivy.Container.static_flipud(m)
    {
        a: ivy.array(
            [[ 0.,  0.,  3.],
             [ 0.,  2.,  0.],
             [ 1.,  0.,  0.]]
        )
        b: ivy.array([3, 2, 1, 0])
    }
    """
    pass


def flipud(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.flipud. This method simply
    wraps the function, and so the docstring for ivy.flipud also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with arrays to be flipped.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the input container's array
        with elements order reversed along axis 0.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> m = ivy.Container(a=ivy.diag([1, 2, 3]), b=ivy.arange(4))
    >>> m.flipud()
    {
        a: ivy.array(
            [[ 0.,  0.,  3.],
             [ 0.,  2.,  0.],
             [ 1.,  0.,  0.]]
        )
        b: ivy.array([3, 2, 1, 0])
    }
    """
    pass


def vstack(
    self: ivy.Container,
    /,
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.stack. This method
    simply wraps the function, and so the docstring for ivy.stack
    also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
    >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
    >>> x.vstack([y])
    {
        a: ivy.array([[[0, 1],
                    [2, 3]],
                    [[3, 2],
                    [1, 0]]]),
        b: ivy.array([[[4, 5]],
                    [[1, 0]]])
    }
    """
    pass


def static_vstack(
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.stack. This method simply wraps the
    function, and so the docstring for ivy.vstack also applies to this method
    with minimal changes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])],
                          b=ivy.arange(3))
    >>> ivy.Container.static_vstack(c)
    {
        a: ivy.array([[1, 2, 3],
                      [0, 0, 0]]),
        b: ivy.array([[0],
                      [1],
                      [2]])
    }
    """
    pass


def hstack(
    self: ivy.Container,
    /,
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.hstack. This method
    simply wraps the function, and so the docstring for ivy.hstack
    also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
    >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
    >>> x.hstack([y])
    {
        a: ivy.array([[0, 1, 3, 2],
                      [2, 3, 1, 0]]),
        b: ivy.array([[4, 5, 1, 0]])
    }
    """
    pass


def static_hstack(
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.hstack. This method simply wraps the
    function, and so the docstring for ivy.hstack also applies to this method
    with minimal changes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])])
    >>> ivy.Container.static_hstack(c)
    {
        a: ivy.array([1, 2, 3, 0, 0, 0])
    }
    """
    pass


def static_rot90(
    m: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    k: Optional[int] = 1,
    axes: Optional[Tuple[int, int]] = (0, 1),
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.rot90.
    This method simply wraps the function, and so the docstring for
    ivy.rot90 also applies to this method with minimal changes.

    Parameters
    ----------
    m
        Input array of two or more dimensions.
    k
        Number of times the array is rotated by 90 degrees.
    axes
        The array is rotated in the plane defined by the axes. Axes must be
        different.
    key_chains
        The key-chains to apply or not apply the method to. Default is None.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is True.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is False.
    map_sequences
        Whether to also map method to sequences (lists, tuples). Default is False.
    out
        optional output container, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        Container with a rotated view of m.
        
    Examples
    --------
    >>> m = ivy.Container(a=ivy.array([[1,2], [3,4]]),\
                    b=ivy.array([[1,2,3,4],\
                                [7,8,9,10]]))
    >>> ivy.Container.static_rot90(m)
    {
        a: ivy.array([[2, 4],
                      [1, 3]]),
        b: ivy.array([[4, 10],
                      [3, 9],
                      [2, 8],
                      [1, 7]])
    }
    """
    pass


def rot90(
    self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    k: Optional[int] = 1,
    axes: Optional[Tuple[int, int]] = (0, 1),
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.rot90.
    This method simply wraps the function, and so the docstring for
    ivy.rot90 also applies to this method with minimal changes.

    Parameters
    ----------
    self
        Input array of two or more dimensions.
    k
        Number of times the array is rotated by 90 degrees.
    axes
        The array is rotated in the plane defined by the axes. Axes must be
        different.
    key_chains
        The key-chains to apply or not apply the method to. Default is None.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is True.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is False.
    map_sequences
        Whether to also map method to sequences (lists, tuples). Default is False.
    out
        optional output container, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        Container with a rotated view of input array.

    Examples
    --------
    >>> m = ivy.Container(a=ivy.array([[1,2], [3,4]]),\
                    b=ivy.array([[1,2,3,4],\
                                [7,8,9,10]]))
    >>> m.rot90()
    {
        a: ivy.array([[2, 4],
                      [1, 3]]),
        b: ivy.array([[4, 10],
                      [3, 9],
                      [2, 8],
                      [1, 7]])
    }
    """
    pass


def static_top_k(
    x: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    k: int,
    /,
    *,
    axis: Optional[int] = -1,
    largest: Optional[bool] = True,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[Tuple[ivy.Container, ivy.Container]] = None,
) -> Tuple[ivy.Container, ivy.Container]:
    """ivy.Container static method variant of ivy.top_k. This method simply wraps
    the function, and so the docstring for ivy.top_k also applies to this method
    with minimal changes.

    Parameters
    ----------
    x
        The container to compute top_k for.
    k
        Number of top elements to retun must not exceed the array size.
    axis
        The axis along which we must return the top elements default value is 1.
    largest
        If largest is set to False we return k smallest elements of the array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``
    out:
        Optional output tuple, for writing the result to. Must have two Container,
        with a shape that the returned tuple broadcast to.

    Returns
    -------
    ret
        a container with indices and values.

    Examples
    --------
    With :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([-1, 2, -4]), b=ivy.array([4., 5., 0.]))
    >>> y = ivy.Container.static_top_k(x, 2)
    >>> print(y)
    {
        a: [
            values = ivy.array([ 2, -1]),
            indices = ivy.array([1, 0])
        ],
        b: [
            values = ivy.array([5., 4.]),
            indices = ivy.array([1, 0])
        ]
    }
    """
    return ContainerBase.multi_map_in_static_method(
        "top_k",
        x,
        k,
        axis=axis,
        largest=largest,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
        out=out,
    )

def top_k(
    self: ivy.Container,
    k: int,
    /,
    *,
    axis: Optional[int] = -1,
    largest: Optional[bool] = True,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[Tuple[ivy.Container, ivy.Container]] = None,
) -> Tuple[ivy.Container, ivy.Container]:
    """ivy.Container instance method variant of ivy.top_k. This method
    simply wraps the function, and so the docstring for ivy.top_k
    also applies to this method with minimal changes.

    Parameters
    ----------
    self
        The container to compute top_k for.
    k
        Number of top elements to retun must not exceed the array size.
    axis
        The axis along which we must return the top elements default value is 1.
    largest
        If largest is set to False we return k smallest elements of the array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``
    out:
        Optional output tuple, for writing the result to. Must have two Container,
        with a shape that the returned tuple broadcast to.

    Returns
    -------
    ret
        a container with indices and values.

    Examples
    --------
    With :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([-1, 2, -4]), b=ivy.array([4., 5., 0.]))
    >>> y = x.top_k(2)
    >>> print(y)
    {
        a: [
            values = ivy.array([ 2, -1]),
            indices = ivy.array([1, 0])
        ],
        b: [
            values = ivy.array([5., 4.]),
            indices = ivy.array([1, 0])
        ]
    }
    """
    return self.static_top_k(
        self,
        k,
        axis=axis,
        largest=largest,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
        out=out,
    )

@staticmethod
def static_fliplr(
    m: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.fliplr. This method simply wraps
    the function, and so the docstring for ivy.fliplr also applies to this method
    with minimal changes.

    Parameters
    ----------
    m
        the container with arrays to be flipped. Arrays must be at least 2-D.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the input container's array
        with elements order reversed along axis 1.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> m = ivy.Container(a=ivy.diag([1, 2, 3]),\
                        b=ivy.array([[1, 2, 3],[4, 5, 6]]))
    >>> ivy.Container.static_fliplr(m)
    {
        a: ivy.array([[0, 0, 1],
                      [0, 2, 0],
                      [3, 0, 0]]),
        b: ivy.array([[3, 2, 1],
                      [6, 5, 4]])
    }
    """
    pass


def fliplr(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.fliplr. This method simply
    wraps the function, and so the docstring for ivy.fliplr also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with arrays to be flipped. Arrays must be at least 2-D.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the input container's array
        with elements order reversed along axis 1.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> m = ivy.Container(a=ivy.diag([1, 2, 3]),\
                        b=ivy.array([[1, 2, 3],[4, 5, 6]]))
    >>> m.fliplr()
    {
        a: ivy.array([[0, 0, 1],
                      [0, 2, 0],
                      [3, 0, 0]]),
        b: ivy.array([[3, 2, 1],
                      [6, 5, 4]])
    }
    """
    pass


def static_i0(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.i0. This method simply wraps
    the function, and so the docstring for ivy.i0 also applies to this method
    with minimal changes.

    Parameters
    ----------
    x
        the container with array inputs.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays with the modified Bessel
        function evaluated at each of the elements of x.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([1, 2, 3]), b=ivy.array(4))
    >>> ivy.Container.static_i0(x)
    {
        a: ivy.array([1.26606588, 2.2795853 , 4.88079259])
        b: ivy.array(11.30192195)
    }
    """
    pass


def i0(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.i0. This method simply
    wraps the function, and so the docstring for ivy.i0 also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with array inputs.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays with the modified Bessel
        function evaluated at each of the elements of x.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([1, 2, 3]), b=ivy.array(4))
    >>> x.i0()
    {
        a: ivy.array([1.26606588, 2.2795853 , 4.88079259])
        b: ivy.array(11.30192195)
    }
    """
    pass


def static_flatten(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    start_dim: Optional[int] = 0,
    end_dim: Optional[int] = -1,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.flatten. This method simply wraps the
    function, and so the docstring for ivy.flatten also applies to this method
    with minimal changes.

    Parameters
    ----------
    x
        input container to flatten at leaves.
    start_dim
        first dim to flatten. If not set, defaults to 0.
    end_dim
        last dim to flatten. If not set, defaults to -1.

    Returns
    -------
    ret
        Container with arrays flattened at leaves.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
    ...                   b=ivy.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]))
    >>> ivy.flatten(x)
    [{
        a: ivy.array([1, 2, 3, 4, 5, 6, 7, 8])
        b: ivy.array([9, 10, 11, 12, 13, 14, 15, 16])
    }]
    """
    pass


def flatten(
    self: ivy.Container,
    *,
    start_dim: Optional[int] = 0,
    end_dim: Optional[int] = -1,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.flatten. This method simply
    wraps the function, and so the docstring for ivy.flatten also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        input container to flatten at leaves.
    start_dim
        first dim to flatten. If not set, defaults to 0.
    end_dim
        last dim to flatten. If not set, defaults to -1.

    Returns
    -------
    ret
        Container with arrays flattened at leaves.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
    ...                   b=ivy.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]))
    >>> ivy.flatten(x)
    [{
        a: ivy.array([1, 2, 3, 4, 5, 6, 7, 8])
        b: ivy.array([9, 10, 11, 12, 13, 14, 15, 16])
    }]
    """
    pass


def static_pad(
    input: ivy.Container,
    pad_width: Union[Iterable[Tuple[int]], int],
    /,
    *,
    mode: Optional[
        Union[
            Literal[
                "constant",
                "edge",
                "linear_ramp",
                "maximum",
                "mean",
                "median",
                "minimum",
                "reflect",
                "symmetric",
                "wrap",
                "empty",
            ],
            Callable,
        ]
    ] = "constant",
    stat_length: Optional[Union[Iterable[Tuple[int]], int]] = None,
    constant_values: Optional[Union[Iterable[Tuple[Number]], Number]] = 0,
    end_values: Optional[Union[Iterable[Tuple[Number]], Number]] = 0,
    reflect_type: Optional[Literal["even", "odd"]] = "even",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
    **kwargs: Optional[Any],
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.pad. This method simply
    wraps the function, and so the docstring for ivy.pad also applies to
    this method with minimal changes.
    """
    pass


def pad(
    self: ivy.Container,
    pad_width: Union[Iterable[Tuple[int]], int],
    /,
    *,
    mode: Optional[
        Union[
            Literal[
                "constant",
                "edge",
                "linear_ramp",
                "maximum",
                "mean",
                "median",
                "minimum",
                "reflect",
                "symmetric",
                "wrap",
                "empty",
            ],
            Callable,
        ]
    ] = "constant",
    stat_length: Optional[Union[Iterable[Tuple[int]], int]] = None,
    constant_values: Optional[Union[Iterable[Tuple[Number]], Number]] = 0,
    end_values: Optional[Union[Iterable[Tuple[Number]], Number]] = 0,
    reflect_type: Optional[Literal["even", "odd"]] = "even",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
    **kwargs: Optional[Any],
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.pad. This method simply
    wraps the function, and so the docstring for ivy.pad also applies to
    this method with minimal changes.
    """
    pass


def static_vsplit(
    ary: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    indices_or_sections: Union[int, Tuple[int]],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.vsplit. This method simply wraps
    the function, and so the docstring for ivy.vsplit also applies to this method
    with minimal changes.

    Parameters
    ----------
    ary
        the container with array inputs.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n vertically, each section will be of equal
        size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including input arrays split vertically.

    Examples
    --------
    >>> ary = ivy.Container(
        a = ivy.ivy.array(
                [[[0.,  1.],
                  [2.,  3.]],
                  [[4.,  5.],
                  [6.,  7.]]]
            ),
        b=ivy.array(
                [[ 0.,  1.,  2.,  3.],
                 [ 4.,  5.,  6.,  7.],
                 [ 8.,  9., 10., 11.],
                 [12., 13., 14., 15.]])
            )
        )
    >>> ivy.Container.static_vsplit(ary, 2)
    {
        a: [ivy.array([[[0., 1.], [2., 3.]]]),
            ivy.array([[[4., 5.], [6., 7.]]])],
        b: [ivy.array([[0., 1., 2., 3.], [4., 5., 6., 7.]]),
            ivy.array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]])]
    }
    """
    pass


def vsplit(
    self: ivy.Container,
    indices_or_sections: Union[int, Tuple[int]],
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.vsplit. This method simply
    wraps the function, and so the docstring for ivy.vsplit also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with array inputs.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n vertically, each section will be of equal
        size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays with the modified Bessel
        function evaluated at each of the elements of x.

    Examples
    --------
    >>> ary = ivy.Container(
        a = ivy.ivy.array(
                [[[0.,  1.],
                  [2.,  3.]],
                  [[4.,  5.],
                  [6.,  7.]]]
            ),
        b=ivy.array(
                [[ 0.,  1.,  2.,  3.],
                 [ 4.,  5.,  6.,  7.],
                 [ 8.,  9., 10., 11.],
                 [12., 13., 14., 15.]])
            )
        )
    >>> ary.vsplit(2)
    {
        a: [ivy.array([[[0., 1.], [2., 3.]]]),
            ivy.array([[[4., 5.], [6., 7.]]])],
        b: [ivy.array([[0., 1., 2., 3.], [4., 5., 6., 7.]]),
            ivy.array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]])]
    }
    """
    pass


def static_dsplit(
    ary: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    indices_or_sections: Union[int, Tuple[int]],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.dsplit. This method simply wraps
    the function, and so the docstring for ivy.dsplit also applies to this method
    with minimal changes.

    Parameters
    ----------
    ary
        the container with array inputs.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n along the 3rd axis, each section will be of
        equal size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including input arrays split along the 3rd axis.

    Examples
    --------
    >>> ary = ivy.Container(
        a = ivy.ivy.array(
                [[[0.,  1.],
                  [2.,  3.]],
                  [[4.,  5.],
                  [6.,  7.]]]
            ),
        b=ivy.array(
                [[ 0.,  1.,  2.,  3.],
                 [ 4.,  5.,  6.,  7.],
                 [ 8.,  9., 10., 11.],
                 [12., 13., 14., 15.]])
            )
        )
    >>> ivy.Container.static_dsplit(ary, 2)
    {
        a: [ivy.array([[[0., 1.], [2., 3.]]]),
            ivy.array([[[4., 5.], [6., 7.]]])],
        b: [ivy.array([[0., 1., 2., 3.], [4., 5., 6., 7.]]),
            ivy.array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]])]
    }
    """
    pass


def dsplit(
    self: ivy.Container,
    indices_or_sections: Union[int, Tuple[int]],
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.dsplit. This method simply
    wraps the function, and so the docstring for ivy.dsplit also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with array inputs.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n along the 3rd axis, each section will be of
        equal size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays with the modified Bessel
        function evaluated at each of the elements of x.

    Examples
    --------
    >>> ary = ivy.Container(
        a = ivy.ivy.array(
                [[[0.,  1.],
                  [2.,  3.]],
                  [[4.,  5.],
                  [6.,  7.]]]
            ),
        b=ivy.array(
                [[ 0.,  1.,  2.,  3.],
                 [ 4.,  5.,  6.,  7.],
                 [ 8.,  9., 10., 11.],
                 [12., 13., 14., 15.]])
            )
        )
    >>> ary.dsplit(2)
    {
        a: [ivy.array([[[0., 1.], [2., 3.]]]),
            ivy.array([[[4., 5.], [6., 7.]]])],
        b: [ivy.array([[0., 1., 2., 3.], [4., 5., 6., 7.]]),
            ivy.array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]])]
    }
    """
    pass


def dstack(
    self: ivy.Container,
    /,
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.stack. This method
    simply wraps the function, and so the docstring for ivy.stack
    also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
    >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
    >>> x.dstack([y])
    {
        a: ivy.array([[[0, 3],
                       [1, 2]],
                      [[2, 1],
                       [3, 0]]]),
        b: ivy.array([[[4, 1]],
                       [[5, 0]]])
    }
    """
    pass


def static_dstack(
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.stack. This method simply wraps the
    function, and so the docstring for ivy.dstack also applies to this method
    with minimal changes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])],
                          b=ivy.arange(3))
    >>> ivy.Container.static_dstack(c)
    {
        a: ivy.array([[1, 0],
                      [2, 0]
                      [3,0]]),
        b: ivy.array([[0, 1, 2])
    }
    """
    pass


def static_atleast_2d(
    *arys: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
) -> List[ivy.Container]:
    """
    ivy.Container static method variant of ivy.atleast_2d. This method simply wraps
    the function, and so the docstring for ivy.atleast_2d also applies to this
    method with minimal changes.

    Parameters
    ----------
    arys
        one or more container with array inputs.
    key_chains
        The keychains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.

    Returns
    -------
    ret
        container or list of container where each elements within container is
        atleast 2D. Copies are made only if necessary.

    Examples
    --------
    >>> ary = ivy.Container(a=ivy.array(1), b=ivy.array([3,4,5]),\
                    c=ivy.array([[3]]))
    >>> ivy.Container.static_atleast_2d(ary)
    {
        a: ivy.array([[1]]),
        b: ivy.array([[3, 4, 5]]),
        c: ivy.array([[3]])
    }
    """
    return ContainerBase.multi_map_in_static_method(
        "atleast_2d",
        *arys,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
    )

def atleast_2d(
    self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    *arys: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
) -> List[ivy.Container]:
    """ivy.Container instance method variant of ivy.atleast_2d. This method simply
    wraps the function, and so the docstring for ivy.atleast_2d also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        container with array inputs.
    arys
        one or more container with array inputs.
    key_chains
        The keychains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.

    Returns
    -------
    ret
        container or list of container where each elements within container is
        atleast 2D. Copies are made only if necessary.

    Examples
    --------
    >>> ary1 = ivy.Container(a=ivy.array(1), b=ivy.array([3,4]),\
                        c=ivy.array([[5]]))
    >>> ary2 = ivy.Container(a=ivy.array(9), b=ivy.array(2),\
                        c=ivy.array(3))
    >>> ary1.atleast_2d(ary2)
    [{
        a: ivy.array([[1]]),
        b: ivy.array([[3, 4]]),
        c: ivy.array([[5]])
    }, {
        a: ivy.array([[9]]),
        b: ivy.array([[2]]),
        c: ivy.array([[3]])
    }]
    """
    return self.static_atleast_2d(
        self,
        *arys,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
    )

#ivy.container.experimental.random
# global
from typing import Optional, Union, List, Dict

# local
import ivy
from ivy.container.base import ContainerBase


def static_dirichlet(
    alpha: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    size: Optional[Union[ivy.Shape, ivy.NativeShape, ivy.Container]] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    seed: Optional[int] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.dirichlet. This method
    simply wraps the function, and so the docstring for ivy.dirichlet also
    applies to this method with minimal changes.

    Parameters
    ----------
    alpha
        Sequence of floats of length k 
    size
        optional container including ints or tuple of ints, 
        Output shape for the arrays in the input container. 
    dtype
        output container array data type. If ``dtype`` is ``None``, the output data
        type will be the default floating-point data type. Default ``None``
    seed
        A python integer. Used to create a random seed distribution
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including the drawn samples.

    Examples
    --------
    >>> alpha = ivy.Container(a=ivy.array([7,6,5]), \
                              b=ivy.array([8,9,4]))
    >>> size = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_dirichlet(alpha, size)
    {
        a: ivy.array(
            [[0.43643127, 0.32325703, 0.24031169],
             [0.34251311, 0.31692529, 0.3405616 ],
             [0.5319725 , 0.22458365, 0.24344385]]
            ),
        b: ivy.array(
            [[0.26588406, 0.61075421, 0.12336174],
             [0.51142915, 0.25041268, 0.23815817],
             [0.64042903, 0.25763214, 0.10193883],
             [0.31624692, 0.46567987, 0.21807321],
             [0.37677699, 0.39914594, 0.22407707]]
            )
    }
    """
    pass


def dirichlet(
    self: ivy.Container,
    /,
    *,
    size: Optional[Union[ivy.Shape, ivy.NativeShape, ivy.Container]] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype, ivy.Container]] = None,
    seed: Optional[int] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.dirichlet. This method
    simply wraps the function, and so the docstring for ivy.shuffle also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        Sequence of floats of length k 
    size
        optional container including ints or tuple of ints, 
        Output shape for the arrays in the input container. 
    dtype
        output container array data type. If ``dtype`` is ``None``, the output data
        type will be the default floating-point data type. Default ``None``
    seed
        A python integer. Used to create a random seed distribution
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including the drawn samples.

    Examples
    --------
    >>> alpha = ivy.Container(a=ivy.array([7,6,5]), \
                              b=ivy.array([8,9,4]))
    >>> size = ivy.Container(a=3, b=5)
    >>> alpha.dirichlet(size)
    {
        a: ivy.array(
            [[0.43643127, 0.32325703, 0.24031169],
             [0.34251311, 0.31692529, 0.3405616 ],
             [0.5319725 , 0.22458365, 0.24344385]]
            ),
        b: ivy.array(
            [[0.26588406, 0.61075421, 0.12336174],
             [0.51142915, 0.25041268, 0.23815817],
             [0.64042903, 0.25763214, 0.10193883],
             [0.31624692, 0.46567987, 0.21807321],
             [0.37677699, 0.39914594, 0.22407707]]
            )
    }
    """
    pass


#ivy.container.experimental.sorting
# global
from typing import Optional, List, Union, Dict

# local
from ivy.container.base import ContainerBase
import ivy


def static_msort(
    a: Union[ivy.Array, ivy.NativeArray, ivy.Container, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.msort. This method simply wraps the
    function, and so the docstring for ivy.msort also applies to this method
    with minimal changes.

    Parameters
    ----------
    a
        array-like or container input.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        a container containing sorted input arrays.

    Examples
    --------
    With :class:`ivy.Container` input:

    >>> a = ivy.Container(x = ivy.randint(10, size=(2,3)),
    ...                   y = ivy.randint(5, size=(2,2))
    >>> ivy.Container.static_msort(a)
    {
        x: ivy.array(
            [[6, 2, 6],
             [8, 9, 6]]
            ),
        y: ivy.array(
            [[0, 0],
             [4, 0]]
            )
    }
    """
    pass


def msort(
    self: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.msort.
    This method simply wraps the function, and
    so the docstring for ivy.msort also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        input container with array-like inputs to sort.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        a container containing the sorted input arrays.

    Examples
    --------
    >>> a = ivy.Container(x = ivy.randint(10, size=(2,3)),
    ...                   y = ivy.randint(5, size=(2,2))
    >>> a.msort()
    {
        x: ivy.array(
            [[6, 2, 6],
             [8, 9, 6]]
            ),
        y: ivy.array(
            [[0, 0],
             [4, 0]]
            )
    }
    """
    pass


#ivy.container.experimental.statistical
# global
from typing import (
    Optional,
    Union,
    List,
    Dict,
    Tuple,
)

# local
import ivy
from ivy.container.base import ContainerBase


def static_median(
    input: ivy.Container,
    /,
    *,
    axis: Optional[Union[Tuple[int], int]] = None,
    keepdims: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.median. This method simply wraps
    the function, and so the docstring for ivy.median also applies to this method
    with minimal changes.

    Parameters
    ----------
    input
        Input container including arrays.
    axis
        Axis or axes along which the medians are computed. The default is to compute
        the median along a flattened version of the array.
    keepdims
        If this is set to True, the axes which are reduced are left in the result
        as dimensions with size one.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The median of the array elements.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.zeros((3, 4, 5)), b=ivy.zeros((2,7,6)))
    >>> ivy.Container.static_moveaxis(x, 0, -1).shape
    {
        a: (4, 5, 3)
        b: (7, 6, 2)
    }
    """
    pass


def median(
    self: ivy.Container,
    /,
    *,
    axis: Optional[Union[Tuple[int], int]] = None,
    keepdims: Optional[bool] = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.median. This method simply
    wraps the function, and so the docstring for ivy.median also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container including arrays.
    axis
        Axis or axes along which the medians are computed. The default is to compute
        the median along a flattened version of the array.
    keepdims
        If this is set to True, the axes which are reduced are left in the result
        as dimensions with size one.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The median of the array elements.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(
    >>>     a=ivy.array([[10, 7, 4], [3, 2, 1]]),
    >>>     b=ivy.array([[1, 4, 2], [8, 7, 0]])
    >>> )
    >>> x.median(axis=0)
    {
        a: ivy.array([6.5, 4.5, 2.5]),
        b: ivy.array([4.5, 5.5, 1.])
    }
    """
    pass


def static_nanmean(
    input: ivy.Container,
    /,
    *,
    axis: Optional[Union[Tuple[int], int]] = None,
    keepdims: Optional[bool] = False,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.nanmean. This method simply wraps
    the function, and so the docstring for ivy.nanmean also applies to this method
    with minimal changes.

    Parameters
    ----------
    input
        Input container including arrays.
    axis
        Axis or axes along which the means are computed.
        The default is to compute the mean of the flattened array.
    keepdims
        If this is set to True, the axes which are reduced are left in the result
        as dimensions with size one. With this option, the result will broadcast
        correctly against the original a. If the value is anything but the default,
        then keepdims will be passed through to the mean or sum methods of 
        sub-classes of ndarray. If the sub-classes methods does not implement 
        keepdims any exceptions will be raised.
    dtype
        The desired data type of returned tensor. Default is None.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The nanmean of the array elements in the container.

    Examples
    --------
    >>> a = ivy.Container(x=ivy.array([[1, ivy.nan], [3, 4]]),\
                            y=ivy.array([[ivy.nan, 1, 2], [1, 2, 3]])
    >>> ivy.Container.static_moveaxis(a)
    {
        x: 2.6666666666666665
        y: 1.8
    }
    """
    pass


def nanmean(
    self: ivy.Container,
    /,
    *,
    axis: Optional[Union[Tuple[int], int]] = None,
    keepdims: Optional[bool] = False,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.nanmean. This method simply
    wraps the function, and so the docstring for ivy.nanmean also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container including arrays.
    axis
        Axis or axes along which the means are computed.
        The default is to compute the mean of the flattened array.
    keepdims
        If this is set to True, the axes which are reduced are left in the result
        as dimensions with size one. With this option, the result will broadcast
        correctly against the original a. If the value is anything but the default,
        then keepdims will be passed through to the mean or sum methods of 
        sub-classes of ndarray. If the sub-classes methods does not implement 
        keepdims any exceptions will be raised.
    dtype
        The desired data type of returned tensor. Default is None.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The nanmean of the array elements in the input container.

    Examples
    --------
    >>> a = ivy.Container(x=ivy.array([[1, ivy.nan], [3, 4]]),\
                            y=ivy.array([[ivy.nan, 1, 2], [1, 2, 3]])
    >>> a.nanmean()
    {
        x: 2.6666666666666665
        y: 1.8
    }
    """
    pass


def static_unravel_index(
    indices: ivy.Container,
    shape: Tuple[int],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.unravel_index.
    This method simply wraps the function, and so the docstring
    for ivy.unravel_index also applies to this method with minimal
    changes.

    Parameters
    ----------
    input
        Input container including arrays.
    shape
        The shape of the array to use for unraveling indices.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Container with tuples that have arrays with the same shape as
        the arrays in the input container.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> indices = ivy.Container(a=ivy.array([22, 41, 37])), b=ivy.array([30, 2]))
    >>> ivy.Container.static_unravel_index(indices, (7,6))
    {
        a: (ivy.array([3, 6, 6]), ivy.array([4, 5, 1]))
        b: (ivy.array([5, 0], ivy.array([0, 2])))
    }
    """
    pass


def unravel_index(
    self: ivy.Container,
    shape: Tuple[int],
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.unravel_index.
    This method simply wraps the function, and so the docstring for
    ivy.unravel_index also applies to this method with minimal changes.

    Parameters
    ----------
    self
        Input container including arrays.
    shape
        The shape of the array to use for unraveling indices.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Container with tuples that have arrays with the same shape as
        the arrays in the input container.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> indices = ivy.Container(a=ivy.array([22, 41, 37])), b=ivy.array([30, 2]))
    >>> indices.unravel_index((7, 6))
    {
        a: (ivy.array([3, 6, 6]), ivy.array([4, 5, 1]))
        b: (ivy.array([5, 0], ivy.array([0, 2])))
    }
    """
    pass


#ivy.container.experimental.creation
# global
from typing import Optional, Tuple, Union, List, Dict

# local
import ivy
from ivy.container.base import ContainerBase


def static_triu_indices(
    n_rows: int,
    n_cols: Optional[int] = None,
    k: Optional[int] = 0,
    /,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    *,
    device: Optional[Union[ivy.Device, ivy.NativeDevice]] = None,
    out: Optional[Tuple[ivy.Array]] = None,
) -> ivy.Container:
    pass


def triu_indices(
    self: ivy.Container,
    n_rows: int,
    n_cols: Optional[int] = None,
    k: Optional[int] = 0,
    /,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    *,
    device: Optional[Union[ivy.Device, ivy.NativeDevice]] = None,
    out: Optional[Tuple[ivy.Array]] = None,
) -> ivy.Container:
    pass


def static_hann_window(
    window_length: Union[int, ivy.Container],
    periodic: Optional[bool] = True,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.hann_window. This method simply wraps
    the function, and so the docstring for ivy.hann_window also applies to this
    method with minimal changes.

    Parameters
    ----------
    window_length
        container including multiple window sizes.
    periodic
        If True, returns a window to be used as periodic function.
        If False, return a symmetric window.
    dtype
        The data type to produce. Must be a floating point type.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that contains the Hann windows.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_hann(x)
    {
        a: ivy.array([0.0000, 0.7500, 0.7500])
        b: ivy.array([0.0000, 0.3455, 0.9045, 0.9045, 0.3455])
    }
    """
    pass


def hann_window(
    self: ivy.Container,
    periodic: Optional[bool] = True,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.hann_window. This method simply
    wraps the function, and so the docstring for ivy.hann_window also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input container with window sizes.
    periodic
        If True, returns a window to be used as periodic function.
        If False, return a symmetric window.
    dtype
        The data type to produce. Must be a floating point type.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container containing the Hann windows.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.hann_window(x)
    {
        a: ivy.array([0.0000, 0.7500, 0.7500])
        b: ivy.array([0.0000, 0.3455, 0.9045, 0.9045, 0.3455])
    }
    """
    pass


def static_kaiser_window(
    window_length: Union[int, ivy.Container],
    periodic: bool = True,
    beta: float = 12.0,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.kaiser_window. This method
    simply wraps the function, and so the docstring for ivy.kaiser_window
    also applies to this method with minimal changes.

    Parameters
    ----------
    window_length
        input container including window lenghts.
    periodic
        If True, returns a periodic window suitable for use in spectral analysis.
        If False, returns a symmetric window suitable for use in filter design.
    beta
        a float used as shape parameter for the window.
    dtype
        data type of the returned array.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Kaiser windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_kaiser_window(x, True, 5)
    {
        a: ivy.array([0.2049, 0.8712, 0.8712]),
        a: ivy.array([0.0367, 0.7753, 0.7753]),
    }
    """
    pass


def kaiser_window(
    self: ivy.Container,
    periodic: bool = True,
    beta: float = 12.0,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.kaiser_window. This method
    simply wraps the function, and so the docstring for ivy.kaiser_window
    also applies to this method with minimal changes.

    Parameters
    ----------
    self
        input container including window lenghts.
    periodic
        If True, returns a periodic window suitable for use in spectral analysis.
        If False, returns a symmetric window suitable for use in filter design.
    beta
        a float used as shape parameter for the window.
    dtype
        data type of the returned array.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Kaiser windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_kaiser_window(x, True, 5)
    {
        a: ivy.array([0.2049, 0.8712, 0.8712]),
        a: ivy.array([0.0367, 0.7753, 0.7753]),
    }
    """
    pass


def static_kaiser_bessel_derived_window(
    x: Union[int, ivy.Array, ivy.NativeArray, ivy.Container],
    periodic: bool = True,
    beta: float = 12.0,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.kaiser_bessel_derived_window.
    This method simply wraps the function, and so the docstring for
    ivy.kaiser_bessel_derived_window also applies to this method with
    minimal changes.

    Parameters
    ----------
    x
        input container including window lenghts.
    periodic
        If True, returns a periodic window suitable for use in spectral analysis.
        If False, returns a symmetric window suitable for use in filter design.
    beta
        a float used as shape parameter for the window.
    dtype
        data type of the returned array.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Kaiser Bessel Derived windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_kaiser_bessel_derived_window(x, True, 5)
    {
        a: ivy.array([0.70710677, 0.70710677]),
        b: ivy.array([0.18493208, 0.9827513 , 0.9827513 , 0.18493208]),
    }
    """
    pass


def kaiser_bessel_derived_window(
    self: ivy.Container,
    periodic: bool = True,
    beta: float = 12.0,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.kaiser_bessel_derived_window.
    This method simply wraps the function, and so the docstring for
    ivy.kaiser_bessel_derived_window also applies to this method with
    minimal changes.

    Parameters
    ----------
    self
        input container including window lenghts.
    periodic
        If True, returns a periodic window suitable for use in spectral analysis.
        If False, returns a symmetric window suitable for use in filter design.
    beta
        a float used as shape parameter for the window.
    dtype
        data type of the returned array.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Kaiser Bessel Derived windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5))
    >>> x.kaiser_bessel_derived_window(True, 5)
    {
        a: ivy.array([0.70710677, 0.70710677]),
        b: ivy.array([0.18493208, 0.9827513 , 0.9827513 , 0.18493208]),
    }
    """
    pass


def static_hamming_window(
    x: Union[int, ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    periodic: Optional[bool] = True,
    alpha: Optional[float] = 0.54,
    beta: Optional[float] = 0.46,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.hamming_window.
    This method simply wraps the function, and so the docstring for
    ivy.hamming_window also applies to this method with
    minimal changes.

    Parameters
    ----------
    x
        input container including window lenghts.
    periodic
        If True, returns a window to be used as periodic function.
        If False, return a symmetric window.
    alpha
        The coefficient alpha in the hamming window equation
    beta
        The coefficient beta in the hamming window equation
    dtype
        data type of the returned arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Hamming windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_hamming_window(x, periodic=True, alpha=0.2, beta=2)
    {
        a: ivy.array([-1.8000,  1.2000,  1.2000]),
        b: ivy.array([-1.8000, -0.4180,  1.8180,  1.8180, -0.4180])
    }
    """
    pass


def hamming_window(
    self: ivy.Container,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    periodic: Optional[bool] = True,
    alpha: Optional[float] = 0.54,
    beta: Optional[float] = 0.46,
    dtype: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.hamming_window.
    This method simply wraps the function, and so the docstring for
    ivy.hamming_window also applies to this method with
    minimal changes.

    Parameters
    ----------
    self
        input container including window lenghts.
    periodic
        If True, returns a window to be used as periodic function.
        If False, return a symmetric window.
    alpha
        The coefficient alpha in the hamming window equation
    beta
        The coefficient beta in the hamming window equation
    dtype
        data type of the returned arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The container that includes the Hamming windows.

    Examples
    --------
    >>> x = ivy.Container(a=3, b=5))
    >>> x.hamming_window(periodic=True, alpha=0.2, beta=2)
    {
        a: ivy.array([-1.8000,  1.2000,  1.2000]),
        b: ivy.array([-1.8000, -0.4180,  1.8180,  1.8180, -0.4180])
    }
    """
    pass


#ivy.container.experimental.elementwise
# global
from typing import Optional, Union, List, Dict, Tuple

# local
import ivy
from ivy.container.base import ContainerBase


def static_sinc(
    x: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.sinc. This method simply
    wraps the function, and so the docstring for ivy.sinc also
    applies to this method with minimal changes.

    Parameters
    ----------
    x
        input container whose elements are each expressed in radians.
        Should have a floating-point data type.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        optional output container, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        a container containing the sinc of each element in ``x``. The returned
        container must have a floating-point data type determined by
        :ref:`type-promotion`.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([0.5, 1.5, 2.5]),
    ...                   b=ivy.array([3.5, 4.5, 5.5]))
    >>> y = ivy.Container.static_sinc(x)
    >>> print(y)
    {
        a: ivy.array([0.636, -0.212, 0.127]),
        b: ivy.array([-0.090, 0.070, -0.057])
    }
    """
    pass


def sinc(
    self: ivy.Container,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.sinc. This method simply
    wraps the function, and so the docstring for ivy.sinc also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        input container whose elements are each expressed in radians.
        Should have a floating-point data type.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        optional output container, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        a container containing the sinc of each element in ``self``.
        The returned container must have a floating-point data type
        determined by :ref:`type-promotion`.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([0.5, 1.5, 2.5]),
    ...                   b=ivy.array([3.5, 4.5, 5.5]))
    >>> y = x.sinc()
    >>> print(y)
    {
        a: ivy.array([0.637,-0.212,0.127]),
        b: ivy.array([-0.0909,0.0707,-0.0579])
    }
    """
    pass


def static_lcm(
    x1: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.lcm. This method simply wraps the
    function, and so the docstring for ivy.lcm also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        first input container.
    x2
        second input container.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        a container containing the element-wise least common multiples
        of the arrays contained in x1 and x2.

    Examples
    --------
    >>> x1=ivy.Container(a=ivy.array([2, 3, 4]),
    ...                  b=ivy.array([6, 54, 62, 10]))
    >>> x2=ivy.Container(a=ivy.array([5, 8, 15]),
    ...                  b=ivy.array([32, 40, 25, 13]))
    >>> ivy.Container.lcm(x1, x2)
    {
        a: ivy.array([10, 21, 60]),
        b: ivy.array([96, 1080, 1550, 130])
    }

    """
    pass


def lcm(
    self: ivy.Container,
    x2: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.lcm. This method simply wraps the
    function, and so the docstring for ivy.lcm also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        first input container.
    x2
        second input container.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        a container containing the the element-wise least common multiples
        of the arrays contained in x1 and x2.

    Examples
    --------
    >>> x1=ivy.Container(a=ivy.array([2, 3, 4]),
    ...                  b=ivy.array([6, 54, 62, 10]))
    >>> x2=ivy.Container(a=ivy.array([5, 8, 15]),
    ...                  b=ivy.array([32, 40, 25, 13]))
    >>> x1.lcm(x2)
    {
        a: ivy.array([10, 24, 60]),
        b: ivy.array([96, 1080, 1550, 130])
    }

    """
    pass


def static_fmod(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.fmod. This method simply wraps
    the function, and so the docstring for ivy.fmod also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        container with the first input arrays.
    x2
        container with the second input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise remainder of divisions.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([2, 3, 4]),\
                           b=ivy.array([ivy.nan, 0, ivy.nan]))
    >>> x2 = ivy.Container(a=ivy.array([1, 5, 2]),\
                           b=ivy.array([0, ivy.nan, ivy.nan]))
    >>> ivy.Container.static_fmod(x1, x2)
    {
        a: ivy.array([ 0,  3,  0])
        b: ivy.array([ nan,  nan,  nan])
    }
    """
    pass


def fmod(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.fmod. This method simply
    wraps the function, and so the docstring for ivy.fmod also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        container with the first input arrays.
    x2
        container with the second input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise remainder of divisions.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([2, 3, 4]),\
                           b=ivy.array([ivy.nan, 0, ivy.nan]))
    >>> x2 = ivy.Container(a=ivy.array([1, 5, 2]),\
                           b=ivy.array([0, ivy.nan, ivy.nan]))
    >>> x1.fmod(x2)
    {
        a: ivy.array([ 0,  3,  0])
        b: ivy.array([ nan,  nan,  nan])
    }
    """
    pass


def static_fmax(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.fmax. This method simply wraps
    the function, and so the docstring for ivy.fmax also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        container with the first input arrays.
    x2
        container with the second input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise maximums.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([2, 3, 4]),\
                           b=ivy.array([ivy.nan, 0, ivy.nan]))
    >>> x2 = ivy.Container(a=ivy.array([1, 5, 2]),\
                           b=ivy.array([0, ivy.nan, ivy.nan]))
    >>> ivy.Container.static_fmax(x1, x2)
    {
        a: ivy.array([ 2.,  5.,  4.])
        b: ivy.array([ 0,  0,  nan])
    }
    """
    pass


def fmax(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.fmax. This method simply
    wraps the function, and so the docstring for ivy.fmax also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        container with the first input arrays.
    x2
        container with the second input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise maximums.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([2, 3, 4]),\
                           b=ivy.array([ivy.nan, 0, ivy.nan]))
    >>> x2 = ivy.Container(a=ivy.array([1, 5, 2]),\
                           b=ivy.array([0, ivy.nan, ivy.nan]))
    >>> x1.fmax(x2)
    {
        a: ivy.array([ 2.,  5.,  4.])
        b: ivy.array([ 0,  0,  nan])
    }
    """
    pass


def static_float_power(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.float_power. This method simply wraps
    the function, and so the docstring for ivy.float_power also applies to this
    method with minimal changes.

    Parameters
    ----------
    x1
        container with the base input arrays.
    x2
        container with the exponent input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with base arrays raised to the powers
        of exponents arrays, element-wise .

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([2, 10]))
    >>> x2 = ivy.Container(a=ivy.array([1, 3, 1]), b=0)
    >>> ivy.Container.static_float_power(x1, x2)
    {
        a: ivy.array([1,  8,  3])
        b: ivy.array([1, 1])
    }
    """
    pass


def float_power(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.float_power. This method simply
    wraps the function, and so the docstring for ivy.float_power also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    x2
        container with the exponent input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with base arrays raised to the powers
        of exponents arrays, element-wise .

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([2, 10]))
    >>> x2 = ivy.Container(a=ivy.array([1, 3, 1]), b=0)
    >>> x1.float_power(x2)
    {
        a: ivy.array([1,  8,  3])
        b: ivy.array([1, 1])
    }
    """
    pass


def static_exp2(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.exp2. This method simply wraps
    the function, and so the docstring for ivy.exp2 also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise 2 to the power
        of input arrays elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=[5, 6, 7])
    >>> ivy.Container.static_exp2(x)
    {
        a: ivy.array([2.,  4.,  8.])
        b: ivy.array([32., 64., 128.])
    }
    """
    pass


def exp2(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.exp2. This method simply
    wraps the function, and so the docstring for ivy.exp2 also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise 2 to the power
        of input array elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=[5, 6, 7])
    >>> x.exp2()
    {
        a: ivy.array([2.,  4.,  8.])
        b: ivy.array([32., 64., 128.])
    }
    """
    pass


def static_count_nonzero(
    a: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: Optional[bool] = False,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.count_nonzero. This method simply
    wraps the function, and so the docstring for ivy.count_nonzero also applies
    to this method with minimal changes.

    Parameters
    ----------
    a
        container with the base input arrays.
    axis
        optional axis or tuple of axes along which to count non-zeros. Default is
        None, meaning that non-zeros will be counted along a flattened
        version of the input array.
    keepdims
        optional, if this is set to True, the axes that are counted are left in the
        result as dimensions with size one. With this option, the result
        will broadcast correctly against the input array.
    dtype
        optional output dtype. Default is of type integer.
    key_chains
        The key-chains to apply or not apply the method to. Default is None.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is True.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is False.
    map_sequences
        Whether to also map method to sequences (lists, tuples). Default is False.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including number of non-zero values in the array along a
        given axis. Otherwise, container with the total number of non-zero
        values in the array is returned.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> ivy.Container.static_count_nonzero(x)
    {
        a: ivy.array(7),
        b: ivy.array(7)
    }
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> ivy.Container.static_count_nonzero(x, axis=0)
    {
        a: ivy.array([1, 2, 2, 2]),
        b: ivy.array([[1, 2],
                      [2, 2]])
    }
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> ivy.Container.static_count_nonzero(x, axis=(0,1), keepdims=True)
    {
        a: ivy.array([[7]]),
        b: ivy.array([[[3, 4]]])
    }
    """
    pass


def count_nonzero(
    self: ivy.Container,
    /,
    *,
    axis: Optional[Union[int, Tuple[int, ...]]] = None,
    keepdims: Optional[bool] = False,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.count_nonzero. This method
    simply wraps the function, and so the docstring for ivy.count_nonzero also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    axis
        optional axis or tuple of axes along which to count non-zeros. Default is
        None, meaning that non-zeros will be counted along a flattened
        version of the input array.
    keepdims
        optional, if this is set to True, the axes that are counted are left in the
        result as dimensions with size one. With this option, the result
        will broadcast correctly against the input array.
    dtype
        optional output dtype. Default is of type integer.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including number of non-zero values in the array along a
        given axis. Otherwise, container with the total number of non-zero
        values in the array is returned.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> x.count_nonzero()
    {
        a: ivy.array(7),
        b: ivy.array(7)
    }
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> x.count_nonzero(axis=0)
    {
        a: ivy.array([1, 2, 2, 2]),
        b: ivy.array([[1, 2],
                      [2, 2]])
    }
    >>> x = ivy.Container(a=ivy.array([[0, 1, 2, 3],[4, 5, 6, 7]]),\
                    b=ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]]))
    >>> x.count_nonzero(axis=(0,1), keepdims=True)
    {
        a: ivy.array([[7]]),
        b: ivy.array([[[3, 4]]])
    }
    """
    pass


def static_nansum(
    x: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    axis: Optional[Union[tuple, int]] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    keepdims: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.nansum. This method simply wraps
    the function, and so the docstring for ivy.nansum also applies to this method
    with minimal changes.
    
    Parameters
    ----------
    x
        Input array.
    axis
        Axis or axes along which the sum is computed.
        The default is to compute the sum of the flattened array.
    dtype
        The type of the returned array and of the accumulator in
        which the elements are summed. By default, the dtype of input is used.
    keepdims
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one.
    out
        Alternate output array in which to place the result.
        The default is None.
    
    Returns
    -------
    ret
        A new array holding the result is returned unless out is specified,
        in which it is returned.
    
    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([[10, 7, 4], [3, 2, 1]]),\
            b=ivy.array([[1, 4, 2], [ivy.nan, ivy.nan, 0]]))
    >>> ivy.Container.static_nansum(x)
    {
        a: 27,
        b: 7.0
    }
    >>> ivy.Container.static_nansum(x, axis=0)
    {
        a: ivy.array([13, 9, 5]),
        b: ivy.array([1., 4., 2.])
    }
    >>> ivy.Container.static_nansum(x, axis=1)
    {
        a: ivy.array([21, 6]),
        b: ivy.array([7., 0.])
    }
    """
    pass


def nansum(
    self: ivy.Container,
    /,
    *,
    axis: Optional[Union[tuple, int]] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    keepdims: Optional[bool] = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.nansum. This method simply
    wraps the function, and so the docstring for ivy.nansum also applies to this
    method with minimal changes.
    
    Parameters
    ----------
    self
        Input container including arrays.
    axis
        Axis or axes along which the sum is computed.
        The default is to compute the sum of the flattened array.
    dtype
        The type of the returned array and of the accumulator in
        which the elements are summed. By default, the dtype of input is used.
    keepdims
        If this is set to True, the axes which are reduced are left
        in the result as dimensions with size one.
    out
        Alternate output array in which to place the result.
        The default is None.
    
    Returns
    -------
    ret
        A new array holding the result is returned unless out is specified,
        in which it is returned.
    
    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([[10, 7, 4], [3, 2, 1]]),\
            b=ivy.array([[1, 4, 2], [ivy.nan, ivy.nan, 0]]))
    >>> x.nansum(axis=0)
    {
        a: ivy.array([13, 9, 5]),
        b: ivy.array([1., 4., 2.])
    }
    >>> x.nansum(axis=1)
    {
        a: ivy.array([21, 6]),
        b: ivy.array([7., 0.])
    }
    """
    pass


def static_gcd(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container, int, list, tuple],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container, int, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.gcd. This method simply wraps
    the function, and so the docstring for ivy.gcd also applies to this
    method with minimal changes.

    Parameters
    ----------
    x1
        first input container with array-like items.
    x2
        second input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise gcd of input arrays.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([1, 2, 3]))
    >>> x2 = ivy.Container(a=ivy.array([5, 6, 7]),\
                           b=10)
    >>> ivy.Container.static_gcd(x1, x2)
    {
        a: ivy.array([1.,  1.,  3.])
        b: ivy.array([1., 2., 1.])
    }
    """
    pass


def gcd(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.gcd. This method simply
    wraps the function, and so the docstring for ivy.gcd also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        first input container with array-like items.
    x2
        second input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise gcd of input arrays.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([1, 2, 3]))
    >>> x2 = ivy.Container(a=ivy.array([5, 6, 7]),\
                           b=10)
    >>> x1.gcd(x2)
    {
        a: ivy.array([1.,  1.,  3.])
        b: ivy.array([1., 2., 1.])
    }
    """
    pass


def static_isclose(
    a: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    b: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    rtol: Optional[float] = 1e-05,
    atol: Optional[float] = 1e-08,
    equal_nan: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.isclose. This method simply wraps
    the function, and so the docstring for ivy.isclose also applies to this method
    with minimal changes.

    Parameters
    ----------
    a
        Input container containing first input array.
    b
        Input container containing second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in a will be
        considered equal to NaN's in b in the output array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        A new array holding the result is returned unless out is specified,
        in which it is returned.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([1.0, ivy.nan]),\
            b=ivy.array([1.0, ivy.nan]))
    >>> y = ivy.Container(a=ivy.array([1.0, ivy.nan]),\
            b=ivy.array([1.0, ivy.nan]))
    >>> ivy.Container.static_isclose(x, y)
    {
        a: ivy.array([True, False]),
        b: ivy.array([True, False])
    }
    >>> ivy.Container.static_isclose(x, y, equal_nan=True)
    {
        a: ivy.array([True, True]),
        b: ivy.array([True, True])
    }
    >>> x = ivy.Container(a=ivy.array([1.0, 2.0]),\
            b=ivy.array([1.0, 2.0]))
    >>> y = ivy.Container(a=ivy.array([1.0, 2.001]),\
            b=ivy.array([1.0, 2.0]))
    >>> ivy.Container.static_isclose(x, y, atol=0.0)
    {
        a: ivy.array([True, False]),
        b: ivy.array([True, True])
    }
    >>> ivy.Container.static_isclose(x, y, rtol=0.01, atol=0.0)
    {
        a: ivy.array([True, True]),
        b: ivy.array([True, True])
    }
    """
    pass


def isclose(
    self: ivy.Container,
    b: ivy.Container,
    /,
    *,
    rtol: Optional[float] = 1e-05,
    atol: Optional[float] = 1e-08,
    equal_nan: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.isclose. This method simply
    wraps the function, and so the docstring for ivy.isclose also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container containing first input array.
    b
        Input container containing second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in a will be
        considered equal to NaN's in b in the output array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        A new array holding the result is returned unless out is specified,
        in which it is returned.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([1.0, ivy.nan]),\
            b=ivy.array([1.0, ivy.nan]))
    >>> y = ivy.Container(a=ivy.array([1.0, ivy.nan]),\
            b=ivy.array([1.0, ivy.nan]))
    >>> x.isclose(y)
    {
        a: ivy.array([True, False]),
        b: ivy.array([True, False])
    }
    >>> x.isclose(y, equal_nan=True)
    {
        a: ivy.array([True, True]),
        b: ivy.array([True, True])
    }
    >>> x = ivy.Container(a=ivy.array([1.0, 2.0]),\
            b=ivy.array([1.0, 2.0]))
    >>> y = ivy.Container(a=ivy.array([1.0, 2.001]),\
            b=ivy.array([1.0, 2.0]))
    >>> x.isclose(y, atol=0.0)
    {
        a: ivy.array([True, False]),
        b: ivy.array([True, True])
    }
    >>> x.isclose(y, rtol=0.01, atol=0.0)
    {
        a: ivy.array([True, True]),
        b: ivy.array([True, True])
    }
    """
    pass


def static_isposinf(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.isposinf. This method simply wraps
    the function, and so the docstring for ivy.isposinf also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including a boolean array with values
        True where the corresponding element of the input
        is positive infinity and values False where the
        element of the input is not positive infinity.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, ivy.inf, -ivy.inf]),\
                            b=ivy.array([5, ivy.inf, ivy.inf]))
    >>> ivy.Container.static_isposinf(x)
    {
        a: ivy.array([False, True, False]),
        b: ivy.array([False, True, True])
    }
    """
    pass


def isposinf(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.isposinf. This method simply
    wraps the function, and so the docstring for ivy.isposinf also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Returns container including a boolean array with values
        True where the corresponding element of the input
        is positive infinity and values False where the
        element of the input is not positive infinity.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, ivy.inf, -ivy.inf]),\
                           b=ivy.array([5, ivy.inf, ivy.inf]))
    >>> x.isposinf()
    {
        a: ivy.array([False, True, False]),
        b: ivy.array([False, True, True])
    }
    """
    pass


def static_isneginf(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.isneginf. This method simply wraps
    the function, and so the docstring for ivy.isneginf also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including a boolean array with values
        True where the corresponding element of the input
        is negative infinity and values False where the
        element of the input is not negative infinity.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, ivy.inf, -ivy.inf]),\
                            b=ivy.array([5, -ivy.inf, -ivy.inf]))
    >>> ivy.Container.static_isneginf(x)
    {
        a: ivy.array([False, False, True]),
        b: ivy.array([False, True, True])
    }
    """
    pass


def isneginf(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.isneginf. This method simply
    wraps the function, and so the docstring for ivy.isneginf also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        container with the base input arrays.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Returns container including a boolean array with values
        True where the corresponding element of the input
        is negative infinity and values False where the
        element of the input is not negative infinity.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, ivy.inf, -ivy.inf]),\
                           b=ivy.array([5, -ivy.inf, -ivy.inf]))
    >>> x.isneginf()
    {
        a: ivy.array([False, False, True]),
        b: ivy.array([False, True, True])
    }
    """
    pass


def static_nan_to_num(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    copy: Optional[bool] = True,
    nan: Optional[Union[float, int]] = 0.0,
    posinf: Optional[Union[float, int]] = None,
    neginf: Optional[Union[float, int]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.nan_to_num. This method simply wraps
    the function, and so the docstring for ivy.nan_to_num also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        Input container with array items.
    copy
        Whether to create a copy of x (True) or to replace values in-place (False).
        The in-place operation only occurs if casting to an array does not require
        a copy. Default is True.
    nan
        Value to be used to fill NaN values. If no value is passed then NaN values
        will be replaced with 0.0.
    posinf
        Value to be used to fill positive infinity values. If no value is passed
        then positive infinity values will be replaced with a very large number.
    neginf
        Value to be used to fill negative infinity values.
        If no value is passed then negative infinity values
        will be replaced with a very small (or negative) number.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with replaced non-finite elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, 2, 3, nan]),\
                           b=ivy.array([1, 2, 3, inf]))
    >>> ivy.Container.static_nan_to_num(x, posinf=5e+100)
    {
        a: ivy.array([1.,  1.,  3.,  0.0])
        b: ivy.array([1., 2., 1.,  5e+100])
    }
    """
    pass


def nan_to_num(
    self: ivy.Container,
    /,
    *,
    copy: Optional[bool] = True,
    nan: Optional[Union[float, int]] = 0.0,
    posinf: Optional[Union[float, int]] = None,
    neginf: Optional[Union[float, int]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.nan_to_num. This method simply
    wraps the function, and so the docstring for ivy.nan_to_num also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input container with array items.
    copy
        Whether to create a copy of x (True) or to replace values in-place (False).
        The in-place operation only occurs if casting to an array does not require
        a copy. Default is True.
    nan
        Value to be used to fill NaN values. If no value is passed then NaN values
        will be replaced with 0.0.
    posinf
        Value to be used to fill positive infinity values. If no value is passed
        then positive infinity values will be replaced with a very large number.
    neginf
        Value to be used to fill negative infinity values.
        If no value is passed then negative infinity values
        will be replaced with a very small (or negative) number.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with replaced non-finite elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, 2, 3, nan]),\
                           b=ivy.array([1, 2, 3, inf]))
    >>> x.nan_to_num(posinf=5e+100)
    {
        a: ivy.array([1.,  1.,  3.,  0.0])
        b: ivy.array([1., 2., 1.,  5e+100])
    }
    """
    pass


def static_logaddexp2(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.logaddexp2. This method simply wraps
    the function, and so the docstring for ivy.logaddexp2 also applies to this
    method with minimal changes.

    Parameters
    ----------
    x1
        first input container with array-like items.
    x2
        second input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise logaddexp2 of input arrays.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([1, 2, 3]))
    >>> x2 = ivy.Container(a=ivy.array([4, 5, 6]),\
                           b=5)
    >>> ivy.Container.static_logaddexp2(x1, x2)
    {
        a: ivy.array([4.169925, 5.169925, 6.169925])
        b: ivy.array([5.08746284, 5.169925  , 5.32192809])
    }
    """
    pass


def logaddexp2(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.logaddexp2. This method simply
    wraps the function, and so the docstring for ivy.logaddexp2 also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        first input container with array-like items.
    x2
        second input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise logaddexp2 of input arrays.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1, 2, 3]),\
                           b=ivy.array([1, 2, 3]))
    >>> x2 = ivy.Container(a=ivy.array([4, 5, 6]),\
                           b=5)
    >>> x1.logaddexp2(x2)
    {
        a: ivy.array([4.169925, 5.169925, 6.169925])
        b: ivy.array([5.08746284, 5.169925  , 5.32192809])
    }
    """
    pass


def static_signbit(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container, float, int, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.signbit. This method simply wraps
    the function, and so the docstring for ivy.signbit also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise signbit of input arrays.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, -2, 3]),\
                           b=-5)
    >>> ivy.Container.static_signbit(x)
    {
        a: ivy.array([False, True, False])
        b: ivy.array([True])
    }
    """
    pass


def signbit(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.signbit. This method simply
    wraps the function, and so the docstring for ivy.signbit also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input container with array-like items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise signbit of input arrays.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([1, -2, 3]),\
                           b=-5)
    >>> x.signbit()
    {
        a: ivy.array([False, True, False])
        b: ivy.array([True])
    }
    """
    pass


def static_allclose(
    x1: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    rtol: Optional[float] = 1e-05,
    atol: Optional[float] = 1e-08,
    equal_nan: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.allclose. This method simply wraps
    the function, and so the docstring for ivy.allclose also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        Input container containing first input array.
    x2
        Input container containing second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in x1 will be
        considered equal to NaN's in x2 in the output array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        A new container holding the result is returned unless out is specified,
        in which it is returned.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> x2 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> y = ivy.Container.static_allclose(x1, x2)
    >>> print(y)
    {
        a: true,
        b: true
    }

    >>> x1 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> x2 = ivy.Container(a=ivy.array([1., 2., 3.0003]),\
    ...                         b=ivy.array([1.0006, 2., 3.]))
    >>> y = ivy.Container.static_allclose(x1, x2, rtol=1e-3)
    >>> print(y)
    {
        a: true,
        b: true
    }
    """
    pass


def allclose(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    rtol: Optional[float] = 1e-05,
    atol: Optional[float] = 1e-08,
    equal_nan: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.allclose. This method simply
    wraps the function, and so the docstring for ivy.allclose also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container containing first input array.
    x2
        Input container containing second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in x1 will be
        considered equal to NaN's in x2 in the output array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        A new container holding the result is returned unless out is specified,
        in which it is returned.

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> x2 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> y = x1.allclose(x2)
    >>> print(y)
    {
        a: true,
        b: true
    }

    >>> x1 = ivy.Container(a=ivy.array([1., 2., 3.]),\
    ...                         b=ivy.array([1., 2., 3.]))
    >>> x2 = ivy.Container(a=ivy.array([1., 2., 3.0003]),\
    ...                         b=ivy.array([1.0006, 2., 3.]))
    >>> y = x1.allclose(x2, rtol=1e-3)
    >>> print(y)
    {
        a: true,
        b: true
    }
    """
    pass


def static_fix(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.fix. This method simply wraps
    the function, and so the docstring for ivy.fix also applies to this
    method with minimal changes.

    Parameters
    ----------
    x
        input container with array items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise rounding of
        input arrays elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([2.1, 2.9, -2.1]),\
                           b=ivy.array([3.14]))
    >>> ivy.Container.static_fix(x)
    {
        a: ivy.array([ 2.,  2., -2.])
        b: ivy.array([ 3.0 ])
    }
    """
    pass


def fix(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.fix. This method simply
    wraps the function, and so the docstring for ivy.fix also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input container with array items.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with element-wise rounding of
        input arrays elements.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([2.1, 2.9, -2.1]),\
                           b=ivy.array([3.14]))
    >>> x.fix()
    {
        a: ivy.array([ 2.,  2., -2.])
        b: ivy.array([ 3.0 ])
    }
    """
    pass


def static_nextafter(
    x1: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    x2: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.nextafter. This method simply wraps
    the function, and so the docstring for ivy.nextafter also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        Input container containing first input arrays.
    x2
        Input container containing second input arrays.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        container including the next representable values of
        input container's arrays, element-wise

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1.0e-50, 2.0e+50]),\
    ...                         b=ivy.array([2.0, 1.0])
    >>> x2 = ivy.Container(a=ivy.array([5.5e-30]),\
    ...                         b=ivy.array([-2.0]))
    >>> ivy.Container.static_nextafter(x1, x2)
    {
        a: ivy.array([1.4013e-45., 3.4028e+38]),
        b: ivy.array([5.5e-30])
    }
    """
    pass


def nextafter(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.nextafter. This method simply
    wraps the function, and so the docstring for ivy.nextafter also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container containing first input array.
    x2
        Input container containing second input array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        container including the next representable values of
        input container's arrays, element-wise

    Examples
    --------
    >>> x1 = ivy.Container(a=ivy.array([1.0e-50, 2.0e+50]),\
    ...                         b=ivy.array([2.0, 1.0])
    >>> x2 = ivy.Container(a=ivy.array([5.5e-30]),\
    ...                         b=ivy.array([-2.0]))
    >>> x1.nextafter(x2)
    {
        a: ivy.array([1.4013e-45., 3.4028e+38]),
        b: ivy.array([5.5e-30])
    }
    """
    pass


#ivy.container.experimental.layers
# global
from typing import Optional, Union, List, Dict, Tuple, Literal

# local
import ivy
from ivy.container.base import ContainerBase


def static_max_pool1d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kernel: Union[int, Tuple[int]],
    strides: Union[int, Tuple[int]],
    padding: str,
    /,
    *,
    data_format: str = "NWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.max_pool1d. This method simply
    wraps the function, and so the docstring for ivy.max_pool1d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Container of input images *[batch_size, w, d_in]*.
    kernel
        Size of the kernel i.e., the sliding window for each
        dimension of input. *[w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list
        indicating the per-dimension paddings.
    data_format
        NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12.).reshape((2,2,3))
    >>> b = ivy.arange(24.).reshape((2,3,4))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(ivy.Container.static_max_pool1d(x,2, 2, "VALID"))
    {
        a: ivy.array([[[3., 4., 5.]],
                      [[9., 10., 11.]]]),
        b: ivy.array([[[4., 5., 6., 7.]],
                      [[16., 17., 18., 19.]]])
    }
    """
    pass


def max_pool1d(
    self: ivy.Container,
    kernel: Union[int, Tuple[int]],
    strides: Union[int, Tuple[int]],
    padding: str,
    /,
    *,
    data_format: str = "NWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of `ivy.max_pool1d`. This method simply
    wraps the function, and so the docstring for `ivy.max_pool1d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Container of input images *[batch_size, w, d_in]*.
    kernel
        Size of the kernel i.e., the sliding window for each
        dimension of input. *[w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list
        indicating the per-dimension paddings.
    data_format
        NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12.).reshape((2,2,3))
    >>> b = ivy.arange(24.).reshape((2,3,4))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.max_pool1d(2, 2, "VALID"))
    {
        a: ivy.array([[[3., 4., 5.]],
                      [[9., 10., 11.]]]),
        b: ivy.array([[[4., 5., 6., 7.]],
                      [[16., 17., 18., 19.]]])
    }
    """
    pass


def static_max_pool2d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kernel: Union[int, Tuple[int], Tuple[int, int]],
    strides: Union[int, Tuple[int], Tuple[int, int]],
    padding: str,
    /,
    *,
    data_format: str = "NHWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.max_pool2dd. This method simply
    wraps the function, and so the docstring for ivy.max_pool2d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window to take a max over.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(ivy.Container.static_max_pool2d(x, (2, 2), (1, 1), "SAME"))
    {
        a: (<class ivy.array.array.Array> shape=[2, 1, 3, 2]),
        b: (<class ivy.array.array.Array> shape=[2, 4, 3, 2])
    }
    """
    pass


def max_pool2d(
    self: ivy.Container,
    kernel: Union[int, Tuple[int], Tuple[int, int]],
    strides: Union[int, Tuple[int], Tuple[int, int]],
    padding: str,
    /,
    *,
    data_format: str = "NHWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of `ivy.max_pool2d`. This method simply
    wraps the function, and so the docstring for `ivy.max_pool2d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window to take a max over.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    dilations
        The dilation factor for each dimension of input. (Default value = 1)
    out
        optional output array, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.max_pool2d(2, 2), (1, 1), "SAME"))
    {
        a: (<class ivy.array.array.Array> shape=[2, 1, 3, 2]),
        b: (<class ivy.array.array.Array> shape=[2, 4, 3, 2])
    }
    """
    pass


def static_max_pool3d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
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
    """ivy.Container static method variant of ivy.max_pool3d. This method simply
    wraps the function, and so the docstring for ivy.max_pool3d also applies
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
    >>> print(ivy.Container.static_max_pool3d(x, 2, 1, "VALID"))
    {
        a: ivy.array([], shape=(1, 1, 0, 2, 2)),
        b: ivy.array([[[[[20, 21],
                         [22, 23]]]],
                   [[[[44, 45],
                         [46, 47]]]]])
    }
    """
    pass


def max_pool3d(
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
    """ivy.Container static method variant of ivy.max_pool3d. This method simply
    wraps the function, and so the docstring for ivy.max_pool3d also applies
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
        b: ivy.array([[[[[20, 21],
                         [22, 23]]]],
                   [[[[44, 45],
                         [46, 47]]]]])
    }
    """
    pass


def static_avg_pool1d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kernel: Union[int, Tuple[int]],
    strides: Union[int, Tuple[int]],
    padding: str,
    /,
    *,
    data_format: str = "NWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.avg_pool1d. This method simply
    wraps the function, and so the docstring for ivy.avg_pool1d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Container of input images *[batch_size, w, d_in]*.
    kernel
        Size of the kernel i.e., the sliding window for each
        dimension of input. *[w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list
        indicating the per-dimension paddings.
    data_format
        NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12.).reshape((2,2,3))
    >>> b = ivy.arange(24.).reshape((2,3,4))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(ivy.Container.static_avg_pool1d(x,2, 2, "VALID"))
    {
        a: ivy.array([[[1.5, 2.5, 3.5]],
                      [[7.5, 8.5, 9.5]]]),
        b: ivy.array([[[2., 3., 4., 5.]],
                      [[14., 15., 16., 17.]]])
    }
    """
    pass


def avg_pool1d(
    self: ivy.Container,
    kernel: Union[int, Tuple[int]],
    strides: Union[int, Tuple[int]],
    padding: str,
    /,
    *,
    data_format: str = "NWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of `ivy.avg_pool1d`. This method simply
    wraps the function, and so the docstring for `ivy.avg_pool1d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Container of input images *[batch_size, w, d_in]*.
    kernel
        Size of the kernel i.e., the sliding window for each
        dimension of input. *[w]*.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        SAME" or "VALID" indicating the algorithm, or list
        indicating the per-dimension paddings.
    data_format
        NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12.).reshape((2,2,3))
    >>> b = ivy.arange(24.).reshape((2,3,4))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.avg_pool1d(2, 2, "VALID"))
    {
        a: ivy.array([[[1.5, 2.5, 3.5]],
                      [[7.5, 8.5, 9.5]]]),
        b: ivy.array([[[2., 3., 4., 5.]],
                      [[14., 15., 16., 17.]]])
    }
    """
    pass


def static_avg_pool2d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    kernel: Union[int, Tuple[int], Tuple[int, int]],
    strides: Union[int, Tuple[int], Tuple[int, int]],
    padding: str,
    /,
    *,
    data_format: str = "NHWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.avg_pool2d. This method simply
    wraps the function, and so the docstring for ivy.avg_pool2d also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window to take a max over.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(ivy.Container.static_avg_pool2d(x, (2, 2), (1, 1), "SAME"))
    {
        a: ivy.array([], shape=(2, 0, 2, 2)),
        b: (<class ivy.array.array.Array> shape=[2, 3, 2, 2])
    }
    """
    pass


def avg_pool2d(
    self: ivy.Container,
    kernel: Union[int, Tuple[int], Tuple[int, int]],
    strides: Union[int, Tuple[int], Tuple[int, int]],
    padding: str,
    /,
    *,
    data_format: str = "NHWC",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of `ivy.avg_pool2d`. This method simply
    wraps the function, and so the docstring for `ivy.avg_pool2d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window to take a max over.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> a = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> b = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> x = ivy.Container({'a': a, 'b': b})
    >>> print(x.avg_pool2d((2, 2), (1, 1), "SAME"))
    {
        a: ivy.array([], shape=(2, 0, 2, 2)),
        b: (<class ivy.array.array.Array> shape=[2, 3, 2, 2])
    }
    """
    pass


def static_avg_pool3d(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
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
    >>> print(ivy.Container.static_avg_pool3d(x, 2, 1, "VALID"))
    {
        a: ivy.array([], shape=(1, 1, 0, 2, 2)),
        b: ivy.array([[[[[10., 11.],
                         [12., 13.]]]],
                   [[[[34., 35.],
                         [36., 37.]]]]])
    }
    """
    pass


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
    """
    pass


def static_dct(
    x: ivy.Container,
    /,
    *,
    type: Optional[Literal[1, 2, 3, 4]] = 2,
    n: Optional[int] = None,
    axis: Optional[int] = -1,
    norm: Optional[Literal["ortho"]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.dct. This method simply wraps
    the function, and so the docstring for ivy.dct also applies to this method
    with minimal changes.

    Parameters
    ----------
    x
        Container with the input signals.
    type
        The type of the dct. Must be 1, 2, 3 or 4.
    n
        The lenght of the transform. If n is less than the input signal lenght,
        then x is truncated, if n is larger than x is zero-padded.
    norm
        The type of normalization to be applied. Must be either None or "ortho".
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The transformed input.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([8, 16, 24, 32, 40, 48, 56, 64]),
    ...                   b=ivy.array([1,  2,  3,  4,  5,  6,  7,  8]))
    >>> ivy.Container.static_dct(x, type=2, norm='ortho')
    {
        a: ivy.array([102., -51.5, 0., -5.39, 0., -1.61, 0.,
                    -0.406]),
        b: ivy.array([12.7, -6.44, 0., -0.673, 0., -0.201, 0.,
                    -0.0507])
    }

    With multiple :class:`ivy.Container` inputs:

    >>> x = ivy.Container(a=ivy.array([  8, 16,  24,  32,   40,   48,   56,   64]),
    ...                   b=ivy.array([11., 54, 23., 13., 255., 255., 132., 182.]))
    >>> n = ivy.Container(a=9, b=5)
    >>> type = ivy.Container(a=2, b=4)
    >>> norm = ivy.Container(a="ortho", b=None)
    >>> ivy.Container.static_dct(x, type=type, n=n, norm=norm)
    {
        a: ivy.array([96., -28.2, -31.9, 22.9, -26., 19.8, -17., 10.9,
                    -5.89]),
        b: ivy.array([242., -253., 286., -515., 467.])
    }
    """
    pass


def dct(
    self: ivy.Container,
    /,
    *,
    type: Optional[Literal[1, 2, 3, 4]] = 2,
    n: Optional[int] = None,
    axis: Optional[int] = -1,
    norm: Optional[Literal["ortho"]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.dct. This method simply wraps
    the function, and so the docstring for ivy.dct also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        Container with the input signals.
    type
        The type of the dct. Must be 1, 2, 3 or 4.
    n
        The lenght of the transform. If n is less than the input signal lenght,
        then x is truncated, if n is larger then x is zero-padded.
    norm
        The type of normalization to be applied. Must be either None or "ortho".
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        The transformed input.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([8, 16, 24, 32, 40, 48, 56, 64]),
    ...                   b=ivy.array([1,  2,  3,  4,  5,  6,  7,  8]))
    >>> x.dct(type=2, norm='ortho')
    {
        a: ivy.array([102., -51.5, 0., -5.39, 0., -1.61, 0.,
                    -0.406]),
        b: ivy.array([12.7, -6.44, 0., -0.673, 0., -0.201, 0.,
                    -0.0507])
    }
    """
    pass


#ivy.container.experimental.linear_algebra
# global
from typing import Union, Optional, List, Dict

# local
from ivy.container.base import ContainerBase
import ivy


def static_diagflat(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    offset: Optional[int] = 0,
    padding_value: Optional[float] = 0,
    align: Optional[str] = "RIGHT_LEFT",
    num_rows: Optional[int] = -1,
    num_cols: Optional[int] = -1,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    pass


def diagflat(
    self: ivy.Container,
    /,
    *,
    offset: Optional[int] = 0,
    padding_value: Optional[float] = 0,
    align: Optional[str] = "RIGHT_LEFT",
    num_rows: Optional[int] = -1,
    num_cols: Optional[int] = -1,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.diagflat.
    This method simply wraps the function, and so the docstring for
    ivy.diagflat also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.Container(a=[1,2])
    >>> ivy.diagflat(x, k=1)
    {
        a: ivy.array([[0, 1, 0],
                      [0, 0, 2],
                      [0, 0, 0]])
    }
    """
    pass


def static_kron(
    a: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    b: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.kron. This method simply wraps
    the function, and so the docstring for ivy.kron also applies to this method
    with minimal changes.

    Parameters
    ----------
    a
        first container with input arrays.
    b
        second container with input arrays
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the Kronecker product of
        the arrays in the input containers, computed element-wise

    Examples
    --------
    >>> a = ivy.Container(x=ivy.array([1,2]), y=ivy.array(50))
    >>> b = ivy.Container(x=ivy.array([3,4]), y=ivy.array(9))
    >>> ivy.Container.static_kron(a, b)
    {
        a: ivy.array([3, 4, 6, 8])
        b: ivy.array([450])
    }
    """
    pass


def kron(
    self: ivy.Container,
    b: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.kron.
    This method simply wraps the function, and so the docstring for
    ivy.kron also applies to this method with minimal changes.

    Examples
    --------
    >>> a = ivy.Container(x=ivy.array([1,2]), y=ivy.array([50]))
    >>> b = ivy.Container(x=ivy.array([3,4]), y=ivy.array(9))
    >>> a.kron(b)
    {
        a: ivy.array([3, 4, 6, 8])
        b: ivy.array([450])
    }
    """
    pass


#ivy.container.experimental.manipulation
# global
from typing import (
    Optional,
    Union,
    List,
    Dict,
    Sequence,
    Tuple,
    Literal,
    Any,
    Callable,
    Iterable,
)
from numbers import Number

# local
import ivy
from ivy.container.base import ContainerBase


def static_moveaxis(
    a: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    source: Union[int, Sequence[int]],
    destination: Union[int, Sequence[int]],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.moveaxis. This method simply wraps
    the function, and so the docstring for ivy.moveaxis also applies to this method
    with minimal changes.

    Parameters
    ----------
    a
        The container with the arrays whose axes should be reordered.
    source
        Original positions of the axes to move. These must be unique.
    destination
        Destination positions for each of the original axes.
        These must also be unique.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with moved axes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.zeros((3, 4, 5)), b=ivy.zeros((2,7,6)))
    >>> ivy.Container.static_moveaxis(x, 0, -1).shape
    {
        a: (4, 5, 3)
        b: (7, 6, 2)
    }
    """
    pass


def moveaxis(
    self: ivy.Container,
    source: Union[int, Sequence[int]],
    destination: Union[int, Sequence[int]],
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.moveaxis. This method simply
    wraps the function, and so the docstring for ivy.flatten also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        The container with the arrays whose axes should be reordered.
    source
        Original positions of the axes to move. These must be unique.
    destination
        Destination positions for each of the original axes.
        These must also be unique.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        Container including arrays with moved axes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.zeros((3, 4, 5)), b=ivy.zeros((2,7,6)))
    >>> x.moveaxis(, 0, -1).shape
    {
        a: (4, 5, 3)
        b: (7, 6, 2)
    }
    """
    pass


def static_heaviside(
    x1: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    x2: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.heaviside. This method simply wraps
    the function, and so the docstring for ivy.heaviside also applies to this method
    with minimal changes.

    Parameters
    ----------
    x1
        input container including the arrays.
    x2
        values to use where the array is zero.
    out
        optional output container array, for writing the result to.

    Returns
    -------
    ret
        output container with element-wise Heaviside step function of each array.

    Examples
    --------
    With :class:`ivy.Array` input:
    >>> x1 = ivy.Container(a=ivy.array([-1.5, 0, 2.0]), b=ivy.array([3.0, 5.0])
    >>> x2 = ivy.Container(a=0.5, b=[1.0, 2.0])
    >>> ivy.Container.static_heaviside(x1, x2)
    {
        a: ivy.array([ 0. ,  0.5,  1. ])
        b: ivy.array([1.0, 1.0])
    }
    """
    pass


def heaviside(
    self: ivy.Container,
    x2: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.heaviside. This method simply
    wraps the function, and so the docstring for ivy.heaviside also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        input container including the arrays.
    x2
        values to use where the array is zero.
    out
        optional output container array, for writing the result to.

    Returns
    -------
    ret
        output container with element-wise Heaviside step function of each array.

    Examples
    --------
    With :class:`ivy.Array` input:
    >>> x1 = ivy.Container(a=ivy.array([-1.5, 0, 2.0]), b=ivy.array([3.0, 5.0])
    >>> x2 = ivy.Container(a=0.5, b=[1.0, 2.0])
    >>> x1.heaviside(x2)
    {
        a: ivy.array([ 0. ,  0.5,  1. ])
        b: ivy.array([1.0, 1.0])
    }
    """
    pass


def static_flipud(
    m: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.flipud. This method simply wraps
    the function, and so the docstring for ivy.flipud also applies to this method
    with minimal changes.

    Parameters
    ----------
    m
        the container with arrays to be flipped.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the input container's array
        with elements order reversed along axis 0.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> m = ivy.Container(a=ivy.diag([1, 2, 3]), b=ivy.arange(4))
    >>> ivy.Container.static_flipud(m)
    {
        a: ivy.array(
            [[ 0.,  0.,  3.],
             [ 0.,  2.,  0.],
             [ 1.,  0.,  0.]]
        )
        b: ivy.array([3, 2, 1, 0])
    }
    """
    pass


def flipud(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.flipud. This method simply
    wraps the function, and so the docstring for ivy.flipud also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with arrays to be flipped.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the input container's array
        with elements order reversed along axis 0.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> m = ivy.Container(a=ivy.diag([1, 2, 3]), b=ivy.arange(4))
    >>> m.flipud()
    {
        a: ivy.array(
            [[ 0.,  0.,  3.],
             [ 0.,  2.,  0.],
             [ 1.,  0.,  0.]]
        )
        b: ivy.array([3, 2, 1, 0])
    }
    """
    pass


def vstack(
    self: ivy.Container,
    /,
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.stack. This method
    simply wraps the function, and so the docstring for ivy.stack
    also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
    >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
    >>> x.vstack([y])
    {
        a: ivy.array([[[0, 1],
                    [2, 3]],
                    [[3, 2],
                    [1, 0]]]),
        b: ivy.array([[[4, 5]],
                    [[1, 0]]])
    }
    """
    pass


def static_vstack(
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.stack. This method simply wraps the
    function, and so the docstring for ivy.vstack also applies to this method
    with minimal changes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])],
                          b=ivy.arange(3))
    >>> ivy.Container.static_vstack(c)
    {
        a: ivy.array([[1, 2, 3],
                      [0, 0, 0]]),
        b: ivy.array([[0],
                      [1],
                      [2]])
    }
    """
    pass


def hstack(
    self: ivy.Container,
    /,
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.hstack. This method
    simply wraps the function, and so the docstring for ivy.hstack
    also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
    >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
    >>> x.hstack([y])
    {
        a: ivy.array([[0, 1, 3, 2],
                      [2, 3, 1, 0]]),
        b: ivy.array([[4, 5, 1, 0]])
    }
    """
    pass


def static_hstack(
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.hstack. This method simply wraps the
    function, and so the docstring for ivy.hstack also applies to this method
    with minimal changes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])])
    >>> ivy.Container.static_hstack(c)
    {
        a: ivy.array([1, 2, 3, 0, 0, 0])
    }
    """
    pass


def static_rot90(
    m: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    k: Optional[int] = 1,
    axes: Optional[Tuple[int, int]] = (0, 1),
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.rot90.
    This method simply wraps the function, and so the docstring for
    ivy.rot90 also applies to this method with minimal changes.

    Parameters
    ----------
    m
        Input array of two or more dimensions.
    k
        Number of times the array is rotated by 90 degrees.
    axes
        The array is rotated in the plane defined by the axes. Axes must be
        different.
    key_chains
        The key-chains to apply or not apply the method to. Default is None.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is True.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is False.
    map_sequences
        Whether to also map method to sequences (lists, tuples). Default is False.
    out
        optional output container, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        Container with a rotated view of m.
        
    Examples
    --------
    >>> m = ivy.Container(a=ivy.array([[1,2], [3,4]]),\
                    b=ivy.array([[1,2,3,4],\
                                [7,8,9,10]]))
    >>> ivy.Container.static_rot90(m)
    {
        a: ivy.array([[2, 4],
                      [1, 3]]),
        b: ivy.array([[4, 10],
                      [3, 9],
                      [2, 8],
                      [1, 7]])
    }
    """
    pass


def rot90(
    self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    /,
    *,
    k: Optional[int] = 1,
    axes: Optional[Tuple[int, int]] = (0, 1),
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.rot90.
    This method simply wraps the function, and so the docstring for
    ivy.rot90 also applies to this method with minimal changes.

    Parameters
    ----------
    self
        Input array of two or more dimensions.
    k
        Number of times the array is rotated by 90 degrees.
    axes
        The array is rotated in the plane defined by the axes. Axes must be
        different.
    key_chains
        The key-chains to apply or not apply the method to. Default is None.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is True.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is False.
    map_sequences
        Whether to also map method to sequences (lists, tuples). Default is False.
    out
        optional output container, for writing the result to. It must have a shape
        that the inputs broadcast to.

    Returns
    -------
    ret
        Container with a rotated view of input array.

    Examples
    --------
    >>> m = ivy.Container(a=ivy.array([[1,2], [3,4]]),\
                    b=ivy.array([[1,2,3,4],\
                                [7,8,9,10]]))
    >>> m.rot90()
    {
        a: ivy.array([[2, 4],
                      [1, 3]]),
        b: ivy.array([[4, 10],
                      [3, 9],
                      [2, 8],
                      [1, 7]])
    }
    """
    pass


def static_top_k(
    x: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    k: int,
    /,
    *,
    axis: Optional[int] = -1,
    largest: Optional[bool] = True,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[Tuple[ivy.Container, ivy.Container]] = None,
) -> Tuple[ivy.Container, ivy.Container]:
    """ivy.Container static method variant of ivy.top_k. This method simply wraps
    the function, and so the docstring for ivy.top_k also applies to this method
    with minimal changes.

    Parameters
    ----------
    x
        The container to compute top_k for.
    k
        Number of top elements to retun must not exceed the array size.
    axis
        The axis along which we must return the top elements default value is 1.
    largest
        If largest is set to False we return k smallest elements of the array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``
    out:
        Optional output tuple, for writing the result to. Must have two Container,
        with a shape that the returned tuple broadcast to.

    Returns
    -------
    ret
        a container with indices and values.

    Examples
    --------
    With :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([-1, 2, -4]), b=ivy.array([4., 5., 0.]))
    >>> y = ivy.Container.static_top_k(x, 2)
    >>> print(y)
    {
        a: [
            values = ivy.array([ 2, -1]),
            indices = ivy.array([1, 0])
        ],
        b: [
            values = ivy.array([5., 4.]),
            indices = ivy.array([1, 0])
        ]
    }
    """
    return ContainerBase.multi_map_in_static_method(
        "top_k",
        x,
        k,
        axis=axis,
        largest=largest,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
        out=out,
    )

def top_k(
    self: ivy.Container,
    k: int,
    /,
    *,
    axis: Optional[int] = -1,
    largest: Optional[bool] = True,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[Tuple[ivy.Container, ivy.Container]] = None,
) -> Tuple[ivy.Container, ivy.Container]:
    """ivy.Container instance method variant of ivy.top_k. This method
    simply wraps the function, and so the docstring for ivy.top_k
    also applies to this method with minimal changes.

    Parameters
    ----------
    self
        The container to compute top_k for.
    k
        Number of top elements to retun must not exceed the array size.
    axis
        The axis along which we must return the top elements default value is 1.
    largest
        If largest is set to False we return k smallest elements of the array.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``
    out:
        Optional output tuple, for writing the result to. Must have two Container,
        with a shape that the returned tuple broadcast to.

    Returns
    -------
    ret
        a container with indices and values.

    Examples
    --------
    With :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([-1, 2, -4]), b=ivy.array([4., 5., 0.]))
    >>> y = x.top_k(2)
    >>> print(y)
    {
        a: [
            values = ivy.array([ 2, -1]),
            indices = ivy.array([1, 0])
        ],
        b: [
            values = ivy.array([5., 4.]),
            indices = ivy.array([1, 0])
        ]
    }
    """
    return self.static_top_k(
        self,
        k,
        axis=axis,
        largest=largest,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
        out=out,
    )

@staticmethod
def static_fliplr(
    m: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.fliplr. This method simply wraps
    the function, and so the docstring for ivy.fliplr also applies to this method
    with minimal changes.

    Parameters
    ----------
    m
        the container with arrays to be flipped. Arrays must be at least 2-D.
    key_chains
        The key-chains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the input container's array
        with elements order reversed along axis 1.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> m = ivy.Container(a=ivy.diag([1, 2, 3]),\
                        b=ivy.array([[1, 2, 3],[4, 5, 6]]))
    >>> ivy.Container.static_fliplr(m)
    {
        a: ivy.array([[0, 0, 1],
                      [0, 2, 0],
                      [3, 0, 0]]),
        b: ivy.array([[3, 2, 1],
                      [6, 5, 4]])
    }
    """
    pass


def fliplr(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.fliplr. This method simply
    wraps the function, and so the docstring for ivy.fliplr also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with arrays to be flipped. Arrays must be at least 2-D.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays corresponding to the input container's array
        with elements order reversed along axis 1.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> m = ivy.Container(a=ivy.diag([1, 2, 3]),\
                        b=ivy.array([[1, 2, 3],[4, 5, 6]]))
    >>> m.fliplr()
    {
        a: ivy.array([[0, 0, 1],
                      [0, 2, 0],
                      [3, 0, 0]]),
        b: ivy.array([[3, 2, 1],
                      [6, 5, 4]])
    }
    """
    pass


def static_i0(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.i0. This method simply wraps
    the function, and so the docstring for ivy.i0 also applies to this method
    with minimal changes.

    Parameters
    ----------
    x
        the container with array inputs.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays with the modified Bessel
        function evaluated at each of the elements of x.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([1, 2, 3]), b=ivy.array(4))
    >>> ivy.Container.static_i0(x)
    {
        a: ivy.array([1.26606588, 2.2795853 , 4.88079259])
        b: ivy.array(11.30192195)
    }
    """
    pass


def i0(
    self: ivy.Container,
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.i0. This method simply
    wraps the function, and so the docstring for ivy.i0 also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with array inputs.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays with the modified Bessel
        function evaluated at each of the elements of x.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.array([1, 2, 3]), b=ivy.array(4))
    >>> x.i0()
    {
        a: ivy.array([1.26606588, 2.2795853 , 4.88079259])
        b: ivy.array(11.30192195)
    }
    """
    pass


def static_flatten(
    x: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    start_dim: Optional[int] = 0,
    end_dim: Optional[int] = -1,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.flatten. This method simply wraps the
    function, and so the docstring for ivy.flatten also applies to this method
    with minimal changes.

    Parameters
    ----------
    x
        input container to flatten at leaves.
    start_dim
        first dim to flatten. If not set, defaults to 0.
    end_dim
        last dim to flatten. If not set, defaults to -1.

    Returns
    -------
    ret
        Container with arrays flattened at leaves.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
    ...                   b=ivy.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]))
    >>> ivy.flatten(x)
    [{
        a: ivy.array([1, 2, 3, 4, 5, 6, 7, 8])
        b: ivy.array([9, 10, 11, 12, 13, 14, 15, 16])
    }]
    """
    pass


def flatten(
    self: ivy.Container,
    *,
    start_dim: Optional[int] = 0,
    end_dim: Optional[int] = -1,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.flatten. This method simply
    wraps the function, and so the docstring for ivy.flatten also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        input container to flatten at leaves.
    start_dim
        first dim to flatten. If not set, defaults to 0.
    end_dim
        last dim to flatten. If not set, defaults to -1.

    Returns
    -------
    ret
        Container with arrays flattened at leaves.

    Examples
    --------
    With one :class:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]),
    ...                   b=ivy.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]]))
    >>> ivy.flatten(x)
    [{
        a: ivy.array([1, 2, 3, 4, 5, 6, 7, 8])
        b: ivy.array([9, 10, 11, 12, 13, 14, 15, 16])
    }]
    """
    pass


def static_pad(
    input: ivy.Container,
    pad_width: Union[Iterable[Tuple[int]], int],
    /,
    *,
    mode: Optional[
        Union[
            Literal[
                "constant",
                "edge",
                "linear_ramp",
                "maximum",
                "mean",
                "median",
                "minimum",
                "reflect",
                "symmetric",
                "wrap",
                "empty",
            ],
            Callable,
        ]
    ] = "constant",
    stat_length: Optional[Union[Iterable[Tuple[int]], int]] = None,
    constant_values: Optional[Union[Iterable[Tuple[Number]], Number]] = 0,
    end_values: Optional[Union[Iterable[Tuple[Number]], Number]] = 0,
    reflect_type: Optional[Literal["even", "odd"]] = "even",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
    **kwargs: Optional[Any],
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.pad. This method simply
    wraps the function, and so the docstring for ivy.pad also applies to
    this method with minimal changes.
    """
    pass


def pad(
    self: ivy.Container,
    pad_width: Union[Iterable[Tuple[int]], int],
    /,
    *,
    mode: Optional[
        Union[
            Literal[
                "constant",
                "edge",
                "linear_ramp",
                "maximum",
                "mean",
                "median",
                "minimum",
                "reflect",
                "symmetric",
                "wrap",
                "empty",
            ],
            Callable,
        ]
    ] = "constant",
    stat_length: Optional[Union[Iterable[Tuple[int]], int]] = None,
    constant_values: Optional[Union[Iterable[Tuple[Number]], Number]] = 0,
    end_values: Optional[Union[Iterable[Tuple[Number]], Number]] = 0,
    reflect_type: Optional[Literal["even", "odd"]] = "even",
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
    **kwargs: Optional[Any],
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.pad. This method simply
    wraps the function, and so the docstring for ivy.pad also applies to
    this method with minimal changes.
    """
    pass


def static_vsplit(
    ary: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    indices_or_sections: Union[int, Tuple[int]],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.vsplit. This method simply wraps
    the function, and so the docstring for ivy.vsplit also applies to this method
    with minimal changes.

    Parameters
    ----------
    ary
        the container with array inputs.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n vertically, each section will be of equal
        size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including input arrays split vertically.

    Examples
    --------
    >>> ary = ivy.Container(
        a = ivy.ivy.array(
                [[[0.,  1.],
                  [2.,  3.]],
                  [[4.,  5.],
                  [6.,  7.]]]
            ),
        b=ivy.array(
                [[ 0.,  1.,  2.,  3.],
                 [ 4.,  5.,  6.,  7.],
                 [ 8.,  9., 10., 11.],
                 [12., 13., 14., 15.]])
            )
        )
    >>> ivy.Container.static_vsplit(ary, 2)
    {
        a: [ivy.array([[[0., 1.], [2., 3.]]]),
            ivy.array([[[4., 5.], [6., 7.]]])],
        b: [ivy.array([[0., 1., 2., 3.], [4., 5., 6., 7.]]),
            ivy.array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]])]
    }
    """
    pass


def vsplit(
    self: ivy.Container,
    indices_or_sections: Union[int, Tuple[int]],
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.vsplit. This method simply
    wraps the function, and so the docstring for ivy.vsplit also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with array inputs.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n vertically, each section will be of equal
        size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays with the modified Bessel
        function evaluated at each of the elements of x.

    Examples
    --------
    >>> ary = ivy.Container(
        a = ivy.ivy.array(
                [[[0.,  1.],
                  [2.,  3.]],
                  [[4.,  5.],
                  [6.,  7.]]]
            ),
        b=ivy.array(
                [[ 0.,  1.,  2.,  3.],
                 [ 4.,  5.,  6.,  7.],
                 [ 8.,  9., 10., 11.],
                 [12., 13., 14., 15.]])
            )
        )
    >>> ary.vsplit(2)
    {
        a: [ivy.array([[[0., 1.], [2., 3.]]]),
            ivy.array([[[4., 5.], [6., 7.]]])],
        b: [ivy.array([[0., 1., 2., 3.], [4., 5., 6., 7.]]),
            ivy.array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]])]
    }
    """
    pass


def static_dsplit(
    ary: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    indices_or_sections: Union[int, Tuple[int]],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.dsplit. This method simply wraps
    the function, and so the docstring for ivy.dsplit also applies to this method
    with minimal changes.

    Parameters
    ----------
    ary
        the container with array inputs.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n along the 3rd axis, each section will be of
        equal size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including input arrays split along the 3rd axis.

    Examples
    --------
    >>> ary = ivy.Container(
        a = ivy.ivy.array(
                [[[0.,  1.],
                  [2.,  3.]],
                  [[4.,  5.],
                  [6.,  7.]]]
            ),
        b=ivy.array(
                [[ 0.,  1.,  2.,  3.],
                 [ 4.,  5.,  6.,  7.],
                 [ 8.,  9., 10., 11.],
                 [12., 13., 14., 15.]])
            )
        )
    >>> ivy.Container.static_dsplit(ary, 2)
    {
        a: [ivy.array([[[0., 1.], [2., 3.]]]),
            ivy.array([[[4., 5.], [6., 7.]]])],
        b: [ivy.array([[0., 1., 2., 3.], [4., 5., 6., 7.]]),
            ivy.array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]])]
    }
    """
    pass


def dsplit(
    self: ivy.Container,
    indices_or_sections: Union[int, Tuple[int]],
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.dsplit. This method simply
    wraps the function, and so the docstring for ivy.dsplit also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        the container with array inputs.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n along the 3rd axis, each section will be of
        equal size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including arrays with the modified Bessel
        function evaluated at each of the elements of x.

    Examples
    --------
    >>> ary = ivy.Container(
        a = ivy.ivy.array(
                [[[0.,  1.],
                  [2.,  3.]],
                  [[4.,  5.],
                  [6.,  7.]]]
            ),
        b=ivy.array(
                [[ 0.,  1.,  2.,  3.],
                 [ 4.,  5.,  6.,  7.],
                 [ 8.,  9., 10., 11.],
                 [12., 13., 14., 15.]])
            )
        )
    >>> ary.dsplit(2)
    {
        a: [ivy.array([[[0., 1.], [2., 3.]]]),
            ivy.array([[[4., 5.], [6., 7.]]])],
        b: [ivy.array([[0., 1., 2., 3.], [4., 5., 6., 7.]]),
            ivy.array([[ 8.,  9., 10., 11.], [12., 13., 14., 15.]])]
    }
    """
    pass


def dstack(
    self: ivy.Container,
    /,
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.stack. This method
    simply wraps the function, and so the docstring for ivy.stack
    also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.Container(a=ivy.array([[0, 1], [2,3]]), b=ivy.array([[4, 5]]))
    >>> y = ivy.Container(a=ivy.array([[3, 2], [1,0]]), b=ivy.array([[1, 0]]))
    >>> x.dstack([y])
    {
        a: ivy.array([[[0, 3],
                       [1, 2]],
                      [[2, 1],
                       [3, 0]]]),
        b: ivy.array([[[4, 1]],
                       [[5, 0]]])
    }
    """
    pass


def static_dstack(
    xs: Union[
        Tuple[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
        List[Union[ivy.Array, ivy.NativeArray, ivy.Container]],
    ],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.stack. This method simply wraps the
    function, and so the docstring for ivy.dstack also applies to this method
    with minimal changes.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> c = ivy.Container(a=[ivy.array([1,2,3]), ivy.array([0,0,0])],
                          b=ivy.arange(3))
    >>> ivy.Container.static_dstack(c)
    {
        a: ivy.array([[1, 0],
                      [2, 0]
                      [3,0]]),
        b: ivy.array([[0, 1, 2])
    }
    """
    pass


def static_atleast_2d(
    *arys: Union[ivy.Array, ivy.NativeArray, ivy.Container],
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
) -> List[ivy.Container]:
    """
    ivy.Container static method variant of ivy.atleast_2d. This method simply wraps
    the function, and so the docstring for ivy.atleast_2d also applies to this
    method with minimal changes.

    Parameters
    ----------
    arys
        one or more container with array inputs.
    key_chains
        The keychains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.

    Returns
    -------
    ret
        container or list of container where each elements within container is
        atleast 2D. Copies are made only if necessary.

    Examples
    --------
    >>> ary = ivy.Container(a=ivy.array(1), b=ivy.array([3,4,5]),\
                    c=ivy.array([[3]]))
    >>> ivy.Container.static_atleast_2d(ary)
    {
        a: ivy.array([[1]]),
        b: ivy.array([[3, 4, 5]]),
        c: ivy.array([[3]])
    }
    """
    return ContainerBase.multi_map_in_static_method(
        "atleast_2d",
        *arys,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
    )

def atleast_2d(
    self: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    *arys: Union[ivy.Container, ivy.Array, ivy.NativeArray],
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
) -> List[ivy.Container]:
    """ivy.Container instance method variant of ivy.atleast_2d. This method simply
    wraps the function, and so the docstring for ivy.atleast_2d also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        container with array inputs.
    arys
        one or more container with array inputs.
    key_chains
        The keychains to apply or not apply the method to. Default is ``None``.
    to_apply
        If True, the method will be applied to key_chains, otherwise key_chains
        will be skipped. Default is ``True``.
    prune_unapplied
        Whether to prune key_chains for which the function was not applied.
        Default is ``False``.
    map_sequences
        Whether to also map method to sequences (lists, tuples).
        Default is ``False``.

    Returns
    -------
    ret
        container or list of container where each elements within container is
        atleast 2D. Copies are made only if necessary.

    Examples
    --------
    >>> ary1 = ivy.Container(a=ivy.array(1), b=ivy.array([3,4]),\
                        c=ivy.array([[5]]))
    >>> ary2 = ivy.Container(a=ivy.array(9), b=ivy.array(2),\
                        c=ivy.array(3))
    >>> ary1.atleast_2d(ary2)
    [{
        a: ivy.array([[1]]),
        b: ivy.array([[3, 4]]),
        c: ivy.array([[5]])
    }, {
        a: ivy.array([[9]]),
        b: ivy.array([[2]]),
        c: ivy.array([[3]])
    }]
    """
    return self.static_atleast_2d(
        self,
        *arys,
        key_chains=key_chains,
        to_apply=to_apply,
        prune_unapplied=prune_unapplied,
        map_sequences=map_sequences,
    )

#ivy.container.experimental.random
# global
from typing import Optional, Union, List, Dict

# local
import ivy
from ivy.container.base import ContainerBase


def static_dirichlet(
    alpha: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    size: Optional[Union[ivy.Shape, ivy.NativeShape, ivy.Container]] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    seed: Optional[int] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container static method variant of ivy.dirichlet. This method
    simply wraps the function, and so the docstring for ivy.dirichlet also
    applies to this method with minimal changes.

    Parameters
    ----------
    alpha
        Sequence of floats of length k 
    size
        optional container including ints or tuple of ints, 
        Output shape for the arrays in the input container. 
    dtype
        output container array data type. If ``dtype`` is ``None``, the output data
        type will be the default floating-point data type. Default ``None``
    seed
        A python integer. Used to create a random seed distribution
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including the drawn samples.

    Examples
    --------
    >>> alpha = ivy.Container(a=ivy.array([7,6,5]), \
                              b=ivy.array([8,9,4]))
    >>> size = ivy.Container(a=3, b=5)
    >>> ivy.Container.static_dirichlet(alpha, size)
    {
        a: ivy.array(
            [[0.43643127, 0.32325703, 0.24031169],
             [0.34251311, 0.31692529, 0.3405616 ],
             [0.5319725 , 0.22458365, 0.24344385]]
            ),
        b: ivy.array(
            [[0.26588406, 0.61075421, 0.12336174],
             [0.51142915, 0.25041268, 0.23815817],
             [0.64042903, 0.25763214, 0.10193883],
             [0.31624692, 0.46567987, 0.21807321],
             [0.37677699, 0.39914594, 0.22407707]]
            )
    }
    """
    pass


def dirichlet(
    self: ivy.Container,
    /,
    *,
    size: Optional[Union[ivy.Shape, ivy.NativeShape, ivy.Container]] = None,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype, ivy.Container]] = None,
    seed: Optional[int] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.dirichlet. This method
    simply wraps the function, and so the docstring for ivy.shuffle also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        Sequence of floats of length k 
    size
        optional container including ints or tuple of ints, 
        Output shape for the arrays in the input container. 
    dtype
        output container array data type. If ``dtype`` is ``None``, the output data
        type will be the default floating-point data type. Default ``None``
    seed
        A python integer. Used to create a random seed distribution
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        container including the drawn samples.

    Examples
    --------
    >>> alpha = ivy.Container(a=ivy.array([7,6,5]), \
                              b=ivy.array([8,9,4]))
    >>> size = ivy.Container(a=3, b=5)
    >>> alpha.dirichlet(size)
    {
        a: ivy.array(
            [[0.43643127, 0.32325703, 0.24031169],
             [0.34251311, 0.31692529, 0.3405616 ],
             [0.5319725 , 0.22458365, 0.24344385]]
            ),
        b: ivy.array(
            [[0.26588406, 0.61075421, 0.12336174],
             [0.51142915, 0.25041268, 0.23815817],
             [0.64042903, 0.25763214, 0.10193883],
             [0.31624692, 0.46567987, 0.21807321],
             [0.37677699, 0.39914594, 0.22407707]]
            )
    }
    """
    pass


#ivy.container.experimental.sorting
# global
from typing import Optional, List, Union, Dict

# local
from ivy.container.base import ContainerBase
import ivy


def static_msort(
    a: Union[ivy.Array, ivy.NativeArray, ivy.Container, list, tuple],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.msort. This method simply wraps the
    function, and so the docstring for ivy.msort also applies to this method
    with minimal changes.

    Parameters
    ----------
    a
        array-like or container input.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        a container containing sorted input arrays.

    Examples
    --------
    With :class:`ivy.Container` input:

    >>> a = ivy.Container(x = ivy.randint(10, size=(2,3)),
    ...                   y = ivy.randint(5, size=(2,2))
    >>> ivy.Container.static_msort(a)
    {
        x: ivy.array(
            [[6, 2, 6],
             [8, 9, 6]]
            ),
        y: ivy.array(
            [[0, 0],
             [4, 0]]
            )
    }
    """
    pass


def msort(
    self: ivy.Container,
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """
    ivy.Container instance method variant of ivy.msort.
    This method simply wraps the function, and
    so the docstring for ivy.msort also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        input container with array-like inputs to sort.
    out
        optional output container, for writing the result to.

    Returns
    -------
    ret
        a container containing the sorted input arrays.

    Examples
    --------
    >>> a = ivy.Container(x = ivy.randint(10, size=(2,3)),
    ...                   y = ivy.randint(5, size=(2,2))
    >>> a.msort()
    {
        x: ivy.array(
            [[6, 2, 6],
             [8, 9, 6]]
            ),
        y: ivy.array(
            [[0, 0],
             [4, 0]]
            )
    }
    """
    pass


#ivy.container.experimental.statistical
# global
from typing import (
    Optional,
    Union,
    List,
    Dict,
    Tuple,
)

# local
import ivy
from ivy.container.base import ContainerBase


def static_median(
    input: ivy.Container,
    /,
    *,
    axis: Optional[Union[Tuple[int], int]] = None,
    keepdims: Optional[bool] = False,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.median. This method simply wraps
    the function, and so the docstring for ivy.median also applies to this method
    with minimal changes.

    Parameters
    ----------
    input
        Input container including arrays.
    axis
        Axis or axes along which the medians are computed. The default is to compute
        the median along a flattened version of the array.
    keepdims
        If this is set to True, the axes which are reduced are left in the result
        as dimensions with size one.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The median of the array elements.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(a=ivy.zeros((3, 4, 5)), b=ivy.zeros((2,7,6)))
    >>> ivy.Container.static_moveaxis(x, 0, -1).shape
    {
        a: (4, 5, 3)
        b: (7, 6, 2)
    }
    """
    pass


def median(
    self: ivy.Container,
    /,
    *,
    axis: Optional[Union[Tuple[int], int]] = None,
    keepdims: Optional[bool] = False,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.median. This method simply
    wraps the function, and so the docstring for ivy.median also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container including arrays.
    axis
        Axis or axes along which the medians are computed. The default is to compute
        the median along a flattened version of the array.
    keepdims
        If this is set to True, the axes which are reduced are left in the result
        as dimensions with size one.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The median of the array elements.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> x = ivy.Container(
    >>>     a=ivy.array([[10, 7, 4], [3, 2, 1]]),
    >>>     b=ivy.array([[1, 4, 2], [8, 7, 0]])
    >>> )
    >>> x.median(axis=0)
    {
        a: ivy.array([6.5, 4.5, 2.5]),
        b: ivy.array([4.5, 5.5, 1.])
    }
    """
    pass


def static_nanmean(
    input: ivy.Container,
    /,
    *,
    axis: Optional[Union[Tuple[int], int]] = None,
    keepdims: Optional[bool] = False,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.nanmean. This method simply wraps
    the function, and so the docstring for ivy.nanmean also applies to this method
    with minimal changes.

    Parameters
    ----------
    input
        Input container including arrays.
    axis
        Axis or axes along which the means are computed.
        The default is to compute the mean of the flattened array.
    keepdims
        If this is set to True, the axes which are reduced are left in the result
        as dimensions with size one. With this option, the result will broadcast
        correctly against the original a. If the value is anything but the default,
        then keepdims will be passed through to the mean or sum methods of 
        sub-classes of ndarray. If the sub-classes methods does not implement 
        keepdims any exceptions will be raised.
    dtype
        The desired data type of returned tensor. Default is None.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The nanmean of the array elements in the container.

    Examples
    --------
    >>> a = ivy.Container(x=ivy.array([[1, ivy.nan], [3, 4]]),\
                            y=ivy.array([[ivy.nan, 1, 2], [1, 2, 3]])
    >>> ivy.Container.static_moveaxis(a)
    {
        x: 2.6666666666666665
        y: 1.8
    }
    """
    pass


def nanmean(
    self: ivy.Container,
    /,
    *,
    axis: Optional[Union[Tuple[int], int]] = None,
    keepdims: Optional[bool] = False,
    dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.nanmean. This method simply
    wraps the function, and so the docstring for ivy.nanmean also applies to this
    method with minimal changes.

    Parameters
    ----------
    self
        Input container including arrays.
    axis
        Axis or axes along which the means are computed.
        The default is to compute the mean of the flattened array.
    keepdims
        If this is set to True, the axes which are reduced are left in the result
        as dimensions with size one. With this option, the result will broadcast
        correctly against the original a. If the value is anything but the default,
        then keepdims will be passed through to the mean or sum methods of 
        sub-classes of ndarray. If the sub-classes methods does not implement 
        keepdims any exceptions will be raised.
    dtype
        The desired data type of returned tensor. Default is None.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The nanmean of the array elements in the input container.

    Examples
    --------
    >>> a = ivy.Container(x=ivy.array([[1, ivy.nan], [3, 4]]),\
                            y=ivy.array([[ivy.nan, 1, 2], [1, 2, 3]])
    >>> a.nanmean()
    {
        x: 2.6666666666666665
        y: 1.8
    }
    """
    pass


def static_unravel_index(
    indices: ivy.Container,
    shape: Tuple[int],
    /,
    *,
    key_chains: Optional[Union[List[str], Dict[str, str]]] = None,
    to_apply: bool = True,
    prune_unapplied: bool = False,
    map_sequences: bool = False,
    out: Optional[ivy.Array] = None,
) -> ivy.Container:
    """
    ivy.Container static method variant of ivy.unravel_index.
    This method simply wraps the function, and so the docstring
    for ivy.unravel_index also applies to this method with minimal
    changes.

    Parameters
    ----------
    input
        Input container including arrays.
    shape
        The shape of the array to use for unraveling indices.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Container with tuples that have arrays with the same shape as
        the arrays in the input container.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> indices = ivy.Container(a=ivy.array([22, 41, 37])), b=ivy.array([30, 2]))
    >>> ivy.Container.static_unravel_index(indices, (7,6))
    {
        a: (ivy.array([3, 6, 6]), ivy.array([4, 5, 1]))
        b: (ivy.array([5, 0], ivy.array([0, 2])))
    }
    """
    pass


def unravel_index(
    self: ivy.Container,
    shape: Tuple[int],
    /,
    *,
    out: Optional[ivy.Container] = None,
) -> ivy.Container:
    """ivy.Container instance method variant of ivy.unravel_index.
    This method simply wraps the function, and so the docstring for
    ivy.unravel_index also applies to this method with minimal changes.

    Parameters
    ----------
    self
        Input container including arrays.
    shape
        The shape of the array to use for unraveling indices.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Container with tuples that have arrays with the same shape as
        the arrays in the input container.

    Examples
    --------
    With one :class:`ivy.Container` input:
    >>> indices = ivy.Container(a=ivy.array([22, 41, 37])), b=ivy.array([30, 2]))
    >>> indices.unravel_index((7, 6))
    {
        a: (ivy.array([3, 6, 6]), ivy.array([4, 5, 1]))
        b: (ivy.array([5, 0], ivy.array([0, 2])))
    }
    """
    pass


