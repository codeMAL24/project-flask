from flask import Flask, jsonify , request

app = Flask(__name__)

data = [
    {
        'Contact' : u"9923455545",
        'name' : u"Van'dyll",
        'done' : False,
        'id' : 1

    },
    {
        'Contact' : u"9829344400",
        'name' : u"Rick",
        'done' : False,
        'id' : 1
    },
]
@app.route("/")
def name():
    return "This is the homepage use /contact to move to the contact list"

@app.route("/contact",methods = ["POST"] )   
def contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'id': data[-1]['id'] + 1,
        'name': request.json['name'],
        'Contact': request.json.get('Contact',""), 
        'done': False
     }        
    data.append(task)
    return jsonify({
        "status":"success",
        "message": "task added succesfully!"
     })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":data
    })
    
if (__name__ == "__main__"):
    app.run(debug=True)


    