# terminatex/core.py

import sys
import tempfile
import os
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# Direct import. This is correct.
from term_image.image import from_file
from term_image.exceptions import TermImageError


def display(latex_string: str, color: str = 'white'):
    """
    Renders a LaTeX string and displays it in the terminal.
    """
    image_path = None
    try:
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"${latex_string}$", size=80, ha='center', va='center', color=color)
        ax.axis('off')
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
        
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            fig.savefig(tmp.name, format='png', dpi=300, bbox_inches='tight', pad_inches=0.2, transparent=True)
            plt.close(fig)
            image_path = tmp.name

        image = from_file(image_path)
        image.draw()

    except TermImageError as e:
        print(f"Error: term-image failed to render. Your terminal may not be supported. Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error: An unexpected error occurred. Error: {e}", file=sys.stderr)
    finally:
        if image_path and os.path.exists(image_path):
            os.remove(image_path)


def display_from_url(url: str):
    """
    Fetches an image from a URL, saves it to a temporary file,
    and displays it in the terminal. The file is deleted immediately after.
    """
    image_path = None
    try:
        # 1. Fetch the image content from the URL
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # 2. Write the image content to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp.write(response.content)
            image_path = tmp.name
        
        # 3. Pass the temporary file's PATH to from_file
        image = from_file(image_path)
        image.draw()

    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch image from URL. Error: {e}", file=sys.stderr)
    except TermImageError as e:
        print(f"Error: term-image failed to render. Your terminal may not be supported. Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error: An unexpected error occurred. Error: {e}", file=sys.stderr)
    finally:
        # 4. Ensure the temporary file is always deleted
        if image_path and os.path.exists(image_path):
            os.remove(image_path)

