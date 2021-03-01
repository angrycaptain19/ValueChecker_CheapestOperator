# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:02:05 2021

@author: Shardul Kulkarni
"""
import os
from main import *
import unittest


class test_cheapest_operator_utility(unittest.TestCase):
    
    def test_1(self):
        path = os.getcwd() +'\\Data\\' 
        self.assertEqual(cheapest_operator_utility.find_cheapest_operator('222923654234',path), 'operator_15')  

    def test_2(self):
        path = os.getcwd() +'\\Dat\\' 
        self.assertEqual(cheapest_operator_utility.find_cheapest_operator('222923654234',path), 'Invalid Path')  
        
    def test_3(self):
        path = os.getcwd() +'\\Data\\' 
        self.assertEqual(cheapest_operator_utility.find_cheapest_operator('+46727602584',path), 'Invalid Phone Number')

    def test_4(self):
        path = os.getcwd() +'\\Data\\' 
        self.assertEqual(cheapest_operator_utility.find_cheapest_operator('46727602584as',path), 'Invalid Phone Number')
        
    def test_5(self):
        path = os.getcwd() +'\\Data\\' 
        self.assertEqual(cheapest_operator_utility.find_cheapest_operator('123456789',path), 'Invalid Phone Number')
        
    def test_6(self):
        path = os.getcwd() +'\\Test Data 1\\'
        self.assertEqual(cheapest_operator_utility.find_cheapest_operator('222923654234',path), 'No files found')
           
    def test_7(self):
        path = os.getcwd() +'\\Test Data 2\\' 
        self.assertEqual(cheapest_operator_utility.find_cheapest_operator('222923654234',path), 'All files are invalid')
        
    def test_8(self):
        path = os.getcwd() +'\\Data\\' 
        self.assertEqual(cheapest_operator_utility.find_cheapest_operator('000234324890',path), 'No operators available')
    

if __name__ == '__main__':
    unittest.main()
