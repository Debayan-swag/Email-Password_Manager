from master_key import mas_val
import time 
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("fernet.key", "wb") as kf:
    kf.write(key)
with open("fernet.key", "rb") as kf:
    key = kf.read()
    
f = Fernet(key)
MASTER_KEY = str(mas_val())
token = f.encrypt(MASTER_KEY.encode("utf-8"))

def access(MASTER_KEY, info_of_generation):
    
    while (info_of_generation == 0):
        print(f"Your Master key : {MASTER_KEY}")
        user_master = input("Enter Master key : ")
        if(user_master != MASTER_KEY):
            print("Invalid Master key")
            continue
        else:
            user_set_email = input("Email to set : ")
            user_set_password = input("Password to set : ")
             
            with open("DETAILS.txt", "w") as det:
                det.write("Email : "+ user_set_email)
                det.write("Password : "+ user_set_password)
                
            print("Successfully, set email and password")
            break
    
    while (info_of_generation > 0):
        user_master = input("Enter Master key : ")
        if(user_master != MASTER_KEY):
            print("Access Denied")
            want_what = input("Your access is denied, want to again try? (yes/no): ").strip().lower()
            if(want_what == "yes"):
                continue
            elif (want_what == "no"):
                break
            else:
                print(f"As your said {want_what} .\nYou can't continue..")
                break
        else:
            with open("DETAILS.txt", "r") as det:
                det.read()

generated_already = 0    
print("NOTE : You can generate Master key once, for each password. If you change Master key, that leads to a new password\n")

print("Generating Master key")
with open("Master.key", "wb") as f: # this will override the master key file, for each new key
    f.write(token)

time.sleep(3)   
print("Successfully generated Master key")
access(MASTER_KEY, generated_already)
generated_already += 1