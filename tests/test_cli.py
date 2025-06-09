import subprocess
import sys
import os
from pathlib import Path

SCRIPT_PATH = Path(__file__).parent.parent / 'main.py'

def test_cli_single_car():
    '''
    Test single car case with CLI
    '''
    inputs = (
        '10 10\n'
        '1\n'
        'A\n'
        '1 2 N\n'
        'FFRFFFFRRL\n'
        '2\n'
        '2\n'
    )

    result = subprocess.run(
        [sys.executable, SCRIPT_PATH],
        input=inputs,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    assert 'A, (5,4), S' in result.stdout
    assert 'Thank you for running the simulation. Goodbye!' in result.stdout


def test_cli_multiple_car_collision():
    '''
    Test multiple car collision with cli
    '''
    inputs = (
        '10 10\n'
        '1\n'
        'A\n'
        '1 2 N\n'
        'FFRFFFFRRL\n'
        '1\n'
        'B\n'
        '7 8 W\n'
        'FFLFFFFFFF\n'
        '2\n'
        '2\n'
    )

    result = subprocess.run(
        [sys.executable, SCRIPT_PATH],
        input=inputs,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    assert 'A, collides with B at (5,4) at step 7' in result.stdout
    assert 'B, collides with A at (5,4) at step 7' in result.stdout
    assert 'Thank you for running the simulation. Goodbye!' in result.stdout
