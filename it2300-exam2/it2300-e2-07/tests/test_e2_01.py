import ast
import unittest,os

#import asttest
import sql_helper
from bin import co
try:
    os.remove("bin/data.db")
except:
    pass
co.addCSVToDB("bin/HallOfFame.csv","bin/data.db")
class Testsql_e2_01(unittest.TestCase):

    def setUp(self):
        pass

    def test_uses_group_by(self):
        conn = sql_helper.create_connection("bin/data.db")
        mylist = sql_helper.run_sqlfile(conn,"exam.sql")
        #print(mylist)
        self.assertTrue(mylist==[[('Umpire', 10), ('Pioneer/Executive', 41), ('Manager', 74), ('Player', 4066)]],"Your select statement does not have the correct output")
        pass


if __name__ == "__main__":
    unittest.main()
