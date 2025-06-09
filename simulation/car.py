from simulation.constants import DIRECTIONS, MOVE_DISTANCE


class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.collision_info = None
    
    def __str__(self):
        return f'{self.name}, ({self.x},{self.y}), {self.direction}, {"".join(self.commands)}'
    
    @property
    def position(self):
        return (self.x, self.y)

    @property
    def is_collide(self):
        return self.collision_info is not None
    
    def move(self, command_index, height, width):
        '''
        Execute next command in command list
        '''
        if command_index >= len(self.commands):
            return False

        command = self.commands[command_index]
        if command == 'L':
            dir_index = (DIRECTIONS.index(self.direction) - 1) % 4
            self.direction = DIRECTIONS[dir_index]
        elif command == 'R':
            dir_index = (DIRECTIONS.index(self.direction) + 1) % 4
            self.direction = DIRECTIONS[dir_index]
        elif command == 'F':
            x_dist, y_dist = MOVE_DISTANCE[self.direction]
            new_x = self.x + x_dist
            new_y = self.y + y_dist
            if 0 <= new_x < width and 0 <= new_y < height:
                # Only move to new position if within field
                self.x = new_x
                self.y = new_y

    def set_collision(self, command_index, cars):
        '''
        Sets crash information
        '''
        collision_cars = [car for car in cars if car != self]
        collision_car_info = ','.join([car.name for car in collision_cars])
        self.collision_info = f'{self.name}, collides with {collision_car_info} at ({self.x},{self.y}) at step {command_index + 1}'

    def print_car_info(self):
        '''
        Return collision info if collided, else return namne, position and direction
        '''
        if self.collision_info:
            print(self.collision_info)
        else:
            print(f'{self.name}, ({self.x},{self.y}), {self.direction}')
