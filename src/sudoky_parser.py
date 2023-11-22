def parse_grid(sudoku):
    """
    Convert text-based suduko grid into a list of list.
    
    This function allows for easier manipulation of the grid by accessing numbers via their row and column index.

    Parameters
    ----------
    sudoku: str
        Text-based grid representation of Sudoku. Empty cells should be denoted
        with a 0, with '|' and '-' used to seperate subgrid columns and rows, respectively.
        The intersections of each subgrid should be marked with '+'.
        Example:

        ::

            000|007|000
            000|009|504
            000|050|169
            ---+---+---
            080|000|305
            075|000|290
            406|000|080
            ---+---+---
            762|080|000
            103|900|000
            000|600|000

    Returns
    ----------
    sudoku_list (list  of lists) : 
        A list of list where elements can be accessed by row [i] & column [j]. Each sublist represents a row in the grid.
    
    Raises
    ----------
    TypeError
        If input is not a string.
    ValueError
        If input is not an 11x11 grid, including '|', '-', and '+' characters.
    """
    # Check if input is valid (string)
    if type(sudoku) != str:
        raise TypeError('Input must be a string')
    
    # Flatten input string into a list
    sudoku_list_raw = []
    for char in sudoku:
        if char != '\n':
            sudoku_list_raw.append(char)
    
    # Check if input is valid (length)
    if len(sudoku_list_raw) != 11*11:
        raise ValueError('Input grid must be 11x11, don\'t forget to seperate girds with |, -, and + signs!')

    # Convert flattened list of strs into a list of list of ints
    sudoku_list = []
    for i in range(11):
        sudoku_list.append([])
        for j in range(11):
            curr_val = sudoku_list_raw[i*11+j]
            if curr_val == '|' or curr_val == '-' or curr_val == '+':
                pass
            else:
                sudoku_list[i].append(int(curr_val))
    
    # Remove empty sublists
    sudoku_list = [row for row in sudoku_list if row != []]
    
    return sudoku_list
