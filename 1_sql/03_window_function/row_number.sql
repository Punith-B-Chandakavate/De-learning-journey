-- Get the top 3 highest-rated movies from each industry.
SELECT *
FROM (
    SELECT 
        title,
        industry,
        ROW_NUMBER() OVER (PARTITION BY industry ORDER BY imdb_rating DESC) AS rn
    FROM movies
) t
WHERE rn <= 3;