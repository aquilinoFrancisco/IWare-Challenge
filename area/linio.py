#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

#Prints all the numbers from 1 to 100. However, for multiples of 3, instead of the number, print "Linio". 
#For multiples of 5 print"IT". For numbers which are multiples of both 3 and 5, print "Linianos".
def linio(n):
    return [(not (n % 5 or n % 3) ) * 'Linianos' or (not n % 3) * 'Linio' or (not n % 5) * 'IT'  or n for n in range(1, 101)]

#**
# * Unit test for simple module.
#**
class TestMyModule(unittest.TestCase):
    
    # Create the test case
    def setUp(self):
	#only numbers
        self.numbers = 100
    
    # Run the test case
    def test(self):
        r = [linio(self.numbers) ]
        #Test that first and second are equal. If the values do not compare equal, the test will fail.
        self.assertEqual(r, [[1, 2, 'Linio', 4, 'IT', 'Linio', 7, 8, 'Linio', 'IT', 11, 'Linio', 13, 14, 'Linianos', 16, 17, 'Linio', 19, 'IT', 'Linio', 22, 23, 'Linio', 'IT', 26, 'Linio', 28, 29, 'Linianos', 31, 32, 'Linio', 34, 'IT', 'Linio', 37, 38, 'Linio', 'IT', 41, 'Linio', 43, 44, 'Linianos', 46, 47, 'Linio', 49, 'IT', 'Linio', 52, 53, 'Linio', 'IT', 56, 'Linio', 58, 59, 'Linianos', 61, 62, 'Linio', 64, 'IT', 'Linio', 67, 68, 'Linio', 'IT', 71, 'Linio', 73, 74, 'Linianos', 76, 77, 'Linio', 79, 'IT', 'Linio', 82, 83, 'Linio', 'IT', 86, 'Linio', 88, 89, 'Linianos', 91, 92, 'Linio', 94, 'IT', 'Linio', 97, 98, 'Linio', 'IT']])
    
    # Method called immediately after the test method has been called and the result recorded.
    def tearDown(self):
        del(self.numbers)

if __name__ == "__main__":
	unittest.main() 
