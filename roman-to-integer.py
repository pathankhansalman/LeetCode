# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:13:29 2022

@author: patha
"""

class Solution(object):
    def romanToInt(self, num):
        """
        :type num: int
        :rtype: str
        """
        def _int_rom_helper_(arg):
            if arg == '':
                return 0
            if len(arg) == 1:
                return mydict[arg]
            if arg[0] == 'M':
                return 1000 + _int_rom_helper_(arg[1:])
            if arg[0:2] == 'CM':
                return 900 + _int_rom_helper_(arg[2:])
            if arg[0] == 'D':
                return 500 + _int_rom_helper_(arg[1:])
            if arg[0:2] == 'CD':
                return 400 + _int_rom_helper_(arg[2:])
            if arg[0] == 'C':
                return 100 + _int_rom_helper_(arg[1:])
            if arg[0:2] == 'XC':
                return 90 + _int_rom_helper_(arg[2:])
            if arg[0] == 'L':
                return 50 + _int_rom_helper_(arg[1:])
            if arg[0:2] == 'XL':
                return 40 + _int_rom_helper_(arg[2:])
            if arg[0] == 'X':
                return 10 + _int_rom_helper_(arg[1:])
            if arg[0:2] == 'IX':
                return 9 + _int_rom_helper_(arg[2:])
            if arg[0:2] == 'IV':
                return 4 + _int_rom_helper_(arg[2:])
            if arg[0] == 'V':
                return 5 + _int_rom_helper_(arg[1:])
            if arg[0] == 'I':
                return 1 + _int_rom_helper_(arg[1:])
        def _rom_int_helper_(arg):
            if arg == 0:
                return ''
            if arg in mydict.keys():
                return mydict[arg]
            if arg > 1000:
                return 'M' + _rom_int_helper_(arg - 1000)
            if arg >= 900:
                return 'CM' + _rom_int_helper_(arg - 900)
            if arg > 500:
                return 'D' + _rom_int_helper_(arg - 500)
            if arg >= 400:
                return 'CD' + _rom_int_helper_(arg - 400)
            if arg > 100:
                return 'C' + _rom_int_helper_(arg - 100)
            if arg >= 90:
                return 'XC' + _rom_int_helper_(arg - 90)
            if arg > 50:
                return 'L' + _rom_int_helper_(arg - 50)
            if arg >= 40:
                return 'XL' + _rom_int_helper_(arg - 40)
            if arg > 10:
                return 'X' + _rom_int_helper_(arg - 10)
            if arg > 5:
                return 'V' + _rom_int_helper_(arg - 5)
            return 'I'*arg
            
            
        mydict = {1000: 'M',
                  500: 'D',
                  100: 'C',
                  50: 'L',
                  10: 'X',
                  9: 'IX',
                  5: 'V',
                  4: 'IV',
                  1: 'I'}
        mydict = {'M': 1000,
                  'D': 500,
                  'C': 100,
                  'L': 50,
                  'X': 10,
                  'IX': 9,
                  'V': 5,
                  'IV': 4,
                  'I': 1}
        return _int_rom_helper_(num)


if __name__ == '__main__':
    mysol = Solution()
    print(mysol.romanToInt('MCMXCIV'))
