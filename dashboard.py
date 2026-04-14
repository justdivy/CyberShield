from colorama import Fore, Style, init
init(autoreset=True)

def print_banner():
    print(Fore.CYAN + """
  ██████╗██╗   ██╗██████╗ ███████╗██████╗ ███████╗██╗  ██╗██╗███████╗██╗     ██████╗
 ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║  ██║██║██╔════╝██║     ██╔══██╗
 ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝███████╗███████║██║█████╗  ██║     ██║  ██║
 ╚██████╗  ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗╚════██║██╔══██║██║██╔══╝  ██████╗ ██████╔╝
  ╚═════╝   ██║   ██████╔╝███████╗██║  ██║███████║██║  ██║██║███████╗███████╗██╔═══╝
            ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝
    """ + Style.RESET_ALL)

def print_dashboard(engine):
    print_banner()
    print(Fore.WHITE + "=" * 70)
    print(f"  {'THREAT TYPE':<20} {'STATUS':<16} {'TARGET'}")
    print("=" * 70 + Style.RESET_ALL)

    for threat in engine.threats:
        threat.report()

    total, detected = engine.get_summary()
    print(Fore.WHITE + "=" * 70)

    if detected == 0:
        print(Fore.GREEN + f"  RESULT: All {total} scans CLEAN. System is SECURE. ✔")
    else:
        print(Fore.RED + f"  RESULT: {detected}/{total} threats DETECTED! Immediate action required. ✘")

    print("=" * 70 + Style.RESET_ALL)