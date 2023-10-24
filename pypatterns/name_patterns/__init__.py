from pypatterns.name import Name

def get_name(name=None, symbol=None, animate=False):

    """
    Generate and print your name consisting of any symbol from keyboard (`*` id default).

    Args:
        name : The name or string you want to print.

        symbol (str, optional): Symbol using which you want to print your string.

    Raises:
        ValueError: Raised when the input `name` contains non alphabets or space.

    Returns:
        None: This function does not return a value. It prints the pyramid pattern directly.

    Example:

        To print an upright pyramid with 5 rows:
        get_name(name="SAQIB", symbol="/")
        ```
           / / /         / /         / / /     / / / / /   / / / /    
         /       /     /     /     /       /       /       /       /  
        /             /       /   /         /      /       /        / 
         /           /         /  /         /      /       /       /  
           / / /     / / / / / /  /         /      /       / / / /    
                 /   /         /  /         /      /       /       /  
                  /  /         /  /      /  /      /       /        / 
         /       /   /         /   /       /       /       /       /  
           / / /     /         /     / / /   / / / / / /   / / / /    
        ```

    Note:
        - You do not require to use print function for printing the pattern. 
          Just function calling will print the pattern.
        - name parameter is case insensitive. Patterns always printed in upper case.
    """
    if len(name) <= 16 :
        Name().get_name(name, symbol, animate)
    elif 17 <= len(name) <= 32 :
        Name().get_name(name[:16], symbol, animate)
        print()
        Name().get_name(name[16:], symbol, animate)
    else :
        raise ValueError("Your Name is too large Please give some short name.")