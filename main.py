import smtplib
import os



def send_email(messege):
    sender = "1kuperster@gmail.com"
    password = os.getenv()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, messege)

        return "yes"
    except Exception as _ex:
        return f"{_ex}\nCheck your login inn psaword please!"


def main():
    messege = input("test")
    print(send_email(messege=messege))


if __name__ == "__main__":
    main()
