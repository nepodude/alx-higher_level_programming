--  didsplays top 3 hot cities by temperature. during July and August.
SELECT city, temperature, date
FROM weather
WHERE MONTH(date) IN (7, 8)
ORDER BY temperature DESC
LIMIT 3;
