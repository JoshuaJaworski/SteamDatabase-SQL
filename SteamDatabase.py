import mysql.connector
import datetime
#Joshua Jaworski

def main():
    database = mysql.connector.connect(user='root', password='', host='localhost')
    cc = database.cursor()

    try:
        #Easiest to use in beginning. Think it is necessary.
        cc.execute('DROP SCHEMA STEAM')
        #print("\nDatabase dropped.")
    except:
        print("\nMaking database")
    createDatabase(database)
    print("Database created")

    #Synthetic data
    #Account
    insert_account = ("INSERT INTO ACCOUNT"
                  "(ID, Balance)"
                  "VALUES (1, 65)")
    cc.execute(insert_account, )
    #Account_Login
    insert_login = ("INSERT INTO ACCOUNT_LOGIN"
                  "(ID, Username, Email, Password)"
                  "VALUES (%s, %s, %s, %s)")
    login_data = ("1", "JJaws", "jaws", "a")
    cc.execute(insert_login, login_data)
    #Achievements
    insert_achievements = ("INSERT INTO ACHIEVEMENTS_LIST"
                           "(ID, Achievement_name)"
                           "VALUES (%s, %s)")
    achievement_data = ("1", "All Items")
    achievement_data1 = ("1", "All Quests")
    cc.execute(insert_achievements, achievement_data)
    cc.execute(insert_achievements, achievement_data1)
    achievement_data2 = ("1", "All Locations")
    cc.execute(insert_achievements, achievement_data2)
    #Game
    insert_game = ("INSERT INTO GAME" 
                   "(Game_ID, Game_name, Developer, Cost, Release_date)"
                   "VALUES (%s, %s, %s, %s, %s)")
    game_data = ("1", "Dark Souls", "FromSoftware", "40.00", "2011-09-22")
    cc.execute(insert_game, game_data)
    game_data1 = ("2", "Elden Ring", "FromSoftware", "60.00", "2022-02-25")
    cc.execute(insert_game, game_data1)
    game_data2 = ("3", "Dark Souls 3", "FromSoftware", "60.00", "2016-09-20")
    cc.execute(insert_game, game_data2)
    game_data3 = ("4", "Sekiro", "FromSoftware", "60.00", "2018-02-21")
    cc.execute(insert_game, game_data3)
    game_data4 = ("5", "Bloodborne", "FromSoftware", "40.00", "2014-08-18")
    cc.execute(insert_game, game_data4)
    game_data5 = ("6", "Mario", "Nintendo", "60.00", "2008-05-12")
    cc.execute(insert_game, game_data5)
    game_data6 = ("7", "Skyrim", "Bethesda", "60.00", "2011-11-11")
    cc.execute(insert_game, game_data6)
    game_data7 = ("8", "Fallout", "Bethesda", "60.00", "2016-12-10")
    cc.execute(insert_game, game_data7)
    game_data8 = ("9", "League of Legends", "Riot", "0.00", "2002-01-02")
    cc.execute(insert_game, game_data8)
    game_data9 = ("10", "Red Dead Redemption", "Rockstar", "60.00", "2018-05-05")
    cc.execute(insert_game, game_data9)
    #Purchase
    insert_purch = ("INSERT INTO PURCHASE"
                    "(Order_no, ID, Game_ID, Order_date, Total)"
                    "VALUES (%s, %s, %s, %s, %s)")
    purch_data = ("1", "1", "2", "2022-02-26", "60.00")
    cc.execute(insert_purch, purch_data)
    purch_data1 = ("2", "1", "1", "2022-02-20", "40.00")
    cc.execute(insert_purch, purch_data1)
    #Friends
    insert_friend = ("INSERT INTO FRIENDS"
                     "(Account_ID, ID, Friend_name, Friendship_status)"
                     "VALUES (%s, %s, %s, %s)")
    friend_data = ("100", "1", "Han", "Maximum")
    cc.execute(insert_friend, friend_data)
    friend_data1 = ("150", "1", "Finn", "Medium")
    cc.execute(insert_friend, friend_data1)
    #End of data

    #Load menu
    menuPrompt(database)

    dropDatabase(database)
    shutDown(cc, database)
    print("\nHave a nice day!\n")

#Function to handle menu
#Typical menu prompt to run a loop that calls the function based off the user's inputted value
def menuPrompt(database):
    #Need to keep track of who is logged in
    id_acc = 0
    user = 0
    #Prompt
    while (user != 6):
        print("\n1. Login")
        print("2. Make new account")
        print("3. View games")
        print("4. View achievements")
        print("5. Place order")
        print("6. Quit")

        #Ensure only ints are inputted
        try:
            user = int(input())
        except:
            print("Enter a number 1-6.")
            continue

        #Login
        if (user == 1):
            id_acc = login(database)
        #Make new account
        elif (user == 2):
            newAccount(database)
        #View games if logged in
        elif (user == 3):
            if (id_acc == 0):
                print("You need to login to view your games.")
            else:
                viewGames(database, id_acc)
        #View achievements if logged in
        elif (user == 4):
            if (id_acc == 0):
                print("You need to login to view your achievements.")
            else:
                viewAchievements(database, id_acc)
        #Make a new purchase if logged in
        elif (user == 5):
            if (id_acc == 0):
                print("You need to login to make a purchase.")
            else:
                makePurchase(database, id_acc)
        
#Create a new account 
def newAccount(database):
    cc = database.cursor()

    print("\nPlease enter your new account information.\n")

    #Prompt for username
    username = input("Username: ")
    #Check if username exists
    name_que = ("SELECT * FROM ACCOUNT_LOGIN WHERE Username = %s")
    name_data = (username, )
    cc.execute(name_que, name_data)
    result = cc.fetchall()
    #If username is found display error message.
    if(len(result) == 1):
        print("\nThere is already an account with this username.\n")
        return
    
    #Prompt for email and password.
    email = input("Email: ")
    password = input("Password: ")

    #Count how many tuples exist to calculate ID
    id_acc = ("SELECT COUNT(*) FROM ACCOUNT")
    cc.execute(id_acc)
    result = cc.fetchall()
    #Add one for the new account id
    id_acc = result[0][0] + 1

    #Update tables with information.
    insert_acc = ("INSERT INTO ACCOUNT"
                  "(ID, Balance)"
                  "VALUES (%s, %s)")
    acc_data = (id_acc, 1000)
    cc.execute(insert_acc, acc_data)
    #Update Account_login info
    insert_login = ("INSERT INTO ACCOUNT_LOGIN"
                  "(ID, Username, Email, Password)"
                  "VALUES (%s, %s, %s, %s)")
    login_data = (id_acc, username, email, password)
    cc.execute(insert_login, login_data)

    print("\nAccount created. Welcome to Steam!")

#Used to login with an existing user. Will check to make sure one exists.
def login(database):
    cc = database.cursor()

    print("\nPlease input your login:")
    #username = input("Username: ")
    email = input("Email: ")
    password = input("Password:  ")
    #Ensure the login is available
    #Query to search
    login_que = ("SELECT * FROM ACCOUNT_LOGIN WHERE Email = %s AND Password = %s")
    #Data you are searching for
    login_data = (email, password)
    #Executes to mySQL using the query and data
    cc.execute(login_que, login_data)
    #Returns mySQL query to result with fetchall
    result = cc.fetchall()
    #print(result)
    #Check if the account was found
    if(len(result) == 0):
        print("Cannot find account. Please register before logging in.")
        return 0
    else:
        print("\nWelcome back!")
        #return if found
        return result[0][0]
        
    
#Print out all achievments associated with this account ID
def viewAchievements(database, id_acc):
    cc = database.cursor()
    print("\nACHIEVEMENTS")

    achievement_que = ("SELECT * FROM ACHIEVEMENTS_LIST WHERE ID = %s")
    achievement_data = (id_acc, )
    cc.execute(achievement_que, achievement_data)
    result = cc.fetchall()
    if (len(result) == 0):
        print("You don't have any achievements yet.")
        return
    #print("Achievements:", result)
    #Print all achievements associated with the id
    for i in result:
        print(i[1])


#Print out all games associated with this account ID
def viewGames(database, id_acc):
    cc = database.cursor()

    print("\nGAMES")

    #Check purchase history to see what games this account has bought
    purch_que = ("SELECT Game_ID FROM PURCHASE WHERE ID = %s")
    purch_data = (id_acc, )
    cc.execute(purch_que, purch_data)
    purch_result = cc.fetchall()
    #print(purch_result)
    if (len(purch_result) == 0):
        print("You don't have any games yet.")
        return

    #Go through game_id's found in Purchase and pull the game_name's from Game
    for i in purch_result:
        game_que = ("SELECT Game_name FROM GAME WHERE Game_ID = %s")
        game_data = (i[0], )
        cc.execute(game_que, game_data)
        game_result = cc.fetchall()
        print(game_result[0][0])

#Executes a purchase order to buy a single game chosen by the user
#Updates necessary tables to support this operation
def makePurchase(database, id_acc):
    cc = database.cursor()

    #Prompt to see if searched game exists.
    user = input("\nWhat game would you like to purchase?\n")
    game_id_que = ("SELECT * FROM GAME WHERE Game_name = %s")
    game_name_data = (user, )
    cc.execute(game_id_que, game_name_data)
    game_result = cc.fetchall()
    #Return to menu if can't find game
    if(len(game_result) == 0):
        print("Sorry, it doesn't look like the game you're looking for is in our database.")
        return
    
    print(f"\n{game_result[0][1]} costs ${game_result[0][3]}\n")
    #Prompt if user wants to purchase
    user = input("Would you like to purchase this game? (yes/no): ")
    if(user.lower() == "no"):
        return
    
    #Check if Account already owns this game
    check_acc_que = ("SELECT * FROM PURCHASE WHERE Game_ID = %s AND ID = %s")
    check_acc_data = (game_result[0][0], id_acc)
    cc.execute(check_acc_que, check_acc_data)
    check_result = cc.fetchall()
    if(len(check_result) != 0):
        print("\nIt appears you already own this game.")
        return
    
    #Check if Account balance is enough
    account_que = ("SELECT Balance FROM ACCOUNT WHERE ID = %s")
    account_data = (id_acc, )
    cc.execute(account_que, account_data)
    account_result = cc.fetchall()
    if(game_result[0][3] > account_result[0][0]):
        print("Sorry, you don't have enough money in your account balance to purchase this game.")
        return
    
    #Need to count to determine order_no
    purchase_no = ("SELECT COUNT(*) FROM PURCHASE")
    cc.execute(purchase_no)
    purchase_no_result = cc.fetchall()
    #Add one for the new order
    purchase_no = purchase_no_result[0][0] + 1

    #Need to get current date
    today = datetime.datetime.now()

    #Insert a new purchase with order information
    insert_purchase = ("INSERT INTO PURCHASE"
                    "(Order_no, ID, Game_ID, Order_date, Total)"
                    "VALUES (%s, %s, %s, %s, %s)")
    purchase_data = (purchase_no, id_acc, game_result[0][0], today, game_result[0][3])
    cc.execute(insert_purchase, purchase_data)

    #Update Account balance
    new_balance = account_result[0][0] - game_result[0][3]
    #Space is necessary
    update_acc_balance = ("UPDATE ACCOUNT "
                          "SET Balance = %s "
                          "WHERE ID = %s")
    acc_balance_data = (new_balance, id_acc)
    cc.execute(update_acc_balance, acc_balance_data)

    print("\nCongratulations, your purchase has been approved. Enjoy!")




#Function to close database in reverse order of creation
def dropDatabase(database):
    cc = database.cursor()
    cc.execute('DROP TABLE ACHIEVEMENTS_LIST')
    cc.execute('DROP TABLE FRIENDS')
    cc.execute('DROP TABLE PURCHASE')
    cc.execute('DROP TABLE GAME')
    cc.execute('DROP TABLE ACCOUNT_LOGIN')
    cc.execute('DROP TABLE ACCOUNT')
    cc.execute('DROP SCHEMA STEAM')

#Closes mySQL and the database
def shutDown(cc, database):
    cc.close()
    database.close()

#Creates steam database with designated tables
def createDatabase(database):
    cc = database.cursor()

    cc.execute('CREATE SCHEMA STEAM')
    cc.execute('USE STEAM')

    #ACCOUNT table
    cc.execute('''CREATE TABLE ACCOUNT(
        ID INT NOT NULL,
        Balance FLOAT,
        PRIMARY KEY(ID)
    )''')

    #ACCOUNT_LOGIN table
    cc.execute('''CREATE TABLE ACCOUNT_LOGIN(
        ID INT NOT NULL,
        Username varchar(32),
        Email varchar(32),
        Password varchar(64),
        PRIMARY KEY(ID),
        FOREIGN KEY(ID) REFERENCES ACCOUNT(ID)
    )''')

    #GAME table
    cc.execute('''CREATE TABLE GAME (
        Game_ID INT NOT NULL,
        Game_name varchar(32),
        Developer varchar(32),
        Cost FLOAT,
        Release_Date DATE,
        PRIMARY KEY(Game_ID)
    )''')

    #PURCHASE table
    cc.execute('''CREATE TABLE PURCHASE(
        Order_no INT NOT NULL,
        ID INT NOT NULL,
        Game_ID INT NOT NULL,
        Order_date DATE,
        Total FLOAT,
        PRIMARY KEY(Order_no),
        FOREIGN KEY(ID) REFERENCES ACCOUNT(ID),
        FOREIGN KEY(Game_ID) REFERENCES GAME(Game_ID)
    )''')

    #FRIENDS table
    cc.execute('''CREATE TABLE FRIENDS(
        Account_ID INT NOT NULL,
        ID INT NOT NULL,
        Friend_name varchar(32),
        Friendship_status varchar(32),
        PRIMARY KEY(Account_ID),
        FOREIGN KEY(ID) REFERENCES ACCOUNT(ID)
    )''')

    #ACHIEVEMENTS_LIST table
    cc.execute('''CREATE TABLE ACHIEVEMENTS_LIST(
        ID INT NOT NULL,
        Achievement_name varchar(32),
        PRIMARY KEY(Achievement_name),
        FOREIGN KEY(ID) REFERENCES ACCOUNT(ID)
    )''')

    database.commit()

main()

