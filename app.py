from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        # Get the math expression from the hidden input or text box
        expression = request.form.get("expression", "")
        try:
            # Safely evaluate the math string
            if expression:
                result = eval(expression)
        except Exception:
            result = "Error"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
    