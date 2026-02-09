"""
Stromer 2019 E-Bike: Multi-Variable Commute Analysis
Comparing Flat (Alameda) vs. Hilly (SF) performance.
"""

def analyze_commute(speed_mph, terrain='flat'):
    # --- Braking Physics ---
    friction = 0.7  # Dry road
    speed_mps = speed_mph * 0.44704
    stop_time = round(speed_mps / (friction * 9.81), 2)
    
    # --- Battery Physics (Est. Wh/mi) ---
    # Base consumption + aerodynamic drag increase
    base_wh_mi = 12 + (0.03 * (speed_mph**2))
    
    # Terrain Multiplier
    multiplier = 1.0 if terrain == 'flat' else 2.5
    final_wh_mi = round(base_wh_mi * multiplier, 1)
    
    return stop_time, final_wh_mi

speeds = [15, 20, 28]

print(f"{'Speed (MPH)':<12} | {'Stop Time (s)':<15} | {'Wh/mi (Flat)':<15} | {'Wh/mi (Hilly)':<15}")
print("-" * 65)

for s in speeds:
    stop_t, wh_flat = analyze_commute(s, 'flat')
    _, wh_hill = analyze_commute(s, 'hilly')
    print(f"{s:<12} | {stop_t:<15} | {wh_flat:<15} | {wh_hill:<15}")

# Note: Your Stromer Battery is approx 983Wh. 
# Total Range = 983 / Wh_mi
