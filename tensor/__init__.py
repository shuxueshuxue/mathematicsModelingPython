class Space:
    def __init__(self, dimension=1):
        self.dimension = dimension

    def __str__(self):
        print(f"R^{self.dimension}")

    @staticmethod
    def R(dimension=1):
        return Space(dimension=dimension)


class Tensor:
    def __init__(self, *args):
        self.space = Space.R(1)
        for arg in args:
            if isinstance(arg, Space):
                self.space = arg
                