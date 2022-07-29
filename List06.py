def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    list = []
    for i in list1:
        if i == 0:
            list += [0]
        else:
            list += [True]
    return list