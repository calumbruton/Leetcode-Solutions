class Solution(object):
    def nextClosestTime(self, time):

        first, second, third, fourth = int(time[0]), int(time[1]), int(time[3]), int(time[4])
        locs = sorted([first,second,third,fourth])
        l = min(locs)
        
        #Fourth digits
        for num in locs:
            if num > fourth:
                return "".join([str(first),str(second),":",str(third),str(num)])
            
        #Third digit
        for num in locs:
            if num > third and num<6:
                return "".join([str(first),str(second),":",str(num), str(l)])
            
        #Second digit
        for num in locs:
            if first == 2:
                if num > second and num<4:
                    return "".join([str(first),str(num),":",str(l), str(l)])
            else:
                if num>second:
                    return "".join([str(first),str(num),":",str(l), str(l)])
                
        #First digit
        for num in locs:
            if num>first and num<3:
                return "".join([str(num),str(l),":",str(l), str(l)])
        
        
        # If non of these are possible return a string with all of the min value
        # This value is guaranteed to be legal because the first digit of the hour
        # will be a 0, 1, or 2 which is elidgible for every location 
        return "".join([str(l),str(l),":",str(l), str(l)])
        
        
        
        
        