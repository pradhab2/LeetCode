class Soution(object):
    """ Running Length Encoding ::
    Input : wwwwaaadexxxxxx
    Output: w4a3d1e1x6  """

    def RLE(s):

        n = len(s)
        i = 0
        res = ''
        while i <= n - 1:
            count = 1
            while i < n - 1 and s[i] == s[i + 1]:
                count += 1
                i += 1
            res += s[i] + str(count)
            i += 1

        return res

    def decodeRLE(d):
        res = ''
        i = 0
        while i < len(d):
            ltr = d[i]
            cntr = d[i + 1]
            for j in range(int(cntr)):
                res += ltr
            i += 2
        return res

    if __name__ == "__main__":
        st = "wwwwaaadexxxxxxt"
        print("Input: %s" % st)
        en = RLE(st)
        print("En-coded value is : %s" % en)
        print("De-Coded value is : %s" % decodeRLE(en))
