"""
This is the first day homework, hope it's fine
"""


def o_func(thing):
    print(thing*5 + '\n' +
          thing + '\t' + thing + '\n' +
          thing + '\t' + thing + '\n' +
          thing + '\t' + thing + '\n' +
          thing*5 + '\n')


def h_func(thing):
    print(thing + '\t' + thing + '\n' +
          thing + '\t' + thing + '\n' +
          thing * 5 + '\n' +
          thing + '\t' + thing + '\n' +
          thing + '\t' + thing + '\n')


var = '#'

# module execution


if __name__ == '__main__':
    o_func(var)
    h_func(var)


