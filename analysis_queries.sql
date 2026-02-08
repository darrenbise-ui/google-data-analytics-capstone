-- Google Capstone Prep: Bike Ride Analysis
-- Purpose: Calculate average ride duration by bike type

SELECT 
    bike_type, 
    AVG(end_time - start_time) AS avg_duration
FROM bike_rides
GROUP BY bike_type;

-- Experimental: Night Shift Analysis (Rides after 8 PM)
SELECT 
    bike_type, 
    COUNT(*) as night_rides
FROM bike_rides
WHERE EXTRACT(HOUR FROM start_time) >= 20
GROUP BY bike_type;