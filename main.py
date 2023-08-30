from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

lexer = PythonLexer()
formatter = TerminalFormatter()

def get_triangle1_code() -> None :

    code = """
def get_triangle1(n : int = 5 , inverted : bool = False) -> None :

    # Check if n is a positive integer, otherwise raise a ValueError
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")

    # Initialize the ASCII value for character printing
    asci = 65

    # If inverted is False, print the triangle in regular order
    if inverted == False :
        # Loop through rows from 1 to n
        for i in range(1 , n + 1) :
            # Loop through columns based on the current row
            for j in range(i) :
               # Print the character corresponding to the ASCII value
                print(chr(asci) , end = "  ")

                # Increment ASCII value, cycle back to 'A' if it exceeds 'Z'
                asci += 1
                if asci > 90 :
                    asci = 65
                    
            # Move to the next line after each row is printed
            print()
        return
        
    # If inverted is True, print the triangle in inverted order
    for i in range(n , 0 , -1) :
        for j in range(i) :
            print(chr(asci) , end = "  ")
            asci += 1
            if asci > 90 :
                asci = 65
        print()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

from patterns import star_patterns
from patterns.star_patterns import *
for i in dir(star_patterns):
    if callable(getattr(star_patterns,i)) :
        globals()[i]()
        print()
        print()

