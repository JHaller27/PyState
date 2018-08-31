# Author: James Haller


from context import Context
from abc import ABC, abstractmethod


class State(ABC):
    """
    Interface for encapsulating the behavior associated with a particular
    state of the Context.
    """

    def __init__(self, context: Context):
        """
        :param context: Context object with data globally available to the
                        state machine.
        """
        self.context = context

    @abstractmethod
    def run(self) -> 'State' or None:
        """
        Perform this State's behavior.
        :return: The next State, or None if this is a final State.
        """
        return None
