"""
Stromer 2019 E-Bike: Braking Analysis Table
Calculates stopping times across various speeds and conditions.
"""

def calculate_stop_time(speed_mph, surface_condition='dry'):
    friction = 0.7 if surface_condition == 'dry' else 0.4
    speed_mps = speed_mph * 0.44704
    gravity = 9.81 
    return round(speed_mps / (friction * gravity), 2)

# Speeds to analyze (MPH)
speeds = [10, 15, 20, 25, 28]

print(f"{'Speed (MPH)':<12} | {'Dry Stop (s)':<12} | {'Wet Stop (s)':<12}")
print("-" * 42)

for s in speeds:
    dry_time = calculate_stop_time(s, 'dry')
    wet_time = calculate_stop_time(s, 'wet')
    print(f"{s:<12} | {dry_time:<12} | {wet_time:<12}")

# Empty line for Pylint compliance