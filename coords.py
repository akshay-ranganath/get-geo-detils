from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from util import get_location

app = FastAPI()

@app.get("/")
def read_root():
    """Default function to be used for troubleshooting.

    Returns:
        Null
    """
    return {"Hello": "World"}

@app.get("/coords")
def get_coordinates(coords: Union[str, None] = None, public_id: Union[str, None] = None):
    """Look up the city, state and country information for a give lat/long combination.

    Returns:
        JSON containing the geo information

    """    
    return get_location(coords)    

# invoking and restarting the screens:
# https://www.howtogeek.com/662422/how-to-use-linuxs-screen-command/