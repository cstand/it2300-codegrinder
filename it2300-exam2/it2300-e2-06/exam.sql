select substr(Series_Title,1,10) as 'Short Title', IMDB_Rating as 'Drama IMDB Rating' from IMDB_Top100 where Genre like '%Drama%';