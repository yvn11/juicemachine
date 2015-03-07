#!/usr/bin/env python
#
# checker.py
# Restrictions on data fields
#
# Author: Yun Li <Yun_Li1@DellTeam.com>
#
#
from basic import *
   
class Checker(property):
    """
    Schema related restrictions

    @ilen   length of one item, 0 for unlimited
    @nr     number of items, 0 for unlimited 
    @tlen   total length of a fields, 0 for unlimited
    """
    _value = None
    __ilen = 0
    __nr   = 0
    __tlen = __ilen * __nr

    @property
    def ilen(self): return self.__ilen

    @ilen.setter
    def ilen(self, entry):
        self.__ilen = entry
        self.tlen = self.ilen * self.nr

    @property
    def nr(self): return self.__nr

    @nr.setter
    def nr(self, entry):
        self.__nr = entry
        self.tlen = self.ilen * self.nr

    @property
    def tlen(self): return self.__tlen

    @tlen.setter
    def tlen(self, entry):
        self.__tlen = entry

    def __init__(self, func):

        pass

    def __get__(self, obj, cls):

        return self._value

    def __set__(self, obj, entry):

        self._value = entry

#    def __setattr__(self, name, entry):
#
#        property.__setattr__(self, name, entry)
#
#        if name in ['ilen', 'nr']:
#            self.tlen = self.ilen * self.nr

class list_chk(Checker):

    _value = []

    def __set__(self, obj, entry):

        if not isinstance(entry, list):
            raise TypeError('list type required')

        if self.tlen > 0 and len(entry) > self.tlen:
            raise ValueError('too much items')

        self._value = entry

class string_chk(Checker):

    _value = str()

    def __set__(self, obj, entry):

        if not isinstance(entry, str):
            raise TypeError('string type required')

        if self.tlen > 0 and len(entry) > self.tlen:
            raise ValueError('value length exceed')

        self._value = entry

class integer_chk(Checker):

    _value = int()

    def __set__(self, obj, entry):

        if not isinstance(entry, int):
            raise TypeError('integer type required')

        self._value = entry

class boolean_chk(Checker):

    _value = bool()

    def __set__(self, obj, entry):

        if not isinstance(entry, bool):
            raise TypeError('boolean value required')

        self._value = entry

class map_chk(Checker):

    _value = {}

    def __set__(self, obj, entry):

        if not isinstance(entry, dict):
            raise TypeError('list required')

        self._value = entry

class list_of_string_chk(list_chk):

    def __set__(self, obj, entry):

        if not isinstance(entry, list):
            raise TypeError('list of string required')

        for e in entry:
            if not isinstance(e, str):
                raise TypeError('list of string required')

        self._value = entry