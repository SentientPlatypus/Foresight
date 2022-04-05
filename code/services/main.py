from flask import Flask,render_template, request, session, redirect, url_for
import smtplib, ssl
from threading import Thread
import csv
context = ssl.create_default_context()


class constants():
    EMAILREGEX            = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    EMAIL                 = "trexycrocs@gmail.com"
    EMAILPASSWORD         = "geneavianina"
    PORT                  = 465  # For SSL

#path = '/home/SentientPlatypus/Personal-platypus-website/code'
#if path not in sys.path:
#    sys.path.append(path)

#from services.main import app as application

def createApp():
    app = Flask(
    __name__,
    template_folder=r"templates",
    static_folder=r"static"
    )
    return app

app = createApp()

@app.route("/")
def home():
    return render_template("./index.html")

@app.route("/index")
def home1():
    return render_template("./index.html")

@app.route("/ContactMe/<int:sent>")
def ContactMe(sent):
    bool = False
    if sent == 1:
        bool = True
    return render_template("./index.html", sent=bool)


    
@app.route("/ContactMe/HandleData", methods=['POST'])
def HandleData():
    projectpath = request.form
    print(projectpath)
    form = {}
    for key in projectpath.keys():
        values = projectpath.getlist(key)
        if len(values) == 1:
            form[key] = values[0]
        else:
            form[key] = values

    sendingEmail = form["email"]
    name = form["name"]
    subject = form["subject"]
    message = form["content"]

    # with open("./contacts.csv", "a") as f:
    #     csvWriter = csv.writer(f)
    #     csvWriter.writerow([name, sendingEmail, subject, message])
    gmail_user = constants.EMAIL
    gmail_password = constants.EMAILPASSWORD
    to = [constants.EMAIL]
    email_text = """
    From: %s , %s
    To: %s
    Subject: %s

    %s
    """ % (sendingEmail,name, ", ".join(to), subject, message)
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sendingEmail, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….", ex)
    return redirect(url_for("ContactMe", sent=1))


def run():
  app.run(host='0.0.0.0',port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()


if __name__ == '__main__':
    keep_alive()

