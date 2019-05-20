from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('cr_pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    return render_template("index.html", all_pets=pets)

@app.route('/create_pet', methods=["POST"])
def add_pet():
    mysql = connectToMySQL('cr_pets')
    query = 'INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());'
    data = {
        'name': request.form['pet_name'],
        'type': request.form['pet_type']
    }
    new_pet_id = mysql.query_db(query, data)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry! No response. Try again.'

if __name__=='__main__':
    app.run(debug=True)