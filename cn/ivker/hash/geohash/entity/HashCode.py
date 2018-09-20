class HashCode:
    """
    (非精确)编码结果,
    """

    def __init__(self, x: float, y: float):
        """
        
        :param x:
        :param y:
        """

        self.geohashCode = ""
        self.LeftTop = lt  # type:Point
        self.LeftBottom = lb  # type:Point
        self.RightTop = rt  # type:Point
        self.RightBottom = rb  # type:Point
