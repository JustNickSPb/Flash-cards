from blacksheep import Application, Request, delete, get, post, put

app = Application()


@get("/")
def home():
    return "Hello, World!"


@get("/cards")
def get_all_cards():
    return "Тут будет ендпойнт, отдающий все карточки"


@get("/cards/{id}")
def get_card_by_id(id: int):
    return f"Тут будет ендпойнт, отдающий карточку с id = {id}"


@post("/cards")
def add_card(request: Request):
    return "Тут будет ендпойнт, добавляющий карточку"


@put("/cards/{id}")
def update_card(id: int, request: Request):
    return f"Тут будет ендпойнт, обновляющий карточку с id = {id}"


@delete("/cards/{id}")
def delete_card(id: int):
    return f"Тут будет ендпойнт, удаляющий карточку с id = {id}"
