## Assignment Overview

This project was developed as part of a programming assignment to demonstrate how to integrate Python applications with external APIs.
The goal of the assignment was to build a simple command-line trading tool that can interact with the Binance Futures Testnet.

The bot allows users to place market and limit orders using command-line arguments. It validates user input, sends requests to the Binance API, and returns the order response in the terminal.

This assignment helped in understanding API integration, command-line interfaces (CLI), and modular Python project structure.

## Usage Example

Run a market order using the command line:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Features
- CLI-based trading bot
- Binance Futures Testnet integration
- Market & Limit order execution
- Input validation
- Logging support
