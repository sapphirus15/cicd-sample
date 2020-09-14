from flask import Flask, request, jsonify
import datetime 

app = Flask (__name__)
 
@app.route('/')
def index():
    return 'This is Toy Project!'
 

@app.route('/api/time', methods=['GET', "POST"])                                                                                                    
def get_time():                                                                                                                              
    get_data = request.get_json()
    print(get_data)

    now = datetime.datetime.now()
    cur_time = now.strftime('%Y-%m-%d %H:%M:%S')
    data = {
        "SValue" : cur_time
    }
    return jsonify(data)



if __name__ == "__main__":
    app.run()