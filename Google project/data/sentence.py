from dataclasses import dataclass
from typing import List


@dataclass
class Sentence:
    sentence: str
    source: str


@dataclass
class SentenceContainer:
    sentences: List[Sentence]

