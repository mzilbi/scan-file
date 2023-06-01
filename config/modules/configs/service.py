class Service:
    def __init__(self):
       self._malicious_words = ["eicar", "eval('unescape)"]

    def __call__(self) -> any:
       return self

    def get(self) -> list[str]:
        return self._malicious_words

    def update(self, malicious_words: list[str]):
        self._malicious_words = malicious_words