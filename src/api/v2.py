from fastapi import FastAPI

app_v2 = FastAPI()


@app_v2.get('/pokemon')
async def get_pokemon_new():
    return {
        "Id": "0006",
        # Newly Added in v2
        "Generation": "1",
        "Name": "Charizard",
        "Type": ["FIRE", "FLYING"],
        "Species": "Flame Pokémon",
        "Height": "1.7 m",
        "Weight": "90.5 kg",
        "Abilities": [
            "Blaze",
            "Solar Power"
        ],
        # New support added in v2
        "stats": {
            "HP": {
                "Base": 78,
                "Min": 266,
                "Max": 360
            },
            "Attack": {
                "Base": 84,
                "Min": 155,
                "Max": 293
            }
        }
    }
