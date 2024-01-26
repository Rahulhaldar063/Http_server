from flask import Flask,request
import os 

app = Flask(__name__)

@app.get('/data')
def handler():
    n = int(request.args.get('n'))
    m = request.args.get('m')


    if(n < 0 or n > 30):
        return "The text file only exist from 1 to 30"
    
    fp = open(os.path.join("random_text_files", f"{n}.txt"), 'r')

    if(m == None):
        return fp.read()
    else:
        m = int(m)
    if(m < 0):
        return "can't have -ve line numbers"
    
    
    data = fp.readlines()
    if(len(data) <= m):
        return "m is greater than file length"
    
    return data[m]

app.run(host='0.0.0.0', debug=True, port=8080)