#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:23:32 2017

@author: manitagahlayan
"""

class PythonDB:
    def __init__(self):
        self.connection = Connection()

    def connect(self, connection_string):
        return self.connection

class Connection:
    def __init__(self):
        self.cur = Cursor()

    def cursor(self):
        return self.cur

    def close(self):
        pass

class Cursor():
    def execute(self, query):
        if query == "select id from employee_db where name=John":
            return 123
        elif query == "select id from employee_db where name=Tom":
            return 789
        else:
            return -1

    def close(self):
        pass
