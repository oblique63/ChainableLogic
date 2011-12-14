def _handle_not_set(cmp, true, fallback):
    return Comparison(true) if not cmp.is_set else fallback

def _or(cmp, true):
    return _handle_not_set(cmp, true, Comparison(true or cmp.true))

def _and(cmp, true):
    return _handle_not_set(cmp, true, Comparison(true and cmp.true))


class Comparison(object):
    def __init__(self, truth=-1):
        if truth == -1:
            self.true = None
        else:
            self.true = bool(truth)

    def __str__(self):
        return str(self.true)

    @property
    def is_set(self):
        return self.true != None
    
    def AND(self, *args):
        if len(args) == 0: return Comparison()

        for arg in args:
            if type(arg) is Comparison:
                if not arg.true:
                    return _and(self, False)
            elif not arg:
                return _and(self, False)

        return _and(self, True)
    
    def OR(self, *args):
        if len(args) == 0: return Comparison()

        for arg in args:
            if type(arg) is Comparison:
                if arg.true:
                    return _or(self, True)
            elif arg:
                return _or(self, True)

        return _or(self, False)

    def NAND(self, *args):
        return Comparison(not self.AND(*args).true)

    def NOR(self, *args):
        return Comparison(not self.OR(*args).true)
