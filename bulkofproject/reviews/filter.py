def filter(origin, category, filter):
    #set up output
    output = []

    #check entire origin list
    for entry in origin:
        if entry[category] == filter:
            output.append(entry)

    #output
    return output
        