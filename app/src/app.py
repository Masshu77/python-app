from flask import *
app = Flask("app server")

@app.route('/',methods = ['GET'])
def root():
    return make_response(jsonify({'success':'success'}),200)
app.run(debug = True, host= "0.0.0.0", port = 80)