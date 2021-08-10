class Window:
    h: int = None
    w: int = None
    size: tuple = None
    name: str = None

    def __init__(self, h: int = 300, w: int = 300, name: str = "Default Window"):
        self.size = (h, w)
        self.name = name

