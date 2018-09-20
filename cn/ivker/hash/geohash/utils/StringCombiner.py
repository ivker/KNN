class StringCombiner:

    @staticmethod
    def cross(s1: str, s2: str) -> str:
        """
        将两个字符串以交叉的方式进行合并
        """
        l1 = len(s1)
        l2 = len(s2)
        lager = max(l1, l2)
        res = ""
        for idx in range(lager):
            if idx < l1:
                res += s1[idx]
            else:
                res += s2[idx::]
                return res
            if idx < l2:
                res += s2[idx]
            else:
                res += s1[idx::]
                return res
        return res

    @staticmethod
    def extract2(s: str) -> list:
        """
        将字符串交叉提取为两个字符串
        :param s:
        :return:
        """
        return [s[0::2], s[1::2]]
