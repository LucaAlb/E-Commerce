import pandas as pd
import json as js


# trasformazione magazzino.csv in json per API
magazzino = pd.read_csv("../csv/csv_analisi/magazzino.csv", delimiter = ",")
magazzino_json = magazzino.to_json(orient = "records")
with open ("../json/json_api/magazzino.json","w") as file:
    file.write(magazzino_json)
magazzino_json = js.load(open("../json/json_api/magazzino.json"))


# trasformazione vendite.csv in json per API
vendite = pd.read_csv("../csv/csv_analisi/vendite.csv", delimiter = ",")
vendite_json = vendite.to_json(orient = "records")
with open ("../json/json_api/vendite.json","w") as file:
    file.write(vendite_json)
vendite_json = js.load(open("../json/json_api/vendite.json"))


# trasformazione prodotti.csv in json per API
prodotti = pd.read_csv("../csv/csv_analisi/prodotti_.csv", delimiter = ",")
prodotti_json = prodotti.to_json(orient = "records")
with open ("../json/json_api/prodotti.json","w") as file:
    file.write(prodotti_json)
prodotti_json = js.load(open("../json/json_api/prodotti.json"))


# trasformazione eventi.csv in json per API
eventi = pd.read_csv("../csv/csv_analisi/eventi_tot.csv", delimiter = ",")
eventi_json = eventi.to_json(orient = "records")
with open ("../json/json_api/eventi.json","w") as file:
    file.write(eventi_json)
eventi_json = js.load(open("../json/json_api/eventi.json"))