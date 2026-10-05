def convert( s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1 or numRows >= len(s):
        return s

    res = [[] for _ in range(numRows)]
    row = 0
    incr = -1

    for x in s:
        res[row].append(x)

        if row == 0 or row == numRows - 1:
            incr *= -1
        row += incr

    for i in range(len(res)):
        res[i] = "".join(res[i])
    return "".join(res)