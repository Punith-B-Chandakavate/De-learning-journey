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


--Get actors who acted in movies released after 2015


--Find movies with the highest revenue


--🔹 Advanced Filtering
--Get movies where revenue is greater than budget


--Find top 5 highest rated movies


--Get movies with "Marvel Studios" as studio


--🔹 Many-to-Many (Important 🔥)
--Count number of actors in each movie


--Find movies with more than 2 actors


--Get actors who acted in more than 3 movies


--🔹 Data Cleaning / NULL Handling
--Replace NULL studio names with "Unknown"


--Find movies where IMDb rating is NULL


--Count how many movies have missing ratings


--🔴 BONUS (INTERVIEW STYLE)
--Find top 3 highest revenue movies


--Get second highest IMDb rated movie


--Rank movies based on rating (if window allowed skip)


--Find most frequent actor (acted in most movies)


--Get movie with highest profit (revenue - budget)


--Find movies that have no actors assigned


--Get actors who never acted in any movie


--Find duplicate movie titles (if any)

