# Classical Cryptography Tool

This project is a simple tool that implements classical cryptographic algorithms and allows users to encrypt and decrypt messages using ciphers such as **Caesar Cipher**, **Vigenère Cipher**, and **Playfair Cipher**. Additionally, basic cryptanalysis techniques are provided to break these ciphers.

## Features

- **Caesar Cipher**: A substitution cipher that shifts each letter by a certain number.
- **Vigenère Cipher**: A more advanced cipher based on the use of a keyword to shift letters.
- **Playfair Cipher**: A digraph cipher that encrypts pairs of letters.
- **Cryptanalysis**: Basic techniques for breaking the ciphers, such as frequency analysis (for Caesar and Vigenère).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Algorithms Implemented](#algorithms-implemented)
  - [Caesar Cipher](#caesar-cipher)
  - [Vigenère Cipher](#vigenère-cipher)
  - [Playfair Cipher](#playfair-cipher)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- Tkinter (for GUI version)
- Flask (for web version)

### Steps to Install

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/classical-cryptography-tool.git
    ```

2. Navigate into the project directory:

    ```bash
    cd classical-cryptography-tool
    ```


    

4. For the Tkinter GUI version, ensure that Tkinter is installed. Tkinter is usually bundled with Python. If it's not, you can install it based on your operating system.

    - **For Windows**: Tkinter comes pre-installed with Python.
    - **For macOS**: Tkinter is included with Python 3.x, but you may need to install `tcl/tk` via Homebrew if you encounter issues.
    - **For Linux**: You may need to install Tkinter using:

      ```bash
      sudo apt-get install python3-tk
      ```

### Running the Application

#### Tkinter (GUI Version)

To run the GUI version of the tool, simply run:

```bash
python tkinter_app.py


