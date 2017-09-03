
class TestMyGenerator(object):

    def test_comprehensions(self):
        list_a = list(range(1, 11))
        result = [x*x for x in list_a if(x % 2 == 0)]

    def test_generator1(self):
        list_a = list(range(1, 100))
        result = (x * x for x in list_a if (x % 2 == 0))
        return result
        return 2

    def test_generator2(self, max1):
        n, a, b = 0, 0, 1
        while n < max1:
            yield b
            a, b = b, a + b
            n = n + 1
        return b

if __name__ == '__main__':
    obj_spider = TestMyGenerator()
    print(obj_spider.test_generator2(5))
