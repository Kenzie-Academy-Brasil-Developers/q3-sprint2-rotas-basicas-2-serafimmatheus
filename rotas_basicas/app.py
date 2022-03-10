from flask import Flask

from http import HTTPStatus

from datetime import datetime

app = Flask(__name__)

@app.get("/")
def home():
    return {"data": "Hello Flask!"}, HTTPStatus.OK

@app.get("/current_datetime")
def current_datetime():
    data = int(datetime.now().strftime("%H"))
    data_formated = datetime.now().strftime("%d/%m/%Y %I:%M:%S %P").upper()

    if data < 12:
         return {"current_datetime": data_formated, "message": "Bom dia!"}, HTTPStatus.OK

    elif data >= 12 and data < 18:
         return {"current_datetime": data_formated, "message": "Boa tarde!"}, HTTPStatus.OK

    else:
         return {"current_datetime": data_formated, "message": "Boa noite!"}, HTTPStatus.OK


