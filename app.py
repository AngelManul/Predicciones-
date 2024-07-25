from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'alumnos'
}

def execute_query(query, data=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    result = cursor.fetchall() if cursor.description else None
    conn.commit()
    cursor.close()
    conn.close()
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students', methods=['GET'])
def fetch_all_students():
    query = "SELECT * FROM estudiantes"
    students = execute_query(query)
    return jsonify(students)

@app.route('/student', methods=['GET'])
def fetch_student_by_matricula():
    matricula = request.args.get('matricula')
    query = "SELECT * FROM estudiantes WHERE Matricula = %s"
    student = execute_query(query, (matricula,))
    return jsonify(student)

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.json
    query = """
    INSERT INTO estudiantes (
        Nombre, Matricula, Turno, Plantel, Edad, Genero, Promedio_General, Porcentaje_de_asistencia, 
        Numero_de_materias_reprobadas, Horas_de_estudio_semanal, Cuatrimestres_cursados, Tiene_beca, 
        Participa_en_actividades_extra, Nivel_de_estres, Satisfaccion_con_la_carrera, Tiempo_para_llegar, Es_puntual, Area_de_mejora
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    execute_query(query, (
        data['Nombre'], data['Matricula'], data['Turno'], data['Plantel'], data['Edad'], 
        data['Genero'], data['Promedio_General'], data['Porcentaje_de_asistencia'], data['Numero_de_materias_reprobadas'], 
        data['Horas_de_estudio_semanal'], data['Cuatrimestres_cursados'], data['Tiene_beca'], 
        data['Participa_en_actividades_extra'], data['Nivel_de_estres'], data['Satisfaccion_con_la_carrera'], 
        data['Tiempo_para_llegar'], data['Es_puntual'], data['Area_de_mejora']
    ))
    return jsonify({"status": "success"})

@app.route('/update_student', methods=['POST'])
def update_student():
    data = request.json
    query = """
    UPDATE estudiantes SET 
        Nombre=%s, Turno=%s, Plantel=%s, Edad=%s, Genero=%s, Promedio_General=%s, Porcentaje_de_asistencia=%s, 
        Numero_de_materias_reprobadas=%s, Horas_de_estudio_semanal=%s, Cuatrimestres_cursados=%s, Tiene_beca=%s, 
        Participa_en_actividades_extra=%s, Nivel_de_estres=%s, Satisfaccion_con_la_carrera=%s, Tiempo_para_llegar=%s, 
        Es_puntual=%s, Area_de_mejora=%s WHERE Matricula=%s
    """
    execute_query(query, (
        data['Nombre'], data['Turno'], data['Plantel'], data['Edad'], 
        data['Genero'], data['Promedio_General'], data['Porcentaje_de_asistencia'], data['Numero_de_materias_reprobadas'], 
        data['Horas_de_estudio_semanal'], data['Cuatrimestres_cursados'], data['Tiene_beca'], 
        data['Participa_en_actividades_extra'], data['Nivel_de_estres'], data['Satisfaccion_con_la_carrera'], 
        data['Tiempo_para_llegar'], data['Es_puntual'], data['Area_de_mejora'], data['Matricula']
    ))
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
