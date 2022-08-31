from flask import Flask,render_template, request, session, redirect, url_for
from flask_mail import Mail, Message
import smtplib, ssl
from threading import Thread
from flaskApp import constants
from flaskApp import helperfunctions

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

app.config.update(dict(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = constants.EMAIL,
    MAIL_PASSWORD = constants.EMAILPASSWORD,
))


mail = Mail(app)


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

@app.route("/about")
def about():
    return render_template("./about.html")


@app.route("/howItWorks")
def howItWorks():
    return render_template("./howItWorks.html")

@app.route("/legal")
def legal():
    return render_template("./legal.html")

@app.route("/search", methods=["GET"])
def search():
    args = request.args
    ticker = args.get("searchedTicker")
    if helperfunctions.isTickerValid(ticker):
        return redirect(
            url_for(
                "data", 
                companyTicker= ticker
            )
        )
    else:
        return redirect(url_for("tickerNotFound", InvalidTicker = ticker ))



@app.route("/tickerNotFound/<string:InvalidTicker>", methods=["GET"])
def tickerNotFound(InvalidTicker):
    args = request.args
    return render_template("./TickerNotFound.html", InvalidTicker = InvalidTicker)

@app.route("/data/<string:companyTicker>")
def data(companyTicker:str):
    return render_template(
        "data.html", 
        info = helperfunctions.getInfo(companyTicker),
        financials = helperfunctions.getFinancials(companyTicker),
        newsList = helperfunctions.getNews(companyTicker)
    )

@app.route("/ContactMe/HandleData", methods=['POST'])
def HandleData():
    projectpath = request.form    
    sendingEmail = projectpath.get("email")
    name = projectpath.get("name")
    subject = projectpath.get("subject")
    message = projectpath.get("content")
    msg = Message(
        subject = subject,
        recipients= [constants.SENDTOEMAIL],
        body = f"FROM: {name}, EMAIL: {sendingEmail}, \n {message}"
    )
    msg.sender = constants.EMAIL
    mail.send(msg)
    return redirect(url_for("ContactMe", sent=1))


if __name__ == '__main__':
    def run():
        app.run(host='0.0.0.0',port=8080)

    def keep_alive():
        t = Thread(target=run)
        t.start()
    keep_alive()

