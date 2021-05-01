def bubble(listy):
    indexing_length = len(listy) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if listy[i] > listy[i+1]:
                sorted = False
                listy[i], listy[i+1] = listy[i+1], listy[i]

    return listy




