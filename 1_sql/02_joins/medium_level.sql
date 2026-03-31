--🟠 MEDIUM LEVEL
--🔹 Multi-table Joins
--Get movie title, actor name, and release year
select
	m.title as movie_title,
	a.name as actor_name,
	m.release_year as movie_year
from movies m 
join movie_actor ma 
	on ma.movie_id = m.movie_id
join actors a 
	on a.actor_id  = ma.actor_id;


--Find all actors who acted in "Avengers: Endgame"
select 
	a.name
from actors a
join movie_actor ma 
	on ma.actor_id = a.actor_id
join movies m 
	on m.movie_id = ma.movie_id
where m.title = 'Avengers: Endgame';


--List all movies with their language and industry
select
	m.title as movie_title,
	l.name as language ,
	m.industry
from movies m
join languages l 
	on l.language_id = m.language_id;


--🔹 Aggregation with GROUP BY
--Count number of movies per industry
select 
	m.industry,
	count(*)
from movies m 
group by m.industry;

--Find average IMDb rating per industry
select
	m.industry,
	avg(m.imdb_rating) as avg_industry
from movies m 
group by m.industry;

--Count number of movies per language
select
	l.name as language,
	count(*) as total_movies
from movies m
join languages l 
	on l.language_id = m.language_id
group by l.name
order by total_movies desc;

--Get total revenue per currency
select
	f.currency,
	sum(
		case
			when f.unit = 'Billions' then f.revenue * 1000
			when f.unit = 'Thousands' then f.revenue / 1000
			else f.revenue
		end
	) as revenue_in_millions
from financials f
group by f.currency;


--🔹 HAVING Clause
--Get industries having more than 5 movies
select
	m.industry
from movies m
group by m.industry 
having count(*) > 5;

--Find languages with average rating above 8
select
	l.name,
	avg(coalesce(m.imdb_rating, 0)) as avg_rating
from languages l 
join movies m
	on m.language_id=l.language_id
group by l.name
having count(*) > 8;


--🔹 Subqueries
--Find movies with rating higher than average rating
SELECT title
FROM movies m 
WHERE m.imdb_rating > (SELECT AVG(imdb_rating) FROM movies);

--Get actors who acted in movies released after 2015
SELECT * 
FROM actors a 
WHERE a.actor_id IN (
    SELECT ma.actor_id 
    FROM movie_actor ma 
    WHERE ma.movie_id IN (
        SELECT m.movie_id 
        FROM movies m
        WHERE m.release_year > 2015
    )
);

--Alternative using JOIN
SELECT DISTINCT a.*
FROM actors a
JOIN movie_actor ma ON a.actor_id = ma.actor_id
JOIN movies m ON m.movie_id = ma.movie_id
WHERE m.release_year > 2015;


--Find movies with the highest revenue
select * from movies m 
where m.movie_id in (
	select f.movie_id 
	from financials f
	where f.revenue = (
		select max(revenue) from financials
	)
);

--Alternative using JOIN
SELECT m.*, f.revenue
FROM movies m
JOIN financials f ON m.movie_id = f.movie_id
WHERE f.revenue = (
    SELECT MAX(revenue) FROM financials
);


--🔹 Advanced Filtering
--Get movies where revenue is greater than budget
select * from movies m  
where m.movie_id in (
	select f.movie_id from financials f
	where f.revenue > f.budget
);

--Alternative using JOIN
SELECT m.*, f.revenue, f.budget
FROM movies m  
JOIN financials f 
    ON m.movie_id = f.movie_id
WHERE f.revenue > f.budget;

--Find top 5 highest rated movies
select * from movies m
where m.imdb_rating is not null
order by imdb_rating desc
limit 5;

--Alternative using NULLS LAST
SELECT *
FROM movies
ORDER BY imdb_rating desc nulls last
LIMIT 5;

--Get movies with "Marvel Studios" as studio
select * from movies m 
where m.studio = 'Marvel Studios';


--🔹 Many-to-Many (Important 🔥)
--Count number of actors in each movie
SELECT m.title, COUNT(ma.actor_id) AS actor_count
FROM movies m
left JOIN movie_actor ma 
    ON ma.movie_id = m.movie_id
GROUP BY m.title;


--Find movies with more than 2 actors
select m.title, count(*) from movies m
join movie_actor ma 
	on ma.movie_id =m.movie_id
group by m.title
having count(ma.actor_id) > 2;

--Get actors who acted in more than 3 movies
select a.actor_id , a.name from actors a 
join movie_actor ma 
	on ma.actor_id = a.actor_id 
group by a.actor_id , a.name
having count(distinct ma.movie_id) > 3;

--🔹 Data Cleaning / NULL Handling
--Replace NULL studio names with "Unknown"
select 
	case
		when (m.studio = '' or m.studio is null) then 'Unknown'
		else m.studio 
	end
from movies m;
--Find movies where IMDb rating is NULL
select * from movies m
where m.imdb_rating is null;

--Count how many movies have missing ratings
select count(*) as total_movies from movies m
where m.imdb_rating is null;

--🔴 BONUS (INTERVIEW STYLE)
--Find top 3 highest revenue movies
SELECT 
    f.movie_id, 
    m.title,
    CASE
        WHEN f.unit = 'Thousands' THEN f.revenue / 1000
        WHEN f.unit = 'Millions' THEN f.revenue
        WHEN f.unit = 'Billions' THEN f.revenue * 1000
        ELSE 0
    END AS revenue_millions
FROM financials f
JOIN movies m 
    ON m.movie_id = f.movie_id
ORDER BY revenue_millions DESC
LIMIT 3;



--Get second highest IMDb rated movie
select max(m.imdb_rating) from movies m 
where m.imdb_rating is not null and m.imdb_rating < (
select max(ma.imdb_rating) 
from movies ma
 where ma.imdb_rating is not null)
 
SELECT *
FROM (
    SELECT 
        m.*,
        DENSE_RANK() OVER (ORDER BY imdb_rating DESC) AS rank_num
    FROM movies m
    WHERE imdb_rating IS NOT NULL
) t
WHERE rank_num = 2;
--Rank movies based on rating (if window allowed skip)
SELECT *
FROM (
    SELECT 
        m.*,
        DENSE_RANK() OVER (ORDER BY imdb_rating DESC) AS rank_num
    FROM movies m
    WHERE imdb_rating IS NOT NULL
) t;


--Find most frequent actor (acted in most movies)
select a.actor_id, a.name, count(*) as movie_count
from actors a 
join movie_actor ma 
	on ma.actor_id = a.actor_id 
group by a.actor_id, a.name
order by movie_count desc
LIMIT 1;

WITH actor_counts AS (
    SELECT 
        a.actor_id,
        a.name,
        COUNT(ma.movie_id) AS movie_count
    FROM actors a
    JOIN movie_actor ma 
        ON ma.actor_id = a.actor_id
    GROUP BY a.actor_id, a.name
)
SELECT *
FROM actor_counts
WHERE movie_count = (
    SELECT MAX(movie_count) FROM actor_counts
);

select *
from (
	select
		a.actor_id,
		a.name,
		count(ma.movie_id) as movie_count,
		dense_rank() over (order by count(ma.movie_id) desc) as rnk
	from actors a
	join movie_actor ma
		on ma.actor_id = a.actor_id
	group by a.actor_id, a,name
) t
where rnk=1;


--Get movie with highest profit (revenue - budget)
select t.title, (t.ind_curr_revenue - ind_curr_budget) as profit from (select
	*,
	(case
		when f.currency = 'USD' then f.budget *82
		else f.budget  
	end) as ind_curr_budget,
	(case
		when f.currency = 'USD' then f.revenue*82
		else f.revenue 
	end) as ind_curr_revenue
from movies m 
join financials f 
	on f.movie_id = m.movie_id
) t
order by profit desc
limit  1


WITH converted_financials AS (
    SELECT 
        m.title,
        CASE
            WHEN f.currency = 'USD' THEN f.budget * 82
            ELSE f.budget
        END AS budget_in_inr,
        
        CASE
            WHEN f.currency = 'USD' THEN f.revenue * 82
            ELSE f.revenue
        END AS revenue_in_inr
        
    FROM movies m
    JOIN financials f 
        ON f.movie_id = m.movie_id
)

SELECT 
    title,
    (revenue_in_inr - budget_in_inr) AS profit
FROM converted_financials
ORDER BY profit DESC
LIMIT 1;


--Find movies that have no actors assigned
select * 
from movies 
where movie_id not in (
	select ma.movie_id
	from movie_actor ma
	)

SELECT m.*
FROM movies m
LEFT JOIN movie_actor ma 
    ON m.movie_id = ma.movie_id
WHERE ma.movie_id IS NULL;

--Get actors who never acted in any movie
SELECT a.*
FROM actors a
LEFT JOIN movie_actor ma
    ON a.actor_id = ma.actor_id
WHERE ma.actor_id IS NULL;

SELECT *
FROM actors a
WHERE NOT EXISTS (
    SELECT 1
    FROM movie_actor ma
    WHERE ma.actor_id = a.actor_id
);

--Find duplicate movie titles (if any)
SELECT title, COUNT(*) AS count
FROM movies
GROUP BY title
HAVING COUNT(*) > 1;

SELECT *
FROM (
    SELECT 
        m.*,
        COUNT(*) OVER (PARTITION BY title) AS title_count
    FROM movies m
) t
WHERE title_count > 1;

SELECT *
FROM (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY title ORDER BY movie_id) AS rn
    FROM movies
) t
WHERE rn > 1;


