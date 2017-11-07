select Weather.id as 'Id'
from Weather join Weather w
	on datediff(Weather.date, w.date) = 1
	and Weather.temperature > w.temperature;
