class ApiKeyConverter:
    regex = '[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})'

    def to_python(self, value):
        return bytes(value)

    def to_url(self, value):
        return str(value)