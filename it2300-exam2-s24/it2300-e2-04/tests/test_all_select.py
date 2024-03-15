import ast
import unittest,os

#import asttest
import sql_helper
from bin import co
try:
    os.remove("bin/data.db")
except:
    pass
co.addCSVToDB("bin/ManagersHalf.csv","bin/data.db")
class TestAll_Select(unittest.TestCase):

    def setUp(self):
        pass

    def test_select_all(self):
        conn = sql_helper.create_connection("bin/data.db")
        mylist = sql_helper.run_sqlfile(conn,"exam.sql")
        #print(mylist)
        self.assertTrue(mylist==[[('BLN',), ('BRO',), ('BSN',), ('BAL',), ('BOS',)]],"select statement giving incorrect data")
        pass


if __name__ == "__main__":
    unittest.main()
