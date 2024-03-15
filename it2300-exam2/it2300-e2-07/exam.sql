select category as 'Category', count(category) as 'Count by Category' 
from HallOfFame 
group by category
order by count(category);
