class Worker:
    def __init__(self, occupation):
        self._occupation = occupation

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation

    def worker_detail(self):
        return f"My Occupation is: {self._occupation}"
