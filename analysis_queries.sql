-- Google Capstone Prep: Bike Ride Analysis
-- Purpose: Calculate average ride duration by bike type

SELECT 
    bike_type, 
    AVG(end_time - start_time) AS avg_duration
FROM bike_rides
GROUP BY bike_type;

-- Refactored for Intel Mac Performance & Stakeholder Clarity
WITH base_counts AS (
    SELECT 
        bike_type,
        COUNT(*) AS total_rides,
        -- Using a CASE statement inside a COUNT is faster than two separate CTEs
        COUNT(*) FILTER (WHERE EXTRACT(HOUR FROM start_time) >= 20) AS night_rides
    FROM bike_rides
    GROUP BY bike_type
)
SELECT 
    bike_type,
    night_rides,
    total_rides,
    -- Calculate the percentage only once at the very end
    CASE 
        WHEN total_rides > 0 THEN ROUND(100.0 * night_rides / total_rides, 2)
        ELSE 0 
    END AS night_shift_pct
FROM base_counts
ORDER BY night_shift_pct DESC;