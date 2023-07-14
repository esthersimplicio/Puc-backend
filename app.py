from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL
from flasgger import Swagger, swag_from
from flask_cors import CORS 
import pymysql

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mvp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # Usado para obter resultados em formato de dicionário


template = 'api/swagger.yml'
CORS(app)
CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "True"}})
swagger = Swagger(app, template_file=template)


mysql = MySQL(app)

# Verificar conexão com o servidor MySQL
try:
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        db=app.config['MYSQL_DB']
    )
    print("Conexão com o servidor MySQL estabelecida com sucesso!")
except pymysql.MySQLError as e:
    print("Não foi possível estabelecer conexão com o servidor MySQL:", str(e))


@app.route('/')
def Index():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM animais")
            data = cursor.fetchall()
        print(data)  # Verifique os dados impressos no terminal
        return render_template('index.html', animais=data)
    except pymysql.MySQLError as e:
        flash("Erro ao obter dados dos pacientes do banco de dados")
        return redirect(url_for('Index'))




@app.route('/insert', methods=['POST'])
@swag_from('api/endpoints/cadastrar.yml')
def insert():
    if request.method == "POST":
        try:
            nome_tutor = request.form['nome_tutor']
            contato = request.form['contato']
            nome_animal = request.form['nome_animal']
            especie = request.form['especie']
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO animais (nome_tutor, contato, nome_animal, especie) VALUES (%s, %s, %s, %s)", (nome_tutor, contato, nome_animal, especie))
                connection.commit()
            flash("Dados salvos com sucesso")
        except pymysql.MySQLError as e:
            flash("Não foi possível salvar os dados")
        return redirect(url_for('Index'))



@app.route('/delete/<int:id>', methods=['POST'])
@swag_from('api/endpoints/deletar.yml')
def delete(id):
    if request.method == 'POST':
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM animais WHERE id=%s", (id,))
                connection.commit()
            flash("Usuário excluído com sucesso")
        except Exception as e:
            flash("Não foi possível excluir o usuário")
        return redirect(url_for('Index'))
    else:
        return redirect(url_for('Index'))

    

@app.route('/update/<int:id>', methods=['POST'])
@swag_from('api/endpoints/atualizar.yml')
def update(id):
    if request.method == 'POST':
        try:
            nome_tutor = request.form['nome_tutor']
            contato = request.form['contato']
            nome_animal = request.form['nome_animal']
            especie = request.form['especie']
            with connection.cursor() as cursor:
                cursor.execute("""
                UPDATE animais SET nome_tutor=%s, contato=%s, nome_animal=%s, especie=%s
                WHERE id=%s
                """, (nome_tutor, contato, nome_animal, especie, id))
                connection.commit()
            flash("Dados do paciente atualizados com sucesso")
        except pymysql.MySQLError as e:
            flash("Não foi possível atualizar os dados: " + str(e))
        except Exception as e:
            flash("Ocorreu um erro durante a atualização dos dados: " + str(e))
        return redirect(url_for('Index'))




if __name__ == "__main__":
    app.run(debug=True, port=3306)