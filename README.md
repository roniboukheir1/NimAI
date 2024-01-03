# Nim AI

## Overview

This project is an implementation of an AI to play the game of Nim. Nim is a mathematical game of strategy where two players take turns removing objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap/pile. The goal of the game is to avoid being the player who must remove the last object.

## Implementation

The codebase is split into two main classes: `Nim` and `NimAI`.

### Nim

The `Nim` class represents the state of the game. It initializes the game with a default state and handles the switching of players after each move. The game continues until a winner is decided (when all objects are removed).

- **Methods**:
  - `__init__`: Initializes the game with a default state.
  - `switch_player`: Switches the turn to the other player.
  - `other_player`: Class method to get the opponent of the current player.
  - `available_action`: Class method to get all possible actions a player can take from the current state.
  - `move`: Executes a move and updates the game state.

### NimAI

The `NimAI` class implements the AI that learns to play Nim using reinforcement learning (specifically Q-learning).

- **Methods**:
  - `__init__`: Initializes the AI with a learning rate (alpha) and an exploration rate (epsilon).
  - `update`: Updates the Q-table with new information after a move is played.
  - `get_q_value`: Gets the Q-value for a given state-action pair.
  - `update_q_value`: Updates the Q-value for a given state-action pair.
  - `best_future_reward`: Returns the best possible future reward for a given state.
  - `choose_action`: Chooses an action for the AI to take in a given state.

## Usage

To train the AI, you can call the `train` function with the desired number of games for training:

```python
ai = train(10000)
#after the training is finished you can play against the AI by calling the `play()` function
play(ai)
```
## Dependencies
- Python 3.x
- random module for generating random numbers
- time module for adding delays
## Contributions
We welcome contributions to Nim AI. If you have suggestions or bug reports, please open an issue. If you'd like to contribute to the codebase, please open a pull request.

---
