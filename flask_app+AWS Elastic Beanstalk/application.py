from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello, World from Flask Main Page"


@application.route("/help")
def help_page():
    return "<b>This is a Help Page</b>"


@application.route("/user")
def user_page():
    return "User`s main page"


@application.route("/user/<username>")
def show_user_page(username):
    return "Hello, " + username.upper()


@application.route("/path/<path:subpath>")
def show_subpath(subpath):
    return "Subpath is: " + subpath


@application.route("/power_of/<int:x>")
def power_of(x):
    return "Power of " + str(x) + " = " + str(x*x)


@application.route("/html")
def show_html():
    my_file = open("index.html", mode='r') #mock-up of future site
    page = my_file.read()
    my_file.close()
    return page


#------------------MAIN------------------#
if __name__ == "__main__":
#    application.debug = True    #adds restarting feature after detecting changes
#    application.env = "Testing"
     application.run()
#----------------------------------------#