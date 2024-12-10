class MessageManager:
    SUCCESS = "92m"
    DANGER = "91m"
    INFO = "96m"

    @staticmethod
    def customMessage(message: str, styleMessage: str):
        border = f"\033[{styleMessage}+" + "="* (len(message) + 4) + "+\033[0m"
        print(border)
        print(f"\033[{styleMessage}|  {message}  |\033[0m")
        print(border)
        input()

    @staticmethod
    def invalidOption():
        print("\033[91m+=================================================================+\033[0m")
        print("\033[91m| OPÇÃO INVÁLIDA, TENTE NOVAMENTE, PRESSIONE ENTER PARA CONTINUAR |\033[0m")
        print("\033[91m+=================================================================+\033[0m")
        input()