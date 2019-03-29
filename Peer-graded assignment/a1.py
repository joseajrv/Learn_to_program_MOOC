import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(0)
    0
    >>> num_buses(1)
    1
    >>> num_buses(50)
    1
    >>> num_buses(51)
    2
    >>> num_buses(1756)
    36
    
    """
    return math.ceil(n/50)
    

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0.01])
    (0.01, 0)
    >>> stock_price_summary([-0.03])
    (0, -0.03)
    >>> stock_price_summary([0.01, 0.02, 0, 0.14, 0.5])
    (0.67, 0)
    >>> stock_price_summary([-0.01, -0.4, -0.08, -0.05, 0])
    (0, -0.54)
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    
    """
    gains = 0
    losses = 0
    for change in price_changes:
        if change > 0:
            gains = gains + change
        else:
            losses = losses + change
    return (gains,losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [2, 3]
    >>> swap_k(nums, 0)
    >>> nums
    [2, 3]
    
    >>> nums = [1, 6]
    >>> swap_k(nums, 1)
    >>> nums
    [6, 1]
    
    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
      
    >>> nums = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_k(nums, 3)
    >>> nums
    [5, 6, 7, 4, 1, 2, 3]
    """
    if k > 0:
        L[0:k], L[-k:] = L[-k:], L[0:k]

    
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
