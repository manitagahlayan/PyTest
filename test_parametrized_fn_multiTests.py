#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:16:30 2017

@author: manitagahlayan
"""

import unit_demo
import pytest

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = unit_demo.calc_square(test_input)
    assert result == expected_output