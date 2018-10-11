# Author: James Haller


class State:
    """
    Interface for encapsulating the behavior associated with a particular
    state of the Context.
    """

    def __init__(self, context: 'Context' = None):
        """
        :param context: Context object with data globally available to the
                        state machine.
        """
        self.context = context

    def run(self) -> 'State' or None:
        """
        Perform this State's behavior.
        :return: The next State, or None if this is a final State.
        """
        raise NotImplementedError

