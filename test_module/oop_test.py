class Robot:
    def __init__(self, x, y):
        self.x = x
        self._y = y


def foo():
    pass


if __name__ == "__main__":
    a = Robot(3, 4)
    print(a.__dict__)
    print(a.y)

