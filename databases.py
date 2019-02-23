from typing import List
from random import randint
import webbrowser

GOOD_WORDS = [
    'sustainable',
    'environmentally friendly',
    'zero waste',
    'ethically sourced'
]


class Database:
    """
    A database of keywords.

    === Attributes ===
    selected: Whether this keyword database was selected by the user.
    keywords: The keywords in this database.
    """
    selected: bool
    keywords: List[str]

    def ___init___(self, lst: List[str]) -> None:
        """Initialize this database with the keywords from lst."""
        self.selected = False
        self.keywords = lst

    def __contains__(self, word: str) -> bool:
        """Return whether word is in this database."""
        return word.lower() in self.keywords

    def get_search(self, word: str) -> str:
        """Return the related sustainable search sbased on <word>."""
        suggestion = word
        if self.selected:
            n = randint(0, len(GOOD_WORDS) - 1)
            extension = GOOD_WORDS[n]
            suggestion = extension + ' ' + suggestion
            # webbrowser.open_new(suggestion)
        return suggestion

if __name__ == '__main__':
    d = Database()
    d.get_suggestion('food')
