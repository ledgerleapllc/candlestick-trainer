## Candlestick Trainer

Candlestick Trainer is a simple flashcard-based training application to help users recognize and memorize candlestick patterns used in trading. The application randomly displays a candlestick pattern, allowing users to guess its type before revealing the name, signal, and type.

### Features
- Displays random candlestick patterns as flashcards
- A "Reveal" button to show pattern details
- "Auto" mode for automatic cycling through flashcards every 10 seconds (5 seconds challenge, 5 seconds reveal)
- Background border changes color based on pattern signal:
  - Green for Bullish
  - Red for Bearish
  - Grey for Neutral
- Timer display when auto mode is enabled
- Ensures no consecutive duplicate patterns

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/candlestick-trainer.git
   cd candlestick-trainer
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage
Run the application using:
```sh
python candlestick-trainer.py
```

### Requirements
- Python 3.x
- Tkinter (Built-in with Python)
- Pillow (For image handling, if needed)

### File Structure
```
/
├── patterns/                  # Folder containing candlestick images
├── patterns.json              # JSON file with pattern details
├── candlestick-trainer.py     # Main application script
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
```

### Contributions
Feel free to submit issues or contribute improvements via pull requests.

### License
MIT License

