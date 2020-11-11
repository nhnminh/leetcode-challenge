import copy
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def notInt(x):
            if(x == 1):
                return 0
            else:
                return 1
        B = copy.deepcopy(A)
        l = len(A)
        for j in range(l):
            if(l == 1):
                B[j][0] = notInt(A[j][0])
            else:
                for i in range(l//2):
                    if(l%2 == 0):
                        B[j][i] = notInt(A[j][l-i-1])
                        B[j][ l-i-1] = notInt(A[j][i])
                    else:
                        B[j][i] = notInt(A[j][l - i - 1])
                        B[j][l//2] =  notInt(A[j][l//2])
                        B[j][l-i-1] = notInt(A[j][i])
        
        return B