from cn.ivker.mbr.entity.Point import Point
from cn.ivker.mbr.entity.Polygon import Polygon
from cn.ivker.mbr.entity.Rectangle import Rectangle


class MBR:

    @staticmethod
    def mbr(polygon: Polygon) -> Rectangle:
        """
        输入一个规则的多边形,返回其最小外接矩形
        :param polygon:
        :return:
        """
        p0 = polygon.points[0]
        left = p0.x
        right = p0.x
        top = p0.y
        bottom = p0.y

        for p in polygon.points[1::]:
            if p.x < left:
                left = p.x
            if p.x > right:
                right = p.x
            if p.y > top:
                top = p.y
            if p.y < bottom:
                bottom = p.y

        return Rectangle(Point(left, top), Point(left, bottom),
                         Point(right, top), Point(right, bottom))
