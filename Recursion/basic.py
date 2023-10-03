c = 0


def fun():
    global c
    if c == 3:
        return
    print("c->", c)
    c += 1
    fun()


if __name__ == '__main__':
    fun()
