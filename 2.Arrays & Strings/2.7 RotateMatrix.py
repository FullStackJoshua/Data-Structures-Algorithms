import unittest
# Rotate Matrix: Gicen an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
# write a method to rotate the image by 90 degrees. Can you do this in place?


def rotate(matrix):
    l,r = 0, len(matrix)-1
    
    while l < r: 
        for i in range(r-l):
            top, bottom = l,r
            
            # Save top left
            topLeft = matrix[top][l+i]
            
            #move bottom left to top left
            matrix[top][l+i] = matrix[bottom-i][l]
            
            #move bottom right to bottom left
            matrix[bottom-i][l] = matrix[bottom][r-i]
            
            #move top right to bottom right
            matrix[bottom][r-i] = matrix[top+i][r]
            
            #move top left to top right
            matrix[top+i][r] = topLeft
           
        # Move to the next layer  
        r -= 1
        l += 1

# Transpos + Horizontal reflection
def rotateMatrix(matrix):
    n = len(matrix)
    for i in range(n): # Transpose
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    for i in range(n): #Reflection 
        for j in range(n//2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
    return matrix


class Test(unittest.TestCase):
    data = [
        ([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]),
        ([
            [ 5, 1, 9,11],
            [ 2, 4, 8,10],
            [13, 3, 6, 7],
            [15,14,12,16]
        ], [
            [15,13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7,10,11]
    ])
    ]


    def test_stringCompression(self):
        for matrix, expected in self.data:
            rotateMatrix(matrix)
            self.assertEqual(matrix, expected, msg=f"Failed for: {matrix}")
            
if __name__ == "__main__":
    unittest.main()

    
    
    
