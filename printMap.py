def printMap(index, map):
    map[index] = ">"
    result = ""
    for i in map:
        result += i
    map[index] = "="
    return result
