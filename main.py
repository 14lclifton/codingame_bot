# template to be used when documenting functions
################################################
# FUNCTION NAME :
# FUNCTION ARGS : 
# FUNCTION RETURN :
# PURPOSE : 
################################################

# Foreword:
# The map is split into 190 cells
# A cell is regarded as 'traversable' if it is empty and has not
# been travelled through before

class Game():
    def __init__(self):
        self.game_map = []
        self.robot_count = 0
        self.arrows = []
        self.read_map()
        self.run()
    
    # FUNCTION NAME : read_map
    # FUNCTION ARGS : NONE
    # FUNCTION RETURN : NONE
    # PURPOSE : READS GAME MAP
    def read_map(self):
        for i in range(10):
            line = input()
            self.game_map.append(line)
        self.robot_count = int(input())
    
    # FUNCTION NAME : get_neighbours
    # FUNCTION ARGS : x and y position of a cell
    # FUNCTION RETURN : amount of cell 'neighbours'
    # PURPOSE : gets the amount of traversable neighbouring cells to the robot
    def get_neighbours(self,x,y):
        # TO BE IMPLEMENTED
        pass
    
    # FUNCTION NAME : get_free
    # FUNCTION ARGS : x and y position of a cell
    # FUNCTION RETURN : x and y position of a neighbouring cell
    # PURPOSE : returns the position of the only traversable neighbouring cell to the robot
    def get_free(self,x,y):
        # TO BE IMPLEMENTED
        pass
    
    def add_arrow(self,x,y,direction):
        new_arrow = str(x)+str(y)+direction
    
    # FUNCTION NAME : move
    # FUNCTION ARGS : x and y position and direction
    # FUNCTION RETURN : new x and y position
    # PURPOSE : modifies an x and y coordinate based on a direction
    def move(self,x,y,direction):
        if (direction == "U"):
            y += -1
        elif (direction == "D"):
            y += 1
        if (direction == "L"):
            x += -1
        elif (direction == "R"):
            x += 1
        return x,y
    
    def new_robot_map(self):
        robot_map = []
        for element in self.game_map:
            robot_map.append(element)
        return robot_map
    
    def run(self):
        for i in range(self.robot_count):
            # Get robot x,y and direction
            x, y, direction = input().split()
            x = int(x)
            y = int(y)
            robot_map = self.new_robot_map()
            cell_is_on = robot_map[y][x]
            
            while 1:
                # Simulate the robot's movements
                x,y = self.move(x,y,direction)
                neighbours = self.get_neighbours(x,y)
                if not neighbours:
                    break
                else if (neighbours == 1):
                    
            
        # Print final result
        print("0 0 U 1 1 R 2 2 D 3 3 L")

game = Game()
