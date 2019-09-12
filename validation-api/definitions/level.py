class Enumeration(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError
    def __setattr__(self, name, value):
        raise RuntimeError("Cannot override values")
    def __delattr__(self, name):
        raise RuntimeError("Cannot delete values")

    def get_level(self, level):
        for l in levels:
            if l == level:
                return l

LEVEL = Enumeration(["ERROR","WARN","INFO"])
levels = [LEVEL.ERROR, LEVEL.WARN, LEVEL.INFO]
