import re
from exceptions.InvalidPatternException import InvalidPatternException
class Validator:

    @staticmethod
    def emailValidation(email: str) -> bool:
        pattern = r"[A-Za-z0-9_.-]+@([A-Za-z0-9_]+\.[A-Za-z]{2,4})"
        m = re.search(pattern, email)
        if(m): return True
        else: raise InvalidPatternException("E-MAIL INVÁLIDO")

    def cpfValidation(cpf: str) -> bool:
        pattern = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
        m = re.search(pattern, cpf)
        if(m): return True
        else: raise InvalidPatternException("CPF INVÁLIDO")

    def dateValidation(date: str) -> bool:
        pattern = r"\d{2}/\d{2}/\d{4}"
        m = re.search(pattern, date)
        print(m)
        if(m): return True
        else: raise InvalidPatternException("DATA INVÁLIDA")

