import time
import smtplib
sent = 0

sender = "YOUR EMAIL HERE"
password = "APP PASSWORD HERE"
receiver = input("Enter receiver email: ")

print("Finding email...")
time.sleep(2)
print(f"Email {receiver} found")
print("Sending emails...")
time.sleep(1)

while True:

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender, password)
        message = "Hello"
        s.sendmail(sender, receiver, message)
        s.quit()
        sent += 1
        print(f"\rSent {sent} emails to {receiver}", end="", flush=True)
        if sent % 50 == 0:
            s.quit()
            print(f"Reached {sent} emails. Pausing for 5 seconds...")
            time.sleep(5)
            break

    except (smtplib.SMTPException, ConnectionError, OSError) as e:
        print(f"Connection lost: {e}. Retrying...")
        time.sleep(10)
