--- Module: Join More Than Two Tables
-- Show comma separated actor names for each movie 
	-- Note: group_concat is a MySQL function.or 
		SELECT 
				m.title, group_concat(name separator " | ") as actors
		FROM movies m
		JOIN movie_actor ma ON m.movie_id=ma.movie_id
		JOIN actors a ON a.actor_id=ma.actor_id
		GROUP BY m.movie_id;

	-- PostgreSQL, you can use string_agg or Array_agg + Array_to_string.
		SELECT 
				m.title, string_agg(name, ' | ') as actors
		FROM movies m
		JOIN movie_actor ma ON m.movie_id=ma.movie_id
		JOIN actors a ON a.actor_id=ma.actor_id
		GROUP BY m.movie_id;

		SELECT 
				m.title, array_to_string(array_agg(name), ' | ') as actors
		FROM movies m
		JOIN movie_actor ma ON m.movie_id=ma.movie_id
		JOIN actors a ON a.actor_id=ma.actor_id
		GROUP BY m.movie_id;


-- Print actor name and all the movies they are part of
	SELECT 
            a.name, GROUP_CONCAT(m.title SEPARATOR ' | ') as movies
	FROM actors a
	JOIN movie_actor ma ON a.actor_id=ma.actor_id
	JOIN movies m ON ma.movie_id=m.movie_id
	GROUP BY a.actor_id;

-- Print actor name and how many movies they acted in
	SELECT 
            a.name, 
            GROUP_CONCAT(m.title SEPARATOR ' | ') as movies,
            COUNT(m.title) as num_movies
	FROM actors a
	JOIN movie_actor ma ON a.actor_id=ma.actor_id
	JOIN movies m ON ma.movie_id=m.movie_id
	GROUP BY a.actor_id
	ORDER BY num_movies DESC;

--- Generate a report of all Hindi movies sorted by their revenue amount in millions. Print movie name, revenue, currency, and unit
select
	m.title, 
	f.revenue,
	f.currency,
	f.unit,
	round(
		case
			when unit='Billions' then f.revenue*1000
			when unit='Thousands' then f.revenue / 1000
			else f.revenue 
		end::numeric, 1
	) as revenue_in_millions
from movies m
join financials f
	on f.movie_id = m.movie_id
join languages l 
	on l.language_id = m.language_id 
where l."name" = 'Hindi'
order by revenue_in_millions desc;

--- Select all the movies with minimum and maximum release_year. Note that there can be more than one movie in min and a max year hence output rows can be more than 2

SELECT title, release_year
FROM movies
WHERE release_year in (
		(SELECT MIN(release_year) FROM movies), 
		(SELECT MAX(release_year) FROM movies)
	);

--- Select all the rows from the movies table whose imdb_rating is higher than the average rating
SELECT *
FROM movies
WHERE imdb_rating > (SELECT AVG(imdb_rating) FROM movies);


--- CTE with Subquery
-- Get all actors whose age is between 70 and 80
-- Type 1
WITH actors_age AS (
	SELECT
		name AS actor_name,
		EXTRACT(YEAR FROM CURRENT_DATE) - birth_year AS age
	FROM actors
)
------------------
-- Type 2
WITH actors_age (actor_name, age) AS (
	SELECT
		name,
		EXTRACT(YEAR FROM CURRENT_DATE) - birth_year
	FROM actors
)

SELECT actor_name, age
FROM actors_age
WHERE age > 70 AND age < 80;

--- movies that produced 500% or more profit and their rating was less than avge rating for all movies
WITH avg_rating AS (
    SELECT AVG(imdb_rating) AS avg_imdb
    FROM movies
),
movies_profit_pct AS (
    SELECT
        movie_id,
        ((revenue - budget) * 100.0 / budget) AS profit_pct
    FROM financials
),
avg_imdb_rating AS (
    SELECT
        movie_id,
        title,
        imdb_rating
    FROM movies
    WHERE imdb_rating < (
        SELECT avg_imdb
        FROM avg_rating
    )
)
SELECT
    x.movie_id,
    x.profit_pct,
    y.title,
    y.imdb_rating
FROM movies_profit_pct x
JOIN avg_imdb_rating y
    ON x.movie_id = y.movie_id
WHERE x.profit_pct >= 500;


--- Select all Hollywood movies released after the year 2000 that made more than 500 million $ profit or more profit.
--- Note that all Hollywood movies have millions as a unit hence you don't need to do the unit conversion. 
--- Also, you can write this query without CTE as well but you should try to write this using CTE only
--- without CTE
SELECT
	f.movie_id,
	m.title,
	f.unit,
	f.budget,
	f.revenue,
	(f.revenue - f.budget) AS profit,
	ROUND(
		((f.revenue - f.budget) * 100.0 / f.budget)::numeric,
		2
	) AS profit_pct
FROM financials f
JOIN movies m
	ON m.movie_id = f.movie_id
WHERE m.industry = 'Hollywood'
  AND m.release_year > 2000
  AND (f.revenue - f.budget) >= 500;

-- Using CTE
WITH movie_profit AS (
	SELECT
		movie_id,
		unit,
		revenue,
		budget,
		(revenue - budget) AS profit,
		ROUND(
			((revenue - budget) * 100.0 / budget)::numeric,
			2
		) AS profit_pct
	FROM financials
),
hollywood_movies AS (
	SELECT 
		m.movie_id,
		title
	FROM movies m 
	WHERE m.industry = 'Hollywood'
	  AND m.release_year > 2000
)
SELECT 
	mp.movie_id,
	hm.title,
	mp.unit,
	mp.budget,
	mp.revenue,
	mp.profit,
	mp.profit_pct 
FROM movie_profit mp
JOIN hollywood_movies hm
	ON mp.movie_id = hm.movie_id
WHERE mp.profit >= 500;
