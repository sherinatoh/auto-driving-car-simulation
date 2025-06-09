from simulation.constants import DIRECTIONS
from simulation.car import Car


class Simulation:
    def __init__(self):
        self.cars = []

    def print_cars_list(self):
        '''
        Prints list of cars currently in the simluation
        '''
        print('Your current list of cars are:')
        for car in self.cars:
            print(f'- {car}')

    def setup_field(self):
        '''
        Asks user for height and width of the field and initializes it
        '''
        width, height = map(int, input('Please enter the width and height of the simulation field in x y format:\n').split(' '))
        self.width = width
        self.height = height

    def add_car(self):
        '''
        Asks the user for car information and adds it into the simulation
        '''
        # Name of the car
        name = input('Please enter the name of the car:\n')
        x, y, direction = input(f'Please enter initial position of car {name} in x y Direction format:\n').split(' ')
        x = int(x)
        y = int(y)
        if direction not in DIRECTIONS:
            print('Invalid Direction input. Only N, S, E, W is allowed. Please add the car again.')
        # Commands for the car
        commands = list(input(f'Please enter the commands for car {name}:\n'))
        car = Car(name, x, y, direction, commands)
        self.cars.append(car)
        self.print_cars_list()

    def run_simulation(self):
        '''
        Runs the simulation with the current list of cars
        '''
        self.print_cars_list()
        max_steps = max(len(car.commands) for car in self.cars)
    
        for step in range(max_steps):
            car_positions = {}

            for car in self.cars:
                if not car.is_collide:
                    # Skip moving if car already collided somewhere
                    car.move(step, self.height, self.width)

                if car_positions.get(car.position):
                    car_positions[car.position].append(car)
                else:
                    car_positions[car.position] = [car]
                
            # Check for collisions
            for pos, cars in car_positions.items():
                if len(cars) > 1:
                    # Collision happened, store information if have not collided before
                    for car in cars:
                        if not car.is_collide:
                            car.set_collision(step, cars)
            
        print('After simulation, the result is:')
        for car in self.cars:
            car.print_car_info()

    def reset(self):
        '''
        Clears all list of cars
        '''
        self.cars = []
                    
    def run(self):
        '''
        Main function to run the simulation
        '''
        print('Welcome to Auto Driving Car Simulation!\n')
        self.setup_field()

        while True:
            print('Please choose from the following options:')
            print('[1] Add a car to field')
            print('[2] Run simulation')
            option = input()
            if option == '1':
                self.add_car()
            elif option == '2':
                self.run_simulation()
                break

        print('Please choose from the following options:')
        print('[1] Start over')
        print('[2] Exit')
        option =  input()
        if option == '1':
            print('Restarting...')
            self.reset()
            return self.run()
        else:
            print('Thank you for running the simulation. Goodbye!')
            return
