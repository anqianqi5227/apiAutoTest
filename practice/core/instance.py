class Data(object):
    instance = None

    @staticmethod
    def getInstance():
        if not Data.instance:
            # todo
            Data.instance = 111
        return Data.instance


print(Data.getInstance)

print(Data.getInstance)