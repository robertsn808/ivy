# ivy.array.experimental.elementwise
# global
import abc
from typing import Optional, Union, Tuple

# local
import ivy


def sinc(self: ivy.Array, *, out: Optional[ivy.Array] = None) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.sinc. This method simply wraps the
    function, and so the docstring for ivy.sinc also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        input array whose elements are each expressed in radians. Should have a
        floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        an array containing the sinc of each element in ``self``. The returned
        array must have a floating-point data type determined by
        :ref:`type-promotion`.

    Examples
    --------
    >>> x = ivy.array([0.5, 1.5, 2.5, 3.5])
    >>> y = x.sinc()
    >>> print(y)
    ivy.array([0.637,-0.212,0.127,-0.0909])
    """
    pass


def lcm(
        self: ivy.Array, x2: ivy.Array, *, out: Optional[ivy.Array] = None
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.lcm. This method simply wraps the
    function, and so the docstring for ivy.lcm also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        first input array.
    x2
        second input array
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        an array that includes the element-wise least common multiples
        of 'self' and x2

    Examples
    --------
    >>> x1=ivy.array([2, 3, 4])
    >>> x2=ivy.array([5, 8, 15])
    >>> x1.lcm(x2)
    ivy.array([10, 21, 60])
    """
    pass


def fmod(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.fmod. This method simply
    wraps the function, and so the docstring for ivy.fmod also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
    x1
        First input array.
    x2
        Second input array
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array with element-wise remainder of divisions.

    Examples
    --------
    >>> x1 = ivy.array([2, 3, 4])
    >>> x2 = ivy.array([1, 5, 2])
    >>> x1.fmod(x2)
    ivy.array([ 0,  3,  0])

    >>> x1 = ivy.array([ivy.nan, 0, ivy.nan])
    >>> x2 = ivy.array([0, ivy.nan, ivy.nan])
    >>> x1.fmod(x2)
    ivy.array([ nan,  nan,  nan])
    """
    pass


def fmax(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.fmax. This method simply
    wraps the function, and so the docstring for ivy.fmax also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
    x1
        First input array.
    x2
        Second input array
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array with element-wise maximums.

    Examples
    --------
    >>> x1 = ivy.array([2, 3, 4])
    >>> x2 = ivy.array([1, 5, 2])
    >>> ivy.fmax(x1, x2)
    ivy.array([ 2.,  5.,  4.])

    >>> x1 = ivy.array([ivy.nan, 0, ivy.nan])
    >>> x2 = ivy.array([0, ivy.nan, ivy.nan])
    >>> x1.fmax(x2)
    ivy.array([ 0,  0,  nan])
    """
    pass


def trapz(
        self: ivy.Array,
        /,
        *,
        x: Optional[ivy.Array] = None,
        dx: Optional[float] = 1.0,
        axis: Optional[int] = -1,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.trapz. This method simply
    wraps the function, and so the docstring for ivy.trapz also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        The array that should be integrated.
    x
        The sample points corresponding to the input array values.
        If x is None, the sample points are assumed to be evenly spaced
        dx apart. The default is None.
    dx
        The spacing between sample points when x is None. The default is 1.
    axis
        The axis along which to integrate.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Definite integral of n-dimensional array as approximated along
        a single axis by the trapezoidal rule. If the input array is a
        1-dimensional array, then the result is a float. If n is greater
        than 1, then the result is an n-1 dimensional array.

    Examples
    --------
    >>> y = ivy.array([1, 2, 3])
    >>> ivy.trapz(y)
    4.0
    >>> y = ivy.array([1, 2, 3])
    >>> x = ivy.array([4, 6, 8])
    >>> ivy.trapz(y, x=x)
    8.0
    >>> y = ivy.array([1, 2, 3])
    >>> ivy.trapz(y, dx=2)
    8.0
    """
    pass


def float_power(
        self: Union[ivy.Array, float, list, tuple],
        x2: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.float_power. This method simply
    wraps the function, and so the docstring for ivy.float_power also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Array-like with elements to raise in power.
    x2
        Array-like of exponents. If x1.shape != x2.shape,
        they must be broadcastable to a common shape
        (which becomes the shape of the output).
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The bases in x1 raised to the exponents in x2.
        This is a scalar if both x1 and x2 are scalars

    Examples
    --------
    >>> x1 = ivy.array([1, 2, 3, 4, 5])
    >>> x1.float_power(3)
    ivy.array([1.,    8.,   27.,   64.,  125.])
    >>> x1 = ivy.array([1, 2, 3, 4, 5])
    >>> x2 = ivy.array([2, 3, 3, 2, 1])
    >>> x1.float_power(x2)
    ivy.array([1.,   8.,  27.,  16.,   5.])
    """
    pass


def exp2(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.exp2. This method simply
    wraps the function, and so the docstring for ivy.exp2 also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Array-like input.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Element-wise 2 to the power x. This is a scalar if x is a scalar.

    Examples
    --------
    >>> x = ivy.array([1, 2, 3])
    >>> x.exp2()
    ivy.array([2.,    4.,   8.])
    >>> x = [5, 6, 7]
    >>> x.exp2()
    ivy.array([32.,   64.,  128.])
    """
    pass


def count_nonzero(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[int, Tuple[int, ...]]] = None,
        keepdims: Optional[bool] = False,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.count_nonzero. This method simply
    wraps the function, and so the docstring for ivy.count_nonzero also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input array for which to count non-zeros.
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
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
       Number of non-zero values in the array along a given axis. Otherwise,
       the total number of non-zero values in the array is returned.

    Examples
    --------
    >>> x = ivy.array([1, 2, 3])
    >>> x.count_nonzero()
    ivy.array(3)
    >>> x = ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]])
    >>> x.count_nonzero(axis=0)
    ivy.array([[1, 2],
           [2, 2]])
    >>> x = ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]])
    >>> x.count_nonzero(axis=(0,1), keepdims=True)
    ivy.array([[[3, 4]]])
    """
    pass


def nansum(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[tuple, int]] = None,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        keepdims: Optional[bool] = False,
        out: Optional[ivy.Container] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.nansum. This method simply
    wraps the function, and so the docstring for ivy.nansum also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
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
    >>> a = ivy.array([[ 2.1,  3.4,  ivy.nan], [ivy.nan, 2.4, 2.1]])
    >>> ivy.nansum(a)
    10.0
    >>> ivy.nansum(a, axis=0)
    ivy.array([2.1, 5.8, 2.1])
    >>> ivy.nansum(a, axis=1)
    ivy.array([5.5, 4.5])
    """
    pass


def gcd(
        self: Union[ivy.Array, int, list, tuple],
        x2: Union[ivy.Array, int, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.gcd. This method simply
    wraps the function, and so the docstring for ivy.gcd also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        First array-like input.
    x2
        Second array-like input
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Element-wise gcd of |x1| and |x2|.

    Examples
    --------
    >>> x1 = ivy.array([1, 2, 3])
    >>> x2 = ivy.array([4, 5, 6])
    >>> x1.gcd(x2)
    ivy.array([1.,    1.,   3.])
    >>> x1 = ivy.array([1, 2, 3])
    >>> x1.gcd(10)
    ivy.array([1.,   2.,  1.])
    """
    pass


def isclose(
        self: ivy.Array,
        b: ivy.Array,
        /,
        *,
        rtol: Optional[float] = 1e-05,
        atol: Optional[float] = 1e-08,
        equal_nan: Optional[bool] = False,
        out: Optional[ivy.Container] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.isclose. This method simply
    wraps the function, and so the docstring for ivy.isclose also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        First input array.
    b
        Second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in a will be
        considered equal to NaN's in b in the output array.
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
    >>> a = ivy.array([[ 2.1,  3.4,  ivy.nan], [ivy.nan, 2.4, 2.1]])
    >>> b = ivy.array([[ 2.1,  3.4,  ivy.nan], [ivy.nan, 2.4, 2.1]])
    >>> a.isclose(b)
    ivy.array([[True, True, False],
           [False, True, True]])
    >>> a.isclose(b, equal_nan=True)
    ivy.array([[True, True, True],
           [True, True, True]])
    >>> a=ivy.array([1.0, 2.0])
    >>> b=ivy.array([1.0, 2.001])
    >>> a.isclose(b, atol=0.0)
    ivy.array([True, False])
    >>> a.isclose(b, rtol=0.01, atol=0.0)
    ivy.array([True, True])
    """
    pass


def isposinf(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Container] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.isposinf. This method simply
    wraps the function, and so the docstring for ivy.isposinf also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        Returns a boolean array with values True where
        the corresponding element of the input is positive
        infinity and values False where the element of the
        input is not positive infinity.

    Examples
    --------
    >>> a = ivy.array([12.1, -ivy.inf, ivy.inf])
    >>> ivy.isposinf(a)
    ivy.array([False, False,  True])
    """
    pass


def isneginf(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Container] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.isneginf. This method simply
    wraps the function, and so the docstring for ivy.isneginf also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        Returns a boolean array with values True where
        the corresponding element of the input is negative
        infinity and values False where the element of the
        input is not negative infinity.

    Examples
    --------
    >>> x = ivy.array([12.1, -ivy.inf, ivy.inf])
    >>> x.isneginf()
    ivy.array([False, True,  False])
    """
    pass


def nan_to_num(
        self: ivy.Array,
        /,
        *,
        copy: Optional[bool] = True,
        nan: Optional[Union[float, int]] = 0.0,
        posinf: Optional[Union[float, int]] = None,
        neginf: Optional[Union[float, int]] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.nan_to_num. This method simply
    wraps the function, and so the docstring for ivy.nan_to_num also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Array input.
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
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array with the non-finite values replaced.
        If copy is False, this may be x itself.

    Examples
    --------
    >>> x = ivy.array([1, 2, 3, nan])
    >>> x.nan_to_num()
    ivy.array([1.,    1.,   3.,   0.0])
    >>> x = ivy.array([1, 2, 3, inf])
    >>> x.nan_to_num(posinf=5e+100)
    ivy.array([1.,   2.,   3.,   5e+100])
    """
    pass


def logaddexp2(
        self: Union[ivy.Array, float, list, tuple],
        x2: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.logaddexp2. This method
    simply wraps the function, and so the docstring for ivy.logaddexp2 also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        First array-like input.
    x2
        Second array-like input
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Element-wise logaddexp2 of x1 and x2.

    Examples
    --------
    >>> x1 = ivy.array([1, 2, 3])
    >>> x2 = ivy.array([4, 5, 6])
    >>> x1.logaddexp2(x2)
    ivy.array([4.169925, 5.169925, 6.169925])
    """
    pass


def signbit(
        self: Union[ivy.Array, float, int, list, tuple],
        x2: Union[ivy.Array, float, int, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.signbit. This method
    simply wraps the function, and so the docstring for ivy.signbit also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        Array-like input.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Element-wise signbit of x.

    Examples
    --------
    >>> x = ivy.array([1, -2, 3])
    >>> x.signbit()
    ivy.array([False, True, False])
    """
    pass


def allclose(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        rtol: Optional[float] = 1e-05,
        atol: Optional[float] = 1e-08,
        equal_nan: Optional[bool] = False,
        out: Optional[ivy.Container] = None,
) -> bool:
    """
    ivy.Array instance method variant of ivy.allclose. This method simply
    wraps the function, and so the docstring for ivy.allclose also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        First input array.
    x2
        Second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in a will be
        considered equal to NaN's in b in the output array.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        Returns True if the two arrays are equal within the given tolerance;
        False otherwise.

    Examples
    --------
    >>> x1 = ivy.array([1e10, 1e-7])
    >>> x2 = ivy.array([1.00001e10, 1e-8])
    >>> y = x1.allclose(x2)
    >>> print(y)
    False

    >>> x1 = ivy.array([1.0, ivy.nan])
    >>> x2 = ivy.array([1.0, ivy.nan])
    >>> y = x1.allclose(x2, equal_nan=True)
    >>> print(y)
    True

    >>> x1 = ivy.array([1e-10, 1e-10])
    >>> x2 = ivy.array([1.00001e-10, 1e-10])
    >>> y = x1.allclose(x2, rtol=0.005, atol=0.0)
    >>> print(y)

    """
    return ivy.allclose(
        self._data, x2, rtol=rtol, atol=atol, equal_nan=equal_nan, out=out
    )


def fix(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.fix. This method
    simply wraps the function, and so the docstring for ivy.fix also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        Array input.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array of floats with elements corresponding to input elements
        rounded to nearest integer towards zero, element-wise.

    Examples
    --------
    >>> x = ivy.array([2.1, 2.9, -2.1])
    >>> x.fix()
    ivy.array([ 2.,  2., -2.])
    """
    pass


def nextafter(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Container] = None,
) -> bool:
    """
    ivy.Array instance method variant of ivy.nextafter. This method simply
    wraps the function, and so the docstring for ivy.nextafter also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        First input array.
    x2
        Second input array.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        The next representable values of x1 in the direction of x2.

    Examples
    --------
    >>> x1 = ivy.array([1.0e-50, 2.0e+50])
    >>> x2 = ivy.array([2.0, 1.0])
    >>> x1.nextafter(x2)
    ivy.array([1.4013e-45., 3.4028e+38])
    """
    return ivy.nextafter(self._data, x2, out=out)


# ivy.array.experimental.layers
# global
import abc
from typing import Optional, Union, Tuple, Literal

# local
import ivy


def max_pool1d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int]],
        strides: Union[int, Tuple[int]],
        padding: str,
        /,
        *,
        data_format: str = "NHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of `ivy.max_pool1d`. This method simply
    wraps the function, and so the docstring for `ivy.max_pool1d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input image *[batch_size,w,d_in]*.
    kernel
        The size of the window for each dimension of the input tensor.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        The result of the max pooling operation.

    Examples
    --------
    >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
    >>> print(x.max_pool1d(2, 2, 'SAME'))
    ivy.array([[[ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]],

           [[16., 17., 18., 19.],
            [20., 21., 22., 23.]]])
    >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
    >>> print(x.max_pool1d(2, 2, 'VALID'))
    ivy.array([[[ 4.,  5.,  6.,  7.]],

       [[16., 17., 18., 19.]]])
    """
    pass


def max_pool2d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of `ivy.max_pool2d`. This method simply
    wraps the function, and so the docstring for `ivy.max_pool2d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window for each dimension of the input tensor.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        The result of the max pooling operation.

    Examples
    --------
    >>> x = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> print(x.max_pool2d((2, 2), (1, 1), 'SAME'))
    ivy.array([[[[ 2,  3],
    [ 4,  5],
    [ 4,  5]]],
    [[[ 8,  9],
    [10, 11],
    [10, 11]]]])

    >>> x = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> print(x.max_pool2d(3, 1, 'VALID'))
    ivy.array([[[[16, 17]],
    [[22, 23]]],
    [[[40, 41]],
    [[46, 47]]]])
    """
    pass


def max_pool3d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NDHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Computes a 3-D max pool given 5-D input x.

    Parameters
    ----------
    self
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
        optional output array, for writing the result to. It must have
        a shape that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> x = ivy.arange(48.).reshape((2, 3, 2, 2, 2))
    >>> print(x.max_pool3d(2, 2, 'VALID'))
    ivy.array([[[[[14., 15.]]]],



       [[[[38., 39.]]]]])
    >>> print(x.max_pool3d(2, 2, 'SAME'))
    ivy.array([[[[[14., 15.]]],


        [[[22., 23.]]]],



       [[[[38., 39.]]],


        [[[46., 47.]]]]])
    """
    pass


def avg_pool1d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int]],
        strides: Union[int, Tuple[int]],
        padding: str,
        /,
        *,
        data_format: str = "NWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of `ivy.avg_pool1d`. This method simply
    wraps the function, and so the docstring for `ivy.avg_pool1d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input image *[batch_size,w,d_in]*.
    kernel
        The size of the window for each dimension of the input tensor.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        The result of the max pooling operation.

    Examples
    --------
    >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
    >>> print(x.avg_pool1d(2, 2, 'SAME'))
    ivy.array([[[ 2.,  3.,  4.,  5.],
            [ 8.,  9., 10., 11.]],

           [[14., 15., 16., 17.],
            [20., 21., 22., 23.]]])

    >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
    >>> print(x.avg_pool1d(2, 2, 'VALID'))
    ivy.array([[[ 2.,  3.,  4.,  5.]],

           [[14., 15., 16., 17.]]])
    """
    pass


def avg_pool2d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of `ivy.avg_pool2d`. This method simply
    wraps the function, and so the docstring for `ivy.avg_pool2d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window for each dimension of the input tensor.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        The result of the max pooling operation.

    Examples
    --------
    >>> x = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> print(x.max_pool2d((2, 2), (1, 1), 'SAME'))
    ivy.array([[[[ 2,  3],
    [ 4,  5],
    [ 4,  5]]],
    [[[ 8,  9],
    [10, 11],
    [10, 11]]]])

    >>> x = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> print(x.max_pool2d(3, 1, 'VALID'))
    ivy.array([[[[16, 17]],
    [[22, 23]]],
    [[[40, 41]],
    [[46, 47]]]])
    """
    pass


def avg_pool3d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NDHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Computes a 3-D max pool given 5-D input x.

    Parameters
    ----------
    self
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
        optional output array, for writing the result to. It must have
        a shape that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> x = ivy.arange(48.).reshape((2, 3, 2, 2, 2))
    >>> print(x.avg_pool3d(2, 2, 'VALID'))
    ivy.array([[[[[ 7.,  8.]]]],



           [[[[31., 32.]]]]])
    >>> print(x.avg_pool3d(2, 2, 'SAME'))
    ivy.array([[[[[ 7.,  8.]]],


            [[[19., 20.]]]],



           [[[[31., 32.]]],


            [[[43., 44.]]]]])
    """
    pass


def dct(
        self: ivy.Array,
        /,
        *,
        type: Optional[Literal[1, 2, 3, 4]] = 2,
        n: Optional[int] = None,
        axis: Optional[int] = -1,
        norm: Optional[Literal["ortho"]] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.dct. This method simply
    wraps the function, and so the docstring for ivy.dct also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        The input signal.
    type
        The type of the dct. Must be 1, 2, 3 or 4.
    n
        The lenght of the transform. If n is less than the input signal lenght,
        then x is truncated, if n is larger than x is zero-padded.
    norm
        The type of normalization to be applied. Must be either None or "ortho".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array containing the transformed input.

    Examples
    --------
    >>> x = ivy.array([8., 16., 24., 32., 40., 48., 56., 64.])
    >>> x.dct(type=2, norm="ortho")
    ivy.array([ 102.,  -51.5,   0.,  -5.39,   0.,  -1.61,   0., -0.406])
    """
    pass


# ivy.array.experimental.linear_algebra
# global
import abc
from typing import Optional, Union

# local
import ivy


def diagflat(
        self: Union[ivy.Array, ivy.NativeArray],
        *,
        offset: Optional[int] = 0,
        padding_value: Optional[float] = 0,
        align: Optional[str] = "RIGHT_LEFT",
        num_rows: Optional[int] = -1,
        num_cols: Optional[int] = -1,
        out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.diagflat.
    This method simply wraps the function, and so the docstring for
    ivy.diagflat also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.array([1,2])
    >>> x.diagflat(k=1)
    ivy.array([[0, 1, 0],
               [0, 0, 2],
               [0, 0, 0]])
    """
    pass


def kron(
        self: ivy.Array,
        b: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.kron.
    This method simply wraps the function, and so the docstring for
    ivy.kron also applies to this method with minimal changes.

    Examples
    --------
    >>> a = ivy.array([1,2])
    >>> b = ivy.array([3,4])
    >>> a.diagflat(b)
    ivy.array([3, 4, 6, 8])
    """
    pass


# ivy.array.experimental.manipulation
# global
import abc
from typing import (
    Optional,
    Union,
    Sequence,
    Tuple,
    List,
    Iterable,
    Callable,
    Literal,
    Any,
)
from numbers import Number

# local
import ivy


def moveaxis(
        self: ivy.Array,
        source: Union[int, Sequence[int]],
        destination: Union[int, Sequence[int]],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.moveaxis. This method simply
    wraps the function, and so the docstring for ivy.unstack also applies to
    this method with minimal changes.

    Parameters
    ----------
    a
        The array whose axes should be reordered.
    source
        Original positions of the axes to move. These must be unique.
    destination
        Destination positions for each of the original axes.
        These must also be unique.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array with moved axes. This array is a view of the input array.

    Examples
    --------
    >>> x = ivy.zeros((3, 4, 5))
    >>> x.moveaxis(0, -1).shape
    (4, 5, 3)
    >>> x.moveaxis(-1, 0).shape
    (5, 3, 4)
    """
    pass


def heaviside(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.heaviside. This method simply
    wraps the function, and so the docstring for ivy.heaviside also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input array.
    x2
        values to use where x1 is zero.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        output array with element-wise Heaviside step function of x1.
        This is a scalar if both x1 and x2 are scalars.

    Examples
    --------
    >>> x1 = ivy.array([-1.5, 0, 2.0])
    >>> x2 = ivy.array([0.5])
    >>> ivy.heaviside(x1, x2)
    ivy.array([0.0000, 0.5000, 1.0000])

    >>> x1 = ivy.array([-1.5, 0, 2.0])
    >>> x2 = ivy.array([1.2, -2.0, 3.5])
    >>> ivy.heaviside(x1, x2)
    ivy.array([0., -2., 1.])
    """
    pass


def flipud(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.flipud. This method simply
    wraps the function, and so the docstring for ivy.flipud also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        The array to be flipped.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array corresponding to input array with elements
        order reversed along axis 0.

    Examples
    --------
    >>> m = ivy.diag([1, 2, 3])
    >>> m.flipud()
    ivy.array([[ 0.,  0.,  3.],
        [ 0.,  2.,  0.],
        [ 1.,  0.,  0.]])
    """
    pass


def vstack(
        self: ivy.Array,
        /,
        arrays: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray]],
            List[Union[ivy.Array, ivy.NativeArray]],
        ],
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.vstack. This method simply
    wraps the function, and so the docstring for ivy.vstack also applies
    to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.array([[1, 2]])
    >>> y = [ivy.array([[5, 6]]), ivy.array([[7, 8]])]
    >>> print(x.vstack(y))
        ivy.array([[1, 2],
                   [5, 6],
                   [7, 8]])
    """
    pass


def hstack(
        self: ivy.Array,
        /,
        arrays: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray]],
            List[Union[ivy.Array, ivy.NativeArray]],
        ],
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.hstack. This method simply
    wraps the function, and so the docstring for ivy.hstack also applies
    to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.array([[1, 2]])
    >>> y = [ivy.array([[5, 6]]), ivy.array([[7, 8]])]
    >>> print(x.vstack(y))
    ivy.array([1, 2, 5, 6, 7, 8])

    """
    pass


def rot90(
        self: ivy.Array,
        /,
        *,
        k: Optional[int] = 1,
        axes: Optional[Tuple[int, int]] = (0, 1),
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.rot90.
    This method simply wraps the function, and so the docstring
    for ivy.rot90 also applies to this method with minimal changes.

    Parameters
    ----------
    self
        Input array of two or more dimensions.
    k
        Number of times the array is rotated by 90 degrees.
    axes
        The array is rotated in the plane defined by the axes. Axes must be
        different.
    out
        Optional output, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        Array with a rotated view of input array.

    Examples
    --------
    >>> m = ivy.array([[1,2], [3,4]])
    >>> m.rot90()
    ivy.array([[2, 4],
           [1, 3]])
    >>> m = ivy.array([[1,2], [3,4]])
    >>> m.rot90(k=2)
    ivy.array([[4, 3],
           [2, 1]])
    >>> m = ivy.array([[[0, 1],\
                        [2, 3]],\
                       [[4, 5],\
                        [6, 7]]])
    >>> m.rot90(k=2, axes=(1,2))
    ivy.array([[[3, 2],
            [1, 0]],

           [[7, 6],
            [5, 4]]])

    """
    pass


def top_k(
        self: ivy.Array,
        k: int,
        /,
        *,
        axis: Optional[int] = None,
        largest: Optional[bool] = True,
        out: Optional[tuple] = None,
) -> Tuple[ivy.Array, ivy.NativeArray]:
    """ivy.Array instance method variant of ivy.top_k. This method simply
    wraps the function, and so the docstring for ivy.top_k also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        The array to compute top_k for.
    k
        Number of top elements to retun must not exceed the array size.
    axis
        The axis along which we must return the top elements default value is 1.
    largest
        If largest is set to False we return k smallest elements of the array.
    out:
        Optional output tuple, for writing the result to. Must have two arrays,
        with a shape that the returned tuple broadcast to.

    Returns
    -------
    ret
        A named tuple with values and indices of top k elements.

    Examples
    --------
    With :class:`ivy.Array` input:

    >>> x = ivy.array([2., 1., -3., 5., 9., 0., -4])
    >>> y = x.top_k(2)
    >>> print(y)
    top_k(values=ivy.array([9., 5.]), indices=ivy.array([4, 3]))
    """
    return ivy.top_k(self, k, axis=axis, largest=largest, out=out)


def fliplr(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.fliplr. This method simply
    wraps the function, and so the docstring for ivy.fliplr also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        The array to be flipped. Must be at least 2-D.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array corresponding to input array with elements
        order reversed along axis 1.

    Examples
    --------
    >>> m = ivy.diag([1, 2, 3])
    >>> m.fliplr()
    ivy.array([[0, 0, 1],
           [0, 2, 0],
           [3, 0, 0]])
    """
    pass


def i0(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.i0. This method simply
    wraps the function, and so the docstring for ivy.i0 also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    out
        Optional output, for writing the result to.

    Returns
    -------
    ret
        Array with modified Bessel function of the first kind, order 0.

    Examples
    --------
    >>> x = ivy.array([[1, 2, 3]])
    >>> x.i0()
    ivy.array([1.26606588, 2.2795853 , 4.88079259])
    """
    pass


def flatten(
        self: ivy.Array,
        *,
        start_dim: Optional[int] = 0,
        end_dim: Optional[int] = -1,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.flatten. This method simply
    wraps the function, and so the docstring for ivy.flatten also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input array to flatten.
    start_dim
        first dim to flatten. If not set, defaults to 0.
    end_dim
        last dim to flatten. If not set, defaults to -1.

    Returns
    -------
    ret
        the flattened array over the specified dimensions.

    Examples
    --------
    >>> x = ivy.array([1,2], [3,4])
    >>> ivy.flatten(x)
    ivy.array([1, 2, 3, 4])

    >>> x = ivy.array(
        [[[[ 5,  5,  0,  6],
        [17, 15, 11, 16],
        [ 6,  3, 13, 12]],

        [[ 6, 18, 10,  4],
        [ 5,  1, 17,  3],
        [14, 14, 18,  6]]],


    [[[12,  0,  1, 13],
        [ 8,  7,  0,  3],
        [19, 12,  6, 17]],

        [[ 4, 15,  6, 15],
        [ 0,  5, 17,  9],
        [ 9,  3,  6, 19]]],


    [[[17, 13, 11, 16],
        [ 4, 18, 17,  4],
        [10, 10,  9,  1]],

        [[19, 17, 13, 10],
        [ 4, 19, 16, 17],
        [ 2, 12,  8, 14]]]]
        )
    >>> ivy.flatten(x, start_dim = 1, end_dim = 2)
    ivy.array(
        [[[ 5,  5,  0,  6],
        [17, 15, 11, 16],
        [ 6,  3, 13, 12],
        [ 6, 18, 10,  4],
        [ 5,  1, 17,  3],
        [14, 14, 18,  6]],

        [[12,  0,  1, 13],
        [ 8,  7,  0,  3],
        [19, 12,  6, 17],
        [ 4, 15,  6, 15],
        [ 0,  5, 17,  9],
        [ 9,  3,  6, 19]],

        [[17, 13, 11, 16],
        [ 4, 18, 17,  4],
        [10, 10,  9,  1],
        [19, 17, 13, 10],
        [ 4, 19, 16, 17],
        [ 2, 12,  8, 14]]]))
    """
    pass


def pad(
        self: ivy.Array,
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
        out: Optional[ivy.Array] = None,
        **kwargs: Optional[Any],
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.pad. This method simply
    wraps the function, and so the docstring for ivy.pad also applies
    to this method with minimal changes.
    """
    pass


def vsplit(
        self: ivy.Array,
        indices_or_sections: Union[int, Tuple[int]],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.vsplit. This method simply
    wraps the function, and so the docstring for ivy.vsplit also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n along the 3rd axis, each section will be of
        equal size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        Optional output, for writing the result to.

    Returns
    -------
    ret
        input array split along the 3rd axis.

    Examples
    --------
    >>> ary = ivy.array(
        [[[0.,  1.],
          [2.,  3.]],
         [[4.,  5.],
          [6.,  7.]]]
        )
    >>> ary.vsplit(2)
    [ivy.array([[[0., 1.], [2., 3.]]]), ivy.array([[[4., 5.], [6., 7.]]])])
    """
    pass


def dsplit(
        self: ivy.Array,
        indices_or_sections: Union[int, Tuple[int]],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.dsplit. This method simply
    wraps the function, and so the docstring for ivy.dsplit also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n along the 3rd axis, each section will be of
        equal size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        Optional output, for writing the result to.

    Returns
    -------
    ret
        input array split along the 3rd axis.

    Examples
    --------
    >>> ary = ivy.array(
        [[[ 0.,   1.,   2.,   3.],
          [ 4.,   5.,   6.,   7.]],
         [[ 8.,   9.,  10.,  11.],
          [12.,  13.,  14.,  15.]]]
    )
    >>> ary.dsplit(2)
    [ivy.array([[[ 0.,  1.], [ 4.,  5.]], [[ 8.,  9.], [12., 13.]]]),
    ivy.array([[[ 2.,  3.], [ 6.,  7.]], [[10., 11.], [14., 15.]]])]
    """
    pass


def dstack(
        self: ivy.Array,
        /,
        arrays: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray]],
            List[Union[ivy.Array, ivy.NativeArray]],
        ],
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.dstack. This method simply
    wraps the function, and so the docstring for ivy.dstack also applies
    to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.array([1, 2, 3])
    >>> y = ivy.array([2, 3, 4])
    >>> x.dstack(y)
    ivy.array([[[1, 2],
                [2, 3],
                [3, 4]]])
    """
    pass


def atleast_2d(self: ivy.Array, *arys: ivy.Array) -> List[ivy.Array]:
    """
    ivy.Array instance method variant of ivy.atleast_2d. This method simply
    wraps the function, and so the docstring for ivy.atleast_2d also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input array. Cannot be a scalar input.
    arys
        An arbitrary number of input arrays.

    Returns
    -------
    ret
        List of arrays, each with a.ndim >= 2. Copies are made
        only if necessary.

    Examples
    --------
    >>> a1 = ivy.array([[1,2,3]])
    >>> a2 = ivy.array(4)
    >>> a1.atleast_2d(a2,5,6)
    [ivy.array([[1, 2, 3]]), ivy.array([[4]]), ivy.array([[5]]), ivy.array([[6]])]
    """
    return ivy.atleast_2d(self._data, *arys)


# ivy.array.experimental.random
# global
import abc
from typing import Optional, Union

# local
import ivy


def dirichlet(
        self: ivy.Array,
        /,
        *,
        size: Optional[Union[ivy.Shape, ivy.NativeShape]] = None,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        seed: Optional[int] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.dirichlet. This method simply
    wraps the function, and so the docstring for ivy.shuffle also applies to
    this method with minimal changes.

    Parameters
    ----------
    alpha
        Sequence of floats of length k
    size
        optional int or tuple of ints, Output shape. If the given shape is,
        e.g., (m, n), then m * n * k samples are drawn. Default is None,
        in which case a vector of length k is returned.
    dtype
        output array data type. If ``dtype`` is ``None``, the output array data
        type will be the default floating-point data type. Default ``None``
    seed
        A python integer. Used to create a random seed distribution
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The drawn samples, of shape (size, k).

    Examples
    --------
    >>> alpha = ivy.array([1.0, 2.0, 3.0])
    >>> alpha.dirichlet()
    ivy.array([0.10598304, 0.21537054, 0.67864642])

    >>> alpha = ivy.array([1.0, 2.0, 3.0])
    >>> alpha.dirichlet(size = (2,3))
    ivy.array([[[0.48006698, 0.07472073, 0.44521229],
        [0.55479872, 0.05426367, 0.39093761],
        [0.19531053, 0.51675832, 0.28793114]],

    [[0.12315625, 0.29823365, 0.5786101 ],
        [0.15564976, 0.50542368, 0.33892656],
        [0.1325352 , 0.44439589, 0.42306891]]])
    """
    pass


# ivy.array.experimental.sorting
# global
import abc
from typing import Optional

# local

import ivy


def msort(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.msort. This method simply wraps the
    function, and so the docstring for ivy.msort also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        input array.
    out
    optional output array, for writing the result to.

    Returns
    -------
    ret
        sorted array of the same type and shape as a

    Examples
    --------
    >>> a = ivy.randint(10, size=(2,3))
    >>> a.msort()
    ivy.array(
        [[6, 2, 6],
        [8, 9, 6]]
        )
    """
    pass


# ivy.array.experimental.statistical
# global
import abc
from typing import Optional, Union, Tuple

# local
import ivy


def median(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[Tuple[int], int]] = None,
        keepdims: Optional[bool] = False,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.median. This method simply
    wraps the function, and so the docstring for ivy.median also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
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
    >>> a = ivy.array([[10, 7, 4], [3, 2, 1]])
    >>> a.median()
    3.5
    >>> a.median(axis=0)
    ivy.array([6.5, 4.5, 2.5])
    """
    pass


def nanmean(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[Tuple[int], int]] = None,
        keepdims: Optional[bool] = False,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.nanmean. This method simply
    wraps the function, and so the docstring for ivy.nanmean also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
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
        The nanmean of the array elements.

    Examples
    --------
    >>> a = ivy.array([[1, ivy.nan], [3, 4]])
    >>> a.nanmean()
    2.6666666666666665
    >>> a.nanmean(axis=0)
    ivy.array([2.,  4.])
    """
    pass


def unravel_index(
        self: ivy.Array,
        shape: Tuple[int],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.unravel_index. This method simply
    wraps the function, and so the docstring for ivy.unravel_index also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    shape
        The shape of the array to use for unraveling indices.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Tuple with arrays that have the same shape as the indices array.

    Examples
    --------
    >>> indices = ivy.array([22, 41, 37])
    >>> indices.unravel_index((7,6))
    (ivy.array([3, 6, 6]), ivy.array([4, 5, 1]))
    """
    pass


# ivy.array.experimental.elementwise
# global
import abc
from typing import Optional, Union, Tuple

# local
import ivy


def sinc(self: ivy.Array, *, out: Optional[ivy.Array] = None) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.sinc. This method simply wraps the
    function, and so the docstring for ivy.sinc also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        input array whose elements are each expressed in radians. Should have a
        floating-point data type.
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        an array containing the sinc of each element in ``self``. The returned
        array must have a floating-point data type determined by
        :ref:`type-promotion`.

    Examples
    --------
    >>> x = ivy.array([0.5, 1.5, 2.5, 3.5])
    >>> y = x.sinc()
    >>> print(y)
    ivy.array([0.637,-0.212,0.127,-0.0909])
    """
    pass


def lcm(
        self: ivy.Array, x2: ivy.Array, *, out: Optional[ivy.Array] = None
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.lcm. This method simply wraps the
    function, and so the docstring for ivy.lcm also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        first input array.
    x2
        second input array
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        an array that includes the element-wise least common multiples
        of 'self' and x2

    Examples
    --------
    >>> x1=ivy.array([2, 3, 4])
    >>> x2=ivy.array([5, 8, 15])
    >>> x1.lcm(x2)
    ivy.array([10, 21, 60])
    """
    pass


def fmod(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.fmod. This method simply
    wraps the function, and so the docstring for ivy.fmod also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
    x1
        First input array.
    x2
        Second input array
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array with element-wise remainder of divisions.

    Examples
    --------
    >>> x1 = ivy.array([2, 3, 4])
    >>> x2 = ivy.array([1, 5, 2])
    >>> x1.fmod(x2)
    ivy.array([ 0,  3,  0])

    >>> x1 = ivy.array([ivy.nan, 0, ivy.nan])
    >>> x2 = ivy.array([0, ivy.nan, ivy.nan])
    >>> x1.fmod(x2)
    ivy.array([ nan,  nan,  nan])
    """
    pass


def fmax(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.fmax. This method simply
    wraps the function, and so the docstring for ivy.fmax also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
    x1
        First input array.
    x2
        Second input array
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array with element-wise maximums.

    Examples
    --------
    >>> x1 = ivy.array([2, 3, 4])
    >>> x2 = ivy.array([1, 5, 2])
    >>> ivy.fmax(x1, x2)
    ivy.array([ 2.,  5.,  4.])

    >>> x1 = ivy.array([ivy.nan, 0, ivy.nan])
    >>> x2 = ivy.array([0, ivy.nan, ivy.nan])
    >>> x1.fmax(x2)
    ivy.array([ 0,  0,  nan])
    """
    pass


def trapz(
        self: ivy.Array,
        /,
        *,
        x: Optional[ivy.Array] = None,
        dx: Optional[float] = 1.0,
        axis: Optional[int] = -1,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.trapz. This method simply
    wraps the function, and so the docstring for ivy.trapz also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        The array that should be integrated.
    x
        The sample points corresponding to the input array values.
        If x is None, the sample points are assumed to be evenly spaced
        dx apart. The default is None.
    dx
        The spacing between sample points when x is None. The default is 1.
    axis
        The axis along which to integrate.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Definite integral of n-dimensional array as approximated along
        a single axis by the trapezoidal rule. If the input array is a
        1-dimensional array, then the result is a float. If n is greater
        than 1, then the result is an n-1 dimensional array.

    Examples
    --------
    >>> y = ivy.array([1, 2, 3])
    >>> ivy.trapz(y)
    4.0
    >>> y = ivy.array([1, 2, 3])
    >>> x = ivy.array([4, 6, 8])
    >>> ivy.trapz(y, x=x)
    8.0
    >>> y = ivy.array([1, 2, 3])
    >>> ivy.trapz(y, dx=2)
    8.0
    """
    pass


def float_power(
        self: Union[ivy.Array, float, list, tuple],
        x2: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.float_power. This method simply
    wraps the function, and so the docstring for ivy.float_power also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Array-like with elements to raise in power.
    x2
        Array-like of exponents. If x1.shape != x2.shape,
        they must be broadcastable to a common shape
        (which becomes the shape of the output).
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The bases in x1 raised to the exponents in x2.
        This is a scalar if both x1 and x2 are scalars

    Examples
    --------
    >>> x1 = ivy.array([1, 2, 3, 4, 5])
    >>> x1.float_power(3)
    ivy.array([1.,    8.,   27.,   64.,  125.])
    >>> x1 = ivy.array([1, 2, 3, 4, 5])
    >>> x2 = ivy.array([2, 3, 3, 2, 1])
    >>> x1.float_power(x2)
    ivy.array([1.,   8.,  27.,  16.,   5.])
    """
    pass


def exp2(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.exp2. This method simply
    wraps the function, and so the docstring for ivy.exp2 also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Array-like input.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Element-wise 2 to the power x. This is a scalar if x is a scalar.

    Examples
    --------
    >>> x = ivy.array([1, 2, 3])
    >>> x.exp2()
    ivy.array([2.,    4.,   8.])
    >>> x = [5, 6, 7]
    >>> x.exp2()
    ivy.array([32.,   64.,  128.])
    """
    pass


def count_nonzero(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[int, Tuple[int, ...]]] = None,
        keepdims: Optional[bool] = False,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.count_nonzero. This method simply
    wraps the function, and so the docstring for ivy.count_nonzero also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input array for which to count non-zeros.
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
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
       Number of non-zero values in the array along a given axis. Otherwise,
       the total number of non-zero values in the array is returned.

    Examples
    --------
    >>> x = ivy.array([1, 2, 3])
    >>> x.count_nonzero()
    ivy.array(3)
    >>> x = ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]])
    >>> x.count_nonzero(axis=0)
    ivy.array([[1, 2],
           [2, 2]])
    >>> x = ivy.array([[[0,1],[2,3]],[[4,5],[6,7]]])
    >>> x.count_nonzero(axis=(0,1), keepdims=True)
    ivy.array([[[3, 4]]])
    """
    pass


def nansum(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[tuple, int]] = None,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        keepdims: Optional[bool] = False,
        out: Optional[ivy.Container] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.nansum. This method simply
    wraps the function, and so the docstring for ivy.nansum also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
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
    >>> a = ivy.array([[ 2.1,  3.4,  ivy.nan], [ivy.nan, 2.4, 2.1]])
    >>> ivy.nansum(a)
    10.0
    >>> ivy.nansum(a, axis=0)
    ivy.array([2.1, 5.8, 2.1])
    >>> ivy.nansum(a, axis=1)
    ivy.array([5.5, 4.5])
    """
    pass


def gcd(
        self: Union[ivy.Array, int, list, tuple],
        x2: Union[ivy.Array, int, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.gcd. This method simply
    wraps the function, and so the docstring for ivy.gcd also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        First array-like input.
    x2
        Second array-like input
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Element-wise gcd of |x1| and |x2|.

    Examples
    --------
    >>> x1 = ivy.array([1, 2, 3])
    >>> x2 = ivy.array([4, 5, 6])
    >>> x1.gcd(x2)
    ivy.array([1.,    1.,   3.])
    >>> x1 = ivy.array([1, 2, 3])
    >>> x1.gcd(10)
    ivy.array([1.,   2.,  1.])
    """
    pass


def isclose(
        self: ivy.Array,
        b: ivy.Array,
        /,
        *,
        rtol: Optional[float] = 1e-05,
        atol: Optional[float] = 1e-08,
        equal_nan: Optional[bool] = False,
        out: Optional[ivy.Container] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.isclose. This method simply
    wraps the function, and so the docstring for ivy.isclose also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        First input array.
    b
        Second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in a will be
        considered equal to NaN's in b in the output array.
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
    >>> a = ivy.array([[ 2.1,  3.4,  ivy.nan], [ivy.nan, 2.4, 2.1]])
    >>> b = ivy.array([[ 2.1,  3.4,  ivy.nan], [ivy.nan, 2.4, 2.1]])
    >>> a.isclose(b)
    ivy.array([[True, True, False],
           [False, True, True]])
    >>> a.isclose(b, equal_nan=True)
    ivy.array([[True, True, True],
           [True, True, True]])
    >>> a=ivy.array([1.0, 2.0])
    >>> b=ivy.array([1.0, 2.001])
    >>> a.isclose(b, atol=0.0)
    ivy.array([True, False])
    >>> a.isclose(b, rtol=0.01, atol=0.0)
    ivy.array([True, True])
    """
    pass


def isposinf(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Container] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.isposinf. This method simply
    wraps the function, and so the docstring for ivy.isposinf also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        Returns a boolean array with values True where
        the corresponding element of the input is positive
        infinity and values False where the element of the
        input is not positive infinity.

    Examples
    --------
    >>> a = ivy.array([12.1, -ivy.inf, ivy.inf])
    >>> ivy.isposinf(a)
    ivy.array([False, False,  True])
    """
    pass


def isneginf(
        self: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Container] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.isneginf. This method simply
    wraps the function, and so the docstring for ivy.isneginf also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        Returns a boolean array with values True where
        the corresponding element of the input is negative
        infinity and values False where the element of the
        input is not negative infinity.

    Examples
    --------
    >>> x = ivy.array([12.1, -ivy.inf, ivy.inf])
    >>> x.isneginf()
    ivy.array([False, True,  False])
    """
    pass


def nan_to_num(
        self: ivy.Array,
        /,
        *,
        copy: Optional[bool] = True,
        nan: Optional[Union[float, int]] = 0.0,
        posinf: Optional[Union[float, int]] = None,
        neginf: Optional[Union[float, int]] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.nan_to_num. This method simply
    wraps the function, and so the docstring for ivy.nan_to_num also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Array input.
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
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array with the non-finite values replaced.
        If copy is False, this may be x itself.

    Examples
    --------
    >>> x = ivy.array([1, 2, 3, nan])
    >>> x.nan_to_num()
    ivy.array([1.,    1.,   3.,   0.0])
    >>> x = ivy.array([1, 2, 3, inf])
    >>> x.nan_to_num(posinf=5e+100)
    ivy.array([1.,   2.,   3.,   5e+100])
    """
    pass


def logaddexp2(
        self: Union[ivy.Array, float, list, tuple],
        x2: Union[ivy.Array, float, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.logaddexp2. This method
    simply wraps the function, and so the docstring for ivy.logaddexp2 also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        First array-like input.
    x2
        Second array-like input
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Element-wise logaddexp2 of x1 and x2.

    Examples
    --------
    >>> x1 = ivy.array([1, 2, 3])
    >>> x2 = ivy.array([4, 5, 6])
    >>> x1.logaddexp2(x2)
    ivy.array([4.169925, 5.169925, 6.169925])
    """
    pass


def signbit(
        self: Union[ivy.Array, float, int, list, tuple],
        x2: Union[ivy.Array, float, int, list, tuple],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.signbit. This method
    simply wraps the function, and so the docstring for ivy.signbit also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        Array-like input.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Element-wise signbit of x.

    Examples
    --------
    >>> x = ivy.array([1, -2, 3])
    >>> x.signbit()
    ivy.array([False, True, False])
    """
    pass


def allclose(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        rtol: Optional[float] = 1e-05,
        atol: Optional[float] = 1e-08,
        equal_nan: Optional[bool] = False,
        out: Optional[ivy.Container] = None,
) -> bool:
    """
    ivy.Array instance method variant of ivy.allclose. This method simply
    wraps the function, and so the docstring for ivy.allclose also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        First input array.
    x2
        Second input array.
    rtol
        The relative tolerance parameter.
    atol
        The absolute tolerance parameter.
    equal_nan
        Whether to compare NaN's as equal. If True, NaN's in a will be
        considered equal to NaN's in b in the output array.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        Returns True if the two arrays are equal within the given tolerance;
        False otherwise.

    Examples
    --------
    >>> x1 = ivy.array([1e10, 1e-7])
    >>> x2 = ivy.array([1.00001e10, 1e-8])
    >>> y = x1.allclose(x2)
    >>> print(y)
    False

    >>> x1 = ivy.array([1.0, ivy.nan])
    >>> x2 = ivy.array([1.0, ivy.nan])
    >>> y = x1.allclose(x2, equal_nan=True)
    >>> print(y)
    True

    >>> x1 = ivy.array([1e-10, 1e-10])
    >>> x2 = ivy.array([1.00001e-10, 1e-10])
    >>> y = x1.allclose(x2, rtol=0.005, atol=0.0)
    >>> print(y)

    """
    return ivy.allclose(
        self._data, x2, rtol=rtol, atol=atol, equal_nan=equal_nan, out=out
    )


def fix(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.fix. This method
    simply wraps the function, and so the docstring for ivy.fix also
    applies to this method with minimal changes.

    Parameters
    ----------
    self
        Array input.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array of floats with elements corresponding to input elements
        rounded to nearest integer towards zero, element-wise.

    Examples
    --------
    >>> x = ivy.array([2.1, 2.9, -2.1])
    >>> x.fix()
    ivy.array([ 2.,  2., -2.])
    """
    pass


def nextafter(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Container] = None,
) -> bool:
    """
    ivy.Array instance method variant of ivy.nextafter. This method simply
    wraps the function, and so the docstring for ivy.nextafter also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        First input array.
    x2
        Second input array.
    out
        Alternate output array in which to place the result.
        The default is None.

    Returns
    -------
    ret
        The next representable values of x1 in the direction of x2.

    Examples
    --------
    >>> x1 = ivy.array([1.0e-50, 2.0e+50])
    >>> x2 = ivy.array([2.0, 1.0])
    >>> x1.nextafter(x2)
    ivy.array([1.4013e-45., 3.4028e+38])
    """
    return ivy.nextafter(self._data, x2, out=out)


# ivy.array.experimental.layers
# global
import abc
from typing import Optional, Union, Tuple, Literal

# local
import ivy


def max_pool1d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int]],
        strides: Union[int, Tuple[int]],
        padding: str,
        /,
        *,
        data_format: str = "NHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of `ivy.max_pool1d`. This method simply
    wraps the function, and so the docstring for `ivy.max_pool1d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input image *[batch_size,w,d_in]*.
    kernel
        The size of the window for each dimension of the input tensor.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        The result of the max pooling operation.

    Examples
    --------
    >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
    >>> print(x.max_pool1d(2, 2, 'SAME'))
    ivy.array([[[ 4.,  5.,  6.,  7.],
            [ 8.,  9., 10., 11.]],

           [[16., 17., 18., 19.],
            [20., 21., 22., 23.]]])
    >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
    >>> print(x.max_pool1d(2, 2, 'VALID'))
    ivy.array([[[ 4.,  5.,  6.,  7.]],

       [[16., 17., 18., 19.]]])
    """
    pass


def max_pool2d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of `ivy.max_pool2d`. This method simply
    wraps the function, and so the docstring for `ivy.max_pool2d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window for each dimension of the input tensor.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        The result of the max pooling operation.

    Examples
    --------
    >>> x = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> print(x.max_pool2d((2, 2), (1, 1), 'SAME'))
    ivy.array([[[[ 2,  3],
    [ 4,  5],
    [ 4,  5]]],
    [[[ 8,  9],
    [10, 11],
    [10, 11]]]])

    >>> x = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> print(x.max_pool2d(3, 1, 'VALID'))
    ivy.array([[[[16, 17]],
    [[22, 23]]],
    [[[40, 41]],
    [[46, 47]]]])
    """
    pass


def max_pool3d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NDHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Computes a 3-D max pool given 5-D input x.

    Parameters
    ----------
    self
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
        optional output array, for writing the result to. It must have
        a shape that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> x = ivy.arange(48.).reshape((2, 3, 2, 2, 2))
    >>> print(x.max_pool3d(2, 2, 'VALID'))
    ivy.array([[[[[14., 15.]]]],



       [[[[38., 39.]]]]])
    >>> print(x.max_pool3d(2, 2, 'SAME'))
    ivy.array([[[[[14., 15.]]],


        [[[22., 23.]]]],



       [[[[38., 39.]]],


        [[[46., 47.]]]]])
    """
    pass


def avg_pool1d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int]],
        strides: Union[int, Tuple[int]],
        padding: str,
        /,
        *,
        data_format: str = "NWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of `ivy.avg_pool1d`. This method simply
    wraps the function, and so the docstring for `ivy.avg_pool1d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input image *[batch_size,w,d_in]*.
    kernel
        The size of the window for each dimension of the input tensor.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NWC" or "NCW". Defaults to "NWC".
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        The result of the max pooling operation.

    Examples
    --------
    >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
    >>> print(x.avg_pool1d(2, 2, 'SAME'))
    ivy.array([[[ 2.,  3.,  4.,  5.],
            [ 8.,  9., 10., 11.]],

           [[14., 15., 16., 17.],
            [20., 21., 22., 23.]]])

    >>> x = ivy.arange(0, 24.).reshape((2, 3, 4))
    >>> print(x.avg_pool1d(2, 2, 'VALID'))
    ivy.array([[[ 2.,  3.,  4.,  5.]],

           [[14., 15., 16., 17.]]])
    """
    pass


def avg_pool2d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of `ivy.avg_pool2d`. This method simply
    wraps the function, and so the docstring for `ivy.avg_pool2d` also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        Input image *[batch_size,h,w,d_in]*.
    kernel
        The size of the window for each dimension of the input tensor.
    strides
        The stride of the sliding window for each dimension of input.
    padding
        "SAME" or "VALID" indicating the algorithm, or list indicating
        the per-dimension paddings.
    data_format
        "NHWC" or "NCHW". Defaults to "NHWC".
    out
        optional output array, for writing the result to. It must have a shape that
        the inputs broadcast to.

    Returns
    -------
    ret
        The result of the max pooling operation.

    Examples
    --------
    >>> x = ivy.arange(12).reshape((2, 1, 3, 2))
    >>> print(x.max_pool2d((2, 2), (1, 1), 'SAME'))
    ivy.array([[[[ 2,  3],
    [ 4,  5],
    [ 4,  5]]],
    [[[ 8,  9],
    [10, 11],
    [10, 11]]]])

    >>> x = ivy.arange(48).reshape((2, 4, 3, 2))
    >>> print(x.max_pool2d(3, 1, 'VALID'))
    ivy.array([[[[16, 17]],
    [[22, 23]]],
    [[[40, 41]],
    [[46, 47]]]])
    """
    pass


def avg_pool3d(
        self: ivy.Array,
        kernel: Union[int, Tuple[int], Tuple[int, int, int]],
        strides: Union[int, Tuple[int], Tuple[int, int, int]],
        padding: str,
        /,
        *,
        data_format: str = "NDHWC",
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    Computes a 3-D max pool given 5-D input x.

    Parameters
    ----------
    self
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
        optional output array, for writing the result to. It must have
        a shape that the inputs broadcast to.

    Returns
    -------
    ret
        The result of the pooling operation.

    Examples
    --------
    >>> x = ivy.arange(48.).reshape((2, 3, 2, 2, 2))
    >>> print(x.avg_pool3d(2, 2, 'VALID'))
    ivy.array([[[[[ 7.,  8.]]]],



           [[[[31., 32.]]]]])
    >>> print(x.avg_pool3d(2, 2, 'SAME'))
    ivy.array([[[[[ 7.,  8.]]],


            [[[19., 20.]]]],



           [[[[31., 32.]]],


            [[[43., 44.]]]]])
    """
    pass


def dct(
        self: ivy.Array,
        /,
        *,
        type: Optional[Literal[1, 2, 3, 4]] = 2,
        n: Optional[int] = None,
        axis: Optional[int] = -1,
        norm: Optional[Literal["ortho"]] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.dct. This method simply
    wraps the function, and so the docstring for ivy.dct also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        The input signal.
    type
        The type of the dct. Must be 1, 2, 3 or 4.
    n
        The lenght of the transform. If n is less than the input signal lenght,
        then x is truncated, if n is larger than x is zero-padded.
    norm
        The type of normalization to be applied. Must be either None or "ortho".
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array containing the transformed input.

    Examples
    --------
    >>> x = ivy.array([8., 16., 24., 32., 40., 48., 56., 64.])
    >>> x.dct(type=2, norm="ortho")
    ivy.array([ 102.,  -51.5,   0.,  -5.39,   0.,  -1.61,   0., -0.406])
    """
    pass


# ivy.array.experimental.linear_algebra
# global
import abc
from typing import Optional, Union

# local
import ivy


def diagflat(
        self: Union[ivy.Array, ivy.NativeArray],
        *,
        offset: Optional[int] = 0,
        padding_value: Optional[float] = 0,
        align: Optional[str] = "RIGHT_LEFT",
        num_rows: Optional[int] = -1,
        num_cols: Optional[int] = -1,
        out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.diagflat.
    This method simply wraps the function, and so the docstring for
    ivy.diagflat also applies to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.array([1,2])
    >>> x.diagflat(k=1)
    ivy.array([[0, 1, 0],
               [0, 0, 2],
               [0, 0, 0]])
    """
    pass


def kron(
        self: ivy.Array,
        b: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.kron.
    This method simply wraps the function, and so the docstring for
    ivy.kron also applies to this method with minimal changes.

    Examples
    --------
    >>> a = ivy.array([1,2])
    >>> b = ivy.array([3,4])
    >>> a.diagflat(b)
    ivy.array([3, 4, 6, 8])
    """
    pass


# ivy.array.experimental.manipulation
# global
import abc
from typing import (
    Optional,
    Union,
    Sequence,
    Tuple,
    List,
    Iterable,
    Callable,
    Literal,
    Any,
)
from numbers import Number

# local
import ivy


def moveaxis(
        self: ivy.Array,
        source: Union[int, Sequence[int]],
        destination: Union[int, Sequence[int]],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.moveaxis. This method simply
    wraps the function, and so the docstring for ivy.unstack also applies to
    this method with minimal changes.

    Parameters
    ----------
    a
        The array whose axes should be reordered.
    source
        Original positions of the axes to move. These must be unique.
    destination
        Destination positions for each of the original axes.
        These must also be unique.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array with moved axes. This array is a view of the input array.

    Examples
    --------
    >>> x = ivy.zeros((3, 4, 5))
    >>> x.moveaxis(0, -1).shape
    (4, 5, 3)
    >>> x.moveaxis(-1, 0).shape
    (5, 3, 4)
    """
    pass


def heaviside(
        self: ivy.Array,
        x2: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.heaviside. This method simply
    wraps the function, and so the docstring for ivy.heaviside also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input array.
    x2
        values to use where x1 is zero.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        output array with element-wise Heaviside step function of x1.
        This is a scalar if both x1 and x2 are scalars.

    Examples
    --------
    >>> x1 = ivy.array([-1.5, 0, 2.0])
    >>> x2 = ivy.array([0.5])
    >>> ivy.heaviside(x1, x2)
    ivy.array([0.0000, 0.5000, 1.0000])

    >>> x1 = ivy.array([-1.5, 0, 2.0])
    >>> x2 = ivy.array([1.2, -2.0, 3.5])
    >>> ivy.heaviside(x1, x2)
    ivy.array([0., -2., 1.])
    """
    pass


def flipud(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.flipud. This method simply
    wraps the function, and so the docstring for ivy.flipud also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        The array to be flipped.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array corresponding to input array with elements
        order reversed along axis 0.

    Examples
    --------
    >>> m = ivy.diag([1, 2, 3])
    >>> m.flipud()
    ivy.array([[ 0.,  0.,  3.],
        [ 0.,  2.,  0.],
        [ 1.,  0.,  0.]])
    """
    pass


def vstack(
        self: ivy.Array,
        /,
        arrays: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray]],
            List[Union[ivy.Array, ivy.NativeArray]],
        ],
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.vstack. This method simply
    wraps the function, and so the docstring for ivy.vstack also applies
    to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.array([[1, 2]])
    >>> y = [ivy.array([[5, 6]]), ivy.array([[7, 8]])]
    >>> print(x.vstack(y))
        ivy.array([[1, 2],
                   [5, 6],
                   [7, 8]])
    """
    pass


def hstack(
        self: ivy.Array,
        /,
        arrays: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray]],
            List[Union[ivy.Array, ivy.NativeArray]],
        ],
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.hstack. This method simply
    wraps the function, and so the docstring for ivy.hstack also applies
    to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.array([[1, 2]])
    >>> y = [ivy.array([[5, 6]]), ivy.array([[7, 8]])]
    >>> print(x.vstack(y))
    ivy.array([1, 2, 5, 6, 7, 8])

    """
    pass


def rot90(
        self: ivy.Array,
        /,
        *,
        k: Optional[int] = 1,
        axes: Optional[Tuple[int, int]] = (0, 1),
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.rot90.
    This method simply wraps the function, and so the docstring
    for ivy.rot90 also applies to this method with minimal changes.

    Parameters
    ----------
    self
        Input array of two or more dimensions.
    k
        Number of times the array is rotated by 90 degrees.
    axes
        The array is rotated in the plane defined by the axes. Axes must be
        different.
    out
        Optional output, for writing the result to. It must have a shape that the
        inputs broadcast to.

    Returns
    -------
    ret
        Array with a rotated view of input array.

    Examples
    --------
    >>> m = ivy.array([[1,2], [3,4]])
    >>> m.rot90()
    ivy.array([[2, 4],
           [1, 3]])
    >>> m = ivy.array([[1,2], [3,4]])
    >>> m.rot90(k=2)
    ivy.array([[4, 3],
           [2, 1]])
    >>> m = ivy.array([[[0, 1],\
                        [2, 3]],\
                       [[4, 5],\
                        [6, 7]]])
    >>> m.rot90(k=2, axes=(1,2))
    ivy.array([[[3, 2],
            [1, 0]],

           [[7, 6],
            [5, 4]]])

    """
    pass


def top_k(
        self: ivy.Array,
        k: int,
        /,
        *,
        axis: Optional[int] = None,
        largest: Optional[bool] = True,
        out: Optional[tuple] = None,
) -> Tuple[ivy.Array, ivy.NativeArray]:
    """ivy.Array instance method variant of ivy.top_k. This method simply
    wraps the function, and so the docstring for ivy.top_k also applies
    to this method with minimal changes.

    Parameters
    ----------
    x
        The array to compute top_k for.
    k
        Number of top elements to retun must not exceed the array size.
    axis
        The axis along which we must return the top elements default value is 1.
    largest
        If largest is set to False we return k smallest elements of the array.
    out:
        Optional output tuple, for writing the result to. Must have two arrays,
        with a shape that the returned tuple broadcast to.

    Returns
    -------
    ret
        A named tuple with values and indices of top k elements.

    Examples
    --------
    With :class:`ivy.Array` input:

    >>> x = ivy.array([2., 1., -3., 5., 9., 0., -4])
    >>> y = x.top_k(2)
    >>> print(y)
    top_k(values=ivy.array([9., 5.]), indices=ivy.array([4, 3]))
    """
    return ivy.top_k(self, k, axis=axis, largest=largest, out=out)


def fliplr(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.fliplr. This method simply
    wraps the function, and so the docstring for ivy.fliplr also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        The array to be flipped. Must be at least 2-D.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Array corresponding to input array with elements
        order reversed along axis 1.

    Examples
    --------
    >>> m = ivy.diag([1, 2, 3])
    >>> m.fliplr()
    ivy.array([[0, 0, 1],
           [0, 2, 0],
           [3, 0, 0]])
    """
    pass


def i0(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.i0. This method simply
    wraps the function, and so the docstring for ivy.i0 also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    out
        Optional output, for writing the result to.

    Returns
    -------
    ret
        Array with modified Bessel function of the first kind, order 0.

    Examples
    --------
    >>> x = ivy.array([[1, 2, 3]])
    >>> x.i0()
    ivy.array([1.26606588, 2.2795853 , 4.88079259])
    """
    pass


def flatten(
        self: ivy.Array,
        *,
        start_dim: Optional[int] = 0,
        end_dim: Optional[int] = -1,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.flatten. This method simply
    wraps the function, and so the docstring for ivy.flatten also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        input array to flatten.
    start_dim
        first dim to flatten. If not set, defaults to 0.
    end_dim
        last dim to flatten. If not set, defaults to -1.

    Returns
    -------
    ret
        the flattened array over the specified dimensions.

    Examples
    --------
    >>> x = ivy.array([1,2], [3,4])
    >>> ivy.flatten(x)
    ivy.array([1, 2, 3, 4])

    >>> x = ivy.array(
        [[[[ 5,  5,  0,  6],
        [17, 15, 11, 16],
        [ 6,  3, 13, 12]],

        [[ 6, 18, 10,  4],
        [ 5,  1, 17,  3],
        [14, 14, 18,  6]]],


    [[[12,  0,  1, 13],
        [ 8,  7,  0,  3],
        [19, 12,  6, 17]],

        [[ 4, 15,  6, 15],
        [ 0,  5, 17,  9],
        [ 9,  3,  6, 19]]],


    [[[17, 13, 11, 16],
        [ 4, 18, 17,  4],
        [10, 10,  9,  1]],

        [[19, 17, 13, 10],
        [ 4, 19, 16, 17],
        [ 2, 12,  8, 14]]]]
        )
    >>> ivy.flatten(x, start_dim = 1, end_dim = 2)
    ivy.array(
        [[[ 5,  5,  0,  6],
        [17, 15, 11, 16],
        [ 6,  3, 13, 12],
        [ 6, 18, 10,  4],
        [ 5,  1, 17,  3],
        [14, 14, 18,  6]],

        [[12,  0,  1, 13],
        [ 8,  7,  0,  3],
        [19, 12,  6, 17],
        [ 4, 15,  6, 15],
        [ 0,  5, 17,  9],
        [ 9,  3,  6, 19]],

        [[17, 13, 11, 16],
        [ 4, 18, 17,  4],
        [10, 10,  9,  1],
        [19, 17, 13, 10],
        [ 4, 19, 16, 17],
        [ 2, 12,  8, 14]]]))
    """
    pass


def pad(
        self: ivy.Array,
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
        out: Optional[ivy.Array] = None,
        **kwargs: Optional[Any],
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.pad. This method simply
    wraps the function, and so the docstring for ivy.pad also applies
    to this method with minimal changes.
    """
    pass


def vsplit(
        self: ivy.Array,
        indices_or_sections: Union[int, Tuple[int]],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.vsplit. This method simply
    wraps the function, and so the docstring for ivy.vsplit also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n along the 3rd axis, each section will be of
        equal size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        Optional output, for writing the result to.

    Returns
    -------
    ret
        input array split along the 3rd axis.

    Examples
    --------
    >>> ary = ivy.array(
        [[[0.,  1.],
          [2.,  3.]],
         [[4.,  5.],
          [6.,  7.]]]
        )
    >>> ary.vsplit(2)
    [ivy.array([[[0., 1.], [2., 3.]]]), ivy.array([[[4., 5.], [6., 7.]]])])
    """
    pass


def dsplit(
        self: ivy.Array,
        indices_or_sections: Union[int, Tuple[int]],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.dsplit. This method simply
    wraps the function, and so the docstring for ivy.dsplit also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    indices_or_sections
        If indices_or_sections is an integer n, the array is split into n sections.
        If the array is divisible by n along the 3rd axis, each section will be of
        equal size. If input is not divisible by n, the sizes of the first
        int(ary.size(0) % n) sections will have size int(ary.size(0) / n) + 1, and
        the rest will have size int(ary.size(0) / n).
        If indices_or_sections is a tuple of ints, then input is split at each of
        the indices in the tuple.
    out
        Optional output, for writing the result to.

    Returns
    -------
    ret
        input array split along the 3rd axis.

    Examples
    --------
    >>> ary = ivy.array(
        [[[ 0.,   1.,   2.,   3.],
          [ 4.,   5.,   6.,   7.]],
         [[ 8.,   9.,  10.,  11.],
          [12.,  13.,  14.,  15.]]]
    )
    >>> ary.dsplit(2)
    [ivy.array([[[ 0.,  1.], [ 4.,  5.]], [[ 8.,  9.], [12., 13.]]]),
    ivy.array([[[ 2.,  3.], [ 6.,  7.]], [[10., 11.], [14., 15.]]])]
    """
    pass


def dstack(
        self: ivy.Array,
        /,
        arrays: Union[
            Tuple[Union[ivy.Array, ivy.NativeArray]],
            List[Union[ivy.Array, ivy.NativeArray]],
        ],
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.dstack. This method simply
    wraps the function, and so the docstring for ivy.dstack also applies
    to this method with minimal changes.

    Examples
    --------
    >>> x = ivy.array([1, 2, 3])
    >>> y = ivy.array([2, 3, 4])
    >>> x.dstack(y)
    ivy.array([[[1, 2],
                [2, 3],
                [3, 4]]])
    """
    pass


def atleast_2d(self: ivy.Array, *arys: ivy.Array) -> List[ivy.Array]:
    """
    ivy.Array instance method variant of ivy.atleast_2d. This method simply
    wraps the function, and so the docstring for ivy.atleast_2d also applies
    to this method with minimal changes.

    Parameters
    ----------
    self
        Input array. Cannot be a scalar input.
    arys
        An arbitrary number of input arrays.

    Returns
    -------
    ret
        List of arrays, each with a.ndim >= 2. Copies are made
        only if necessary.

    Examples
    --------
    >>> a1 = ivy.array([[1,2,3]])
    >>> a2 = ivy.array(4)
    >>> a1.atleast_2d(a2,5,6)
    [ivy.array([[1, 2, 3]]), ivy.array([[4]]), ivy.array([[5]]), ivy.array([[6]])]
    """
    return ivy.atleast_2d(self._data, *arys)


# ivy.array.experimental.random
# global
import abc
from typing import Optional, Union

# local
import ivy


def dirichlet(
        self: ivy.Array,
        /,
        *,
        size: Optional[Union[ivy.Shape, ivy.NativeShape]] = None,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        seed: Optional[int] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.dirichlet. This method simply
    wraps the function, and so the docstring for ivy.shuffle also applies to
    this method with minimal changes.

    Parameters
    ----------
    alpha
        Sequence of floats of length k
    size
        optional int or tuple of ints, Output shape. If the given shape is,
        e.g., (m, n), then m * n * k samples are drawn. Default is None,
        in which case a vector of length k is returned.
    dtype
        output array data type. If ``dtype`` is ``None``, the output array data
        type will be the default floating-point data type. Default ``None``
    seed
        A python integer. Used to create a random seed distribution
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        The drawn samples, of shape (size, k).

    Examples
    --------
    >>> alpha = ivy.array([1.0, 2.0, 3.0])
    >>> alpha.dirichlet()
    ivy.array([0.10598304, 0.21537054, 0.67864642])

    >>> alpha = ivy.array([1.0, 2.0, 3.0])
    >>> alpha.dirichlet(size = (2,3))
    ivy.array([[[0.48006698, 0.07472073, 0.44521229],
        [0.55479872, 0.05426367, 0.39093761],
        [0.19531053, 0.51675832, 0.28793114]],

    [[0.12315625, 0.29823365, 0.5786101 ],
        [0.15564976, 0.50542368, 0.33892656],
        [0.1325352 , 0.44439589, 0.42306891]]])
    """
    pass


# ivy.array.experimental.sorting
# global
import abc
from typing import Optional

# local

import ivy


def msort(
        self: ivy.Array,
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """
    ivy.Array instance method variant of ivy.msort. This method simply wraps the
    function, and so the docstring for ivy.msort also applies to this method
    with minimal changes.

    Parameters
    ----------
    self
        input array.
    out
    optional output array, for writing the result to.

    Returns
    -------
    ret
        sorted array of the same type and shape as a

    Examples
    --------
    >>> a = ivy.randint(10, size=(2,3))
    >>> a.msort()
    ivy.array(
        [[6, 2, 6],
        [8, 9, 6]]
        )
    """
    pass


# ivy.array.experimental.statistical
# global
import abc
from typing import Optional, Union, Tuple

# local
import ivy


def median(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[Tuple[int], int]] = None,
        keepdims: Optional[bool] = False,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.median. This method simply
    wraps the function, and so the docstring for ivy.median also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
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
    >>> a = ivy.array([[10, 7, 4], [3, 2, 1]])
    >>> a.median()
    3.5
    >>> a.median(axis=0)
    ivy.array([6.5, 4.5, 2.5])
    """
    pass


def nanmean(
        self: ivy.Array,
        /,
        *,
        axis: Optional[Union[Tuple[int], int]] = None,
        keepdims: Optional[bool] = False,
        dtype: Optional[Union[ivy.Dtype, ivy.NativeDtype]] = None,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.nanmean. This method simply
    wraps the function, and so the docstring for ivy.nanmean also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
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
        The nanmean of the array elements.

    Examples
    --------
    >>> a = ivy.array([[1, ivy.nan], [3, 4]])
    >>> a.nanmean()
    2.6666666666666665
    >>> a.nanmean(axis=0)
    ivy.array([2.,  4.])
    """
    pass


def unravel_index(
        self: ivy.Array,
        shape: Tuple[int],
        /,
        *,
        out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """ivy.Array instance method variant of ivy.unravel_index. This method simply
    wraps the function, and so the docstring for ivy.unravel_index also applies to
    this method with minimal changes.

    Parameters
    ----------
    self
        Input array.
    shape
        The shape of the array to use for unraveling indices.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
        Tuple with arrays that have the same shape as the indices array.

    Examples
    --------
    >>> indices = ivy.array([22, 41, 37])
    >>> indices.unravel_index((7,6))
    (ivy.array([3, 6, 6]), ivy.array([4, 5, 1]))
    """
    pass
