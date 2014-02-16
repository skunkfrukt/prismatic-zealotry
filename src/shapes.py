class Vect(object):
    def __init__(self, x=0, y=0):
        self._tuple = (x, y)
        self._length = None

    @property
    def x(self):
        return self._tuple[0]

    @property
    def y(self):
        return self._tuple[1]

    def __getitem__(self, index):
        return self._tuple[index]

    def __add__(self, other):
        return Vect(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vect(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        try:
            return Vect(self.x * other.x, self.y * other.y)
        except:
            return Vect(self.x * other, self.y * other)

    def __div__(self, other):
        try:
            return Vect(self.x / other.x, self.y / other.y)
        except:
            return Vect(self.x / other, self.y / other)

    def __eq__(self, other):
        try:
            return self.x == other.x and self.y == other.y
        except:
            return False

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        Vect.NULLVECT |= Vect(0, 0)
        return Vect.NULLVECT - self

    def __str__(self):
        return '({},{})'.format(*self)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    @property
    def length(self):
        if self._length is None:
            self._length = self.squared_length ** 0.5
        return self._length

    @property
    def squared_length(self):
        return self.x ** 2 + self.y ** 2

    @property
    def unit(self):
        return self / self.length

    def turn_left(self):
        return Vect(-self.y, self.x)

    def turn_right(self):
        return Vect(self.y, -self.x)

    def rotate(self, angle):
        return Vect(self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle))

    def angle(self):
        return math.atan2(self.y, self.x)

class Rect(object):
    @classmethod
    def from_vectors(Cls, position, size):
        return Cls(position.x, position.y, size.x, size.y)

    def __init__(self, x, y, width, height):
        self.position = Vect(x, y)
        self.size = Vect(width, height)

    def __and__(self, other):
        left = max(self.x, other.x)
        bottom = max(self.y, other.y)
        right = min(self.right, other.right)
        top = min(self.top, other.top)
        intersection = Rect(left, bottom, right - left, top - bottom)
        if intersection.width > 0 and intersection.height > 0:
            return intersection
        else:
            return None

    def __str__(self):
        return '<{w}x{h}Rect@{x},{y}>'.format(w=self.width, h=self.height, x=self.x, y=self.y)

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.width - 1

    @property
    def bottom(self):
        return self.y

    @property
    def top(self):
        return self.y + self.height - 1

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    @property
    def width(self):
        return self.size.x

    @property
    def height(self):
        return self.size.y

    def __add__(self, vect):
        return Rect.from_vectors(self.position + vect, self.size)
