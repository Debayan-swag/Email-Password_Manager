import random
import string

def mas_val (): # for random values
    list_numbers = list(range(1, 11))
    random.shuffle(list_numbers) # shuffled numbers
    list_index = list(range(0, 10)) 
    random.shuffle(list_index) # for extra randomness, shuffled indices too
    # Random numbers assigned
    capitals = list_numbers[list_index[1]]
    smalls = list_numbers[list_index[2]]
    numbers = list_numbers[list_index[3]]
    specials = list_numbers[list_index[4]]
    
    return mas_key(capitals, smalls, numbers, specials) # calling the master function
    
def mas_key (capitals, smalls, numbers, specials):
    # Counters for each type
    counter_capitals = 0
    counter_smalls = 0
    counter_numbers = 0
    counter_specials = 0
    # Lists for each type
    list_capitals = list(string.ascii_uppercase)
    list_smalls = list(string.ascii_lowercase)
    list_numbers = list(range(10))
    list_specials = ["@", "#", "$", "&", "~"]
    # Each random shuffling
    random.shuffle(list_capitals)
    random.shuffle(list_smalls)
    random.shuffle(list_numbers)
    random.shuffle(list_specials)
    
    temp_master_key = "" # for temporary store 
    # for capitals
    for caps in list_capitals:
        if(counter_capitals == capitals): # IMP: for not exceeding the capitals parameter range 
            break
        temp_master_key += caps 
        counter_capitals += 1
    # for smalls   
    for sms in list_smalls:
        if(counter_smalls == smalls): # IMP: for not exceeding the smalls parameter range
            break
        temp_master_key += sms 
        counter_smalls += 1
    # for numbers     
    for nums in list_numbers:
        if(counter_numbers == numbers): # IMP: for not exceeding the numbers parameter range
            break
        temp_master_key += str(nums) 
        counter_numbers += 1
    # for specials
    for sps in list_specials:
        if(counter_specials == specials): # IMP: for not exceeding the specials parameter range
            break
        temp_master_key += sps 
        counter_specials += 1
    
    m_l = list(temp_master_key) # needed for shuffling
    random.shuffle(m_l)
    MASTER_KEY = "".join(m_l)
    return MASTER_KEY

mas_val ()