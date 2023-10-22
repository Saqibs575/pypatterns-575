from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

lexer = PythonLexer()
formatter = TerminalFormatter()



# STAR PATTERNS CODE

#  1) GET STAR PYRAMID CODE
def get_star_pyramid_code() -> None :

    """
    Display the source code of the 'get_star_pyramid' function with syntax highlighting.

    This function retrieves the source code of the 'get_star_pyramid' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_star_pyramid_code() will output the properly highlighted source code
        of the 'get_star_pyramid' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_star_pyramid(n = 5, inverted = False) :
    if inverted == True :
        for i in range(1 , n + 1) :
            print("   " * (n - i) + " * " * (2 * i - 1))
        return

    for i in range(n , 0 , -1) :
        print("   " * (n - i) + " * " * (2 * i - 1))
get_star_pyramid()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

#  2) GET STAR HOLLOW PYRAMID CODE
def get_star_hollow_pyramid_code() -> None :

    """
    Print the source code of the 'get_star_hollow_pyramid' function with syntax highlighting.

    This function generates and prints the source code of another function 'get_star_hollow_pyramid'
    that is used to print patterns of hollow pyramid. The hollow  pyramid can be both regular
    or inverted, and the pattern is made of asterisks and spaces.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_star_hollow_pyramid_code() will output the source code of the 'get_star_hollow_pyramid'
        function, which can then be used to create and display hollow pyramid patterns.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code. 
    """

    code = """
def get_star_hollow_pyramid(n = 5, inverted = False) :
    if inverted == False :
        for i in range(1 , n + 1) :
            if i == 1 or i == n :
                print("  " * (n - i) + "* " * (2 * i - 1))
            else :
                print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")  
        return

    for i in range(n , 0 , -1) :
        if i == 1 or i == n :
            print("  " * (n - i) + "* " * (2 * i - 1))
        else :
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")
get_star_hollow_pyramid()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

#  3) GET STAR PYRAMID2 CODE
def get_star_pyramid2_code() -> None :

    """
    Display the source code of the 'get_star_pyramid2' function with syntax highlighting.

    This function retrieves the source code of the 'get_star_pyramid2' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_star_pyramid2_code() will output the properly highlighted source code
        of the 'get_star_pyramid2' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_star_pyramid2(n = 5, inverted = False) :
    if inverted == False :
        for i in range(1 , n + 1) :
            print("  " * (n - i) + " *  " * i)
        return

    for i in range(n , 0 , -1) :
        print("  " * (n - i) + " *  " * i)
get_star_pyramid2()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

#  4) GET STAR TRIANGLE CODE
def get_star_triangle_code() -> None :

    """
    Print the source code of the 'get_star_triangle' function.

    This function generates and prints the source code of another function called 'get_star_triangle'.
    The 'get_star_triangle' function is used to print a right-angled triangle pattern using asterisks ('*').
    The triangle can be either in its regular orientation or inverted, based on the 'inverted' parameter.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_star_triangle_code() will display the source code of the 'get_star_triangle' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_star_triangle(n = 5, inverted = False) :
    if inverted == False :
        for i in range(1 , n + 1) :
            print("*  " * i)
        return

    for i in range(n , 0 , -1) :
        print("*  " * i)
get_star_triangle()        
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

#  5) GET STAR HOLLOW TRIANGLE CODE
def get_star_hollow_triangle_code() -> None :

    """
    Print the source code of the 'get_star_hollow_triangle' function.

    This function generates and prints the source code of another function called 'get_star_hollow_triangle'.
    The 'get_star_hollow_triangle' function is used to print a right-angled hollow triangle pattern using asterisks ('*').
    The triangle can be either in its regular orientation or inverted, based on the 'inverted' parameter.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_star_hollow_triangle_code() will display the source code of the 'get_star_hollow_triangle' function.

    Note:
        You do not require to use print function for printing the source code. Just function calling will print the source code. 
    """

    code = """
def get_star_hollow_triangle(n = 5, inverted = False) :
    if inverted == False :
        for i in range(1 , n + 1) :
            if i == 1 or i == n :
                print("* " * i)
            else :
                print("* " + "  " * (i - 2) + "*")
    else :
        for i in range(n , 0 , -1) :
            if i == 1 or i == n :
                print("* " * i)
            else :
                print("* " + "  " * (i - 2) + "*")
get_star_hollow_triangle()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

#  6) GET STAR DIAMOND CODE
def get_star_diamond_code() -> None :

    """
    Print the source code of the 'get_star_diamond' function.

    This function generates and prints the source code of another function called 'get_star_diamond'.
    The 'get_star_diamond' function is used to print a diamond pattern using asterisks ('*').

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_star_diamond_code() will display the source code of the 'get_star_diamond' function.

    Note:
        You do not require to use print function for printing the source code. Just function calling will print the source code. 
    """
    
    code = """
def get_star_diamond(n = 5) :
    for i in range(1 , n + 1) :
        print("  " * (n - i) + "* " * (2 * i - 1))
    for i in range(n - 1 , 0 , -1) :
        print("  " * (n - i) + "* " * (2 * i - 1))
get_star_diamond()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

#  7) GET STAR HOLLOW DIAMOND CODE
def get_star_hollow_diamond_code() -> None :

    """
    Print the source code of the 'get_star_hollow_diamond' function.

    This function generates and prints the source code of another function called 'get_star_hollow_diamond'.
    The 'get_star_hollow_diamond' function is used to print a hollow Diamond pattern using asterisks ('*').

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_star_hollow_diamond_code() will display the source code of the 'get_star_hollow_diamond' function.
        
    Note:
        You do not require to use print function for printing the source code. Just function calling will print the source code. 
    """

    code = """
def get_star_hollow_diamond(n = 5) :
    for i in range(1 , n + 1) :
        if i == 1 or i == 2 * n -1:
            print("  " * (n - i) + "*")
        else :
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")
    for i in range(n - 1 , 0 , -1) :
        if i == 1 or i == 2 * n -1:
            print("  " * (n - i) + "*")
        else :
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")
get_star_hollow_diamond()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

#  8) GET STAR DIAMOND2
def get_star_diamond2_code() -> None :

    """
    Print the source code of the 'get_star_diamond2' function.

    This function generates and prints the source code of another function called 'get_star_diamond2'.
    The 'get_star_diamond2' function is used to print a diamond pattern using asterisks ('*').

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_star_diamond2_code() will display the source code of the 'get_star_diamond2' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code. 
    """

    code = """
def get_star_diamond2(n = 5) :
    for i in range(1 , n + 1) :
        print("  " * (n - i) + " *  " * i)
    for i in range(n - 1 , 0 , -1) :
        print("  " * (n - i) + " *  " * i)
get_star_diamond2()
"""

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

#  9) GET X PATTERN'S CODE
def get_x_code() -> None :

    """
    Print the source code of the 'get_x' function.

    This function generates and prints the source code of another function called 'get_x'.
    The 'get_x' function is used to print a alphabet 'X' pattern using asterisks ('*').

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_x_code_code() will display the source code of the 'get_x' function.

    Note:
        You do not require to use print function for printing the source code. Just function calling will print the source code. 
    """
    code = """
def get_x(n = 5) :
    for i in range(n , 0 , -1) :
        if i == 1 or i == 2 * n -1:
            print("  " * (n - i) + "*")
        else :
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")

    for i in range(2 , n + 1) :
        if i == 1 or i == 2 * n -1:
            print("  " * (n - i) + "*")
        else :
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")
get_x()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

# 10) GET RHOMBUS CODE
def get_rhombus_code() -> None :

    """
    Print the source code of the 'get_rhombus' function.

    This function generates and prints the source code of another function called 'get_rhombus'.
    The 'get_rhombus' function is used to print a rhombus pattern using asterisks ('*').

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_rhombus_code() will display the source code of the 'get_rhombus' function.

    Note:
        You do not require to use print function for printing the source code. Just function calling will print the source code. 
    """

    code = """
def get_rhombus(n = 5, inverted = False) :
    if inverted == False :
        for i in range(1 , n + 1) :
            print("  " * (n - i) + " * " * n)
        return

    for i in range(n , 0 , -1) :
        print("  " * (n - i) + " * " * n)
get_rhombus()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

# 11) GET HOLLOW RHOMBUS CODE
def get_hollow_rhombus_code() -> None :
    """
    Print the source code of the 'get_rhombus' function.

    This function generates and prints the source code of another function called 'get_rhombus'.
    The 'get_rhombus' function is used to print a hollow rhombus pattern using asterisks ('*').

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_rhombus_code() will display the source code of the 'get_rhombus' function.

    Note:
        You do not require to use print function for printing the source code. Just function calling will print the source code. 
    """

    code = """
def get_hollow_rhombus(n = 5, inverted = False) :
    if inverted == False :
        for i in range(1 , n + 1) :
            if i == 1 or i == n :
                print("  " * (n - i) + " * " * n)
            else :
                print("  " * (n - i) + " * " + "   " * (n - 2) + " *")
        return

    for i in range(n , 0 , -1) :
        if i == 1 or i == n :
            print("  " * (n - i) + " * " * n)
        else :
            print("  " * (n - i) + " * " + "   " * (n - 2) + " *")
get_hollow_rhombus()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

# 12) GET RECTANGLE CODE
def get_rectangle_code() -> None :

    """
    Print the source code of the 'get_rectangle' function.

    This function generates and prints the source code of another function called 'get_rectangle'.
    The 'get_rectangle' function is used to print a rectangle pattern using asterisks ('*').

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_rectangle_code() will display the source code of the 'get_rectangle' function.

    Note:
        You do not require to use print function for printing the source code. Just function calling will print the source code. 
    """
    code = """
def get_rectangle(n = 5) :
    for i in range(1 , n + 1) :
        print("*  " * n)
get_rectangle()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

# 13) GET HOLLOW RECTANGLE CODE
def get_hollow_rectangle_code() -> None :

    """
    Print the source code of the 'get_hollow_rectangle' function.

    This function generates and prints the source code of another function called 'get_hollow_rectangle'.
    The 'get_hollow_rectangle' function is used to print a hollow rectangle pattern using asterisks ('*').

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_hollow_rectangle_code() will display the source code of the 'get_hollow_rectangle' function.

    Note:
        You do not require to use print function for printing the source code. Just function calling will print the source code. 
    """

    code = """
def get_hollow_rectangle(n = 5) :
    for i in range(1 , n + 1) :
        if i == 1 or i == n :
            print("*  " * n)
        else :
            print("* " + "   " * (n - 2) + " *")
get_hollow_rectangle()
    """

    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)



# ALPHABETS PATTERNS CODE

# 1) GET ALPHABETS TRIANGLE CODE
def get_alpha_triangle_code() -> None :

    """
    Display the source code of the 'get_alpha_triangle' function with syntax highlighting.

    This function retrieves the source code of the 'get_alpha_triangle' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_alpha_triangle_code() will output the properly highlighted source code
        of the 'get_alpha_triangle' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_alpha_triangle(n = 5 , inverted = False) :
    asci = 65
    if inverted == False :
        for i in range(1 , n + 1) :
            for j in range(i) :
                print(chr(asci) , end = "  ")
                asci += 1
                if asci > 90 :
                    asci = 65
            print()
        return
        
    for i in range(n , 0 , -1) :
        for j in range(i) :
            print(chr(asci) , end = "  ")
            asci += 1
            if asci > 90 :
                asci = 65
        print()
get_alpha_triangle()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

# 2) GET ALPHABETS PYRAMID1 CODE
def get_alpha_pyramid1_code() -> None :

    """
    Display the source code of the 'get_alpha_pyramid1' function with syntax highlighting.

    This function retrieves the source code of the 'get_alpha_pyramid1' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_alpha_pyramid1_code() will output the properly highlighted source code
        of the 'get_alpha_pyramid1' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_alpha_pyramid1(n = 5 , inverted = False) :
    asci = 65
    if inverted == False :
        for i in range(1 , n + 1) :
            print("   " * (n - i) , end = "")
            for j in range(2*i - 1) :
                print(chr(asci) , end = "  ")
                asci += 1
                if asci > 90 :
                    asci = 65
            print()
        return

    for i in range(n , 0 , -1) :
        print("   " * (n - i) , end = "")
        for j in range(2*i - 1) :
            print(chr(asci) , end = "  ")
            asci += 1
            if asci > 90 :
                asci = 65
        print()
get_alpha_pyramid1()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

# 3) GET ALPHABETS PYRAMID2 CODE
def get_alpha_pyramid2_code() -> None :
    """
    Display the source code of the 'get_alpha_pyramid2' function with syntax highlighting.

    This function retrieves the source code of the 'get_alpha_pyramid2' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_alpha_pyramid2_code() will output the properly highlighted source code
        of the 'get_alpha_pyramid2' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_alpha_pyramid2(n = 5 , inverted = True) :
    asci = 65
    if inverted == False :
        for i in range(1 , n + 1) :
            print("  " * (n - i) , end = "")
            for j in range(i) :
                print(chr(asci) , end = "   ")
                asci += 1
                if asci > 90 :
                    asci = 65
            print()
        return

    for i in range(n , 0 , -1) :
        print("  " * (n - i) , end = "")
        for j in range(i) :
            print(chr(asci) , end = "   ")
            asci += 1
            if asci > 90 :
                asci = 65
        print()
get_alpha_pyramid2()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)



# NUMBER PATTERNS CODE

# 1) GET TRIANGLE1 CODE
def get_triangle1_code() -> None :
    """
    Display the source code of the 'get_triangle1' function with syntax highlighting.

    This function retrieves the source code of the 'get_triangle1' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_triangle1_code() will output the properly highlighted source code
        of the 'get_triangle1' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_triangle1(n = 5 , inverted = False) :
    spacing = len(str(n * (n + 1) // 2)) 
    start = 1

    if inverted == False :
        for i in range(1 , n + 1) :
            for j in range(i) :
                print(str(start + j).ljust(spacing) , end = "  ")
            start += i
            print()
        return

    for i in range(n) :
        for j in range(n - i) :
            print(str(start).ljust(spacing) , end = "  ")
            start += 1
        print()
get_triangle1()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

# 2) GET TRIANGLE2 CODE
def get_triangle2_code() -> None :
    """
    Display the source code of the 'get_triangle2' function with syntax highlighting.

    This function retrieves the source code of the 'get_triangle2' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_triangle2_code() will output the properly highlighted source code
        of the 'get_triangle2' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_triangle2(n = 5 , inverted = False) :
    spacing = len(str(n)) + 1
    if inverted == False :
        for i in range(1 , n + 1) :
            for j in range(i) :
                print(str(i + j).ljust(spacing) , end = "  ")
            print()
        return

    for i in range(1 , n + 1) :
        for j in range(n - i + 1) :
            print(str(i + j).ljust(spacing) , end = "  ")
        print()
get_triangle2()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

# 3) GET PYRAMID1 CODE
def get_pyramid1_code() -> None :
    """
    Display the source code of the 'get_pyramid1' function with syntax highlighting.

    This function retrieves the source code of the 'get_pyramid1' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_pyramid1_code() will output the properly highlighted source code
        of the 'get_pyramid1' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_pyramid1(n = 5 , inverted = False) :
    if inverted == False :
        for i in range(1 , n+1) :
            print(3*" " * (n - i) , end = "")
            for j in range(1 , i + 1) :
                print(str(j).ljust(3) , end = "")
            for k in range(i-1 , 0 , -1) :
                print(str(k).ljust(3) , end = "")
            print()
        return

    for i in range(n , 0 , -1) :
        print(3*" " * (n - i) , end = "")
        for j in range(1 , i + 1) :
            print(str(j).ljust(3) , end = "")
        for k in range(i-1 , 0 , -1) :
            print(str(k).ljust(3) , end = "")
    print()
get_pyramid1()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)


# 4) GET PYRAMID2 CODE
# def get_pyramid2_code() -> None :

#     """
#     Display the source code of the 'get_pyramid2' function with syntax highlighting.

#     This function retrieves the source code of the 'get_pyramid2' function and prints it
#     with syntax highlighting using a specified lexer and formatter.

#     Args:
#         None: This function does not return a value. It directly prints the code to the console.

#     Returns:
#         None: This function does not return a value. It directly prints the code to the console.

#     Example:
#         Calling get_pyramid2_code() will output the properly highlighted source code
#         of the 'get_pyramid2' function.

#     Note:
#         - You do not require to use print function for printing the source code. 
#           Just function calling will print the source code.  
#     """

#     code = """
# def get_pyramid2(n : int = 5 , inverted : bool = False) -> None :
#     if n <= 0 or type(n) != int :
#         raise ValueError("Parameter n should be positive integer")
        
#     if inverted == False :
#         for i in range(1 , n+1) :
#             print(3*" " * (n - i) , end = "")
#             for k in range(i-1 , 0 , -1) :
#                 print(str(k).ljust(3) , end = "")
#             for j in range(1 , i + 1) :
#                 print(str(j).ljust(3) , end = "")
#             print()
#         return

#     for i in range(n , 0 , -1) :
#         print(3*" " * (n - i) , end = "")
#         for k in range(i-1 , 0 , -1) :
#             print(str(k).ljust(3) , end = "")
#         for j in range(1 , i + 1) :
#             print(str(j).ljust(3) , end = "")
#         print()
# """

#     highlighted_code = highlight(code, lexer, formatter)
#     print(highlighted_code)

# 5) GET PASCAL'S TRIANGLE CODE
def get_pascal_triangle_code() -> None :

    """
    Display the source code of the 'get_pascal_triangle' function with syntax highlighting.

    This function retrieves the source code of the 'get_pascal_triangle' function and prints it
    with syntax highlighting using a specified lexer and formatter.

    Args:
        None: This function does not return a value. It directly prints the code to the console.

    Returns:
        None: This function does not return a value. It directly prints the code to the console.

    Example:
        Calling get_pascal_triangle_code() will output the properly highlighted source code
        of the 'get_pascal_triangle' function.

    Note:
        - You do not require to use print function for printing the source code. 
          Just function calling will print the source code.  
    """

    code = """
def get_pascal_triangle(n = 5) :
    if n < 10 :
        spacing = 3
    elif n <= 20 :
        spacing = 5
    else :
        print("Sorry, the input value is too large. Please provide a value of n that is 20 or less.")
        return
    for i in range(1 , n + 1) :
        print(spacing * " " * (n - i) , end = "")
        temp = 1
        for j in range(1 , i + 1) :
            print(str(temp).ljust(spacing) , end = " " * spacing)
            temp = temp * (i - j) // j
        print()
get_pascal_triangle()
"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)



"""
def get_triangle1_code() -> None :

    code = """


"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)


def get_triangle1_code() -> None :

    code = """


"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)

    
def get_triangle1_code() -> None :

    code = """


"""
    highlighted_code = highlight(code, lexer, formatter)
    print(highlighted_code)
"""
