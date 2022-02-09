class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return 0
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]
        i, res = 3, [[1], [1, 1]]
        while i <= numRows:
            tmp = [1]
            for j in range(len(res[i - 2]) - 1):
                tmp.append(res[i - 2][j] + res[i - 2][j + 1])
            tmp.append(1)
            res.append(tmp)
            i += 1

        return res