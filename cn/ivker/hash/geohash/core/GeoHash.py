from cn.ivker.hash.geohash.api.IGeoHash import IGeoHash


class GeoHash(IGeoHash):

    @staticmethod
    def binaryHash(longitude: float, latitude: float, granularity: int) -> list:
        """
        将坐标点按二分法进行hash
        :param longitude: 经度
        :param latitude: 纬度
        :param granularity: 哈希粒度/次数
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
