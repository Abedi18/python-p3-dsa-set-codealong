class MySet:

    def __init__(self, initial_set=None):
        self.dictionary = {}
        if initial_set is not None:
            for item in initial_set:
                self.dictionary[item] = True

    def add(self, item):
        self.dictionary[item] = True

    def delete(self, item):
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        return item in self.dictionary

    def size(self):
        return len(self.dictionary)



    