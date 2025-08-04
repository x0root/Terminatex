# examples.py

from terminatex import display, display_from_url

def main():
    """
    Demonstrates both LaTeX and URL display functionalities.
    """
    # --- 1. Display LaTeX from a string ---
    print("--- Rendering LaTeX: Euler's Identity (in white) ---")
    display(r"e^{i\pi} + 1 = 0", color='white')

    print("\n--- Rendering LaTeX: The Quadratic Formula (in cyan) ---")
    display(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", color='cyan')

    # --- 2. Display an image from a URL ---
    print("\n--- Rendering Image from URL: E = MC2 ---")
    python_logo_url = "https://media.istockphoto.com/id/515369312/id/vektor/kesetaraan-energi-massal.jpg?s=612x612&w=0&k=20&c=bvDzBI-X3joclfryFpMAhGDyD2-3nf6Y8wprtT0k7YU="
    display_from_url(python_logo_url )
    
    print("\nDone.")

if __name__ == "__main__":
    main()
