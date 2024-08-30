
from dados import centro_oeste, sudeste, sul, nordeste, norte, unido
from flask import Flask, render_template, request, redirect
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = "DANIEL"
logado = False 


@app.route("/", methods=["GET"])
def home():
    global logado
    count = 0
    return render_template("index.html",
                           logado = logado,
                            centro_oeste = centro_oeste,
                            sudeste = sudeste,
                            sul = sul,
                            nordeste = nordeste,
                            norte = norte,
                            unido = unido,
                            count = count,
                           )    

@app.route('/entrar', methods = ["GET","POST"])
def entrar():
    
    return render_template('login_cadastro.html')

@app.route('/logar', methods = ["POST"])
def logar():
    global logado 
    email = request.form.get('email')
    senha = request.form.get('senha')

    with open('static/json/usuarios.json','r') as usuarios_doc:
        usuarios = json.load(usuarios_doc)
        
        for usuario in usuarios:
            print(usuario)
            if email == usuario['Email'] and senha == usuario['Senha']:
                logado = True
                return redirect('/')
            else:
                #Avisar o erro de email/senha
                print("Ble")
                print(usuarios)
                print(email)
                print(senha)
                count += 1
                pass
    return redirect('/entrar')
        
            


@app.route('/cadastrar', methods=["POST"])
def cadastrar():
    global logado
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    email = request.form.get('email')
    CEP = request.form.get('CEP')
    senha = request.form.get('senha')
    confirmar_senha = request.form.get('confirmar_senha')
    

    user_data = {"Nome":nome,
                "Telefone":telefone,
                "Email":email,
                "CEP":CEP,
                "Senha":senha,}   
    
    with open('static/json/usuarios.json','r') as usuarios_doc:
        try: 
            usuarios = json.load(usuarios_doc)
        except json.JSONDecodeError:
            usuarios = []
        usuarios.append(user_data)

        #Fazer Verificação de dados
    with open('static/json/usuarios.json',"w") as usuarios_doc: 
        json.dump(usuarios, usuarios_doc,indent=4)
    logado = True
    return redirect("/")











@app.route('/sair', methods = ["GET"])
def sair():
    global logado
    logado = False
    return redirect("/")

app.run()