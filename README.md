# group-six-python-project


# MTN Mobile Money (MoMo) Simulator
Developed by Samuel Agyemang
GitHub: https://github.com/agyesam12/group-six-python-project


def main():
    """Main function that runs the MoMo simulator application."""
    while True:
        print("\n Welcome to MTN MoMo ")
        print("---------------------")
        print("\n 1. Transfer Money ")
        print(" 2. Airtime & Bundles ")
        print(" 3. Momo Pay & Pay Bill ")
        print(" 4. Allow Cash Out ")
        print(" 5. Financial Services ")
        print(" 6. My Wallet ")
        print(" 0. Exit ")

        try:
            num = int(input("\nEnter the number of your preferred choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if num == 0:
            print("Exiting MTN MoMo... Goodbye!")
            break
        elif num == 1:
            transfer_money()
        elif num == 2:
            airtime_and_bundles()
        elif num in [3, 4, 5, 6]:
            print(f"\nOption {num} is currently under maintenance. Please try again later.")
        else:
            print("Invalid selection. Please try again.")

def transfer_money():
    """Handles all money transfer operations."""
    print("\nTransfer Money ")
    print("  1. MoMo User ")
    print("  2. Non MoMo User ")
    print("  3. Send With Care ")
    print("  4. Favourite ")
    print("  5. Other Networks ")
    print("  0. Back to Main Menu ")

    try:
        sub_num = int(input("\nEnter your choice: "))
    except ValueError:
        print("Invalid input!")
        return

    if sub_num == 0:
        return
    elif sub_num == 1:
        transfer_to_momo_user()
    elif sub_num == 2:
        transfer_to_non_momo_user()
    elif sub_num == 3:
        print("\nSend with Care")
        print("The SwC will be unavailable till 30/10/2024. To view your caretaker claim, phrases, use WhatsApp on 0596918253")
    elif sub_num == 4:
        handle_favorites()
    elif sub_num == 5:
        transfer_to_other_networks()
    else:
        print("Invalid selection")

def transfer_to_momo_user():
    """Handles transfers to other MTN MoMo users."""
    while True:
        mNum1 = input("\nEnter Mobile Number: ")
        mNum2 = input("Confirm Number: ")
        
        if mNum1 != mNum2:
            print("Error: Numbers don't match! Try again.")
        elif len(mNum1) != 10 or not mNum1.isdigit():
            print("Error: Invalid mobile number! Must be 10 digits.")
        else:
            break
    
    while True:
        try:
            amt = float(input("Enter Amount: "))
            if amt <= 0:
                print("Amount must be positive")
                continue
            break
        except ValueError:
            print("Invalid amount! Please enter a number.")
    
    refName = input("Enter Reference: ")
    
    while True:
        PIN = input("Enter PIN: ")
        if len(PIN) != 4 or not PIN.isdigit():
            print("PIN must be a 4-digit number")
        else:
            break
    
    print(f"\nAre you sure you want to send GHC {amt} to {mNum1}?")
    print(f"Reference Name: {refName}")
    print("E-Levy: GHC 0.00")
    print("1. Yes")
    print("2. Cancel")
    
    try:
        yc = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!")
        return
    
    if yc == 1:
        print("\nThanks for your confirmation.")
        print("Transaction Completed Successfully")
    elif yc == 2:
        print("\nProcess Terminated")
    else:
        print("\nInvalid choice")

def transfer_to_non_momo_user():
    """Handles transfers to non-MoMo users."""
    rName = input("\nEnter Receiver's Name: ")
    
    while True:
        try:
            amt = float(input("Enter Amount: "))
            if amt <= 0:
                print("Amount must be positive")
                continue
            break
        except ValueError:
            print("Invalid amount! Please enter a number.")
    
    refName = input("Enter Reference: ")
    
    while True:
        sCode1 = input("Enter Secret code: ")
        sCode2 = input("Confirm Secret code: ")
        if sCode1 != sCode2:
            print("Error: Codes do not match! Try again.")
        else:
            break
    
    print("\nTransaction Completed Successfully")

def handle_favorites():
    """Handles favorite contacts management."""
    print("\nFavorite")
    print("1. Name")
    print("2. Find")
    print("0. Back")
    
    try:
        sub_sub_num = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!")
        return
    
    if sub_sub_num == 0:
        return
    elif sub_sub_num in [1, 2]:
        rName = input("Enter Name: ")
        PIN = input("Enter PIN: ")
        print("No Contact Found")
    else:
        print("Invalid selection")

def transfer_to_other_networks():
    """Handles transfers to other networks."""
    print("\nOther Networks")
    print("1. AT")
    print("2. Telecel")
    print("3. E-Zwich")
    print("4. G-Money")
    print("5. ZeePay")
    print("6. GhanaPay")
    print("0. Back")
    
    try:
        net_num = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!")
        return
    
    if net_num == 0:
        return
    elif net_num in [1, 2]:
        network = "AT" if net_num == 1 else "Telecel"
        print(f"\n{network}")
        
        while True:
            mNum1 = input("Enter Mobile Number: ")
            mNum2 = input("Confirm Mobile Number: ")
            if mNum1 != mNum2:
                print("Error: Numbers don't match! Try again.")
            elif len(mNum1) != 10 or not mNum1.isdigit():
                print("Error: Invalid mobile number! Must be 10 digits.")
            else:
                break
        
        while True:
            try:
                amt = float(input("Enter Amount To Transfer: "))
                if amt <= 0:
                    print("Amount must be positive")
                    continue
                break
            except ValueError:
                print("Invalid amount! Please enter a number.")
        
        refName = input("Enter Reference ID: ")
        
        while True:
            PIN = input("Enter PIN: ")
            if len(PIN) != 4 or not PIN.isdigit():
                print("PIN must be a 4-digit number")
            else:
                break
        
        print(f"\nAre you sure you want to send GHC {amt} to {mNum1}?")
        print(f"Reference Name: {refName}")
        print("E-Levy: GHC 0.00")
        print("1. Yes")
        print("2. Cancel")
        
        try:
            yc = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            return
        
        if yc == 1:
            print("\nThanks for your confirmation.")
            print("Transaction Completed Successfully")
        elif yc == 2:
            print("\nProcess Terminated")
        else:
            print("\nInvalid choice")
    elif net_num in [3, 4, 5, 6]:
        print("\nSystem down, please try again later")
    else:
        print("\nInvalid selection")

def airtime_and_bundles():
    """Handles airtime and bundles purchases."""
    print("\nAirtime & Bundles")
    print("1. Airtime")
    print("2. Internet Bundles")
    print("3. Fixed Broadband")
    print("4. Schedule Airtime")
    print("5. Just4U")
    print("0. Back to Main Menu")
    
    try:
        airtime_num = int(input("\nEnter your choice: "))
    except ValueError:
        print("Invalid input!")
        return
    
    if airtime_num == 0:
        return
    elif airtime_num == 1:
        handle_airtime()
    elif airtime_num == 2:
        print("\nInternet Bundles option is coming soon!")
    elif airtime_num in [3, 4, 5]:
        print(f"\nOption {airtime_num} is currently under maintenance.")
    else:
        print("Invalid selection")

def handle_airtime():
    """Handles airtime purchase operations."""
    print("\nAirtime")
    print("1. Self")
    print("2. Others")
    print("3. Welcome Pack")
    print("4. Other Networks")
    print("0. Back")
    
    try:
        self_num = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input!")
        return
    
    if self_num == 0:
        return
    elif self_num == 1:
        while True:
            try:
                amt = float(input("Enter Amount: "))
                if amt <= 0:
                    print("Amount must be positive")
                    continue
                break
            except ValueError:
                print("Invalid amount! Please enter a number.")
        
        while True:
            PIN = input("Enter PIN: ")
            if len(PIN) != 4 or not PIN.isdigit():
                print("PIN must be a 4-digit number")
            else:
                break
        
        print(f"\nYou have successfully purchased airtime @ GHC {amt}")
    elif self_num == 2:
        while True:
            try:
                amt = float(input("Enter Amount: "))
                if amt <= 0:
                    print("Amount must be positive")
                    continue
                break
            except ValueError:
                print("Invalid amount! Please enter a number.")
        
        while True:
            mNum1 = input("Enter Recipient's Number: ")
            if len(mNum1) != 10 or not mNum1.isdigit():
                print("Invalid mobile number! Must be 10 digits.")
            else:
                break
        
        while True:
            PIN = input("Enter PIN: ")
            if len(PIN) != 4 or not PIN.isdigit():
                print("PIN must be a 4-digit number")
            else:
                break
        
        print(f"\nYou have successfully sent airtime to {mNum1} @ GHC {amt}")
    elif self_num == 3:
        print("\nOther Networks")
        print("1. Telecel")
        print("2. AT")
        print("0. Back")
        
        try:
            network_num = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input!")
            return
        
        if network_num == 0:
            return
        elif network_num in [1, 2]:
            network = "Telecel" if network_num == 1 else "AT"
            
            while True:
                mNum1 = input("Enter Recipient's Number: ")
                if len(mNum1) != 10 or not mNum1.isdigit():
                    print("Invalid mobile number! Must be 10 digits.")
                else:
                    break
            
            while True:
                try:
                    amt = float(input("Enter Amount: "))
                    if amt <= 0:
                        print("Amount must be positive")
                        continue
                    break
                except ValueError:
                    print("Invalid amount! Please enter a number.")
            
            while True:
                PIN = input("Enter PIN: ")
                if len(PIN) != 4 or not PIN.isdigit():
                    print("PIN must be a 4-digit number")
                else:
                    break
            
            print(f"\nYou have successfully sent {network} airtime to {mNum1} @ GHC {amt}")
        else:
            print("Invalid selection")
    elif self_num == 4:
        print("Invalid selection")
    else:
        print("Invalid selection")

if __name__ == "__main__":
    main()



How to Use This Code:
Copy the entire code block above

Paste it into a new Python file named momo.py

Run the program using:

python momo.py



Follow the on-screen menus to test all features

Key Features Included:
Complete money transfer functionality

Airtime purchase system

Input validation for all fields

Error handling for invalid inputs

Menu navigation with back options

Realistic MoMo transaction flow


# MTN MoMo CLI Simulation App

This Python script simulates the functionality of the **MTN Mobile Money (MoMo)** service. It provides an interactive command-line interface (CLI) that allows users to simulate various MTN MoMo operations, such as sending money, buying airtime, and checking wallet features.

---

## Features

- **Transfer Money**
  - To MoMo Users
  - To Non-MoMo Users
  - Send With Care (SwC)
  - Favourites
  - Other Networks (AT, Telecel, E-Zwich, G-Money, ZeePay, GhanaPay)

- **Airtime & Bundles**
  - Self Airtime Purchase
  - Airtime for Others
  - Fixed Broadband
  - Schedule Airtime
  - Internet Bundles (Coming Soon)
  - Just4U (Coming Soon)

- **Other Features (Placeholder)**
  - MoMo Pay & Pay Bill (Under Maintenance)
  - Allow Cash Out (Under Maintenance)
  - Financial Services (Under Maintenance)
  - My Wallet (Under Maintenance)

---

## How to Use

1. **Run the Script**
   ```bash
   python momo.py


 1. Transfer Money
 2. Airtime & Bundles
 3. MoMo Pay & Pay Bill
 4. Allow Cash Out
 5. Financial Services
 6. My Wallet
 0. Exit



 Welcome to MTN MoMo 
 ---------------------

 1. Transfer Money 
 2. Airtime & Bundles 
 3. MoMo Pay & Pay Bill 
 4. Allow Cash Out 
 5. Financial Services 
 6. My Wallet 
 0. Exit 

Enter the number of your preferred choice: 1

Transfer Money 
  1. MoMo User 
  2. Non MoMo User 
  3. Send With Care 
  4. Favourite 
  5. Other Networks 
  0. Back to Main Menu 

Enter your choice: 1

Enter Mobile Number: 0551234567
Confirm Number: 0551234567
Enter Amount: 50
Enter Reference: Lunch
Enter PIN: 1234
Are you sure you want to send GHC 50.0 to 0551234567?
Reference Name: Lunch
E-Levy: GHC 0.00
1. Yes
2. Cancel
Enter choice: 1

Thanks for your confirmation.
Transaction Completed Successfully


Notes
This is a simulation only. No actual transactions are made.

PIN codes, phone numbers, and references are for demonstration purposes.

Future updates may include:

Real MoMo API integration (for developers)

Enhanced transaction records

User authentication

License
This project is for educational purposes. Modify and expand it as you wish!


Author
# SAMUEL AGYEMANG

MTN MoMo CLI Simulation Developer



---

## How to Install Python (If Not Installed)

1. **Check if Python is Installed**
   - Open a terminal or command prompt and type:
     ```bash
     python --version
     ```
   - If you see a version number (e.g., Python 3.x.x), Python is already installed.

2. **Download Python**
   - Go to the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Download the latest version for your operating system (Windows, macOS, or Linux).

3. **Install Python**
   - **Windows:** Run the installer and make sure to check the box that says **“Add Python to PATH”** before clicking **Install Now**.
   - **macOS:** Download the `.pkg` installer and follow the installation steps.
   - **Linux:** Use your package manager. For example:
     ```bash
     sudo apt update
     sudo apt install python3
     ```

4. **Verify Installation**
   - After installation, open a terminal or command prompt and type:
     ```bash
     python --version
     ```
   - You should see the installed version of Python.

