# Terminatex

[![GitHub Repo](https://img.shields.io/badge/GitHub-x0root%2FTerminatex-blue?logo=github)](https://github.com/x0root/Terminatex)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/x0root/Terminatex/blob/main/LICENSE)

Display beautiful, high-fidelity LaTeX expressions and web images directly in your terminal.

terminatex is a Python utility that renders any LaTeX string or web image and displays it in modern terminals, providing a seamless way to visualize mathematical formulas and remote images without leaving your command-line environment.

![Terminatex Demo](https://github.com/x0root/Terminatex/blob/cad87abfa53e0a7c38683f00a0543f9b2e66bca8/display.png?raw=true)

## Features

- High-Quality LaTeX Rendering using matplotlib
- Display web images from any URL
- True-color terminal display via term-image
- Customizable LaTeX color options
- Simple and intuitive API

## Requirements

- Python 3.8+
- A modern terminal that supports true color (24-bit) and terminal graphics protocol
  - Recommended on Windows: Windows Terminal
  - Recommended on macOS: iTerm2, WezTerm
  - Recommended on Linux: Konsole, WezTerm, kitty

## Installation

Install terminatex from PyPI:

```bash
pip install terminatex
```

## Usage

Here's a complete example demonstrating how to render both LaTeX and a web image directly in your terminal:

```python
# examples.py

from terminatex import display, display_from_url

def main():
    """
    Demonstrates both LaTeX and URL-based image rendering in the terminal using terminatex.
    """

    # --- 1. Display LaTeX from a string ---

    # Render Euler's Identity using white color
    print("--- Rendering LaTeX: Euler's Identity (in white) ---")
    display(r"e^{i\pi} + 1 = 0", color='white')

    # Render the Quadratic Formula in cyan
    print("\n--- Rendering LaTeX: The Quadratic Formula (in cyan) ---")
    display(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", color='cyan')

    # --- 2. Display an image from a URL ---

    # Render an image from the web: E = MC² illustration
    print("\n--- Rendering Image from URL: E = MC² ---")
    image_url = "https://media.istockphoto.com/id/515369312/id/vektor/kesetaraan-energi-massal.jpg?s=612x612&w=0&k=20&c=bvDzBI-X3joclfryFpMAhGDyD2-3nf6Y8wprtT0k7YU="
    display_from_url(image_url)

    print("\nDone.")

if __name__ == "__main__":
    main()
```

## How It Works

For LaTeX (display):

- matplotlib renders your LaTeX string into a high-resolution PNG image
- This image is saved to a temporary file in your operating system's temp directory

For URLs (display_from_url):

- requests fetches the image data from the web
- The downloaded data is written to a temporary file

Display:

- In both cases, the path to the temporary file is passed to the term-image library
- term-image intelligently detects your terminal's capabilities and draws the image directly in your console

Cleanup:

- Immediately after the image is drawn, the temporary file is deleted to avoid cluttering your disk

## License

This project is licensed under the MIT License.
