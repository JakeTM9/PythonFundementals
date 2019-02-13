"""
https://docs.python.org/3/reference/datamodel.html
"""


class Properties(object):

    def __init__(self, props):
        self.props = []
        if type(props) in (list,tuple):
            self.props.extend(props)

    def __add__(self, other):
        return Properties(self.props + other.props)

    def __sub__(self, other):
        return Properties([p for p in self.props if p not in other.props])

    def __str__(self):
        return f'Properties: {self.props}'


p1 = Properties(['red', 'round', 'small'])
p2 = Properties(['shiny', 'reflective', 'transparent'])
p3 = Properties(['small', 'round'])

print('p1: ' + str(p1))
print('p2: ' + str(p2))
print('p3: ' + str(p3))

print()

p4 = p1 + p2

print('p4: ' + str(p4))

print()

print('p4 - p3: ' + str(p4 - p3))
