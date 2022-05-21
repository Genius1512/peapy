import peapy


class ShapeRenderer(peapy.Component):
    RECTANGLE: str = "rectangle"
    CIRCLE: str = "circle"

    def __init__(
        self,
        shape: str,
        color: peapy.Color = peapy.Color(255, 255, 255),
        width: int = None,
        height: int = None,
    ):
        """
        Creates a new ShapeRenderer.

        :param shape: The shape to render. Can be either "rectangle" or "circle".
        :param color: The color of the shape.
        :param width: The width of the shape.
            When set to None, the width will be the same as the GameObject's transform.width.
        :param height: The height of the shape.
            When set to None, the height will be the same as the GameObject's transform.height.
        """

        super().__init__()

        self.shape = shape
        self.color = color

        if shape == self.RECTANGLE:
            self.width = width
            self.height = height
        elif shape == self.CIRCLE:
            self.radius = width

    def init(self):  # Called when the Component is added to a GameObject.
        pass

    def update(self):  # Called every frame.
        pass
