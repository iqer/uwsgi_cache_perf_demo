
class TestDemo:
    def __init__(self):
        self.node = {i: 'demo_str_with_number_{}'.format(
            val) for i, val in enumerate(range(100))}

        self.node2 = [i for i in range(1000)]

    def __str__(self):
        return 'node1: {}, node2: {}'.format(
            '.'.join(['{}: {}'.format(k, v) for k, v in self.node.items()]),
            '.'.join(str(i) for i in self.node2)
        )


if __name__ == '__main__':
    t = TestDemo()
    print(str(t))