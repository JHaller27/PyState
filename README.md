# PyState
*Made by James Haller*

## Overview

Uses classes to mimic state-based behavior described in the [Gang-of-Four State pattern](https://sourcemaking.com/design_patterns/state).

## Quick-Start

1. Import classes
   * `from state import State`
   * `from state import Context` (optional)
1. Implement the abstract `State` class and its `run(Context)` method
1. (Optional) Extend `Context` and define data globally accessible to the state machine, and or additional behavior
1. Call `Context.run()`

## Example

```python
# These are the only two classes you should need from the state module
# Note: You can also do `from context import ...` buy why would you?
from state import State, Context

MAX_TRANSITIONS = 10


class MyContext(Context):
    """
    While you can use Context out-of-the-box, this is an example of how one
    would create a user-defined Context with state-machine-global data.
    """
    __slots__ = ['_counter']

    def __init__(self, initial_state):
        """
        Call the base Context class's __init__() to set the initial state
        and manually setup global data for this user-defined Context.
        """
        super().__init__(initial_state)
        self._counter = 0

    def set_state(self, state: State):
        """
        This particular user-defined Context performs extra tasks during
        set_state operations (ie each time the current state changes it
        increments a counter.

        Note: `super().set_state(state)` or `this._current_state = state` MUST
        appear somewhere when overriding set_state(). Otherwise, the Context
        will never change state, rendering this state machine useless.
        """
        self._counter += 1
        super().set_state(state)

    def get_counter(self):
        return self._counter

class MyStartState(State):
    """
    The name is arbitrary. The important thing to note is that run() is
    overridden and returns the next State. This pattern continues for all
    custom states below.
    """
    def run(self, context: MyContext):
        if context.get_counter() % 2 == 0:
            return MyStateA()
        else:
            return MyStateB()

class MyStateA(State):
    def run(self, context: MyContext):
        if context.get_counter() >= MAX_TRANSITIONS:
            return MyFinalState()  # Could just return None
        else:
            return MyStateB()

class MyStateB(State):
    def run(self, context: MyContext):
        if context.get_counter() >= MAX_TRANSITIONS:
            return MyFinalState()  # Could just return None
        else:
            return MyStateA()

class MyFinalState(State):
    def run(self, context: MyContext):
        # Do other clean-up things here if necessary
        return None

# Create the state machine (and set the initial state)
state_machine = MyContext(MyStartState())

# There are two ways to run a state machine.
# The easy way...
state_machine.run()

# or the controllable way...
while not state_machine.is_done():
    state = state_machine.run_once()
    # Do stuff before switching states
    state_machine.set_state(state)
```
