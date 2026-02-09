# Braking Logic for Stromer 2019 E-bike Analysis
import math

def calculate_stop_time(speed_mph, surface_condition='dry'):
    """
    Calculates the time it takes to stop based on speed and road surface.
    Friction coefficients: Dry = 0.7, Wet = 0.4
    """
    friction = 0.7 if surface_condition == 'dry' else 0.4
    speed_mps = speed_mph * 0.44704  # Convert mph to meters per second
    gravity = 9.81 
    
    # Formula: v = u + at -> time = velocity / (friction * gravity)
    stop_time = speed_mps / (friction * gravity)
    return round(stop_time, 2)

# Test the logic for a 20mph cruise
print(f"Stopping time on dry road: {calculate_stop_time(20, 'dry')} seconds")
print(f"Stopping time on wet road: {calculate_stop_time(20, 'wet')} seconds")