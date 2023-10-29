from fastapi import FastAPI

app_v1 = FastAPI()


@app_v1.get('/pokemon')
async def get_pokemon():
    return {
        "Id": "0006",
        "Name": "Charizard",
        "Type": ["FIRE", "FLYING"],
        "Species": "Flame Pokémon",
        "Height": "1.7 m",
        "Weight": "90.5 kg",
        "Abilities": [
            "Blaze",
            "Solar Power"
        ],
    }
