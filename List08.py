def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    list = []
    for i in list1:
        if i == 0:
            list += [False]
        else:
            list += [True]
    return list