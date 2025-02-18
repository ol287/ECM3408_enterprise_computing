from flask import Flask, request

app = Flask(__name__)

@app.route("/factorial", methods=["POST"])
def endpoint():
    js = request.get_json()
    argument = js.get("argument")

    if argument is not None and isinstance(argument, int) and argument >= 0:
        result = calculate(argument)
        return {"result": result}, 200  # OK
    else:
        return "", 400  # Bad Request

def calculate(n):
    if n < 0:
        return None  # Handle negative input gracefully
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    app.run(host="localhost", port=3000)
