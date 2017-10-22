class compare(object):
    def __init__(self, other):
        self.other = other

    def __or__(self, compare1):
        if isinstance(compare1, compare):
            if self.other == compare1.other:
                return True
            else:
                return False
        else:
            raise Exception("Type is not true!")

if __name__ == '__main__':
    c1 = compare(5)
    c2 = compare(5)
    print(c1 | c2)

