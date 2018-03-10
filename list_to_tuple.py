def list_to_tuple(_list):
    t = ()
    for e in _list:
        if isinstance(e,list):
            t += (list_to_tuple(e),)
        else:
            t += (e,)
    return t

if __name__ == '__main__':
    a = [[1,2],[3,4]]
    b = list_to_tuple(a)
    print b
