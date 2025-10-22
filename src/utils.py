from colorama import Fore, Style, init
init(autoreset=True)

def banner():
    print(f"{Fore.YELLOW}{'='*40}")
    print(f"{Fore.CYAN}   🌤️  WEATHER CLI APP  🌦️")
    print(f"{Fore.YELLOW}{'='*40}{Style.RESET_ALL}")
