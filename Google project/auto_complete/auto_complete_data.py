from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int

    def __str__(self):
        return self.completed_sentence + " (" + self.source_text + " " + str(self.offset) + ")"

    def __key(self):
        return self.completed_sentence, self.source_text

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, AutoCompleteData):
            return self.__key() == other.__key()
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.score > other.score or self.score == other.score and self.__key() > other.__key()

    def __lt__(self, other):
        return self.score < other.score or self.score == other.score and self.__key() < other.__key()

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other


