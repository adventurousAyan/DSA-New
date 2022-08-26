import abc


class AbstractDeployer(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def deploy(self):
        """Declaration of deploy function"""
        pass
