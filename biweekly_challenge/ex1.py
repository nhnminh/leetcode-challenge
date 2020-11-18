from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # print(code)
        if(k == 0):
            return [0]*len(code)
        # print("k = " + str(k))
        pos = list(range(len(code)))*100
        neg = list(range(len(code)))[::-1]*100
        res = [0]*len(code)

        if (k>0):
            loop = range(0,k,1)
        else: 
            loop = list(range(0, k, -1))
            loop.sort()

        print(loop)
        # print(pos)
        for i in range(len(code)):
            # print("-------")
            # print("i = " + str(i))
            # res[i] = code[i]
            for j in loop:
                # print(pos[i+j+1])
                if(k > 0):
                    res[i] += code[pos[i + j +1]]
                if(k <0):
                    # print(neg[i+j+i])
                    res[i] += code[neg[i + j +1]]
                # print("res = " + str(res[i]))
        return(res)
    
if __name__ == "__main__":
    s = Solution()
    # print(s.decrypt([1,2,3,4], 0))

    # print(s.decrypt([5,7,1,4], 3))
    print(s.decrypt([2,4,9,3], -2))