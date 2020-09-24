class Command:

    def __init__(self, name, data="0"):
        self.name = name
        self.data = data

    def __str__(self) -> str:
        return '{"name": "' + self.name + '", "data": ' + self.data + '}'
