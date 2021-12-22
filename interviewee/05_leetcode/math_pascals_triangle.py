'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
    1 <= numRows <= 30
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas_tr = []
        counter = 0
        while counter < numRows:
            layer = []
            # base case
            if counter == 0:
                layer.append(1)            
                pas_tr.append(layer)
                counter += 1
            else:            
                # create the new layer based on previous one
                layer = []
                loop_len = len(pas_tr[counter-1])-1
                for i in range(loop_len):
                    layer.append(pas_tr[counter-1][i]+pas_tr[counter-1][i+1])

                # add 1s at the edges of the layer
                layer.insert(0, 1)
                layer.append(1)
                pas_tr.append(layer)
                counter += 1           

        return pas_tr

# alternate
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pas_tr = []
        
        # base case        
        pas_tr.append([1])
        counter = 1
        
        # additional layers
        while counter < numRows:
            # create the new layer based on previous one
            layer = []
            loop_len = len(pas_tr[counter-1])-1
            for i in range(loop_len):
                layer.append(pas_tr[counter-1][i]+pas_tr[counter-1][i+1])

            # add 1s at the edges of the layer
            layer.insert(0, 1)
            layer.append(1)
            
            # add the layer to parent triangle
            pas_tr.append(layer)
            counter += 1

        return pas_tr
