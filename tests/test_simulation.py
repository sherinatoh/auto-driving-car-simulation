import pytest
from simulation.car import Car
from simulation.simulation import Simulation


@pytest.fixture
def test_sim():
    sim = Simulation()
    sim.width = 10
    sim.height = 10
    return sim


def test_no_collision(test_sim):
    '''
    Test multiple cars moving without collision
    '''
    car_a = Car('A', 0, 0, 'N', 'FRF')
    car_b = Car('B', 9, 9, 'S', 'FRF')
    test_sim.cars.append(car_a)
    test_sim.cars.append(car_b)
    test_sim.run_simulation()

    assert car_a.is_collide is False
    assert car_b.is_collide is False
    assert car_a.position == (1, 1)
    assert car_b.position == (8, 8)


def test_two_car_collision(test_sim):
    '''
    Test car A colliding into Car B
    '''
    car_a = Car('A', 0, 0, 'E', 'F')
    car_b = Car('B', 2, 0, 'W', 'F')
    test_sim.cars.append(car_a)
    test_sim.cars.append(car_b)
    test_sim.run_simulation()

    assert car_a.is_collide is True
    assert car_b.is_collide is True
    assert car_a.collision_info == f'A, collides with B at (1,0) at step 1'
    assert car_b.collision_info == f'B, collides with A at (1,0) at step 1'


def test_car_multiple_collisions(test_sim):
    '''
    Test car A colliding into Car B
    Car C collides later
    '''
    car_a = Car('A', 0, 0, 'E', 'F')
    car_b = Car('B', 2, 0, 'W', 'F')
    car_c = Car('C', 1, 3, 'S', 'FFFF')
    test_sim.cars.append(car_a)
    test_sim.cars.append(car_b)
    test_sim.cars.append(car_c)
    test_sim.run_simulation()

    assert car_a.is_collide is True
    assert car_b.is_collide is True
    assert car_c.is_collide is True
    assert car_a.collision_info == f'A, collides with B at (1,0) at step 1'
    assert car_b.collision_info == f'B, collides with A at (1,0) at step 1'
    assert car_c.collision_info == f'C, collides with A,B at (1,0) at step 3'
