class Vector2D(object):
    i = 0;
    l = 0;
    vec = [];

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.i = 0;
        self.l = len(vec2d);
        for j in range(self.l):
            self.vec.extend(vec2d[j]);
        self.l = len(self.vec);

    def next(self):
        """
        :rtype: int
        """
        self.i = self.i + 1;
        return self.vec[self.i - 1];

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i <= self.l - 1:
            return True;
        else:
            return False;

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())


vec2d = [];
i, v = Vector2D(vec2d), [];
while i.hasNext():
    v.append(i.next());
print(v);