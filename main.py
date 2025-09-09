import random
import smtplib
import datetime as dt


my_email = "nikshiqinikolas@gmail.com"
password = "akjsjcnxaderunyy"

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 3:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        list_of_quotes = [line.strip() for line in quotes if line.strip()]
        random_quote = random.choice(list_of_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            msg=f"Subject: Hey\n\n"
                                f"{random_quote}",
                            to_addrs="n.nikshiqi@gmail.com")




