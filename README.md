So today this happened:

@standupmaths 
Fun fact: you can arrange all the numbers from 1 to 17 so that each adjacent pair adds to a square number. Off you go! #mathspuzzle

@michiexile 
@standupmaths @haggismaths Even funner: the solution also generates solutions for 1 to 16 and 1 to 15 but breaks down for 1 to 14.

@haggismaths 
@michiexile @standupmaths Is 17 the largest value which has this property?

This repository has a python script built to respond to this last question. In case you don't feel like burning a few cycles, the short response is given by the following output from the script:

    python squaresumgraph.py 
    15 (8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9)
    16 (8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9, 16)
    17 (16, 9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8, 17)
    23 (18, 7, 9, 16, 20, 5, 11, 14, 2, 23, 13, 12, 4, 21, 15, 10, 6, 19, 17, 8, 1, 3, 22)
    25 (4, 21, 15, 10, 6, 19, 17, 8, 1, 3, 22, 14, 2, 23, 13, 12, 24, 25, 11, 5, 20, 16, 9, 7, 18)
    26 (11, 25, 24, 12, 13, 3, 22, 14, 2, 23, 26, 10, 6, 19, 17, 8, 1, 15, 21, 4, 5, 20, 16, 9, 7, 18)
    27 (14, 11, 25, 24, 12, 13, 3, 22, 27, 9, 16, 20, 5, 4, 21, 15, 1, 8, 17, 19, 6, 10, 26, 23, 2, 7, 18)
    28 (15, 1, 3, 13, 12, 24, 25, 11, 14, 22, 27, 9, 16, 20, 5, 4, 21, 28, 8, 17, 19, 6, 10, 26, 23, 2, 7, 18)
    29 (13, 12, 4, 5, 11, 25, 24, 1, 3, 6, 19, 17, 8, 28, 21, 15, 10, 26, 23, 2, 14, 22, 27, 9, 16, 20, 29, 7, 18)

It thus seems that there are plenty of further such sequences that can be arranged. The search as written only goes to 30, but this is simple to modify.
