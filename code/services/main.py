from flask import Flask,render_template, request, session, redirect, url_for
import smtplib, ssl
from threading import Thread
import yfinance as yf
import requests
import constants
import csv
import helperfunctions

context = ssl.create_default_context()


class constants():
    EMAILREGEX            = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    EMAIL                 = "trexycrocs@gmail.com"
    EMAILPASSWORD         = "geneavianina"
    PORT                  = 465  # For SSL
    API_WEBSITE_URL         = "https://ForesightAPI.sentientplatypu.repl.co"

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



@app.errorhandler(404)
def page_not_found(e):
    return render_template(
        "./error.html",
        code = 404,
        msg = f"page not found. It simply does not exist lmao.",
        desc = f"{e}"
    )

@app.errorhandler(500)
def InternalError(e):
    return render_template(
        "./error.html",
        code = 500,
        msg = f"Internal server error.",
        desc = f"{e}"
    )

@app.errorhandler(403)
def forbidden(e):
    return render_template(
        "./error.html",
        code = 403,
        msg = f"Forbidden. We tried to fetch some data. You said no. Thats ok. Consent is great.",
        desc = f"{e}"
    )

@app.route("/")
def home():
    return render_template("./index.html")

@app.route("/home")
def home2():
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



@app.route("/search", methods=["GET"])
def search():
    args = request.args
    ticker = args.get("searchedTicker")
    
    tickerObj = yf.Ticker(ticker)
    if helperfunctions.isTickerValid(tickerObj):
        company_info = tickerObj.info
        print(company_info)
        return redirect(
            url_for(
                "data", 
                company = ("'" + tickerObj.info["longName"] + "'")
            )
        )
    else:
        return redirect(url_for("tickerNotFound", InvalidTicker = ticker ))




@app.route("/tickerNotFound/<string:InvalidTicker>", methods=["GET"])
def tickerNotFound(InvalidTicker):
    args = request.args
    return render_template("./TickerNotFound.html", InvalidTicker = InvalidTicker)

@app.route("/data/<string:company>")
def data(company: str):
    return render_template("data.html", companyName=company)
    













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

