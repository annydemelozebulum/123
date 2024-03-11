
class Point:

    def __init__(self, x, y):
        """
    Init methos that initializes the point with x and y
        :param x: X coordinate value
        :param y:  Y coordinate value

        """

        self.x = x
        self.y = y

A = Point(2, 3)

print(A.x)
print(A.y)

B = Point(7, 9)
print(B.x)
print(B.y)