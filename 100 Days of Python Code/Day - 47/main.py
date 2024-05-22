from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

response = requests.get(url="https://www.amazon.in/ASUS-TUF-Gaming-F17-FX706HF-HX019W/dp/B0CGDN1SFW/ref=sr_1_9?crid=N9DUU3T4DM9T&dib=eyJ2IjoiMSJ9.ups80AfLkzL2phQoR8Ks1O7hYKic0_QEwFe0dvRwF-ViE51B38D9294LpOvfE399fNBjYaSGgyPO4Dus9ym1wlrLJM1jKI46aDKuwsuiwigDAgZ_YlupRUuqaT37nz9GjlNSvJOpn7SpqLK7QAzMWpoEPsG8WuHShEFcAEYKBMbWwPECn7lNsbbnQmDi6GM2_6u8GYHwpplK57eshtJ8p3W3RYuVezd1OjjfyZVSyxI.Rk-7JiePdg8T520HAuI1kD1OuOG_idqpJpKghaknk3w&dib_tag=se&keywords=laptop+asus+tuf&qid=1712431685&sprefix=%2Caps%2C180&sr=8-9")
amazon_item_website = response.text

soup = BeautifulSoup(amazon_item_website, "lxml")
price = soup.find(name="span", class_="a-price-whole").get_text()
price = price[:-1]
price = price.split(",")
price = float("".join(price))
print(price)
if price < 60000:
    my_email = "jmkl0987@gmail.com"
    to_email = "jmkl0987@gmail.com"
    password = os.environ["EMAIL_PASSWORD"]
    message = f"ASUS TUF Laptop is now available at {price}. Order now!!"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: Low price alert for your Asus TUF Laptop!!\n\n{message}"
        )