import pandas as pd
import json as js

# centri distribuzione caricati da csv e trasformati in json
centri_distribution = pd.read_csv("../csv/csv_origini_dati/centri_distribuzione.csv", delimiter = ",")
centri_distribuzione_json = centri_distribution.to_json(orient="records")
with open("../json/json_origini_dati/centri_distribuzione.json", "w") as file:
    file.write(centri_distribuzione_json)
centri_distribuzione_json = js.load(open("../json/json_origine_dati/centri_distribuzione.json"))
centri_distr_ = pd.DataFrame(centri_distribuzione_json)


# ordini prodotti caricati da csv e trasformati in json
ordini_prodotti = pd.read_csv("../csv/csv_origini_dati/ordini_prodotti.csv", delimiter = ',')
ordini_prodotti_json = ordini_prodotti.to_json(orient='records')
with open('../json/json_origine_dati/ordini_prodotti.json', 'w') as file:
    file.write(ordini_prodotti_json)
ordini_prodotti_json = js.load(open("../json/json_origine_dati/ordini_prodotti.json"))
ordini_prodotti_ = pd.DataFrame(ordini_prodotti_json)


# minorenni caricati da csv e trasformati in json
minorenni = pd.read_csv("../csv/csv_origini_dati/eventi/minorenni.csv", delimiter = ',')
minorenni_json = minorenni.to_json(orient='records')
with open('../json/json_origine_dati/minorenni.json', 'w') as file:
    file.write(minorenni_json)
minorenni_json = js.load(open("../json/json_origine_dati/minorenni.json"))
minorenni_ = pd.DataFrame(minorenni_json)


# prodotti caricati da csv e trasformati in json
prodotti = pd.read_csv("../csv/csv_origini_dati/prodotti.csv", delimiter = ',')
prodotti_json = prodotti.to_json(orient='records')
with open('../json/json_origine_dati/prodotti.json', 'w') as file:
    file.write(prodotti_json)
prodotti_json = js.load(open("../json/json_origine_datiprodotti.json"))
prodotti_ = pd.DataFrame(prodotti_json)


# utenti caricati da csv e trasformati in json
utenti = pd.read_csv("../csv/csv_origini_dati/utenti.csv", delimiter = ',')
utenti_json = utenti.to_json(orient='records')
with open('../json/json_origine_dati/utenti.json', 'w') as file:
    file.write(utenti_json)
utenti_json = js.load(open("../json/json_origine_dati/utenti.json"))
utenti_ = pd.DataFrame(utenti_json)


#adulti caricati da csv e trasformati in json
adulti = pd.read_csv("../csv/csv_origini_dati/eventi/adulti.csv", delimiter = ',')
adulti_json = adulti.to_json(orient='records')
with open('../json/json_origine_dati/adulti.json', 'w') as file:
    file.write(adulti_json)
adulti_json = js.load(open("../json/json_origine_dati/adulti.json"))
adulti_ = pd.DataFrame(adulti_json)


# ordini caricati da csv e trasformati in json
ordini = pd.read_csv("../csv/csv_origini_dati//ordini.csv", delimiter = ',')
ordini_json = ordini.to_json(orient='records')
with open('../json/json_origine_dati/ordini.json', 'w') as file:
    file.write(adulti_json)
ordini_json = js.load(open("../json/json_origine_dati/ordini.json"))
ordini_ = pd.DataFrame(ordini_json)