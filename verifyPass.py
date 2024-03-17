import re

class VerifyPass:

def verify_pass(senha):
    if (re.search(r'.{8,}', senha) and
            re.search(r'[A-Z]', senha) and
            re.search(r'[a-z]', senha) and
            re.search(r'\d', senha) and
            re.search(r'[!@#$%^&*()_+{}|:"<>?]', senha)):
        print("Senha válida!")
    else:
        print("Senha inválida!")