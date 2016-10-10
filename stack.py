class Stack(object):
    def __init__(self):
        self.container = []

    def isEmpty(self):
        return len(self.container) == 0

    def top(self):
        if not self.isEmpty():
            return self.container[-1]
        return None

    def pop(self):
        top_elt = self.top()
        if not self.isEmpty():
            return self.container.pop()
        return top_elt

    def push(self, elt):
        self.container.append(elt)

    def getSize(self):
        return len(self.container)
