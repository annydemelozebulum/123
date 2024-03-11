import random

class Point:

    def __init__(self, x, y):
        """
    Init methos that initializes the point with x and y
        :param x: X coordinate value
        :param y:  Y coordinate value

        """

        self.x = x
        self.y = y

    def __str__(self):
        """
        How to print this point
        :return:
        """
        return f"<{self.x}, {self.y}>"


    def __repr__(self):
        """
        How to print if in a list?
        :return:
        """
        return self.__str__()

    def distance_orig(self):
        """""
        Return the distance from origin of the point instance
        :return:
        
        """""
        return(self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        How to compare 2 points? We define it here!
        :param other:
        :return:
        """
        my_size = self.distance_orig()
        their_size = other.distance_orig()
        return my_size > their_size

    def __eq__(self, other):
        """"
        How to compare with
        :param other: the other point instance
        :return
        """
        return self.distance_orig() == other.distance_orig()


if __name__ == "__main__":
    a = Point(2, 3)

    print(a.x)
    print(a.y)

    b = Point(7, 9)
    print(b.x)
    print(b.y)

    # Exercise
    points = []
    for i in range(5):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        points.append(Point(x, y))

    #for _ in range(5):
     #   points.append(Point(random.randint(0, 100), random.randint(0, 100)))

    for point in points:
        print(points) #here it calls point.___ str

    print(points) ##here it iterates and calls point.____rtr

    a = Point(3, 4)
    b = Point(12, 5)
    c = Point(5, 12)
    print(a.distance_orig(), b.distance_orig())
    print( a > b) #Just need to define how ____gt works!
    # a > b this is the magic, this translates to: a____gt___(b)


    print (b < a)
    print(b == c)

    points.sort()
    print(f"the biggest point is:{points[-1]} and the smallest point is: {points[0]}")





