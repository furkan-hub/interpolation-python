import numpy as np

def linear_interpolation(x, y, x0):
    """
    Perform linear interpolation.

    Parameters:
    x (numpy.array): Array of x-coordinates of data points.
    y (numpy.array): Array of y-coordinates of data points.
    x0 (float): Interpolation point.

    Returns:
    float: Interpolated y-value at x0.
    """
    # Find the two data points closest to the interpolation point
    i = np.searchsorted(x, x0)

    # Select the two data points to use for interpolation
    x1, x2 = x[i - 1], x[i]
    y1, y2 = y[i - 1], y[i]

    # Linear interpolation formula
    y0 = y1 + (y2 - y1) * (x0 - x1) / (x2 - x1)

    return y0

def exponential_interpolation(x, y, x0):
    """
    Perform exponential interpolation.

    Parameters:
    x (numpy.array): Array of x-coordinates of data points.
    y (numpy.array): Array of y-coordinates of data points.
    x0 (float): Interpolation point.

    Returns:
    float: Interpolated y-value at x0.
    """
    # Find the two data points closest to the interpolation point
    i = np.searchsorted(x, x0)

    # Select the two data points to use for interpolation
    x1, x2 = x[i - 1], x[i]
    y1, y2 = y[i - 1], y[i]

    # Exponential interpolation formula
    y0 = y1 * np.exp((np.log(y2 / y1) / (x2 - x1)) * (x0 - x1))

    return y0


if __name__ == "__main__":
    # Data points for interpolation
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 1, 5, 7])

    # Point to perform interpolation on
    x0 = 2.5

    # Perform interpolation using the function
    result = linear_interpolation(x, y, x0)
    result2 = exponential_interpolation(x, y, x0)

    print(f"Interpolation result: x = {x0}, y = {result}")
    print(f"Interpolation result: x = {x0}, y = {result2}")
