import random

DINO_NAMES = (
    "Alenossauro Rex",
    "Lucirodonte",
    "Alex Raptor",
    "Caiquerátops",
    "Raphazilla",
    "Gustarodáctilo",
)


def generate_dino_deck() -> list[dict]:

    return [
        {
            "name": name,
            "strength": random.randint(1, 10),
            "agility": round(random.uniform(0, 10), 1),
            "heigth": round(random.uniform(0, 10), 2),
        }
        for name in DINO_NAMES
    ]


def split_deck(deck: list[dict]):
    half_deck = len(deck) // 2

    random.shuffle(deck)

    return (
        deck[:half_deck],
        deck[half_deck:],
    )


def get_random_attr(card: dict) -> str:
    card_keys = [key for key in card.keys() if key != "name"]

    # choice pega um item aleatório de uma sequência
    return random.choice(card_keys)
