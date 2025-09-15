# Email Nuker

A script designed to send bulk emails using app-specific keys with proxy support for enhanced security and anonymity.

## Features

- **App-Specific Keys**: Sends emails using app-generated keys (e.g., Gmail App Passwords).
- **Proxy Support**: Option to route emails through proxies to maintain anonymity.
- **Customizable**: Allows users to specify email subjects, bodies, and more.
- **Random Generation**: Option to use random subject lines and body content for each email.

## DISCLAIMER

**IMPORTANT**: This tool is **only for testing purposes** on systems you own or have explicit permission to test on.

- **Illegal Use**: Unauthorized use, including spamming or any malicious activities, is **strictly prohibited**.
- **Consequences**: Misuse of this tool could lead to **serious legal consequences**.
- **Responsible Usage**: Always ensure you're testing on systems you own or have permission to use.

By using this tool, you agree to take full responsibility for your actions. The author is not liable for any illegal activity or damages resulting from the use of this script.

## Requirements

- Python 3.x
- Required Python packages:
  - `smtplib`
  - `socks`
  - `random`
  - `time`
  - `email`
  - `colorama` (for colored output in terminal)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/email-nuker.git
   cd email-nuker

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `senders.txt` file with the appropriate app-specific keys and sender emails. The format should be as follows:

   ```
   "email1@gmail.com" "app_password1"
   "email2@gmail.com" "app_password2"
   ```

4. (Optional) Set up your `proxy.txt` file with proxies if you want to route emails through them. The format for each line should be `IP:PORT`:

   ```
   192.168.1.1:1080
   192.168.1.2:1080
   ```

## Usage

1. **Run the script**:

   ```bash
   python main.py
   ```

2. **Follow the prompts** to provide:

   * Recipient email
   * Email subject (or opt for random subject generation)
   * Email body (or opt for random body generation)
   * Number of emails to send
   * Option to use proxies for routing the emails

   Example:

   ```bash
   Recipient's Email: target@example.com
   Subject: RandomSubject123
   Body: RandomBody456
   Times to send: 10
   ```

3. **Disclaimer**: This script is intended for **ethical testing** only. Ensure you are legally allowed to use this tool on the target systems.

## Example

```bash
$ python main.py
Recipient's Email: target@example.com
Subject: RandomSubject123
Body: RandomBody456
Times to send: 10
```

The script will generate a random subject and body for each email and send the specified number of emails to the recipient.

## Legal Notice

This script is for **educational and testing purposes only**. The developer is not responsible for any misuse or illegal activities resulting from the use of this tool. Always respect privacy laws and regulations when using this or any similar script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Important Notes:

* **Use responsibly**: This tool should only be used for testing purposes on your own systems or systems where you have explicit permission to test.
* **App Passwords**: If using Gmail, ensure that you generate **App Passwords** for your Google accounts and do **not** use your regular account passwords.
* **Proxy Support**: You can route the emails through proxies by enabling the proxy option in the script. Be aware of the legality and ethical considerations of using proxies.

If you encounter any issues or have any questions, feel free to open an issue or submit a pull request.

---

### How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

Thank you for contributing!
