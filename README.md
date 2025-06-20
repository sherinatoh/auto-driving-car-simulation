# Installation instructions

## Clone the Repository
```
git clone https://github.com/sherinatoh/auto-driving-car-simulation.git
```
## Installing dependencies
```
cd auto-driving-car-simulation
pip install -r requirements.txt
```

## Running the simulation
```
python main.py
```

## Running the test
```
pytest tests
```


# Assumptions
Cars are only assumed to have collided if they are in the same position after moving. If they move towards each other (swap positions), it is not considered a collision

# Areas of Improvement
- Input validations can be added, to request for the user to reenter values if they are not valid
    - Add validation for direction and movement
    - Prevent a car from being added to an already occupied popsition
- Include swapping of positions as a form of collision