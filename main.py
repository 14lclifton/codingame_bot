class Game():
    def __init__(self):
        self.game_map = []
        self.robot_count = 0
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
    
    # 
    def get_free(self,x,y):
        pass
    
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
            
            # Simulate the robot's movements
            x,y = self.move(x,y,direction)
            
        # Print final result
        print("0 0 U 1 1 R 2 2 D 3 3 L")

game = Game()
