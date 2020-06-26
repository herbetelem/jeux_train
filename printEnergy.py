def printEnergy(index, map):
    map[index] = "z"
    result = ""
    for i in map:
        result += i
    map[index] = " "
    return result
