import random
import string
def check_strength(pw):
    if len(pw) < 6:
        return "Weak (Too short)"
    s = 0
    if any(c.islower() for c in pw): s += 1
    if any(c.isupper() for c in pw): s += 1
    if any(c.isdigit() for c in pw): s += 1
    if any(c in string.punctuation for c in pw): s += 1
    return ["Weak", "Medium", "Strong"][s-2] if s >= 2 else "Weak"
def generate_pw(n=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(n))
while True:
    print("\n1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")
    op = input("Choose: ")
    if op == '1':
        pw = input("🔢 Entnr your password: ")
        print("Strength:", check_strength(pw))
    elif op == '2':
        print("Password:", generate_pw())
    elif op == '3':
        break
    else:
        print("❌ Invalid choice.")
