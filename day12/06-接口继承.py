import abc

class All_file(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self):
        pass

    @abc.abstractmethod
    def read(self):
        pass

class Disk(All_file):
    def read(self):
        print('disk read')

    def write(self):
        print('disk write')

class CDRom(All_file):
    def read(self):
        print('cd read')

    # def write(self):
    #     print('cd write')


sony = CDRom()


