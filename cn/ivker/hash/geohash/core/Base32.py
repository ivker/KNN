from functools import reduce

import numpy as np

valueMappingCode = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                    9: '9', 10: 'b', 11: 'c', 12: 'd', 13: 'e', 14: 'f', 15: 'g', 16: 'h',
                    17: 'j', 18: 'k', 19: 'm', 20: 'n', 21: 'p', 22: 'q', 23: 'r', 24: 's',
                    25: 't', 26: 'u', 27: 'v', 28: 'w', 29: 'x', 30: 'y', 31: 'z'}

codeMappingValue = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, ' 5': 5, '6': 6, '7': 7, '8': 8,
                    '9': 9, 'b': 10, 'c': 11, 'd': 12, 'e': 13, 'f': 14, 'g': 15, 'h': 16,
                    'j': 17, 'k': 18, 'm': 19, 'n': 20, 'p': 21, 'q': 22, 'r': 23, 's': 24,
                    't': 25, 'u': 26, 'v': 27, 'w': 28, 'x': 29, 'y': 30, 'z': 31}


class Base32:
    """
    将2进制数据转为32进制数据(用于传输和存储)
    """

    @staticmethod
    def binaryStringToBase32(s: str) -> str:
        """
        将一个二进制字符串进行每五位编码,字符串长度非五位倍数时,默认为零凑整
        :param s:
        :return:
        """
        size = int(np.ceil(len(s) / 5))
        s = s.zfill(size * 5)
        coded = list(map(lambda start: Base32.binaryToBase32(s[start * 5:start * 5 + 5]), range(size)))
        return reduce(lambda x, y: x + y, coded)

    @staticmethod
    def binaryToBase32(s: str) -> str:
        r = 0
        m = 1
        for c in reversed(s):
            if c != '0' and c != '1':
                raise ValueError("'" + s + "' isn't not binary str")
            r += int(c) * m
            m *= 2
        return valueMappingCode[r]

    @staticmethod
    def base32ToBinaryString(coded: str) -> str:
        """
        
        :param coded: 
        :return: 
        """
        res = ""
        for c in coded:
            v = codeMappingValue[c]
            tmp = ""
            while v > 0:
                tmp = str(v & 1) + tmp
                v = v >> 1
            res += tmp.zfill(5)
        return res
