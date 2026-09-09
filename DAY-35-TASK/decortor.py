def login(func):

    def wrap():
        print("Checking login")
        func()

    return wrap
@login
def dashboard():
    print("Welcome to Dashboard")

dashboard()
