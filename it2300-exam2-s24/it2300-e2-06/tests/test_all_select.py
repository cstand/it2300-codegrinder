import ast
import unittest,os

#import asttest
import sql_helper
from bin import co
try:
    os.remove("bin/data.db")
except:
    pass
co.addCSVToDB("bin/IMDB_Top100.csv","bin/data.db")
class TestAll_Select(unittest.TestCase):

    def setUp(self):
        pass

    def test_select_all(self):
        conn = sql_helper.create_connection("bin/data.db")
        mylist = sql_helper.run_sqlfile(conn,"exam.sql")
        #print(mylist)
        self.assertTrue(mylist==[[('The Shawsh', 9.3), ('The Godfat', 9.2), ('The Dark K', 9.0), ('The Godfat', 9.0), ('12 Angry M', 9.0), ('The Lord o', 8.9), ('Pulp Ficti', 8.9), ("Schindler'", 8.9), ('Fight Club', 8.8), ('The Lord o', 8.8), ('Forrest Gu', 8.8), ('The Lord o', 8.7), ('Goodfellas', 8.7), ('One Flew O', 8.7), ('Hamilton', 8.6), ('Gisaengchu', 8.6), ('Soorarai P', 8.6), ('Interstell', 8.6), ('Cidade de ', 8.6), ('Saving Pri', 8.6), ('The Green ', 8.6), ('La vita è ', 8.6), ('Se7en', 8.6), ('The Silenc', 8.6), ('Seppuku', 8.6), ('Shichinin ', 8.6), ("It's a Won", 8.6), ('Joker', 8.5), ('Whiplash', 8.5), ('The Intouc', 8.5), ('The Presti', 8.5), ('The Depart', 8.5), ('The Pianis', 8.5), ('Gladiator', 8.5), ('American H', 8.5), ('Léon', 8.5), ('The Lion K', 8.5), ('Nuovo Cine', 8.5), ('Hotaru no ', 8.5), ('Casablanca', 8.5), ('Modern Tim', 8.5), ('City Light', 8.5), ('Capharnaüm', 8.4), ('Ayla: The ', 8.4), ('Vikram Ved', 8.4), ('Kimi no na', 8.4), ('Dangal', 8.4), ('Avengers: ', 8.4), ('Django Unc', 8.4), ('3 Idiots', 8.4), ('Taare Zame', 8.4), ('The Lives ', 8.4), ('Oldeuboi', 8.4), ('Once Upon ', 8.4), ('The Shinin', 8.4), ('Apocalypse', 8.4), ('Anand', 8.4), ('Tengoku to', 8.4), ('Witness fo', 8.4), ('Paths of G', 8.4), ('Sunset Blv', 8.4), ('The Great ', 8.4), ('1917', 8.3), ('Tumbbad', 8.3), ('Andhadhun', 8.3), ('Drishyam', 8.3), ('Jagten', 8.3), ('Jodaeiye N', 8.3), ('Incendies', 8.3), ('Miracle in', 8.3), ('Babam ve O', 8.3), ('Inglouriou', 8.3), ('Eternal Su', 8.3), ('Requiem fo', 8.3)]],"select statement giving incorrect data")
        pass


if __name__ == "__main__":
    unittest.main()
