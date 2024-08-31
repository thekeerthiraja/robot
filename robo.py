# Robot class : Manages the movement of a robot on the grid. It checks for boundary conditions and occupied positions.
class Robot:
    def __init__(self, robot_id, terrain_size):
        self.robot_id = robot_id
        self.terrain_size = terrain_size
        self.position = (0, 0)  # Start at the top left corner

    def move(self, direction, steps, occupied_positions):
        x, y = self.position
        for _ in range(steps):
            new_x, new_y = x, y
            if direction == 'N':
                if x - 1 >= 0:
                    new_x = x - 1
            elif direction == 'E':
                if y + 1 < self.terrain_size:
                    new_y = y + 1
            elif direction == 'S':
                if x + 1 < self.terrain_size:
                    new_x = x + 1
            elif direction == 'W':
                if y - 1 >= 0:
                    new_y = y - 1

            # Check if the new position is occupied by another robot
            if (new_x, new_y) in occupied_positions:
                break  # Stop before reaching the occupied cell

            x, y = new_x, new_y  # Update to new position if not occupied

        self.position = (x, y)



    def get_position(self):
        return self.position

# Terrain Manages Multiple robots. It allows adding robots, moving them, and getting their current positions.
class Terrain:
    def __init__(self, size):
        self.size = size
        self.robots = {}

    def add_robot(self, robot_id):
        if robot_id not in self.robots:
            self.robots[robot_id] = Robot(robot_id, self.size)

    def move_robot(self, robot_id, command):
        if robot_id in self.robots:
            direction, steps = command[0], int(command[1])
            occupied_positions = {robot.get_position() for rid, robot in self.robots.items() if rid != robot_id}
            self.robots[robot_id].move(direction, steps, occupied_positions)

    def get_robot_position(self, robot_id):
        if robot_id in self.robots:
            return self.robots[robot_id].get_position()
        return None

terrain = Terrain(5)
terrain.add_robot(1)
terrain.add_robot(2)

terrain.move_robot(1, "E3")
terrain.move_robot(1, "W1")
terrain.move_robot(2, "E2")

print(f"Robot 1 Position: {terrain.get_robot_position(1)}")  # Output: (0, 2)
print(f"Robot 2 Position: {terrain.get_robot_position(2)}")  # Output: (0, 1)
