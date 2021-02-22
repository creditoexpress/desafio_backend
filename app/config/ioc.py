class IOC:
    def __init__(self) -> None:
        self.ioc = {}


    def add(self, name: str, dep):
        self.ioc[name] = dep


    def get(self, name: str):
        if name not in self.ioc:
            raise Exception(f'ERROR: Dependency [ {name} ] not found.')
        return self.ioc[name]
