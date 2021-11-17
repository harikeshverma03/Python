import os
import random
import csv

f = open('bank.csv', 'w')
fw = csv.writer(f,)
fw.writerow(['Card Number', 'PIN', 'Account Number', 'Name of Account holder', 'Balance', 'Age'])
fw.writerow(['519608388871', '1234', '123456789', 'Harikesh Verma', 10000, ' 20'])
fw.writerow(['519608388872', '1234', '123456790', 'Riya Verma', 10000, ' 19'])
fw.writerow(['519608388873', '1234', '123456791', 'Puspanjali Verma', 10000, ' 18'])
fw.writerow(['519608388874', '1234', '123456792', 'Deepak Verma', 10000, ' 49'])
fw.writerow(['519608388875', '1234', '123456793', 'Kavita Verma', 10000, ' 44'])
fw.writerow(['519608388876', '1234', '123456794', 'Advitiya Verma', 10000, ' 6'])
fw.writerow(['519608388877', '1234', '123456795', 'Alankriti Verma', 10000, ' 9'])
fw.writerow(['519608388878', '1234', '123456796', 'Girish Verma', 10000, ' 45'])
fw.writerow(['519608388879', '1234', '123456797', 'Geeteshwar Verma', 10000, ' 45'])
fw.writerow(['519608388810', '1234', '123456798', 'Jyoti Verma', 10000, ' 40'])
fw.writerow(['519608388811', '1234', '123456799', 'Neelu Verma', 10000, ' 40'])
f.close()

def admin():
    print("Welcome to National bank of India ATM");
    print("---------------------------------------------------------------------------------------------")
    atm = input("Please Enter Your 12 digit Card Number to continue \t")
    file = open('bank.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        if len(row) > 0:
            rows.append(row)
    file.close();
    size = len(rows)
    j = 0
    for i in range(0,size):
        if(rows[i][0] == atm):
            print("Welcome {} !!".format(rows[i][3]))
            break;
        j = j+1;
    if(j == size):
        print("You don't have a valid card number!");
        retry = input("To re-enter your card number press 0 or press 1 to generate a new account \n")
        if retry == '0':
            print("---------------------------------------------------------------------------------------------");
            print("---------------------------------------------------------------------------------------------");
            admin();
        else:
            newacc();
    else:
        pin = input("Please Enter Your 4 digit PIN \t");
        if(pin == rows[j][1]):
            print("Correct Pin")
            print("Enter 1 to make a withdrawal")
            print("Enter 2 to change your pin")
            print("Enter 3 to check your balance")
            choice = int(input("Enter 4 to deposit money \t"))
            k = 0
            while(k < 5):
                if(choice == 1):
                    withdraw(atm)
                    break;
                elif(choice == 2):
                    pinchange(atm)
                    break;
                elif(choice == 3):
                    balance(atm)
                    break;
                elif(choice == 4):
                    deposit(atm)
                    break;
                else:
                    choice = int(input("Invalid choice! \n Please choose again \t"))
            print("Your session expired please try again!")
            admin();
        else:
            k = 0;
            for i in range(3,0,-1):
                print("You have {} tries remaining".format(i))
                pin = input("Please re-enter your pin \t");
                if(pin == rows[j][1]):
                    print("Correct Pin")
                    break;
                k = k + 1;
            if(k == 3):
                print("Your card has been blocked due to security reasons")
                print("Thank you for using National Bank of India ATM !!")
                print("---------------------------------------------------------------------------------------------")
                admin();
            else:
                print("Enter 1 to make a withdrawal")
                print("Enter 2 to change your pin")
                print("Enter 3 to check your balance")
                choice = int(input("Enter 4 to deposit money \t"))
                k = 0
                while(k < 5):
                    if(choice == 1):
                        withdraw(atm)
                        break;
                    elif(choice == 2):
                        pinchange(atm)
                        break;
                    elif(choice == 3):
                        balance(atm)
                        break;
                    elif(choice == 4):
                        deposit(atm)
                        break;
                    else:
                        choice = int(input("Invalid choice! \n Please choose again \t"))
                print("Your session expired please try again!")
                admin();
def withdraw(atm):
    file = open('bank.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        if len(row) > 0:
            rows.append(row)
    file.close();
    size = len(rows)
    for i in range(0,size):
        if(rows[i][0] == atm):
            j = i;
            break;
    amount = int(input("Enter the amount to be withdrawn in multiples of 100 \t"))
    if(amount % 100 != 0):
        print("Entered amount is not in multiples of 100")
    elif(amount > int(rows[j][4])):
        print("You don't have insufficient balance to complete this transaction.")
        print("Your current balance is: ", rows[j][4]);
    else:
        print("You transaction has been processed succesfully")
        print("Your current balance is ", int(rows[j][4]) - amount)
        rows[j][4] = int(rows[j][4]) - amount
        file = open('temp.csv', 'w')
        fw = csv.writer(file,)
        fw.writerow(header)
        for i in range(0,size):
            fw.writerow(rows[i]);
        file.close();
        os.remove("bank.csv")
        os.rename('temp.csv', 'bank.csv')
    print("Thank you for using National Bank of India ATM !!")
    print("---------------------------------------------------------------------------------------------")
    admin();
def deposit(atm):
    file = open('bank.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        if len(row) > 0:
            rows.append(row)
    file.close();
    size = len(rows)
    for i in range(0,size):
        if(rows[i][0] == atm):
            j = i;
            break;
    amount = int(input("Enter the amount to be deposited in multiples of 100 \t"))
    if(amount % 100 != 0):
        print("Entered amount is not in multiples of 100")
    else:
        print("You transaction has been processed succesfully")
        print("Your current balance is ", int(rows[j][4]) + amount)
        rows[j][4] = int(rows[j][4]) + amount
        file = open('temp.csv', 'w')
        fw = csv.writer(file,)
        fw.writerow(header)
        for i in range(0,size):
            fw.writerow(rows[i]);
        file.close();
        os.remove("bank.csv")
        os.rename('temp.csv', 'bank.csv')
    print("Thank you for using National Bank of India ATM !!")
    print("---------------------------------------------------------------------------------------------")
    admin();
def pinchange(atm):
    file = open('bank.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        if len(row) > 0:
            rows.append(row)
    file.close();
    size = len(rows)
    for i in range(0,size):
        if(rows[i][0] == atm):
            j = i;
            break;
    pin = input("Enter your new pin \t")
    newpin = input("Re-enter your new pin \t")
    if(pin != newpin or len(pin) != 4 or len(newpin) != 4):
        print("Transaction canceled! \nThe entered pins don't match")
    else:
        print("Pin changed succesfully")
        rows[j][1] = newpin
        file = open('temp.csv', 'w')
        fw = csv.writer(file,)
        fw.writerow(header)
        for i in range(0,size):
            fw.writerow(rows[i]);
        file.close();
        os.remove("bank.csv")
        os.rename('temp.csv', 'bank.csv')
    print("Thank you for using National Bank of India ATM !!")
    print("---------------------------------------------------------------------------------------------")
    admin();
def balance(atm):
    file = open('bank.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        if len(row) > 0:
            rows.append(row)
    file.close();
    size = len(rows)
    for i in range(0,size):
        if(rows[i][0] == atm):
            j = i;
            break
    print("Your current balane is: ", rows[j][4])
    print("Thank you for using National Bank of India ATM !!")
    print("---------------------------------------------------------------------------------------------")
    admin();


def newacc():
    print("Thanks for choosing National Bank of India")
    print("Please enter your details to create an account")
    name = input("Enter your name  \t")
    age = input("Enter your age \t")
    amount = input("Enter the amount you want to deposit in your account \t")
    file = open('bank.csv')
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    rows = []
    for row in csvreader:
        if len(row) > 0:
            rows.append(row)
    file.close();
    size = len(rows)
    j = -1
    while(j == -1):
        j = 0
        n = random.randint(10,99)
        accno = '1234567' + str(n)
        for i in range(0,size):
            if(rows[i][2] == accno):
                j = -1;
                break;
    j = -1
    while(j == -1):
        j = 0
        n = random.randint(1000,9999)
        cardno = '51960838' + str(n)
        for i in range(0,size):
            if(rows[i][0] == cardno):
                j = -1;
                break;
    print("Congratulations! Your account has been created")
    print("---------------------------------------------------------------------------------------------")
    print("Please generate a pin to activate your card")
    flag = True
    while(flag):
        pin = input("Enter your new pin\t")
        newpin = input("Re-enter your new pin\t")
        if(len(pin) != 4 or len(newpin) != 4):
            print("The entered pins are invalid")
            print("Please try again")
        elif(pin == newpin):
            print("Your card has been activated")
            flag = False
        else:
            print("The entered pins do not match!")
            print("Please try again")
    print("Note the details of your account")
    print("Account holder name: ", name)
    print("Age: ", age)
    print("Balance: ", amount)
    print("Account Number: ", accno)
    print("Card Number: ", cardno)
    file = open('temp.csv', 'w')
    fw = csv.writer(file,)
    fw.writerow(header)
    for i in range(0,size):
        fw.writerow(rows[i]);
    fw.writerow([cardno, pin, accno, name, amount, age])
    file.close();
    os.remove("bank.csv")
    os.rename('temp.csv', 'bank.csv')
    print("Thank you for using National Bank of India ATM !!")
    print("---------------------------------------------------------------------------------------------")
    admin();

admin();