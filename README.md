# Echo — CS50P Final Project

#### Video Demo: <https://youtu.be/UVcrdyXeD3A>

## Description

  Echo is a fast-paced reaction game built with pygame-ce. The player will see
a direction on top of the screen as up, down, left, or right in yellow or red;
yellow means "follow the direction" and red means "do the opposite". The player
can respond using arrow keys or WASD before the timer runs out. If the player
can make the correct move, their score will increase (+1), with each correct
answer, the timer will shrink and they will have less time to react and press a
key. As the timer runs out or they make a wrong move, the game will end, showing
the player's score and three options, one is to replay, other one is to get to
the main menu, and the last one is to quit.
  The character is deplayed as a white square, positioned above a 3x3 grid of
grey blocks. As the player makes a correct move, the character will move to that
direction while turning green, and quickly get back to where it was, standing in
the middle.

## How to run:

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the game:
```
python project.py
```

## How to play:

- Use **WASD** or the **arrow keys** to make a move.
- A **yellow** direction means press that same direction.
- A **red** direction means press the *opposite* direction.
- Answer before the timer runs out — the time limit shrinks slightly with every
  correct answer, so the game gets progressively harder.
- One wrong answer or timeout ends the game and shows your final score.

## Design notes

  The project is structured around three main screens, each handled by its own
function with its own event loop: the main menu (`loop`), gameplay (`game`), and
the game-over screen (`game_over_screen`). Each screen communicates the player's
choice back up the call chain using return values (`"quit"`, `"menu"`,
`"replay"`) rather than nested function calls, to avoid deeply nested call
stacks across repeated replays.
  Three logic functions were extracted from the game loop specifically to be
testable with pytest, independent of pygame's event/rendering system:
- `get_correct_answer()` — determines the correct key press given the shown
  direction and its color
- `shrink_time_limit()` — calculates the new time limit after a correct answer
- `get_pressed_direction()` — maps a pressed key to its direction

## Files

- `project.py` — main game logic, pygame loop, and all three screens
- `test_project.py` — pytest tests for the three pure logic functions
- `requirements.txt` — external dependencies

## Libraries used

- **pygame-ce** — window creation, drawing, input handling, and timing
