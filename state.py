# Author: James Haller


from context import Context
from abc import ABCMeta, abstractmethod


class State(ABCMeta):
    """
    Interface for encapsulating the behavior associated with a particular
    state of the Context.
    """

    # noinspection PyUnusedLocal
    @abstractmethod
    def run(self, context: Context) -> 'State' or None:
        """
        Perform this State's behavior.
        :param context: Context object with data globally available to the
                        state machine.
        :return: The next State, or None if this is a final State.
        """
        return None
