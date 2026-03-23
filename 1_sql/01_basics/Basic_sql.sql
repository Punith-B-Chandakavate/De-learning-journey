--🟢 EASY LEVEL
--🔹 Basic SELECT
--Get all movies with their titles and release year
select title, release_year from movies;

--Show all actors with their birth year
select name, birth_year from actors;

--Display all movies from Bollywood industry
select * from movies m 
where m.industry = 'Bollywood';

--Get all movies released after 2015
select * from movies
where release_year > 2015;

--Show movies with IMDb rating greater than 8
select * from movies
where imdb_rating > 8;

--List all languages available in the database
select * from languages;

--🔹 Filtering
--Get movies where studio is NULL
select * from movies
where studio is null or studio = '';

--Find actors born after 1980
select * from actors
where birth_year > 1980;

--Show movies with rating between 7 and 9
select * from movies
where imdb_rating between 7 and 9;

--Get all Hollywood movies released before 2000
select * from movies
where industry = 'Hollywood' and release_year < 2000;


--🔹 Sorting
--List movies sorted by IMDb rating (highest first)
select *from movies
order by imdb_rating desc;

--Show actors sorted by birth year (oldest first)
select * from actors
order by birth_year;

--🔹 Aggregation Basics
--Count total number of movies
select count(*) from movies;

--Find average IMDb rating of all movies
select avg(imdb_rating) as avg_rating from movies;

--Get maximum and minimum movie ratings
select 
	max(imdb_rating) as max_rating,
	min(imdb_rating) as min_rating
from movies;
