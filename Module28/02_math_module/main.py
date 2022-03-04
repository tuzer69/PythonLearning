class MyMath:
    __PI = 3.14159265358979323846

    @classmethod
    def circle_len(cls, radius: float) -> float:
                return 2 * MyMath.__PI * radius

    @classmethod
    def circle_square(cls, radius: float) -> float:
        return MyMath.__PI * radius ** 2

    @classmethod
    def cube_v(cls, lenght: float) -> float:
        return (lenght / (2 ** 0.5)) ** 3

    @classmethod
    def sphere_v(cls, radius):
        return 4 * MyMath.__PI * radius ** 2


print(MyMath.circle_len(radius=5))
print(MyMath.circle_square(radius=5))
print(MyMath.cube_v(lenght=5))
print(MyMath.sphere_v(radius=5))
