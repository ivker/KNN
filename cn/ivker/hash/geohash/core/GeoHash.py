from cn.ivker.hash.geohash.api.IGeoHash import IGeoHash


class GeoHash(IGeoHash):

    @staticmethod
    def coordinateBinaryHash(longitude: float, latitude: float, granularity: int) -> list:
        """
        将坐标点按二分法进行hash
        :param longitude: 经度
        :param latitude: 纬度
        :param granularity: 哈希粒度/分层次数
        :return: [latitude,longitude]
        """

        # 坐标编码结果
        loh = ""
        lah = ""

        # 经纬度范围
        loLeft = -180
        loRight = 180

        laLeft = -90
        laRight = 90

        # 二分hash
        for t in range(granularity):
            loMid = (loLeft + loRight) / 2
            if longitude < loMid:
                loh += '0'
                loRight = loMid
            else:
                loh += '1'
                loLeft = loMid

            laMid = (laLeft + laRight) / 2
            if latitude < laMid:
                lah += '0'
                laRight = laMid
            else:
                lah += '1'
                laLeft = laMid

        return [loh, lah]

    @staticmethod
    def binaryHashCoordinate(longitude: str, latitude: str, granularity: int) -> list:
        """
        将二进制编码根据编码粒度(分层次数)转译为矩形区域
        :param longitude: 经度
        :param latitude: 纬度
        :param granularity: 哈希粒度/分层次数
        :return:
        """

        # 经纬度粒度误差
        gr = pow(2, granularity)
        loDiff = 360 / (gr + 1)
        laDiff = 180 / (gr + 1)

        # 经纬度坐标
        lo = -180
        la = -90

        # 查找定位编码
        count = 0
        mul = 1
        for i in reversed(longitude):
            count += int(i) * mul
            mul *= 2
        lo += count * loDiff

        count = 0
        mul = 1
        for i in reversed(latitude):
            count += int(i) * mul
            mul *= 2
        la += count * laDiff

        return [lo, la, 360 / (gr + 1), 180 / (gr + 1)]
