# SimpleDB-challenge
Dependencies: 
    
    python3 -
    
    copy    - Should be available by default with a standard python distribution
    
    random  - Only needed for Timer testing
            - Should be available by default with a standard python distribution
    
    timeit  - Only needed for Timer testing
            - Should be available by default with a standard python distribution

Files:

    - Database.py:  
            - Main file to be run from the command line
            - Runs hash table by default: update __name__ == 'main' to run binary tree 
            - python Database.py < input.txt

    - HashDB.py:    
            - Hash Table database
            - Prints timing diagnostics when run from the command line

    - TreeDB.py:    
            - Tree database
            - Prints timing diagnostics when run from the command line

    - Timing:       
            - Imported by HashDB and TreeDB for timing diagnostics
