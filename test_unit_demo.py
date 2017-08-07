# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Created on Sat Jul 29 15:33:26 2017
@author: manitagahlayan
"""
import unit_demo


def test_total():
    total = unit_demo.calc_total(4,6)
    assert total ==10

    
def test_square():
    square = unit_demo.calc_square(4)
    assert square == 16
    

def test_concatString():
    finalString = unit_demo.concatString("Python","Test")
    assert finalString.startswith("Py")
    assert finalString.endswith("Test")


    
