def find_closest_index(array, searchFor):
    """
    Find the closest index in an ordered array
    :param array: array searched in
    :param searchFor: value that is searched
    :return: index of the closest match
    """
    if len(array) == 1:
        return 0

    # determine the direction of the iteration
    if array[1] < array[0] > searchFor:  # iteration from big to small

        # check if the value does not go out of scope
        if array[0] < searchFor and array[-1] < searchFor:
            return 0
        elif array[0] > searchFor and array[-1] > searchFor:
            return len(array) - 1

        for i in range(len(array)):
            if array[i] <= searchFor:
                valueAtIndex = array[i]
                previousValue = array[i - 1]

                # search for the index with the smallest absolute difference
                if searchFor - valueAtIndex <= previousValue - searchFor:
                    return i
                else:
                    return i - 1

    else:
        # array[0] is smaller than searchFor
        # iteration from small to big

        # check if the value does not go out of scope
        if array[0] < searchFor and array[-1] < searchFor:
            return len(array) - 1
        elif array[0] > searchFor and array[-1] > searchFor:
            return 0

        for i in range(len(array)):
            if array[i] >= searchFor:
                valueAtIndex = array[i]
                previousValue = array[i - 1]

                if valueAtIndex - searchFor <= searchFor - previousValue:
                    return i
                else:
                    return i - 1