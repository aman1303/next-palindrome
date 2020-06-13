from flask import Flask, render_template, request, redirect, flash
import math

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index ():

    if request.method == "POST":

        req = request.form

        number = req["number"]


        i = 1
        try:
            num_float = float(number)
            num = math.floor(num_float)
            while True:
                b = num + i
                i += 1
                b = str(b)
                if b == b[::-1]:
                    print(b)
                    break
        except ValueError:
            return render_template("wrong.html")



        return render_template("/answer.html", number=number, b = b)

    return render_template("index.html")


if __name__ == ("__main__"):
    app.run(debug=True)
