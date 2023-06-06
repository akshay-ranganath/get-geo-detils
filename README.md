# Get Geo Details

This is a [FastAPI](https://fastapi.tiangolo.com/) based implementation for returning the lat/long lookup. The actual lookup occurs using the [reverse-geocoder](https://github.com/thampiman/reverse-geocoder) library.

## Installation

For safety, please create a virtual environment. Next, clone this repository. After that, please install the dependencies.

```
pip install -r requirements.txt
```

## Usage
Once the libraries are installed, start the service. If you are also planning to make changes to the code, enable the option to fast-reload the change.

```
uvicorn coords:app --reload
```

## Testing
To test the service, you would need to pass the lat/long. The service end point is `/coords` and expects a query parameter with the same name. For example, here's a lookup for New York.

```
curl -vs http://127.0.0.1:8000/coords?coords=73%20deg%2056%27%206.87%22%20W:40%20deg%2043%27%2050.19%22%20N
```

where, the value `73° 56' 6.8712" W:40° 43' 50.1954" N` encodes the longitude and latitude for the place.

In many cases, the lat/long is presented as a simple decimal. If you need to convert it to the degree/hour format, please use the [helper service](https://www.fcc.gov/media/radio/dms-decimal).