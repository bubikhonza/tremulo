class _Constants:
    def __set__(key, value):
        raise Exception("Cant set constant")

Constants = _Constants()