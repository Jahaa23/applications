import textwrap

def wrap(str, mw):
    return textwrap.fill(str, mw)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
