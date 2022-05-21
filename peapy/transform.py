import peapy


class Transform(peapy.Component):
    def __init__(
        self, x: float, y: float, width: float, height: float, angle: float = 0
    ):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle

    @property
    def top_left(self) -> (float, float):
        return self.x, self.y

    @property
    def top_right(self) -> (float, float):
        return self.x + self.width, self.y

    @property
    def bottom_left(self) -> (float, float):
        return self.x, self.y + self.height

    @property
    def bottom_right(self) -> (float, float):
        return self.x + self.width, self.y + self.height
