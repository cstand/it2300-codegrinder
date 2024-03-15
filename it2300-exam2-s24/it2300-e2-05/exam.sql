select ReviewDate, 
round((UCAN_ARPU+EMEA_ARPU+LATM_ARPU+APAC_ARPU)/4,2) as 'Total Average Reveue Per User' 
from NetflixRevenue;
