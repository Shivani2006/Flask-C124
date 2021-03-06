from flask import Flask, jsonify, request

data = [
   {
    "Contact":"9884170728",
    "Name": "Vasuki",
    "Id": 1,
    "Done": 'false'
   },{
    "Contact":"9884070728",
    "Name": "Anand",
    "Id": 2,
    "Done":'false'
   }
]


app = Flask(__name__)

@app.route("/add_data",methods = ["POST"])
def addingTask():
    if not request.json:
        return jsonify({"status":"error","message":"pls provide the data"},400)
    Contact = {
      "id":data[-1]["Id"]+1,
      "Name":request.json["Name"],
      "Contact": request.json.get('Contact',""),
      "Done": False
    }
    data.append(Contact)
    return jsonify({"status":"success","message":"contact added"})

if __name__ == "__main__":
    app.run()


