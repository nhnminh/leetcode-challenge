class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1: List[int], p2: List[int]) -> float:
            return(math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1])))
        
        lst = [p2, p3, p4]
        
        diagonal = 0.0
        side = 1000000000.0
        other_point = -1
        flag1 = False
        for i in range(len(lst)):
            print("point: " + str(i))
            d = distance(p1, lst[i])
            if(d <= side):
                side = d
                print("update side, side = " + str(side))
            if(d >= diagonal):
                diagonal = d
                other_point = i
                print("update diagonal, diag = " + str(diagonal))
                print("update other_point,  = " + str(other_point))
        if(side == 0):
            return False
        if(round(diagonal/side,5) == round(math.sqrt(2), 5)):
            print("Flag1 true")
            flag1 = True
        
        d1 = 0.0
        d2 = 0.0
        flag2 = True
        for j in range(len(lst)):
            if(j != other_point):
                d1 = distance(lst[other_point], lst[j])
                if(d1 != side):
                    flag2 = False
                    print("Flag2 false")
                    break
         
        if(flag1 and flag2):
            return True
        else:
            return False
        