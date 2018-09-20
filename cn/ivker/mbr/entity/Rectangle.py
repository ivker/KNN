from cn.ivker.mbr.entity.Point import Point


class Rectangle:
    """
    矩形对象,由四个点(以相对位置具化描述)组成
    """

    def __init__(self, lt: Point, lb: Point, rt: Point, rb: Point):
        self.LeftTop = lt  # type:Point
        self.LeftBottom = lb  # type:Point
        self.RightTop = rt  # type:Point
        self.RightBottom = rb  # type:Point
