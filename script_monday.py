"""
This is the first day homework, hope it's fine
"""


def o_func(o):
    print(o*5 + '\n' +
          o + '\t' + o + '\n' +
          o + '\t' + o + '\n' +
          o + '\t' + o + '\n' +
          o*5 + '\n')


def h_func(h):
    print(h + '\t' + h + '\n' +
          h + '\t' + h + '\n' +
          h * 5 + '\n' +
          h + '\t' + h + '\n' +
          h + '\t' + h + '\n')


var = '#'

# module execution


if __name__ == '__main__':
    o_func(var)
    h_func(var)


