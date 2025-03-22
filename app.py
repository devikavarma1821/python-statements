from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Load the frontend

@app.route('/compare', methods=['POST'])
def compare_statements():
    stmt1 = request.form.get("stmt1", "").strip()  # Get input from form
    stmt2 = request.form.get("stmt2", "").strip()

    if stmt1 == stmt2:
        result = "Both statements are the same."
    else:
        words1 = stmt1.split()
        words2 = stmt2.split()
        diff1 = [word for word in words1 if word not in words2]
        diff2 = [word for word in words2 if word not in words1]

        result = f"Statements are different.<br><b>Words in first but not in second:</b> {', '.join(diff1)}<br><b>Words in second but not in first:</b> {', '.join(diff2)}"

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
