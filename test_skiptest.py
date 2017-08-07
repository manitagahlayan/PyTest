#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:33:26 2017

@author: manitagahlayan
"""
import pytest
import unit_demo
import sys

@pytest.mark.skip(reason="not required")
def test_diff():
    diff = unit_demo.calc_total(6,4)
    assert diff ==2
    
@pytest.mark.skipif(sys.version_info > (3,5), reason=" skip if version is higher")
def test_strLength():
    length = unit_demo.getStrLength("Python")
    assert length == 6
