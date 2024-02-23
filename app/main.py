from blacksheep import Application, get

app = Application()


@get("/")
def home():
    return "Hello, World!"
