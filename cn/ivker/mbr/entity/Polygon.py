from cn.ivker.mbr.entity.Point import Point


class Polygon:
    """
    多边形对象,由若干有序连接的点组成
    """

    def __init__(self, ps: list):
        if len(ps) < 3:
            raise ValueError("polygon at least include 3 points")
        self.points = ps
