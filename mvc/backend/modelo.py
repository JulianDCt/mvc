import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       
        database="mvc"
    )

def get_all_tareas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tareas")
    result = cursor.fetchall()
    conn.close()
    return result

def create_tarea(titulo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tareas (titulo) VALUES (%s)", (titulo,))
    conn.commit()
    conn.close()

def delete_tarea(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tareas WHERE id = %s", (id,))
    conn.commit()
    conn.close()

def toggle_tarea(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tareas SET completada = NOT completada WHERE id = %s", (id,))
    conn.commit()
    conn.close()