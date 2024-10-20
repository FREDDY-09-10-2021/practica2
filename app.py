from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # La página principal con el menú

@app.route("/inscripcion_curso", methods=["GET", "POST"])
def inscripcion_curso():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")
        curso = request.form.get("curso")
        return render_template("salida_inscripcion_curso.html", nombre=nombre, apellidos=apellidos, curso=curso)
    return render_template("formulario1_curso.html")  # Muestra el formulario si la solicitud es GET

@app.route("/registro_usuarios", methods=["GET", "POST"])
def registro_usuarios():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")
        correo_electronico = request.form.get("correo")
        contraseña = request.form.get("contraseña")
        return render_template("salida_usuario.html", nombre=nombre, apellidos=apellidos, correo_electronico=correo_electronico, contraseña=contraseña)
    return render_template("formulario2_registro_usuario.html")  # Muestra el formulario si la solicitud es GET

@app.route("/registro_productos", methods=["GET", "POST"])
def registro_productos():
    if request.method == "POST":
        producto = request.form.get("producto")
        categoria = request.form.get("categoria")
        existencia = request.form.get("existencia")
        precio = request.form.get("precio")
        return render_template("salida_producto.html", producto=producto, categoria=categoria, existencia=existencia,precio=precio)
    return render_template("formulario3_registro_producto.html")  # Muestra el formulario si la solicitud es GET

@app.route("/registro_libros", methods=["GET", "POST"])
def registro_libros():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        autor = request.form.get("autor")
        resumen = request.form.get("resumen")
        medio = request.form.get("medio")
        return render_template("salida_libros.html", titulo=titulo, autor=autor, resumen=resumen, medio=medio)
    return render_template("formulario4_registro_libros.html")  # Muestra el formulario si la solicitud es GET

if __name__ == "__main__":
    app.run(debug=True)
