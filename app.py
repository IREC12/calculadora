
from flask import Flask, request, render_template_string
from calculadora import sumar, restar, multiplicar, dividir
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora</title>
    <style>
        body {
            font-family: Arial;
            background: #202938;
            color: white;
            display: flex;
            justify-content: center;
            padding-top: 70px;
        }
        .calculadora {
            background: #334155;
            padding: 30px;
            border-radius: 15px;
            width: 300px;
            text-align: center;
        }
        input, select, button {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            box-sizing: border-box;
            border-radius: 6px;
            border: none;
        }
        button {
            background: #38bdf8;
            cursor: pointer;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="calculadora">
        <h1>Calculadora</h1>
        <form method="POST">
            <input type="number" step="any" name="a"
                   placeholder="Primer número" required>
            <input type="number" step="any" name="b"
                   placeholder="Segundo número" required>

            <select name="operacion">
                <option value="sumar">Sumar</option>
                <option value="restar">Restar</option>
                <option value="multiplicar">Multiplicar</option>
                <option value="dividir">Dividir</option>
            </select>

            <button type="submit">Calcular</button>
        </form>

        {% if resultado is not none %}
            <h2>Resultado: {{ resultado }}</h2>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        operacion = request.form["operacion"]

        if operacion == "sumar":
            resultado = sumar(a, b)
        elif operacion == "restar":
            resultado = restar(a, b)
        elif operacion == "multiplicar":
            resultado = multiplicar(a, b)
        elif operacion == "dividir":
            resultado = dividir(a, b)

    return render_template_string(HTML, resultado=resultado)
