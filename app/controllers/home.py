from blacksheep.server.controllers import Controller, get


class Cards(Controller):
    @get()
    def index(self):
        return self.view()
