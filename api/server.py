from flask import Flask, jsonify, request,render_template,send_file
import json 
app = Flask(__name__)
# app.debug = True


#caricamento diverse pagine del sito
# per caricare la home page
@app.route('/') 
def home():
    return render_template('index.html')

#per caricare il magazzino
@app.route('/magazzino')
def magazzino():
    return render_template('magazzino.html')

#per caricare il marketing
@app.route("/marketing")
def marketing():
    return render_template("marketing.html")

#per caricare le vendite
@app.route("/vendite")
def vendite():
    return render_template("vendite.html")

#per accedere alle sezione chiedi aiuto
@app.route('/help')
def help():
    return render_template('help.html')

#per accwdere alla sezione "ACCEDI"
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/accesso')
def accesso():
    return render_template('accesso_api.html')


#carimento delle pagine per json
@app.route("/api", methods=['GET']) # API endpoint 2
def api():
    dipartimento = request.args.get("dipartimento","amministratore")
    if dipartimento == "magazzino":
        # content = open("C:\\Users\\win10pro\\Desktop\\GENERATION\\Project-Work\\api\\json\\json_api\\magazzino.json") 
        return send_file ("..\json\\json_api\\magazzino.json") 
    elif dipartimento == "vendite":
        return send_file ("..\\json\\json_api\\vendite.json") 
    elif dipartimento == "marketing":
        return send_file ("..\\json\\json_api\\eventi.json")
    else :
        return f"Effettua l'accesso"
#     content = open('path').read()
# content = #leggete il file dal sistema operativo con open
#     return Response(content, mimetype="text/html")


if __name__ == '__main__':
    app.run(port=8000)

