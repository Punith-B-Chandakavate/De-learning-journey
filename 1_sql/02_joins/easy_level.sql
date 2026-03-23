
--🟡 EASY LEVEL (JOINS START)
--🔹 Inner Join
--Get movie titles with their budget and revenue
select 
	m.title, f.budget, f.revenue 
from movies m
join financials f
	on m.movie_id = f.movie_id;

--Show all movies with their language name
select 
	m.title, l.name as language
from movies m
join languages l
	on m.language_id  = l.language_id;


--Get movie titles along with actors (movie + actor names)
select
	m.title, a.name as "actor names"
from movies m
join movie_actor ma
	on ma.movie_id = m.movie_id
join actors a 
	on a.actor_id = ma.actor_id;

--🔹 Left Join
--Get all movies and their financial data (include missing financials)
select 
	m.movie_id,
	m.title,
	f.budget,
	f.revenue,
	f.currency,
	f.unit
from movies m
left join financials f
	on m.movie_id = f.movie_id;


--Show all movies with language names (even if language is missing)
select m.*, l.name from movies m
left join languages l
	on m.language_id  = l.language_id;

--🔹 Right Join
--Get all financial records with movie titles (include missing movies)
select 
	f.movie_id,
	m.title,
	f.budget,
	f.revenue,
	f.currency,
	f.unit
from movies m
right join financials f
	on f.movie_id = m.movie_id;
