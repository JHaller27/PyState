# Author: James Haller


from state import State


class Context:
    """
    Interface used by the client. Stores the current State, data globally
    available to the state machine, and handles running the state machine.
    """

    __slots__ = ['_initial_state', '_current_state']

    def __init__(self, initial_state: State):
        """
        Create a new Context object.
        :param initial_state: Start state of the state machine.
        """
        self._current_state = self._initial_state = initial_state

    def run_once(self) -> State or None:
        """
        Run the current state, but does not change the current state.
        Set the next state with set_state(State).
        :return: Next state to be transitioned into (possibly None).
        """
        return self._current_state.run(self)

    def run(self) -> None:
        """
        Run the state machine from the current state to the final state.
        """
        while not self.is_done():
            self.set_state(self.run_once())

    def is_done(self) -> bool:
        """
        Check if the state machine has ended.
        :return: True if the current state is None, False otherwise.
        """
        return self._current_state is None

    def set_state(self, state: State, transition: Callable['Context'] = None) -> None:
        """
        Set the current state.
        :param state: New State.
        :param transition: Callable to run BEFORE change to new state.
                           Takes the current context as a parameter.
        """
        if transition is not None:
            transition(self)
        self._current_state = state

    def reset(self) -> None:
        """
        Reset the state machine to the initial state. Does not change any
        internal variables. Overriding classes should call this function
        (like super().reset()) to revert to the initial state.
        """
        self._current_state = self._initial_state
