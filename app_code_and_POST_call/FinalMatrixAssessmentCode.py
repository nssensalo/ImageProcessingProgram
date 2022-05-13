class Pair:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
class ImageProcessing:
    def fillGridSpaceWithEdgePoints(lst,row,col):
    # Define location of 2 of 4 coordinates given
        left_lower = (min(lst))
        right_upper = (max(lst))
        right_upper_coordinate = Pair(right_upper[0],right_upper[1])
        left_lower_coordinate = Pair(left_lower[0],left_lower[1])
        
        #Calculate total space between boundries of corner coordinates
        difference_row = right_upper_coordinate.getX()-left_lower_coordinate.getX()
        difference_col = right_upper_coordinate.getY()-left_lower_coordinate.getY()
    
        #Calculate number of spaces to be filled
        num_row_spaces = int(row)-1
        num_col_spaces = int(col)-1
        
        #Calculate value/amount of each space increment
        row_increment_value = difference_row/num_row_spaces
        col_increment_value = difference_col/num_col_spaces
        
        #Easy access to the main x and y values used for calculation
        x = left_lower_coordinate.getX()
        y = left_lower_coordinate.getY()
        
        #Newly calculated values initiated at 0
        newX = 0
        newY = 0
        results = []
        
        #Looping through each row of each column
        for i in range(int(col)):
            newX = x + (i*col_increment_value)
            for j in range(int(row)):
                newY = y + (j*row_increment_value)
                results.append([newX,newY])
        print(results)

        return results
        
               
    #fillGridSpaceWithEdgePoints([(1,3), (3,1), (1,1), (3,3)],3,3)
    #fillGridSpaceWithEdgePoints([(1.5,8.0),(1.5,1.5), (4.0,8.0), (4.0,1.5) ],3,3) 

                