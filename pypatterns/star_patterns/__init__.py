
# GET STAR PYRAMID
def get_star_pyramid(n : int = 5 , inverted : bool = False) -> None :

    """
    Generate and print a star pyramid pattern based on the given parameters.

    Args:
        n (int, optional): The number of rows in the pyramid. Should be a positive integer.
                           Defaults to 5.

        inverted (bool, optional): Determines whether the pyramid should be inverted or not.
                                   If True, the pyramid is upside down. If False (default),
                                   the pyramid is upright.

    Raises:
        ValueError: Raised when the input `n` is less than or equal to 0 or not an integer.

    Returns:
        None: This function does not return a value. It prints the pyramid pattern directly.

    Patterns:
        Upright Pyramid (inverted=False):
        For each row i in the range 1 to n (inclusive), the function prints spaces
        followed by asterisks in a pattern that forms a pyramid shape.

        Inverted Pyramid (inverted=True):
        For each row i in the range n to 1 (inclusive), the function prints spaces
        followed by asterisks in a pattern that forms an inverted pyramid shape.

    Example:

        To print an upright pyramid with 5 rows:
        get_start_pyramid(5)
        ```
                    * 
                 *  *  * 
              *  *  *  *  * 
           *  *  *  *  *  *  * 
        *  *  *  *  *  *  *  *  * 
        ```

        To print an inverted pyramid with 5 rows:
        get_star_pyramid(5, inverted=True)
        ```
        *  *  *  *  *  *  *  *  * 
           *  *  *  *  *  *  * 
              *  *  *  *  * 
                 *  *  * 
                    * 
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if n is less than or equal to 0 or not an integer.
    # Raise a ValueError if the condition is met.
    if n <= 0 or type(n) != int :
        # Raise a ValueError with the specified error message.
        raise ValueError("Parameter n should be positive integer")

    # Check if the inverted parameter is False (default behavior).
    if inverted == False :

        # Iterate over a range of numbers from 1 to n (inclusive).
        for i in range(1 , n + 1) :
            # Print spaces multiplied by (n - i) followed by asterisks multiplied by (2 * i - 1)
            # This creates a pattern of spaces and asterisks for each row.
            print("   " * (n - i) + " * " * (2 * i - 1))
        # Exit the function after printing the pyramid (non-inverted).
        return
    
    # Iterate over a range of numbers from n to 1 (inclusive), in reverse order.
    for i in range(n , 0 , -1) :
        # Similar to the previous loop, print the pattern for each row, but in reverse order.
        print("   " * (n - i) + " * " * (2 * i - 1))

# GET STAR HOLLOW PYRAMID
def get_star_hollow_pyramid(n : int = 5 , inverted : bool = False) -> None :
    
    """
    Generate and print a pattern of stars (*) representing a hollow pyramid or an inverted hollow pyramid.

    Parameters:
        n (int): The number of rows in the pyramid. Should be a positive integer.
        inverted (bool): Flag indicating whether to print an inverted pyramid. Default is False.

    Raises:
        ValueError: If n is not a positive integer.
    
    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    Prints a pattern of stars in the console, creating either a hollow pyramid or an inverted hollow pyramid.
    The pattern is formed by rows of asterisks and spaces, arranged to create the desired pyramid shape.
    For a non-inverted pyramid, the top and bottom rows are solid lines of asterisks, while the middle rows
    have asterisks at the ends and spaces in between to create the hollow effect. For an inverted pyramid,
    the pattern is reversed, and the wider part is at the top.

    Example:

        To print an upright hollow pyramid with 5 rows:
        get_star_hollow_pyramid(5)
        ```
                * 
              *   *
            *       *
          *           *
        * * * * * * * * *  
        ```

        To print an inverted hollow pyramid with 5 rows:
        get_star_hollow_pyramid(5, inverted=True)
        ```
        * * * * * * * * * 
          *           *
            *       *
              *   *
                * 
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """
    # Check if n is a positive integer; raise an error if not.
    if n <= 0 or type(n) != int :
        # Raise a ValueError with a specific error message if the error condition is met.
        raise ValueError("Parameter n should be positive integer")

    # Check if the inverted flag is False.
    if inverted == False :

        # Iterate through the range from 1 to n (inclusive).
        for i in range(1 , n + 1) :
            # Check if it's the first or last row of the hollow pyramid.
            if i == 1 or i == n :
                # Print spaces and asterisks to create the solid lines of the hollow pyramid.
                print("  " * (n - i) + "* " * (2 * i - 1))
            else :
                # Print spaces and asterisks to create the hollow lines of the hollow pyramid.
                print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")  
        # Exit the function if the inverted flag is False.
        return

    # Iterate through the range from n to 1 in reverse.
    for i in range(n , 0 , -1) :
        # Check if it's the first or last row of the hollow pyramid.
        if i == 1 or i == n :
            # Print spaces and asterisks to create the solid lines of the hollow pyramid.
            print("  " * (n - i) + "* " * (2 * i - 1))
        else :
            # Print spaces and asterisks to create the hollow lines of the hollow pyramid.
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")

# GET STAR PYRAMID2
def get_star_pyramid2(n : int = 5, inverted : bool = False) -> None :

    """
    Generate and print a star pyramid pattern based on the given parameters.

    Args:
        n (int, optional): The number of rows in the pyramid. Should be a positive integer.
                           Defaults to 5.

        inverted (bool, optional): Determines whether the pyramid should be inverted or not.
                                   If True, the pyramid is upside down. If False (default),
                                   the pyramid is upright.

    Raises:
        ValueError: Raised when the input `n` is less than or equal to 0 or not an integer.

    Returns:
        None: This function does not return a value. It prints the pyramid pattern directly.

    Patterns:
        Upright Pyramid (inverted=False):
        For each row i in the range 1 to n (inclusive), the function prints spaces
        followed by asterisks in a pattern that forms a pyramid shape.

        Inverted Pyramid (inverted=True):
        For each row i in the range n to 1 (inclusive), the function prints spaces
        followed by asterisks in a pattern that forms an inverted pyramid shape.

    Example:

        To print an upright pyramid with 5 rows:
        get_start_pyramid2(5)
        ```
                *  
              *   *  
            *   *   *  
          *   *   *   *  
        *   *   *   *   * 
        ```

        To print an inverted pyramid with 5 rows:
        get_star_pyramid2(5, inverted=True)
        ```
        *   *   *   *   *  
          *   *   *   *  
            *   *   *  
              *   *  
                *  
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if n is less than or equal to 0 or not an integer.
    # Raise a ValueError if the condition is met.
    if n <= 0 or type(n) != int :
        # Raise a ValueError with the specified error message.
        raise ValueError("parameter n should be positive integer")

    # Check if the inverted parameter is False (default behavior).
    if inverted == False :
        # Iterate over a range of numbers from 1 to n (inclusive).
        for i in range(1 , n + 1) :
            # Print spaces multiplied by (n - i) followed by asterisks multiplied by i
            # This creates a pattern of spaces and asterisks for each row.
            print("  " * (n - i) + " *  " * i)

        # Exit the function after printing the pyramid (non-inverted).
        return

    for i in range(n , 0 , -1) :
        print("  " * (n - i) + " *  " * i)

# GET STAR TRIANGLE
def get_star_triangle(n : int = 5 , inverted : bool = False) -> None :

    """
    Generate and print a triangle pattern using "*" based on the provided parameters.

    This function generates a triangle pattern using asterisk ('*') characters and optional inversion.
    The triangle can be printed in a regular or inverted orientation.

    Parameters:
        n (int): The number of rows in the triangle. Must be a positive integer.
                 The default value is 5.
                 
        inverted (bool): Determines whether the triangle should be printed in an inverted orientation.
                         If False, the triangle is printed in a regular orientation (increasing rows of stars).
                         If True, the triangle is printed in an inverted orientation (decreasing rows of stars).
                         The default value is False.

    Raises:
        ValueError: If the provided value for 'n' is less than or equal to 0, or if it is not an integer.

    Returns:
        None: This function does not return any values. It prints the triangle pattern directly to the console.

    Example:

        To print an upright triangle with 5 rows:
        get_star_triangle(5)
        ```
        *  
        *  *  
        *  *  *  
        *  *  *  *  
        *  *  *  *  * 
        ```

        To print an inverted triangle with 5 rows:
        get_star_triangle(5, inverted=True)
        ```
        *  *  *  *  *  
        *  *  *  *  
        *  *  *  
        *  *  
        * 
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if the value of 'n' is less than or equal to 0, or if its type is not 'int'.
    # If either condition is True, raise a ValueError with a corresponding error message.
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")

    # Check if the value of 'inverted' is False.
    # If it is, execute the following block of code (non-inverted triangle).
    if inverted == False :
        # Iterate over a range of numbers from 1 to 'n' (inclusive).
        # For each number 'i' in the range, execute the following block of code.
        for i in range(1 , n + 1) :
            # Print a string containing '*' followed by two spaces, repeated 'i' times.
            # This prints a row of asterisks with increasing count in each row.
            print("*  " * i)

        # Exit the function after printing the non-inverted triangle.
        return

    # If 'inverted' is True, iterate over a range of numbers from 'n' to 1 in reverse order.
    # For each number 'i' in the range, execute the following block of code.
    for i in range(n , 0 , -1) :
        # Print a string containing '*' followed by two spaces, repeated 'i' times.
        # This prints a row of asterisks with decreasing count in each row.
        print("*  " * i)

# GET STAR HOLLOW TRIANGLE
def get_star_hollow_triangle(n : int = 5 , inverted : bool = False) -> None :

    """
    Print a pattern of star-filled triangles with optional inversion and hollow lines.

    This function prints a triangle pattern composed of asterisks, with the option to invert the triangle
    and create hollow lines within the triangles.

    Parameters:
        n (int): The number of rows in the triangle. Should be a positive integer.
        inverted (bool): A flag indicating whether the triangle should be inverted or not.
                        If True, the triangle is printed upside-down. If False, it's printed normally.

    Raises:
        ValueError: If n is not a positive integer.

    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    Example:

        To print an upright triangle with 5 rows:
        get_star_hollow_triangle(5)
        ```
        * 
        * *
        *   *
        *     *
        * * * * * 
        ```

        To print an inverted triangle with 5 rows:
        get_star_hollow_triangle(5, inverted=True)
        ```
        * * * * * 
        *     *
        *   *
        * *
        * 
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if n is a positive integer; raise an error if not.
    if n <= 0 or type(n) != int :
        # Raise a ValueError with a specific error message if the error condition is met.
        raise ValueError("Parameter n should be positive integer")

    # Check if the inverted flag is False.
    if inverted == False :
        # Iterate through the range from 1 to n (inclusive).
        for i in range(1 , n + 1) :
            # Check if it's the first or last row of the triangle.
            if i == 1 or i == n :
                # Print spaces and asterisks to create the solid lines of the triangle.
                print("* " * i)
            else :
                # Print spaces and asterisks to create the solid lines of the triangle.
                print("* " + "  " * (i - 2) + "*")
                
        # Exit the function if the inverted flag is False.
        return

    # Iterate through the range from n to 1 in reverse.
    for i in range(n , 0 , -1) :
    # Check if it's the first or last row of the triangle.
        if i == 1 or i == n :
        # Print spaces and asterisks to create the solid lines of the triangle.
            print("* " * i)
        else :
        # Print spaces and asterisks to create the hollow lines of the triangle.
            print("* " + "  " * (i - 2) + "*")

# GET STAR DIAMOND
def get_star_diamond(n : int = 5) -> None :

    """
    Print a pattern of asterisks that forms a Diamond shape.

    Args:
        n (int, optional): The number of rows in the upeer part of. Defaults to 5.

    Raises:
        ValueError: Raised if the input n is not a positive integer.

    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    Example:

        To print an upright diamond with 5 rows:
        get_star_diamond(5)
        ```
                    * 
                 *  *  * 
              *  *  *  *  * 
           *  *  *  *  *  *  * 
        *  *  *  *  *  *  *  *  * 
           *  *  *  *  *  *  * 
              *  *  *  *  * 
                 *  *  * 
                    * 
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if the provided value of "n" is not a positive integer or is less than or equal to 0.
    # If so, raise a ValueError with an appropriate error message.
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")


    # Iterate through a range of numbers from 1 to (n + 1).
    for i in range(1 , n + 1) :
        # For each iteration, print spaces multiplied by (n - i) and asterisks multiplied by (2 * i - 1).
        print("  " * (n - i) + "* " * (2 * i - 1))

    # Iterate through a range of numbers from (n - 1) down to 1.
    for i in range(n - 1 , 0 , -1) :
        # For each iteration, print spaces multiplied by (n - i) and asterisks multiplied by (2 * i - 1).
        print("  " * (n - i) + "* " * (2 * i - 1))

# GET STAR DIAMOND2
def get_star_diamond2(n : int = 5) -> None :

    """
    Print a pattern of asterisks that forms a Diamond shape.

    Args:
        n (int, optional): The number of rows in the upeer part of. Defaults to 5.

    Raises:
        ValueError: Raised if the input n is not a positive integer.

    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    Example:

        To print an upright diamond with 5 rows:
        get_star_diamond2(5)
        ```
                    *   
                 *     *   
              *     *     *   
           *     *     *     *   
        *     *     *     *     *   
           *     *     *     *   
              *     *     *   
                 *     *   
                    *   
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if the provided value of "n" is not a positive integer or is less than or equal to 0.
    # If so, raise a ValueError with an appropriate error message.
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")


    # Iterate through a range of numbers from 1 to (n + 1).
    for i in range(1 , n + 1) :
        # For each iteration, print spaces multiplied by (n - i) and asterisks multiplied by (2 * i - 1).
        print("  " * (n - i) + " *  " * i)

    # Iterate through a range of numbers from (n - 1) down to 1.
    for i in range(n - 1 , 0 , -1) :
        # For each iteration, print spaces multiplied by (n - i) and asterisks multiplied by (2 * i - 1).
        print("  " * (n - i) + " *  " * i)

# GET STAR HOLLOW DIAMOND
def get_star_hollow_diamond(n : int = 5) -> None :

    """
    Print a pattern of asterisks that forms a hollow right angled hollow diamond.

    Args:
        n (int, optional): The number of rows in the upper half of Diamond. Defaults to 5.

    Raises:
        ValueError: Raised if the input n is not a positive integer.

    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    Example:

        To print an upright hollow diamond with 5 rows:
        get_star_hollow_diamond(5)
        ```
                *
              *   *
            *       *
          *           *
        *               *
          *           *
            *       *
              *   *
                *
        ```
    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if n is non-positive or not an integer, raise an error if so
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")

    # Loop through the upper half of the diamond pattern
    for i in range(1 , n + 1) :
        # For the first and last rows, print a single asterisk
        if i == 1 or i == 2 * n -1:
            print("  " * (n - i) + "*")

        # For other rows, print asterisks separated by spaces to form a hollow diamond pattern
        else :
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")

    # Loop through the lower half of the diamond pattern
    for i in range(n - 1 , 0 , -1) :
        # For the first and last rows in this half, print a single asterisk
        if i == 1 or i == 2 * n -1:
            print("  " * (n - i) + "*")

        # For other rows, print asterisks separated by spaces to complete the hollow diamond pattern
        else :
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")

# GET X ALPHABET
def get_x(n : int = 5) -> None :

    """
    Print a pattern resembling the letter 'X' composed of asterisks ('*') and spaces.

    This function generates a visual pattern in the shape of the letter 'X', using asterisks and spaces.
    The pattern is composed of two halves: an upper half and a lower half. Each half consists of lines
    of asterisks that form the distinct 'X' shape. The provided size parameter 'n' determines the size
    of the pattern, allowing for customization of the scale.

    Args:
        n (int, optional): The size parameter for the pattern. Default is 5.
            The value must be a positive integer indicating the size of the pattern.
            Larger values of 'n' will create more intricate and detailed patterns.

    Raises:
        ValueError: If the provided value of 'n' is not a positive integer.
            This exception is raised to prevent invalid inputs that would not produce a meaningful pattern.

    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    Pattern Details:
        The generated pattern has an upper half and a lower half, both resembling the letter 'X'.
        Each half consists of multiple lines, with each line containing a combination of asterisks and spaces.
        The asterisks are strategically placed to form the 'X' shape.

    Examples:
        Calling 'get_x()' with the default value of 'n' (5) produces the following pattern:
        ```
        *               *
          *           *
            *       *
              *   *
                *
              *   *
            *       *
          *           *
        *               *
            
        ```

    Note:
        - The pattern generated by this function is optimized for odd values of 'n'. Even values of 'n' may
          result in patterns that are not symmetric due to the integer division used to calculate spaces.
        - You do not require to use print function for printing the source code. 
          Just function calling will print the pattern.
    """

    # Check if the input value n is less than or equal to 0 or not an integer
    if n <= 0 or type(n) != int :
        # Raise a ValueError with a message if the error condition is met
        raise ValueError("Parameter n should be positive integer")

    # Loop from n down to 1 (inclusive) with a step of -1 for printing upper half of X
    for i in range(n , 0 , -1) :
        # Check if i is equal to 1 or 2*n - 1
        if i == 1 or i == 2 * n -1:
             # Print '*' with leading spaces based on the current iteration
            print("  " * (n - i) + "*")
        else :
            # Print a pattern of '*' and spaces based on the current iteration
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")
    # Loop from 2 up to n (inclusive) for printing lower half of X
    for i in range(2 , n + 1) :
        # Check if i is equal to 1 or 2*n - 1
        if i == 1 or i == 2 * n -1:
            # Print '*' with leading spaces based on the current iteration
            print("  " * (n - i) + "*")
        else :
            # Print a pattern of '*' and spaces based on the current iteration
            print("  " * (n - i) + "* " + "  " * (2*i - 3) + "*")

# GET RHOMBUS
def get_rhombus(n : int = 5 , inverted : bool = False) -> None :

    """
    Print a rhombus pattern composed of asterisks (*).

    This function prints a rhombus pattern composed of asterisks (*)
    with the specified size and orientation.

    Parameters:
        n (int): The size of the rhombus. This should be a positive integer greater
                 than zero. The size corresponds to the number of rows in the rhombus
                 from the center to the edges.
        inverted (bool): Specifies the orientation of the rhombus. If set to False,
                         the rhombus will be point-up, with its widest part at the bottom.
                         If set to True, the rhombus will be point-down, with its widest
                         part at the top. Default is False.

    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    Raises:
        ValueError: If the 'n' parameter is not a positive integer.

    Examples:
        get_rhombus()
        ```
                *  *  *  *  * 
              *  *  *  *  * 
            *  *  *  *  * 
          *  *  *  *  * 
        *  *  *  *  * 
        ```

    Note:
        - The function ensures that the provided 'n' parameter is a positive integer,
          and raises a ValueError if it's not.
        - The generated rhombus pattern consists of 'n' rows, and each row contains
          asterisks (*) arranged in a rhombus shape.
        - The indentation of asterisks creates the rhombus pattern, with spaces used
          to align the pattern based on the current row and size.
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if the input value n is less than or equal to 0 or not an integer
    if n <= 0 or type(n) != int :
        # Raise a ValueError with a message if the error condition is met
        raise ValueError("Parameter n should be positive integer")
    
    # Check if inverted is False (default case)
    if inverted == False :
        # Loop from 1 to n (inclusive)
        for i in range(1 , n + 1) :
            # Print spaces followed by '*' repeated n times
            print("  " * (n - i) + " * " * n)
        # Exit the function
        return

    # If inverted is True print inverted rhombus
    # Loop from n to 1 (inclusive)
    for i in range(n , 0 , -1) :
        # Print spaces followed by '*' repeated n times
        print("  " * (n - i) + " * " * n)

# GET HOLLOW RHOMBUS
def get_hollow_rhombus(n : int = 5 , inverted : bool = False) -> None :

    """
    Print a hollow rhombus pattern composed of asterisks (*).

    This function prints a hollow rhombus pattern composed of asterisks (*)
    with the specified size and orientation.

    Parameters:
        n (int): The size of the hollow rhombus. This should be a positive integer greater
                 than zero. The size corresponds to the number of rows in the rhombus
                 from the center to the edges.
        inverted (bool): Specifies the orientation of the rhombus. If set to False,
                         the rhombus will be point-up, with its widest part at the bottom.
                         If set to True, the rhombus will be point-down, with its widest
                         part at the top. Default is False.

    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    Raises:
        ValueError: If the 'n' parameter is not a positive integer.

    Examples:
        get_rhombus()
        ```
                *  *  *  *  * 
              *  *  *  *  * 
            *  *  *  *  * 
          *  *  *  *  * 
        *  *  *  *  * 
        ```

    Note:
        - The function ensures that the provided 'n' parameter is a positive integer,
          and raises a ValueError if it's not.
        - The generated hollow rhombus pattern consists of 'n' rows, and each row contains
          asterisks (*) arranged in a hollow rhombus shape.
        - The indentation of asterisks creates the hollow rhombus pattern, with spaces used
          to align the pattern based on the current row and size.
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if the input value n is less than or equal to 0 or not an integer
    if n <= 0 or type(n) != int :
        # Raise a ValueError with a message if the error condition is met
        raise ValueError("Parameter n should be positive integer")

    # Check if inverted is False (default case)
    if inverted == False :
        # Loop from 1 to n (inclusive)
        for i in range(1 , n + 1) :
            # if we are in first or last row print asterisks in entire line
            if i == 1 or i == n :
                # Print '*' repeated n times
                print("  " * (n - i) + " * " * n)
            else :
                # Print spaces followed by '*' repeated n times
                print("  " * (n - i) + " * " + "   " * (n - 2) + " *")
        # Exit the function
        return

    # If inverted is True print inverted rhombus
    # Loop from n to 1 (inclusive)
    for i in range(n , 0 , -1) :
        # if we are in first or last row print asterisks in entire line
        if i == 1 or i == n :
            # Print '*' repeated n times
            print("  " * (n - i) + " * " * n)
        else :
            # Print spaces followed by '*' repeated n times
            print("  " * (n - i) + " * " + "   " * (n - 2) + " *")

# GET RECTANGLE
def get_rectangle(n : int = 5) -> None :
    """
    Print a rectangle made of asterisks (*), with each side of length 'n'.

    Parameters:
        n (int, optional): The length of each side of the rectangle. Defaults to 5.

    Raises:
        ValueError: If 'n' is not a positive integer.

    Returns:
        None: This function does not return a value. It directly prints the console to the console.

    This function prints a rectangle using asterisks (*), where each side has 'n' asterisks.
    The function validates the input 'n' to ensure it is a positive integer. If 'n' is not a
    positive integer, a ValueError is raised. The rectangle is printed by looping through the
    range of numbers from 1 to 'n+1' and printing 'n' asterisks for each row, separated by spaces.

    Example:
        get_rectangle(4)
        ```
        *  *  *  *
        *  *  *  *
        *  *  *  *
        *  *  *  *
        ```
        get_rectangle()
        ```
        *  *  *  *  *
        *  *  *  *  *
        *  *  *  *  *
        *  *  *  *  *
        *  *  *  *  *
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if the input value n is less than or equal to 0 or not an integer
    if n <= 0 or type(n) != int :
        # Raise a ValueError with a message if the error condition is met
        raise ValueError("Parameter n should be positive integer")
    
    # Iterate through a range of numbers from 1 to n (inclusive) and print n repetitions of "*  ".
    for i in range(1 , n + 1) :
        print("*  " * n)

# GET HOLLOW RECTANGLE
def get_hollow_rectangle(n : int = 5) -> None :

    """
    Print a hollow rectangle made of asterisks (*), with each side of length 'n'.

    Parameters:
        n (int, optional): The length of each side of the rectangle. Defaults to 5.

    Raises:
        ValueError: If 'n' is not a positive integer.

    Returns:
        None: This function does not return a value. It directly prints the pattern to the console.

    This function prints a hollow rectangle using asterisks (*), where each side has 'n' asterisks.
    The function validates the input 'n' to ensure it is a positive integer. If 'n' is not a
    positive integer, a ValueError is raised. The rectangle is printed by looping through the
    range of numbers from 1 to 'n+1' and printing asterisks corresponds to each row, separated by spaces.

    Example:
        get_rectangle(4)
        ```
        *  *  *  *
        *        *
        *        *
        *  *  *  *
        ```

        get_rectangle()
        ```
        *  *  *  *  *
        *           *
        *           *
        *           *
        *  *  *  *  *
        ```
    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if the input value n is less than or equal to 0 or not an integer
    if n <= 0 or type(n) != int :
        # Raise a ValueError with a message if the error condition is met
        raise ValueError("Parameter n should be positive integer")

    # Iterate through a range of numbers from 1 to n (inclusive).
    for i in range(1 , n + 1) :
        # If it is first or last row then print "*  " n times.
        if i == 1 or i == n :
            print("*  " * n)
        else :
            # Other than first and the last row print stars only at begining and ending to get hollow rectangle.
            print("* " + "   " * (n - 2) + " *")
