from typing import TYPE_CHECKING, List

from .models import Element
if TYPE_CHECKING:
    from .simulation import Simulation

import numpy as np


class Place(Element):

    _num_id = 0

    def __init__(self, parent: "Simulation", capacity: int = np.inf, str_id: str = '', initial_load: int = 0):
        super().__init__(parent, capacity, str_id)

        self._num_id = Place._num_id
        Place._num_id += 1

        if initial_load > 0:
            self._load = initial_load

    def __repr__(self):
        return f'Place: {self._id}, capacity={self._capacity}, load={self.load}'

    @property
    def is_full(self):
        return self.load == self._capacity

    def exclude(self, num: int = 1):
        self._load -= num

    def append(self, num: int = 1):
        if self._load < self._capacity:
            self._load += num
            return True
        else:
            return False
