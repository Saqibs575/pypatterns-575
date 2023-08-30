
# 1) GET TRIANGLE1
def get_triangle1(n : int = 5 , inverted : bool = False) -> None :
    """
    Generate and print a triangular number pattern.

    This function generates and prints a triangular number pattern based on the provided parameters.
    Triangular number pattern is a sequence of numbers where each row represents the first 'n'
    natural numbers arranged in a triangle. It can be displayed in both regular and inverted forms.

    Parameters:
        n (int, optional): The number of rows in the triangle. Should be a positive integer.
            Defaults to 5 if not provided.
        inverted (bool, optional): Determines whether to print the inverted form of the triangle.
            If True, the larger numbers will appear at the top of the triangle. If False, the
            smaller numbers will appear at the top. Defaults to False if not provided.

    Returns:
     None: This function doen't return anythin. It will print pattern to the console directly.

    Raises:
        ValueError: Raised when 'n' is not a positive integer.

    Example:
        get_triangle2(4)
        ```
        1   
        2   3   
        4   5   6   
        7   8   9   10  
        11  12  13  14  15 
        ```
        get_triangle2(4, inverted=True)
        ```
        1   2   3   4   5   
        6   7   8   9   
        10  11  12  
        13  14  
        15  
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if n is less than or equal to 0 or not an integr, and raise value error in case of True.
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")

    # Get spacing to print the space for better alignment.
    spacing = len(str(n * (n + 1) // 2)) 
    # Set start vaalue as 1
    start = 1

    # Check if inverted is True (Default condition).
    if inverted == False :
        # Loop through 1 to n (inclusive), for printing number of rows.
        for i in range(1 , n + 1) :
            # Loop through 0 to n (inclusive).
            for j in range(i) :
                # Print the number with spaces.
                print(str(start + j).ljust(spacing) , end = "  ")

            # Increment the start with factor i.
            start += i
            # Print the new line after each row.
            print()

        # Exist the function.
        return

    # Loop through 1 to n - 1 (inclusive), for printing number of rows.
    for i in range(n) :
        # Loop through 0 to n - i - 1 (inclusive), for printing number of rows.
        for j in range(n - i) :
            # Print the number with spaces.
            print(str(start).ljust(spacing) , end = "  ")
            # Increment the start with factor 1.
            start += 1
        # Print the new line after each row.
        print()


# 2) GET TRIANGLE2
def get_triangle2(n : int = 5 , inverted : bool = False) -> None :

    """
    Generate and print a triangular number pattern.

    This function generates and prints a triangular number pattern based on the provided parameters.
    Triangular number pattern is a sequence of numbers where each row represents the first 'n'
    natural numbers arranged in a triangle. It can be displayed in both regular and inverted forms.

    Parameters:
        n (int, optional): The number of rows in the triangle. Should be a positive integer.
            Defaults to 5 if not provided.
        inverted (bool, optional): Determines whether to print the inverted form of the triangle.
            If True, the larger numbers will appear at the top of the triangle. If False, the
            smaller numbers will appear at the top. Defaults to False if not provided.

    Raises:
        ValueError: Raised when 'n' is not a positive integer.

    returns:
        None: This function doesn't return anythimg. It prints the pattern to the console directly.

    Example:
        get_triangle2()
        ```
        1   
        2   3   
        3   4   5   
        4   5   6   7  
        5   6   7   8  9 
        ```
        get_triangle2(5, inverted=True)
        ```
        1   2   3   4   5   
        2   3   4   5   
        3   4   5  
        4   5  
        5
        ````
    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if n is less than or equal to 0 or not an integer, and raise a ValueError if true.
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")    

    # Calculate the width for aligning numbers based on the number of digits in n.
    spacing = len(str(n)) + 1

    # Check if "inverted" flag is True
    if inverted == False :
        # Loop through range from 1 to n (inclusive)
        for i in range(1 , n + 1) :
            # Loop through range from 0 to i - 1 (inclusive)
            for j in range(i) :
                # Print the number (i + j) left-justified with the specified spacing.
                print(str(i + j).ljust(spacing) , end = "  ")

            # Print the new line after each row is printed.
            print()

        # Exit the function if regular triangle is printed.
        return

    # If "inverted" flag is True.
    # Loop through range from 0 to i - 1 (inclusive)
    for i in range(1 , n + 1) :
        # Loop through range from 0 to n - i (inclusive)
        for j in range(n - i + 1) :
            # Print the number (i + j) left-justified with the specified spacing.
            print(str(i + j).ljust(spacing) , end = "  ")
        print()


# 3) GET PYRAMID1
def get_pyramid1(n : int = 5 , inverted : bool = False) -> None :

    """
    Generate and print a numeric pyramid pattern.

    This function generates and prints a pyramid pattern with numbers. The pattern can be either
    in a regular or inverted orientation based on the 'inverted' parameter.

    Parameters:
        n (int, optional): The number of rows in the pyramid. Default is 5.
        inverted (bool, optional): Whether the pyramid should be inverted. If True, the pyramid
                                   will be upside-down. If False, it will be right-side up. Default is False.

    Raises:
        ValueError: Raised if 'n' is not a positive integer.

    Returns:
        None: This function doesn't return any value. It prints the pattern directly.

    Example:
        To generate a regular pyramid with 7 rows:
        get_pyramid1(n=5, inverted=False)
        ```
                    1  
                 1  2  1  
              1  2  3  2  1  
           1  2  3  4  3  2  1  
        1  2  3  4  5  4  3  2  1  
        ```

        To generate an inverted pyramid with 4 rows:
        get_pyramid1(n=5, inverted=True)
        ```
        1  2  3  4  5  4  3  2  1  
           1  2  3  4  3  2  1  
              1  2  3  2  1  
                 1  2  1  
                    1  
        ```
    
    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if n is a positive integer, otherwise raise a ValueError
    if n <= 0 or type(n) != int :
        raise ValueError("Parameter n should be positive integer")

    # If iverted is False (Default case), print regular pyramid.
    if inverted == False :
    # Generate the pyramid with ascending and descending sequence
        for i in range(1 , n+1) :
            # Print spaces to center-align the pyramid
            print(3*" " * (n - i) , end = "")

            # Print ascending sequence of numbers
            for j in range(1 , i + 1) :
                print(str(j).ljust(3) , end = "")

            # Print descending sequence of numbers
            for k in range(i-1 , 0 , -1) :
                print(str(k).ljust(3) , end = "")

            # Moveto the new line after printing each row.
            print()

        # Exit the function in case of regular pyramid
        return

    # If inverted is True, then print inverted pyramid
    # Generate the pyramid with ascending and descending sequence
    for i in range(n , 0 , -1) :
        # Print spaces to center-align the pyramid
        print(3*" " * (n - i) , end = "")

        # Print ascending sequence of numbers
        for j in range(1 , i + 1) :
            print(str(j).ljust(3) , end = "")

        # Print descending sequence of numbers
        for k in range(i-1 , 0 , -1) :
            print(str(k).ljust(3) , end = "")
        print()

# 4) GET PYRAMID2
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

# 5) GET PASCAL'S TRIANGLE
def get_pascal_triangle(n : int = 5) -> None :

    """
    Generate and print Pascal's triangle up to 'n' rows.

    This function generates Pascal's triangle, a geometric arrangement of numbers where
    each row begins and ends with 1, and each interior number is the sum of the two numbers
    directly above it from the previous row.

    Args:
        n (int, optional): The number of rows to generate in Pascal's triangle. Defaults to 5.

    Raises:
        ValueError: If 'n' is not a positive integer.

    Returns:
        None: This function prints the Pascal's triangle rather than returning it.

    Example:
        get_pascal_triangle()
        ```
                    1
                 1     1
              1     2     1
           1     3     3     1
        1     4     6     4     1
    
        ```
    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
    """

    # Check if n is non-positive or not an integer, and raise a ValueError if so.
    if n <= 0 or type(n) != int :
        raise ValueError("parameter n should be positive integer")

    # Determine the spacing for formatting based on the value of n.
    if n < 10 :
        spacing = 3
    elif n <= 20 :
        spacing = 5
    else :
        # If n is greater than 20, print a message and return early from the function.
        print("Sorry, the input value is too large. Please provide a value of n that is 20 or less.")
        return

    # Iterate through the range from 1 to n+1 (inclusive).
    for i in range(1 , n + 1) :
        # Print spaces based on the value of (n - i) for alignment.
        print(spacing * " " * (n - i) , end = "")

        # Initialize a temporary variable 'temp' with the value 1.
        temp = 1

        # Iterate through the range from 1 to i+1 (inclusive).
        for j in range(1 , i + 1) :
            # Print the value of 'temp' left-justified and padded with spaces based on 'spacing'.
            print(str(temp).ljust(spacing) , end = " " * spacing)
            # Update the value of 'temp' using the formula for the next term in Pascal's triangle.
            temp = temp * (i - j) // j

        # Move to the next line after printing a row of values.
        print()
