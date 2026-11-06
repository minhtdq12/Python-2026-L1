import numpy as np


class Student:
    def __init__(self, s_id, name, dob):
        self._id = s_id
        self._name = name
        self._dob = dob
        self._gpa = 0.0

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def dob(self):
        return self._dob

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        self._gpa = value