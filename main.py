from http.client import BAD_REQUEST, FORBIDDEN, INTERNAL_SERVER_ERROR, METHOD_NOT_ALLOWED, NOT_FOUND, UNAUTHORIZED
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import secrets
from db import create_table_writekey, create_table_readkey, create_table_adc, get_db
import write
import read

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == "READ":
            create_table_readkey()
            keyread = secrets.token_urlsafe(16)
            db = get_db()
            cursor = db.cursor()
            query = "INSERT INTO readkey_table(key) VALUES (?)"
            cursor.execute(query, [keyread])
            db.commit()
            return render_template("read.html", keyread=keyread)
        elif request.form.get('action2') == "WRITE":
            create_table_writekey()
            keywrite = secrets.token_urlsafe(16)
            db = get_db()
            cursor = db.cursor()
            query = "INSERT INTO writekey_table(key) VALUES (?)"
            cursor.execute(query, [keywrite])
            db.commit()
            return render_template("write.html", keywrite=keywrite)
        else:
            pass
    else:
        return render_template('index.html')

@app.route('/api/adc/<keyread>', methods=['GET'])
def get_adc(keyread):
    try:
        if verifyKeyread(keyread) == keyread:
            result = read.get_adc()
            resp = jsonify(result)
            resp.status_code = 200
            return resp
        else:
            pass
    except:
        data = {
                
                'status': 404,
                'message': "APIKey Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

@app.route('/api/adc/<keywrite>', methods=['POST'])
def insert_adc(keywrite):
    try:
        if verifyKeywrite(keywrite) == keywrite:
            data = request.json
            adc = data['adc']
            print(adc)
            result = write.insert_adc(adc)
            data = {
                    
                        'status': 201,
                        'message': result
                    
                    }
                
            resp = jsonify(data)
            resp.status_code = 201
            return resp
        else:
            pass
    except:
        data = {
                
                'status': 404,
                'message': "APIKey Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

def verifyKeyread(key):
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT key FROM readkey_table WHERE key = ?"
    cursor.execute(query, [key])
    result = cursor.fetchone()
    return result[0]

def verifyKeywrite(key):
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT key FROM writekey_table WHERE key = ?"
    cursor.execute(query, [key])
    result = cursor.fetchone()
    return result[0]

@app.errorhandler(404)
def forbidden(error=NOT_FOUND):
    message = {
        
            'status': 404,
            'message': 'Forbidden Access'
        }
    
    resp = jsonify(message)
    resp.status_code = 404
    
    return resp

@app.errorhandler(403)
def forbidden(error=FORBIDDEN):
    message = {
        
            'status': 403,
            'message': 'Forbidden Access'
        }
    
    resp = jsonify(message)
    resp.status_code = 403
    
    return resp

@app.errorhandler(405)
def methodnotallowed(error=METHOD_NOT_ALLOWED):
    message = {
        
            'status': 405,
            'message': 'method not allowed'
        }
    
    resp = jsonify(message)
    resp.status_code = 405
    
    return resp

@app.errorhandler(500)
def internalserver(error=INTERNAL_SERVER_ERROR):
    message = {
        
            'status': 500,
            'message': 'internal server error'
        }
    
    resp = jsonify(message)
    resp.status_code = 500
    
    return resp

@app.errorhandler(400)
def badrequest(error=BAD_REQUEST):
    message = {
        
            'status': 400,
            'message': 'Bad Request'
        }
    
    resp = jsonify(message)
    resp.status_code = 400
    
    return resp

@app.errorhandler(401)
def unauthorized(error=UNAUTHORIZED):
    message = {
        
            'status': 401,
            'message': 'Unauthorized Login'
        }
    
    resp = jsonify(message)
    resp.status_code = 401
    
    return resp

if __name__ == "__main__":
    create_table_readkey()
    create_table_writekey()
    create_table_adc()
    app.run(host="0.0.0.0", debug=True)