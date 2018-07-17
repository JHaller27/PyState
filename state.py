# Author: James Haller


from context import Context
from abc import ABCMeta, abstractmethod


class State(ABCMeta):
    """
    Interface for encapsulating the behavior associated with a
    particular state of the Context.
    """

    # noinspection PyUnusedLocal
    @abstractmethod
    def run(self, context: Context) -> 'State' or None:
        return None
