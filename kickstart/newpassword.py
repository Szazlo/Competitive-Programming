def password_reset():
    pass_len = int(input())
    password = list(input())
    if not any(c.isupper() for c in password):
        password.append('A')
    if not any(c.islower() for c in password):
        password.append('a')
    if not any(c.isdigit() for c in password):
        password.append('1')
    if not any(c in '#@*&' for c in password):
        password.append('#')
    if len(password) < 7:
        password += ['a' for i in range(7-len(password))]
    return ''.join(password)     

if __name__ == "__main__":
    for case in range(int(input())):
        print("Case #{}: {}".format(case+1, password_reset()))