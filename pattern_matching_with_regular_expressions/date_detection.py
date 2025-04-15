import re

def is_valid_date(day, month, year):
    try:
        day = int(day)
        month = int(month)
        year = int(year)
    except ValueError:
        return False
    
    if not (1000 <= year <= 2999):
        return False

    if not (1 <= month <= 12):
        return False
    
    if month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_days = 29 
        else:
            max_days = 28  
    else:
        max_days = 31

    if not (1 <= day <= max_days):
        return False
    
    return True

def main():
    date_str = "30/04/2021"
    

    match = date_regex.match(date_str)
    if match:
        day = match.group(1)
        month = match.group(2)
        year = match.group(3)
        
        if is_valid_date(day, month, year):
            print(f"Valid date: {day}/{month}/{year}")
        else:
            print(f"Invalid date: {day}/{month}/{year}")
    else:
        print("Invalid date format")




if __name__ == "__main__":
    date_regex = re.compile(r'^(\d{2})/(\d{2})/(\d{4})$')
    main()