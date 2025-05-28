def main():
    while True:
        print("\n Welcome to MTN MoMo ")
        print("---------------------")
        print()
        print(" 1. Transfer Money ")
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