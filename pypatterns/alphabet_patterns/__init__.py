
# 1) GET ALPHABETS TRIANGLE
def get_alpha_triangle(n : int = 5 , inverted : bool = False) -> None :

    """
    Generates and prints a triangular pattern of uppercase letters.

    This function prints a triangular pattern of uppercase letters from 'A' to 'Z'
    in rows and columns. The pattern can be oriented in two ways: regular or inverted.

    Args:
        n (int, optional): The number of rows in the triangle. Default is 5.

        inverted (bool, optional): Flag to determine the orientation of the triangle.
                                   If False (default), the triangle is oriented in a regular manner.
                                   If True, the triangle is inverted, i.e., the apex is at the bottom.

    Raises:
        ValueError: Raised when the provided `n` is not a positive integer.

    Returns:
        None: This function doesn't return any value. It directly prints the triangle pattern.

    Example:
        get_alpha_triangle1(4, False)
        ```
        A
        B  C
        D  E  F
        G  H  I  J
        ```
        get_alpha_triangle1(3, True)
        ```
        A  B  C  D  
        E  F  G  
        H  I  
        J  
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern. 
    """

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

# 2) GET ALPHABETS PYRAMID1
def get_alpha_pyramid1(n : int = 5 , inverted : bool = False) -> None :

    """
    Generates and prints a character pyramid pattern based on the specified parameters.

    Args:
        n (int, optional): The number of rows in the pyramid. Should be a positive integer. Defaults to 5.

        inverted (bool, optional): Specifies whether the pyramid should be inverted or not.
                                   If True, the pyramid is inverted; if False, it's not inverted. Defaults to False.

    Raises:
        ValueError: Raised if the value of 'n' is not a positive integer.

    Returns:
        None: This function doesn't return a value, it prints the pyramid pattern directly.

    The function 'get_pyramid' generates a character pyramid pattern using uppercase English letters. The pattern
    can be inverted or not, depending on the 'inverted' parameter. Each row of the pyramid contains a sequence of
    characters starting from 'A' (ASCII 65) and cycling through the alphabet until 'Z', then wrapping back to 'A'.

    The pyramid is created using nested loops and the 'chr' function to convert ASCII values to characters.
    For each row, the appropriate number of spaces is added at the beginning to maintain the pyramid shape.
    The number of characters in each row is calculated using the formula: 2*i - 1, where 'i' represents the row number.

    Example usage:
        get_alpha_pyramid1(3, False)
        ```

              A  
           B  C  D  
        E  F  G  H  I  

        ```
        get_alpha_pyramid1(3, True)
        ```

        A  B  C  D  E  
           F  G  H  
              I  
        ```

    Note: 
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern. 
    """

    # Check if n is a positive integer, otherwise raise a ValueError
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")

    # Initialize the ASCII value for character printing
    asci = 65

    # If inverted is False, print the triangle in regular order
    if inverted == False :

        # Loop through rows from 1 to n
        for i in range(1 , n + 1) :
            # printing leading spaces
            print("   " * (n - i) , end = "")
            # Loop through columns based on the current row
            for j in range(2*i - 1) :
                # printing character and spaces
                print(chr(asci) , end = "  ")

                # Increment ASCII value to get next character
                asci += 1

                # Reset ASCII value if it excedds 'Z'
                if asci > 90 :
                    asci = 65

            # Move to the next line after each row is printed
            print()
        return

    # If pyramid is inverted, iterate over rows from n to 1
    for i in range(n , 0 , -1) :
        # printing leading spaces
        print("   " * (n - i) , end = "")
        # Loop through columns based on the current row
        for j in range(2*i - 1) :
            # printing character and spaces
            print(chr(asci) , end = "  ")

            # Increment ASCII value to get next character
            asci += 1
            # Reset ASCII value if it excedds 'Z'
            if asci > 90 :
                asci = 65

        # Move to the next line after each row is printed
        print()

# 3) GET ALPHABETS PYRAMID2
def get_alpha_pyramid2(n : int = 5 , inverted : bool = False) -> None :

    """
    Generate and print a pyramid pattern of characters in rows with optional inversion.

    Parameters:
        n (int): The number of rows in the pyramid. Should be a positive integer.
        inverted (bool): A flag indicating whether the pyramid should be inverted or not.
                         If True, the pyramid will be inverted; if False, it will be upright.
                         Default is False.

    Raises:
        ValueError: If the parameter n is not a positive integer.

    This function generates a pyramid pattern using uppercase English alphabet characters,
    starting from 'A'. The pattern can be either an inverted pyramid (with the apex at the
    bottom) or an upright pyramid (with the apex at the top). The characters are printed
    in rows, with each row containing a sequence of characters. The sequence of characters
    starts from 'A' and loops back to 'A' after 'Z'.

    Example usage:
        get_alpha_pyramid2(4, inverted=False)
        ```
              A   
            B   C   
          D   E   F   
        G   H   I   J
        ```

        get_alpha_pyramid2(4, inverted=True)
        ```
        A   B   C   D
          E   F   G   
            H   I
              J 
        ```
    Note: 
        - The function will not return any value (None), it will directly print the pattern. 
          So ,don't use print function to print you pattern.
    """

    # Check if n is a positive integer, otherwise raise a ValueError
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")

    # Initialize the ASCII value for character printing
    asci = 65

    # If inverted is False, print the triangle in regular order
    if inverted == False :

        # Loop through rows from 1 to n
        for i in range(1 , n + 1) :
            # printing leading spaces
            print("  " * (n - i) , end = "")

            # Iterate 'i' times....
            for j in range(i) :
                # printing character and spaces
                print(chr(asci) , end = "   ")
                # Increment ASCII value to get next character
                asci += 1
                # Reset ASCII value if it excedds 'Z'
                if asci > 90 :
                    asci = 65

            # Move to the next line after each row is printed
            print()
        return

    # If pyramid is inverted, iterate over rows from n to 1
    for i in range(n , 0 , -1) :
        # printing leading spaces
        print("  " * (n - i) , end = "")
        # Loop through columns based on the current row
        for j in range(i) :
            # printing character and spaces
            print(chr(asci) , end = "   ")

            # Increment ASCII value to get next character
            asci += 1
            # Reset ASCII value if it excedds 'Z'
            if asci > 90 :
                asci = 65

        # Move to the next line after each row is printed
        print()

