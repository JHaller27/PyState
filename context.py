# Author: James Haller


from state import State


class Context:
    """
    Interface used by the client. Stores the current State.
    """

    __slots__ = ['_initial_state', '_current_state']

    def __init__(self, initial_state: State):
        self._current_state = self._initial_state = initial_state

    def run_once(self) -> State or None:
        return self._current_state.run(self)

    def run(self) -> None:
        while not self.is_done():
            self._current_state = self.run_once()

    def is_done(self) -> bool:
        return self._current_state is None

    def reset(self) -> None:
        self._current_state = self._initial_state
