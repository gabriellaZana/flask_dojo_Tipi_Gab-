from flask import Flask, render_template, redirect, request, session, url_for
import csv

app = Flask(__name__)
counts = 0


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/request-counter", methods=["POST", "GET"])
def request_counter():
    global counts
    with open("counts.csv", "r") as csvfile:
        for item in csvfile: 
            counts += 1
    counts += 1
    with open("counts.csv", "w") as csvfile: 
        counts_lines = csv.writer(csvfile, delimiter=";")
        for i in range(counts):
            counts_lines.writerow("1")
    counts = 0

    counts_dict = dict()
    
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = "whoeventriestoguessthis"
    app.run(
        debug=True,
        port=5000
    )