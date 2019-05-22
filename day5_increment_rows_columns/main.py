"""
This script is a practice function that increments rows and columns in an matrix

Examples:
    final(3, 3, ["2r", "2c", "1r", "0c"])

    # Initialize a 3 x 3 matrix of zeroes.

    [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]

    # Apply "2r" (increment index 2 row).

    [
      [0, 0, 0],
      [0, 0, 0],
      [1, 1, 1]
    ]

    # Apply "2c" (increment index 2 column).

    [
        [0, 0, 1],
        [0, 0, 1],
        [1, 1, 2]
    ]

    # Apply "1r" (increment index 1 row).

    [
      [0, 0, 1],
      [1, 1, 2],
      [1, 1, 2]
    ]

    # Apply "0c" (increment index 0 column).
    # This is the result you should return.

    [
      [1, 0, 1],
      [2, 1, 2],
      [2, 1, 2]
    ]
"""

import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging


def final(r, c, i):
    """
    Create matrix
    Args:
        r (int): number of rows
        c (int): number of columns
        i (list): list of increment options

    Returns:
        obj nxn matrix
    """
    if (not isinstance(r, int) or
            not isinstance(c, int) or not isinstance(i, list)):
        raise ValueError

    _matrix = np.zeros([r,c])
    increment_row = [1 for _ in range(0, r)]
    increment_col = [1 for _ in range(0, c)]

    for incr in i:
        try:
            option = incr[-1]
            loc = int(incr[:-1])
            if option not in ['r', 'c']:
                log.warning('Invalid increment option %r', incr)

            if option == 'r':
                if loc > r:
                    log.warning('Increment row index is too large!')
                    continue
                _matrix[loc] = _matrix[loc] + increment_row
            elif option == 'c':
                if loc > c:
                    log.warning('Increment col index is too large!')
                    continue
                _matrix[:,loc] = _matrix[:,loc] + increment_col

        except Exception as e:
            log.error('Issue extracting increment value - %r', e)

    log.info(_matrix)
    return _matrix


if __name__ == '__main__':
    final(3, 3, ["2r", "2c", "1r", "0c"])
    final(2, 2, ["0r", "0r", "0r", "1c"])
    final(3, 3, [])