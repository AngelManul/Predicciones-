import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configura los detalles de conexión a tu base de datos
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

def fetch_all_students():
    query = "SELECT * FROM estudiantes"
    return execute_query(query)

def add_student(data):
    query = """
    INSERT INTO estudiantes (
        Nombre, Matricula, Turno, Plantel, Edad, Genero, Promedio_General, Porcentaje_de_asistencia, 
        Numero_de_materias_reprobadas, Horas_de_estudio_semanal, Cuatrimestres_cursados, Tiene_beca, 
        Participa_en_actividades_extra, Nivel_de_estres, Satisfaccion_con_la_carrera, Tiempo_para_llegar, Es_puntual, Area_de_mejora
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    execute_query(query, data)

def update_student(data):
    query = """
    UPDATE estudiantes SET 
        Nombre=%s, Turno=%s, Plantel=%s, Edad=%s, Genero=%s, Promedio_General=%s, Porcentaje_de_asistencia=%s, 
        Numero_de_materias_reprobadas=%s, Horas_de_estudio_semanal=%s, Cuatrimestres_cursados=%s, Tiene_beca=%s, 
        Participa_en_actividades_extra=%s, Nivel_de_estres=%s, Satisfaccion_con_la_carrera=%s, Tiempo_para_llegar=%s, 
        Es_puntual=%s, Area_de_mejora=%s WHERE Matricula=%s
    """
    execute_query(query, data)

def update_table():
    for row in table.get_children():
        table.delete(row)
    for student in fetch_all_students():
        table.insert('', 'end', values=student)

def predict_improvement_area(promedio_general, porcentaje_de_asistencia, numero_de_materias_reprobadas, horas_de_estudio_semanal):
    if promedio_general < 7.0:
        return "Mejorar el promedio"
    elif porcentaje_de_asistencia < 85.0:
        return "Mejorar la asistencia"
    elif numero_de_materias_reprobadas > 2:
        return "Reducir materias reprobadas"
    elif horas_de_estudio_semanal < 5:
        return "Incrementar horas de estudio"
    else:
        return "Mantener rendimiento"

def add_student_ui():
    def submit():
        data = (
            name_entry.get(), matricula_entry.get(), turno_entry.get(), plantel_entry.get(), int(edad_entry.get()), 
            genero_entry.get(), float(promedio_entry.get()), float(asistencia_entry.get()), int(reprobadas_entry.get()), 
            int(estudio_entry.get()), int(cuatrimestres_entry.get()), beca_entry.get(), actividades_entry.get(), 
            estres_entry.get(), satisfaccion_entry.get(), int(tiempo_entry.get()), puntual_entry.get()
        )
        area_de_mejora = predict_improvement_area(data[6], data[7], data[8], data[9])
        data = data + (area_de_mejora,)
        add_student(data)
        update_table()
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Agregar Alumno")

    fields = [
        "Nombre", "Matricula", "Turno", "Plantel", "Edad", "Genero", "Promedio General", 
        "Porcentaje de Asistencia", "Numero de Materias Reprobadas", "Horas de Estudio Semanal", 
        "Cuatrimestres Cursados", "Tiene Beca", "Participa en Actividades Extra", "Nivel de Estrés", 
        "Satisfacción con la Carrera", "Tiempo para Llegar", "Es Puntual"
    ]

    entries = []
    for field in fields:
        label = tk.Label(add_window, text=field)
        label.pack()
        entry = tk.Entry(add_window)
        entry.pack()
        entries.append(entry)

    name_entry, matricula_entry, turno_entry, plantel_entry, edad_entry, genero_entry, promedio_entry, asistencia_entry, reprobadas_entry, estudio_entry, cuatrimestres_entry, beca_entry, actividades_entry, estres_entry, satisfaccion_entry, tiempo_entry, puntual_entry = entries

    submit_button = tk.Button(add_window, text="Agregar", command=submit)
    submit_button.pack()

def update_student_ui():
    selected_item = table.selection()
    if not selected_item:
        messagebox.showerror("Error", "Selecciona un alumno para actualizar")
        return

    selected_student = table.item(selected_item)['values']

    def submit():
        data = (
            name_entry.get(), turno_entry.get(), plantel_entry.get(), int(edad_entry.get()), 
            genero_entry.get(), float(promedio_entry.get()), float(asistencia_entry.get()), int(reprobadas_entry.get()), 
            int(estudio_entry.get()), int(cuatrimestres_entry.get()), beca_entry.get(), actividades_entry.get(), 
            estres_entry.get(), satisfaccion_entry.get(), int(tiempo_entry.get()), puntual_entry.get(), selected_student[1]
        )
        area_de_mejora = predict_improvement_area(data[5], data[6], data[7], data[8])
        data = data + (area_de_mejora,)
        update_student(data)
        update_table()
        update_window.destroy()

    update_window = tk.Toplevel(root)
    update_window.title("Actualizar Alumno")

    fields = [
        "Nombre", "Matricula", "Turno", "Plantel", "Edad", "Genero", "Promedio General", 
        "Porcentaje de Asistencia", "Numero de Materias Reprobadas", "Horas de Estudio Semanal", 
        "Cuatrimestres Cursados", "Tiene Beca", "Participa en Actividades Extra", "Nivel de Estrés", 
        "Satisfacción con la Carrera", "Tiempo para Llegar", "Es Puntual"
    ]

    entries = []
    for i, field in enumerate(fields):
        label = tk.Label(update_window, text=field)
        label.pack()
        entry = tk.Entry(update_window)
        entry.pack()
        entry.insert(0, selected_student[i])
        entries.append(entry)

    name_entry, matricula_entry, turno_entry, plantel_entry, edad_entry, genero_entry, promedio_entry, asistencia_entry, reprobadas_entry, estudio_entry, cuatrimestres_entry, beca_entry, actividades_entry, estres_entry, satisfaccion_entry, tiempo_entry, puntual_entry = entries

    submit_button = tk.Button(update_window, text="Actualizar", command=submit)
    submit_button.pack()

def show_graph():
    data = fetch_all_students()
    edades = [row[4] for row in data]
    promedios = [row[6] for row in data]
    asistencia = [row[7] for row in data]

    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.scatter(edades, promedios, label='Promedio General')
    ax.scatter(edades, asistencia, label='Asistencia')
    ax.set_xlabel('Edad')
    ax.set_ylabel('Promedio / Asistencia')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("Sistema de Gestión de Estudiantes")

columns = (
    "Nombre", "Matricula", "Turno", "Plantel", "Edad", "Genero", "Promedio General", 
    "Porcentaje de Asistencia", "Numero de Materias Reprobadas", "Horas de Estudio Semanal", 
    "Cuatrimestres Cursados", "Tiene Beca", "Participa en Actividades Extra", "Nivel de Estrés", 
    "Satisfacción con la Carrera", "Tiempo para Llegar", "Es Puntual", "Área de Mejora"
)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

# Agregar Scrollbar horizontal
table_canvas = tk.Canvas(table_frame)
table_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

x_scrollbar = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=table_canvas.xview)
x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

table_canvas.configure(xscrollcommand=x_scrollbar.set)

table = ttk.Treeview(table_canvas, columns=columns, show='headings')
table_canvas.create_window((0, 0), window=table, anchor='nw')

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=120)

# Actualizar la región de scroll
def update_scrollregion(event):
    table_canvas.configure(scrollregion=table_canvas.bbox('all'))

table.bind('<Configure>', update_scrollregion)

update_table()

button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text="Agregar Alumno", command=add_student_ui)
add_button.pack(side=tk.LEFT)

update_button = tk.Button(button_frame, text="Actualizar Alumno", command=update_student_ui)
update_button.pack(side=tk.LEFT)

graph_button = tk.Button(button_frame, text="Mostrar Gráfica", command=show_graph)
graph_button.pack(side=tk.LEFT)

root.mainloop()
