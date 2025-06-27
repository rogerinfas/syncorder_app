from flask import Flask, render_template

app = Flask(__name__)

# Simulación de menú (arrays en backend)
menu_comidas = [
    {"nombre": "Lomo Saltado", "precio": 25},
    {"nombre": "Ceviche", "precio": 20},
    {"nombre": "Aji de Gallina", "precio": 18}
]

menu_bebidas = [
    {"nombre": "Inca Kola", "precio": 5},
    {"nombre": "Agua Mineral", "precio": 3},
    {"nombre": "Chicha Morada", "precio": 4}
]

@app.route('/mozo')
def mozo():
    return render_template('mozo.html', menu_comidas=menu_comidas, menu_bebidas=menu_bebidas)

@app.route('/cocina')
def cocina():
    return render_template('cocina.html')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Abierto a cualquier host
    app.run(host='0.0.0.0', port=5000, debug=True)
