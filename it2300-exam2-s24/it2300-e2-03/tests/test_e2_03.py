import ast
import unittest,os

#import asttest
import sql_helper
from bin import co
try:
    os.remove("bin/data.db")
except:
    pass
co.addCSVToDB("bin/TeamsHalf.csv","bin/data.db")
class TestAll_Select(unittest.TestCase):

    def setUp(self):
        pass

    def test_sql_statement(self):
        conn = sql_helper.create_connection("bin/data.db")
        mylist = sql_helper.run_sqlfile(conn,"exam.sql")
        #print(mylist)
        self.assertTrue(mylist==[[('HOU', 'W'), ('KCA', 'W'), ('LAN', 'W'), ('OAK', 'W'), ('CIN', 'W'), ('CIN', 'W'), ('OAK', 'W'), ('TEX', 'W'), ('CHA', 'W'), ('HOU', 'W'), ('SFN', 'W'), ('TEX', 'W'), ('ATL', 'W'), ('CAL', 'W'), ('LAN', 'W'), ('MIN', 'W'), ('ATL', 'W'), ('KCA', 'W'), ('SEA', 'W'), ('SFN', 'W'), ('CAL', 'W'), ('CHA', 'W'), ('SDN', 'W'), ('SDN', 'W'), ('SEA', 'W'), ('MIN', 'W')]],"select statement giving incorrect data")
        pass


if __name__ == "__main__":
    unittest.main()
