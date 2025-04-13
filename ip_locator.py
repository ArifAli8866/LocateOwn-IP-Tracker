import requests
import os
import time

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print("="*50)
    print("█░░ █▀█ █▀█ ▄▀█ █▀▀ █▀█ █░█ █▄█ █▀█ █▀█ █▄░█")
    print("█▄▄ █▄█ █▀▄ █▀█ █▄█ █▀▄ █▄█ ░█░ █▄█ █▄█ █░▀█")
    print(" "*15 + "by Arif Ali")
    print("="*50)

def get_ip_info(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()

        print("\n[+] IP Info:")
        print("-" * 40)
        print(f" IP Address : {data.get('ip')}")
        print(f" City       : {data.get('city')}")
        print(f" Region     : {data.get('region')}")
        print(f" Country    : {data.get('country')}")
        print(f" Location   : {data.get('loc')}")
        print(f" ISP        : {data.get('org')}")
        print("-" * 40)

    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    clear_screen()
    banner()

    while True:
        ip = input("\nEnter IP Address (or type 'exit' to quit): ")
        if ip.lower() == 'exit':
            print("\nExiting... Thank you for using LocateOwn 💻")
            time.sleep(1)
            break
        else:
            get_ip_info(ip)

if __name__ == "__main__":
    main()
