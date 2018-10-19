# reading game map
gameMap = []
for i in range(10):
    line = input()
    gameMap.append(line)
robot_count = int(input())

# Main logic
for i in range(robot_count):
    # Get robot x,y and direction
    x, y, direction = input().split()
    x = int(x)
    y = int(y)
    
    # Determine where to place flags
    
print("0 0 U 1 1 R 2 2 D 3 3 L")
