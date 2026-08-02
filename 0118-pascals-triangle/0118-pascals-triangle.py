class Solution(object):
    def generate(self, numRows):
        triangle = [[1]]
        prev_row = [1]

        for i in range(numRows - 1):

            row = [1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j+1])

            row.append(1)
            triangle.append(row)
            prev_row = row
        
        return triangle
                

        