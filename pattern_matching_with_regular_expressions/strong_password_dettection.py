import re

def is_strong_password(password):
    if len(password) < 8:
        return f'password {password} is weak'
    
    if not re.search(r'[A-Z]', password):
        return f'password {password} is weak'
    
    if not re.search(r'[a-z]', password):
        return f'password {password} is weak'
    
    if not re.search(r'\d', password):
        return f'password {password} is weak'
    
    return f'password {password} is strong'

if __name__ == "__main__":
    password1 = "StrongPassword123"
    password2 = "weak1234"
    password3 = "Short1"
    print(is_strong_password(password1)) 
    print(is_strong_password(password2)) 
    print(is_strong_password(password3)) 