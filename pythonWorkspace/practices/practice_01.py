class Taco:
    def __init__(self, meat):
        self.meat = meat

    def consume(self):
        print('Om nom nom')

    def inspect(self):
        print('This taco has %s in it.' % self.meat)

taco = Taco('chicken')
taco.inspect()
taco.consume()
