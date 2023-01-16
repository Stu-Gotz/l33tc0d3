class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = [""] * numRows
        rowNumber = 0
        direction = 1

        for i in range(len(s)):
            output[rowNumber] = output[rowNumber] + s[i]
            if rowNumber < (numRows - 1) and direction == 1:
                rowNumber += 1
            elif rowNumber > 0 and direction == -1:
                rowNumber -= 1
            else:
                direction *= -1
                rowNumber += direction
        return ''.join(output)

print(Solution().convert('PAYPALISHIRING',3))