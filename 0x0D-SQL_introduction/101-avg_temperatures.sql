-- calculate average temperature from the city.
SELECT city, AVG(temperature) AS avg_temperature
FROM weather
GROUP BY city
ORDER BY avg_temperature DESC;
