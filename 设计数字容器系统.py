from collections import defaultdict
from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        old_number = self.index_to_number.get(index, None)
        if old_number is not None:
            self.number_to_indices[old_number].discard(index)

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        indices = self.number_to_indices[number]
        return indices[0] if indices else -1

