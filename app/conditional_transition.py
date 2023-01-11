from .transition import Transition
from .place import Place
from .base_simulation import Simulation

from typing import Callable, Literal


class ConditionalTransition(Transition):

    def __init__(self, distribution_type: Literal['const', 'norm', 'exp', 'uni', 'func'], parent: "Simulation",
                 str_id: str, place: str, condition: Callable, **kwargs):
        super().__init__(distribution_type, parent, str_id, **kwargs)
        self._condition_place = self._parent.get_element_by_id(place)
        self._condition_lambda = condition

    def _hold(self, timer: int):
        if self._condition_lambda(self._condition_place.load):
            transition_quantity = min([_input[0].load for _input in self._inputs])
            for _input in self._inputs:
                _input[0].exclude(transition_quantity)
            for _ in range(transition_quantity):
                self._storage.append(self._generate_fin_time(timer))
