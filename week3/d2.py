class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if(len(A) < 3):
            return 0
        
        start = 0
        stop = 0
        res = 0
        n = len(A)
        
        while(start < n):
            stop = start
            if(stop+1 < n and A[stop] < A[stop+1]):
                while(stop+1 < n and A[stop] < A[stop+1]): # go up
                    stop += 1
                if(stop+1 < n and A[stop] > A[stop+1]): # go down
                    while(stop+1 < n and A[stop] > A[stop+1]):
                        stop += 1
                    res = max(res, stop - start + 1)
            
            start = max(start+1, stop)
        
        return res