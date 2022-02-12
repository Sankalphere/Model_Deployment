from flask import Flask , render_template , request
import Heart as hr
import pandas as pd


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/sub", methods = ["POST"])
def submit():
    if request.method == "POST":
        a = request.form["a"]
        b = request.form["b"]
        c = request.form["c"]
        d = request.form["d"]
        e = request.form["e"]
        f = request.form["f"]
        g = request.form["g"]
        h = request.form["h"]
        i = request.form["i"]
        j = request.form["j"]
        k = request.form["k"]
        l = request.form["l"]
        m = request.form["m"]
        data={
            "age"	  :[a],
            "sex"  :[b],	
            "cp"  :[c]	,
            "trestbps"  :[d],	
            "chol"  :[e],	
            "fbs"  :[f]	,
            "restecg"  :[g],	
            "thalach"  :[h],
            "exang" :[i] ,
            "oldpeak" :[j],
            "slope" :[k] ,
            "ca" : [l],
            "thal" : [m],

        }
        df=pd.DataFrame(data)
        num=hr.heart_pred(df)

    return render_template("sub.html", n = num,df = data)

if __name__ == "__main__":
    app.run(debug=True)    