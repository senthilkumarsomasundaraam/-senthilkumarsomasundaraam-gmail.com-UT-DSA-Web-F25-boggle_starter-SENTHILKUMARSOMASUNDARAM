# DSC 395T: Algorithms and Data Structures  
## Boggle Programming Assignment #3

This project implements the classic word game **Boggle™**, emphasizing recursive algorithms, data structures (Trie), and search strategies, all using only the Python standard library and `pytest`.

## 🚀 Features

- Randomly generated **NxN Boggle board**
- Word validation using a **Trie-based dictionary**
- Two search modes:
  - **Board-driven search**: Recursively find all words from board positions
  - **Dictionary-driven search**: Check each dictionary word against the board
- Real-time **user input** and word validation
- **Scoring system** based on word length
- **Replayable game loop** with UI in terminal
- **Custom board and cube configurations** via command line

## 🧠 Concepts Used

- **Recursive Search Algorithms**
- **Trie Data Structure** for efficient prefix and word lookup
- **Object-Oriented Design** using abstract base classes
- **Separation of Concerns** via interfaces (`BoggleGame`, `BoggleDictionary`)
- **Randomized Board Initialization**

