from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro_cliente():
    nome = request.form['nome']
    idade = request.form['idade']

    # Conectar ao banco de dados MySQL
    conn = mysql.connector.connect(host='localhost', user='seu_usuario', password='sua_senha', database='sua_base_de_dados')
    cursor = conn.cursor()

    # Inserir dados na tabela clientes
    cursor.execute("INSERT INTO clientes (nome, idade) VALUES (%s, %s)", (nome, idade))
    conn.commit()

    cursor.close()
    conn.close()

    return 'Cliente cadastrado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
