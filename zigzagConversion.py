class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lineConv = ""
        L = [ [] for _ in range(numRows)]
        m = 0
        while m < len(s):
        #zig
            for j in range(numRows):
                if m >= len(s):
                    break
                L[j].append(s[m])
                m = m + 1
        #zag
            for k in reversed(range(1,numRows-1)):
                if m >= len(s):
                    break
                L[k].append(s[m])
                m = m + 1
        for l in range(numRows):
            for c in range(len(L[l])):
                lineConv += L[l][c]
        return lineConv

