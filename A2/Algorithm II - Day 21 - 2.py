class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maxPoints=0
        if(len(points)<2):return len(points)
        for i in range(len(points)):
            tempNo=0
            for j in range(len(points)):
                tempNo=0
                if(i==j):continue
                if(points[j][0]==points[i][0]):slope='x'
                elif(points[j][1]==points[i][1]):slope='y'
                else:slope=(points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                if(slope!='x' and slope!='y'):c=points[j][1]-(points[j][0]*slope)
                
                for k in range(len(points)):
                    if(slope=='x' and points[k][0]==points[i][0]):tempNo+=1
                    if(slope=='y' and points[k][1]==points[i][1]):tempNo+=1    
                    if(slope!='x' and slope!='y' and points[k][1]==round((slope*points[k][0])+c,5)):tempNo+=1
                    
                maxPoints=max(maxPoints,tempNo)
            
        return maxPoints