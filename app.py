from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index ():

    if request.method == "POST":

        req = request.form

        number = req["number"]

        print(number)

        i = 1
        try:
            while True:
                b = int(number) + i
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



# a = int(input("tyoe a number: "))
