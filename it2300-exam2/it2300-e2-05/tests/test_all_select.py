import ast
import unittest,os

#import asttest
import sql_helper
from bin import co
try:
    os.remove("bin/data.db")
except:
    pass
co.addCSVToDB("bin/NetflixRevenue.csv","bin/data.db")
class TestAll_Select(unittest.TestCase):

    def setUp(self):
        pass

    def test_select_all(self):
        conn = sql_helper.create_connection("bin/data.db")
        mylist = sql_helper.run_sqlfile(conn,"exam.sql")
        print(mylist)
        #self.assertTrue(mylist==[[('31-03-2019', 9.72), ('30-06-2019', 10.02), ('30-09-2019', 10.35), ('31-12-2019', 10.25), ('31-03-2020', 10.12), ('30-06-2020', 10.04), ('30-09-2020', 10.19), ('31-12-2020', 10.25), ('31-03-2021', 10.73), ('30-06-2021', 10.86), ('30-09-2021', 10.95), ('31-12-2021', 10.96), ('31-03-2022', 11.01), ('30-06-2022', 11.16), ('30-09-2022', 11.03), ('31-12-2022', 10.66), ('31-03-2023', 10.93)]],"select statement giving incorrect data")
        pass


if __name__ == "__main__":
    unittest.main()
