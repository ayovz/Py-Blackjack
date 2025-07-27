# 🃏 Blackjack - Python CLI Game

Welcome to **Blackjack**, a simple command-line implementation of the classic card game written in Python.

Play against the computer, draw cards, and try to get as close to 21 as possible without going over!

---

## 🎮 Features

- Terminal-based game with interactive input
- Basic Blackjack rules:
  - Automatic Ace handling (11 or 1)
  - Win conditions include Blackjack, bust, and score comparison
- ASCII art title
- Replayable game loop
- Clean and cross-platform screen clearing

---

## 🛠 Requirements

- Python 3.6 or higher
- No external libraries needed

---

## ▶️ How to Play

1. Clone or download the repo:
   ```bash
   git clone https://github.com/your-username/Py-Blackjack.git
   cd Py-Blackjack
   ```
2. Run the game:
   ```python blackjackmain.py```

3. Follow on-screen instructions to:
   - Draw another card by typing y
   - Stand by typing n
   - Decide whether to play again after each round

## 📝 Example Output
```
Welcome to Blackjack!
Press Enter to start the game...

.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'

Your cards: [10, 7], current score: 17
Computer's first card: 9
Type 'y' to draw another card, or 'n' to stand: n

--------------- Final Results ---------------
Your cards: [10, 7], final score: 17
Computer's cards: [9, 8], final score: 17
DRAW
```

## 📁 File Structure
```
Py-Blackjack/
│
├── blackjackmain.py   # Main game file
├── README.md      # You're reading it!
```

## 📚 Blackjack Rules Summary
  - Cards 2-10 = face value
  - Face cards (J, Q, K) = 10
  - Aces = 11 (or 1 if it helps avoid busting)
  - Blackjack = exactly 21 with 2 cards
  - If the computer or player goes over 21 = bust
  - Computer draws until it reaches 17 or more

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

Want to improve the game? Feel free to fork and submit pull requests. You can add:

    Card graphics

    Score tracking

    Multiplayer support

    GUI version with Tkinter or Pygame

Enjoy the game and beat the dealer! 🎉

Made with love.
---
