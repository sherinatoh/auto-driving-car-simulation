import pytest
from simulation.car import Car


def test_car_rotation():
    '''
    Test rotating the car in both directions
    '''
    car = Car("A", 0, 0, 'N', list("RRRRLLLL"))
    success_directions = ['E', 'S', 'W', 'N', 'W', 'S', 'E', 'N']
    for command_index in range(len(car.commands)):
        car.move(command_index, 10, 10)
        assert car.direction == success_directions[command_index]


def test_car_movement():
    '''
    Test moving forward
    '''
    car = Car("A", 0, 0, 'N', list("FF"))
    for command_index in range(len(car.commands)):
        car.move(command_index, 10, 10)
    assert car.x == 0
    assert car.y == 2


def test_car_out_of_bounds():
    '''
    Test to make sure car does not go out of bounds
    '''
    car = Car("A", 9, 9, 'N', list("F"))
    for command_index in range(len(car.commands)):
        car.move(command_index, 10, 10)
    assert car.x == 9
    assert car.y == 9
