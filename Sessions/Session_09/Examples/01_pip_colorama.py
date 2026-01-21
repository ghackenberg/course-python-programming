import colorama
from colorama import Fore, Style

# Initialize colorama (needed for Windows CMD)
colorama.init()

print(Fore.RED + "Error: Something went wrong!")
print(Fore.GREEN + "Success: Package installed.")
print(Style.RESET_ALL + "System status: Nominal")
