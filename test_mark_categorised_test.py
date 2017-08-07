#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 16:30:41 2017

@author: manitagahlayan
"""

import pytest


@pytest.mark.windows
def test_windows_1():
    assert True
    
@pytest.mark.windows    
def test_windows_2():
    assert True
    
@pytest.mark.mac   
def test_mac_1():
    assert True
    
@pytest.mark.mac 
def test_mac_2():
    assert True