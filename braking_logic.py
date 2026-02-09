"""Braking logic analysis for Google Data Analytics Capstone."""
import math

def calculate_braking_distance(speed_mph):
    """Calculate theoretical braking distance using a standard friction coefficient."""
    # Simplified formula: d = v^2 / (2 * friction * gravity)
    friction = 0.7
    speed_fps = speed_mph * 1.467  # Convert mph to feet per second
    distance = math.pow(speed_fps, 2) / (2 * friction * 32.2)
    return round(distance, 2)

# This blank line at the end satisfies the 'Final newline missing' warning