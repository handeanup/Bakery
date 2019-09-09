# Bakery
Bakery solution.

HOW TO PROVIDE INPUT?
    write input data in sample_input.txt file one input on one line.
    e.g. 
    10 VS5
    14 MB11
    13 CF

    Note: Do not insert blank lines inbetween or at the end.
          Enter space between order_size and bakery item code.

HOW TO RUN?
    > python .\bakery.py

HOW DO I READ OUTPUT?
    Once executable has been run output will be displayed on console as below-
    10 VS5 $17.98
        2 x 5 $8.99
    14 MB11 $54.8
        1 x 8 $24.95
        3 x 2 $9.95
    13 CF $25.85
        2 x 5 $9.95
        1 x 3 $5.95

WHAT IF INCORRECT INPUT IS PROVIDED?
    for incorrect input data, appropriate error message will be displayed on console.
    
        Note: For order size (e.g. 1 or if pack combination is not available) appropriate error message will be displayed on colsole.
