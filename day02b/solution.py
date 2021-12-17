from collections import namedtuple
import sys

State = namedtuple("State", ["x", "y", "aim"])
Action = namedtuple("Action", ["action", "value"])

transitions = {
    "forward": lambda x, state: State(state.x + x, state.y + x * state.aim, state.aim),
    "up": lambda x, state: State(state.x, state.y, state.aim - x),
    "down": lambda x, state: State(state.x, state.y, state.aim + x)
}

inputs = (line.split(' ') for line in sys.stdin)
actions = (Action(action, int(value)) for action, value in inputs)

state = State(0, 0, 0)
for action in actions:
    transition = transitions[action.action]
    state = transition(action.value, state)

print(state.x * state.y)
