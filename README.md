# 🎮 Tic-Tac-Toe Game

This project contains two implementations of the classic **Tic Tac Toe** game:
- A **Console-based version** for terminal play.
- A **GUI-based version** using **PyQt5** for a graphical experience.

---

##  Contents

- [Console Version](#-tic-tac-toe---console-game)
- [GUI Version](#-tic-tac-toe--pyqt5-gui-version)
- [Game Rules](#-game-rules)
- [Run Instructions](#-how-to-run)

---

##  Tic-Tac-Toe - Console Game

This is a simple command-line implementation of the classic **Tic Tac Toe** game using Python. Two players, `R` and `K`, take turns entering a position (0 to 8) to place their mark on a 3x3 grid. The game detects wins/draw, handles invalid inputs, and supports repeated plays.

###  How to Play

- The board is represented as a 3x3 grid with positions numbered from `0` to `8`.
- Players alternate turns entering a position (0–8).
- Invalid or occupied inputs are rejected.
- The game ends with a win or a draw.
- Option to play again after each round.

---

##  Tic Tac Toe – PyQt5 GUI Version

An interactive **Tic Tac Toe** game built with **Python** and **PyQt5**. This version features a clean and colorful interface, real-time scoring, and popup messages.

###  Features

- GUI interface with responsive layout
- 2-player mode (Player X vs Player O)
- Button-based interaction for moves
- Win/draw detection with message popups
- Score tracking: X wins vs O wins
- Option to reset board or exit
- Orange (X) and Green (O) move highlights

---

##  Game Rules

- Player X starts the game.
- Players take alternate turns.
- First to align 3 marks in a row/column/diagonal wins.
- If all 9 cells are filled without a winner, it's a draw.
- After each match, players can choose to **replay or quit**.

---

##  How to Run

### Console Version

1. Ensure **Python 3** is installed.
2. Save the console version as `tic_tac_toe.py`.
3. Run it via terminal:  python `tic_tac_toe.py`.



### GUI Version

1. Ensure **PyQt5** is installed
2. Save the gui version as `tic_tac_toe_gui.py`.
3. Run it via terminal:

```bash
    python tic_tac_toe_gui.py