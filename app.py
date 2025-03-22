from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compare', methods=['POST'])
def compare_statements():
    if not request.is_json:  # Check if the request has JSON data
        return jsonify({"error": "Invalid request, expecting JSON"}), 400

    data = request.get_json()
    stmt1 = data.get("stmt1", "").strip()
    stmt2 = data.get("stmt2", "").strip()

    if stmt1 == stmt2:
        result = {"message": "Both statements are the same."}
    else:
        words1 = stmt1.split()
        words2 = stmt2.split()
        diff1 = [word for word in words1 if word not in words2]
        diff2 = [word for word in words2 if word not in words1]

        result = {
            "message": "Statements are different.",
            "words_in_first_but_not_in_second": diff1,
            "words_in_second_but_not_in_first": diff2
        }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
