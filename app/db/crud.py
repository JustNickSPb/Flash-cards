async def get_all_cards() -> list:
    return []


async def get_card_by_id(id: int) -> dict:  # TODO: тут будет Card, найденный по id или None
    return {}


async def add_card(card_data: dict) -> dict:  # TODO: тут будет Card, созданный в БД
    return {}


async def update_card(card_data: dict) -> dict:  # TODO: тут будет обновленный Card
    return {}


async def delete_card(id: int) -> bool:  # TODO: успешное ли удаление
    return {}
