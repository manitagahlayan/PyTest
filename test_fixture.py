#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 15:06:38 2017

@author: manitagahlayan
"""
import pytest

@pytest.fixture
def i_set_things_up():
    projector = {'status': 'doing fine',
                 'flashing': "dicts can't flash!"}
    return projector

def test_fixture_contents(i_set_things_up):
    assert i_set_things_up['status'] == 'doing fine'
    
        