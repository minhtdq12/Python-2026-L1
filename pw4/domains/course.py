class Course:
    def __init__(self, c_id, name, credits):
        self._id = c_id
        self._name = name
        self._credits = credits

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def credits(self):
        return self._credits