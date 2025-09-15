import smtplib
import socks
import random
import time
import string
from email.mime.text import MIMEText
from colorama import Fore, init

init(autoreset=True)

print(r'''
    _____                _ _  ______                 _               
    |  ___|              (_) | | ___ \               | |              
    | |__ _ __ ___   __ _ _| | | |_/ / ___  _ __ ___ | |__   ___ _ __ 
    |  __| '_ ` _ \ / _` | | | | ___ \/ _ \| '_ ` _ \| '_ \ / _ \ '__|
    | |__| | | | | | (_| | | | | |_/ / (_) | | | | | | |_) |  __/ |   
    \____/_| |_| |_|\__,_|_|_| \____/ \___/|_| |_| |_|_.__/ \___|_|   
                                                                    
                                                                    
''')

def load_senders(file_path):
    senders = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split('"')
            if len(parts) >= 3:
                email = parts[1].strip()
                app_password = parts[3].strip()
                senders.append((email, app_password))
    if not senders:
        raise Exception("No senders found in senders.txt")
    return senders

def load_proxies(file_path):
    proxies = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            proxy = line.strip()
            if proxy:
                proxies.append(proxy)
    if not proxies:
        print(Fore.RED + "No proxies available in proxy.txt.")
    return proxies

def generate_random_string(length):
    """Generate a random string of uppercase, lowercase letters and digits."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send_emails():
    recipient = input(Fore.WHITE + "Recipient's Email: ")

    senders = load_senders("senders.txt")

    use_proxies = input(Fore.WHITE + "Would you like to use proxies? (yes/no): ").strip().lower()

    proxies = []
    if use_proxies == "yes":
        proxies = load_proxies("proxy.txt")
    
    # If no proxies are used, skip proxy-related code
    if use_proxies == "no" and not proxies:
        print(Fore.GREEN + "Proceeding without proxies...")

    smtp_server = "smtp.gmail.com"
    port = 587

    times_to_send = int(input(Fore.WHITE + "Times to send: "))
    
    timeout_count = 0
    random_proxy_option = input(Fore.WHITE + "After 2 timeouts, would you like to use a random proxy? (Y/n): ").strip().lower() or "y"

    for i in range(times_to_send):
        # Generate new random subject and body every time
        subject = generate_random_string(10)  # Random subject with 10 characters
        body = generate_random_string(50)    # Random body with 50 characters
        print(Fore.GREEN + f"Random Subject for email {i+1}: {subject}")
        print(Fore.GREEN + f"Random Body for email {i+1}: {body}")

        # If proxies are being used, handle proxy logic
        if use_proxies == "yes" and proxies:
            if timeout_count >= 2:  # After two timeouts, prompt to use a random proxy
                if random_proxy_option != "n":
                    proxy = random.choice(proxies)
                    print(Fore.GREEN + f"Using random proxy: {proxy}")
                else:
                    proxy = proxies[i % len(proxies)]
                    print(Fore.GREEN + f"Using sequential proxy: {proxy}")

                proxy_ip, proxy_port = proxy.split(":")
                socks.set_default_proxy(socks.SOCKS5, proxy_ip, int(proxy_port))
                socks.wrapmodule(smtplib)

                print(Fore.WHITE + f"Connecting to proxy {proxy}...")
                try:
                    # Test the proxy by making a connection
                    with smtplib.SMTP(smtp_server, port) as test_server:
                        test_server.ehlo()
                        test_server.starttls()
                        test_server.ehlo()
                        print(Fore.GREEN + f"Successfully connected to proxy: {proxy}")
                    time.sleep(2)  # Reset time for next email
                except Exception as e:
                    print(Fore.RED + f"Failed to connect to proxy {proxy}: {e}")
                    time.sleep(2)  # Wait for a while before trying again
                    continue  # Retry this email with the next proxy or default flow

        sender_email, sender_pass = senders[i % len(senders)]
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient

        print(Fore.WHITE + f"Sending email {i+1} from {sender_email} to {recipient}")
        
        try:
            start_time = time.time()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(sender_email, sender_pass)
                
                server.sendmail(sender_email, recipient, msg.as_string())
                elapsed_time = time.time() - start_time
                
                if elapsed_time > 5:
                    print(Fore.RED + f"Timeout! Resetting after 5 seconds for email {i+1}")
                    timeout_count += 1
                    time.sleep(2)
                    continue  # Skip to the next iteration, reset the process
                
            print(Fore.GREEN + "Email sent!\n")
            timeout_count = 0  # Reset timeout count after successful email
            
        except Exception as e:
            print(Fore.RED + f"Error sending email: {e}")
            timeout_count += 1
            if timeout_count >= 2:
                print(Fore.RED + "Two timeouts encountered, consider using a random proxy!")

if __name__ == "__main__":
    send_emails()
