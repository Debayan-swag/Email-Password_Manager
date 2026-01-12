from master_key import mas_val
import time 
from cryptography.fernet import Fernet
import os

class MasterKeyError (Exception):
    def __init__(self, val):
        self.val = val
        super().__init__(f"Error Raised : {val} is not valid")
        
def access(MASTER_KEY):
    
    while True:
        while (not os.path.exists("DETAILS.txt")):
            print(f"Your Master key : {MASTER_KEY}", flush=True)
            print("After 5 seconds Master key will not be visible, copy it")
            time.sleep(5)
            os.system("cls" if os.name == "nt" else "clear")
            
            user_master = input("Enter Master key : ")
            if(user_master != MASTER_KEY):
                print("Invalid Master key")
                continue
            else:
                user_set_email = input("Email to set : ")
                user_set_password = input("Password to set : ")
                
                with open("DETAILS.txt", "a") as det:
                    det.write("Email : "+ user_set_email + "   " +"Password : "+ user_set_password + "\n")
                    
                print("Successfully, set email and password")
                break
        
        if (os.path.exists("DETAILS.txt")):
            want_to_access = input("Want to see or change or quit : ").strip().lower()
            if(want_to_access == "quit"):
                break
            elif(want_to_access == "see"):
                req = input("Enter Master Key :")
                if(req != MASTER_KEY):
                    raise MasterKeyError(req)
                else:
                    with open("DETAILS.txt", "r") as d:
                        det = d.readlines()
                        line = det[-1]
                        print(line)
            elif(want_to_access == "change"):
                req = input("Enter Master Key :")
                if(req != MASTER_KEY):
                    raise MasterKeyError(req)
                else:
                    while True:
                        new_email = input("Enter new Email : ")
                        new_password = input("Enter new Password : ") 
                        with open("DETAILS.txt", "a") as det:
                            det.write("Email : "+ new_email + "   " +"Password : "+ new_password + "\n")
                        satisfied = input("Want to change again? (yes/no) : ").strip().lower()
                        if(satisfied == "yes"):
                            continue 
                        else:
                            break
                break
            else:
                print(f"Since you said {want_to_access}\n Quitting..")
                break

print("For each run, need different Master Key")
ANSI = "\r\033[K"
key = Fernet.generate_key()

with open("fernet.key", "wb") as kf:
    kf.write(key)
with open("fernet.key", "rb") as kf:
    key = kf.read()
    
f = Fernet(key)
MASTER_KEY = str(mas_val())
token = f.encrypt(MASTER_KEY.encode("utf-8"))

print("Generating Master key")
with open("Master.key", "wb") as f: # this will override the master key file, for each new key
    f.write(token)

time.sleep(3)   
print("Successfully generated Master key")
access(MASTER_KEY)