#BunchPattern
class Bunch(dict):
    def __init__(self, *args,**kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dic__=self

x = Bunch(name="Jayne Cobb", position="Public Relations")
print x.name
