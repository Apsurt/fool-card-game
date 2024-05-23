# Fool (Durak) Card Game

## Overview

[Fool (Durak)](https://en.wikipedia.org/wiki/Durak) is a strategic card game where players aim to get rid of all their cards while trying to prevent others from doing so. This project is a digital adaptation of the classic card game, featuring a variation based on the specific rules the developer plays by, which may differ from other versions found online.

## Installation

### Prerequisites

- Python must be installed on your system.
- Dependencies are listed in `requirements.txt`.

### Installation Steps

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/Apsurt/fool-card-game.git
   ```
2. Change into the project directory:
   ```sh
   cd fool-card-game
   ```
3. Install the necessary libraries:
   ```sh
   pip install -r requirements.txt
   ```

## Game Rules and Instructions

### Basic Rules

- Players draw cards until they have 5 in their hand.
- Each turn involves defending against an attack from the previous player and then attacking the next player.

### Number of Players

- The game can be played by 2 to 8 players.

### Special Rules

- This version follows the specific rules the developer uses, which may differ from the standard rules found on the internet.

## Bot Integration

This project includes a bot designed to demonstrate perfect gameplay using the Max^n algorithm. Project automatically simulates games between multiple bot players, showcasing optimal strategies and decision-making processes.

### Bot Functionality

- **Purpose:** To illustrate how perfect gameplay would look.
- **Algorithm:** Uses the Max^n algorithm for decision-making.
- **Integration:** The bot is seamlessly integrated into the game and is enabled automatically.

### Usage

- Currently, the bot only simulates games between bot players (bots vs bots).
- There is no need for user intervention to enable the bot; it runs automatically.

### Customization

- The current version does not offer customization options for the bot's behavior or difficulty level.

## How to Play

1. To start the game, execute:
   ```sh
   python src/main.py
   ```

## Code Structure

- The project is organized into various modules, with `main.py` serving as the entry point to start the game.
- The bot's functionality is included within the game simulation.

## Contributing

Contributions are welcome! Please adhere to the Contributor Code of Conduct.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

No specific contact information is provided. Contributions are encouraged and appreciated.
