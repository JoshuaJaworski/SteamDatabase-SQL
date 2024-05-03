# SteamDatabase-SQL

## Getting the program started  
 -You must enter the root password for your local system in the   “password” parameter at line 6 in SteamDatabase.py  
    -This allows the use of mySQL with Python  
 -You can then run the program normally with command “python SteamDatabase.py” in the terminal (or your typical method for running py).
## Once running  
 -Entering 1 will allow you to login as a previously registered account.  
    -My account will have initial data associated with it.  
        -Email: jaws  
        -Password: a  
 -Entering 2 will allow you to create a new account. You will be prompted to enter a username, email, and password. Once created the account will be loaded with a balance of $1,000, but no other data associated with it.  
    -After creating a new account you can login and continue.  
## After logging in  
 -The program can be used to view achievements or previously bought games associated with the current account.  
 -Its main purpose is to allow you to purchase new games that are available in the table and link them to your account.  
 -When making a purchase you will be prompted for the game’s name and it will check that the game found is the one you’re looking for.  
    -Available games to purchase:  
        -Dark Souls, Elden Ring, Dark Souls 3, Sekiro, Bloodborne, Mario, Skyrim, Fallout, League of Legends, Red Dead Redemption  
    -Games must be spelled correctly with correct capitalization.  
 -Purchases will check to ensure there is a large enough balance to satisfy the cost, and then update said balance once the purchase is confirmed.  
 -After purchasing you can view your updated games list.  
