def parse(intString):
    result = []
    for i in intString.split(','):
        result.append(int(i))
    return result
