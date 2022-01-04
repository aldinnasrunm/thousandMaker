def thousandsMarker(param):
    reversed = str(param)[::-1]
    result =  '.'.join(reversed[x:x+3] for x in range(0, len(reversed), 3))
    return result[::-1]
