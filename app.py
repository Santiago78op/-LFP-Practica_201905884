from flask import Flask, request, Response
from flask import render_template
import pathlib
import imgkit
from imagen.analizar_Imagen import Analizarimagen

headings = ["Producto","Precio Unitario","Cantidad", "Total"]

app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return '<h1>Hola</h1>'

@app.route('/postLista',methods=['POST'])
def start():
    json = request.json
    producto = json['Producto']
    titulo = "Reporte_html"
    #filtro = json['Filtros]
    
    mayor = producto[0]
    menor = producto[-1]

    JsonImg = {
        
        'producto':producto,
        'mayor':mayor,
        'menor':menor
    }
    
    saveHtml(titulo,'reporte',render_template('index.html',**JsonImg))
    return Response()

def saveHtml(nombre,filtro,html):
    pathlib.Path(f'reportes/html/{nombre}').mkdir(parents=True,exist_ok=True)
    with open(f'reportes/html/{nombre}/{filtro}.html','w') as f:
        f.write(html)
        f.close()
 
    
