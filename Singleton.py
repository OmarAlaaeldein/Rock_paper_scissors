class Singleton:
    classvar=None
    def __init__(self):
        if Singleton.classvar!=None:
            raise Exception("Already an instance exist!")
        else:
            Singleton.classvar =self
    def reduction(self):
        if Singleton.classvar==None:
            Singleton()
        return Singleton.classvar