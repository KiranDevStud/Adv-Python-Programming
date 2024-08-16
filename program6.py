from datetime import datetime

def get_birthdate_input(person_num):
    date_str = input(f"Enter the date of birth for person {person_num} (format: YYYY-MM-DD): ")
    return datetime.strptime(date_str, "%Y-%m-%d")

def determine_older_person(birthdate1, birthdate2):
    if birthdate1 < birthdate2:
        return "Person 1 is older."
    elif birthdate1 > birthdate2:
        return "Person 2 is older."
    else:
        return "Both persons are of the same age."

    
birthdate1 = get_birthdate_input(1)
birthdate2 = get_birthdate_input(2)
    
result = determine_older_person(birthdate1, birthdate2)
print(result)
