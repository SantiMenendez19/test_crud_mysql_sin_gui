# MySQL
import pymysql
import os

# Parametros para ingresar a la BBDD en MySQL
DB_HOST = "localhost"  # Nombre del host
DB_USER = "root"  # Nombre del usuario puesto en MySQL server
DB_PASS = "1234"  # Password de la conexion
DB_NAME = "PRUEBAS"  # Schema o database , no olvidar esto!!!

# Funcion de conexion a BBDD y consultas


def conexionBBDD(consulta=""):
    try:
        miConexion = pymysql.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
        miCursor = miConexion.cursor()
        try:
            miCursor.execute(consulta)
        except:
            print("Error en la consulta")
        if consulta.upper().startswith("SELECT"):
            filas = miCursor.fetchall()
            for i in filas:
                print(i)
        if consulta.upper().startswith("SHOW"):
            filas = miCursor.fetchall()
            for i in filas:
                print(i)
        else:
            miConexion.commit()
        miCursor.close()
        miConexion.close()
    except:
        print("Error al conectarse a la DDBB")


def crearDatabase():
    # Crear la base de datos
    try:
        crearbase = """CREATE DATABASE IF NOT EXISTS PRUEBAS"""
        miConexion = pymysql.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASS)
        miCursor = miConexion.cursor()
        miCursor.execute(crearbase)
        miConexion.commit()
        miCursor.close()
        miConexion.close()
        print("DDBB creada con exito")
    except:
        print("Error con la DDBB MySQL")


def crearTabla():
    # Crear tabla
    try:
        creartabla = """CREATE TABLE IF NOT EXISTS PERSONAS(DNI INT(8) PRIMARY KEY,NOMBRE VARCHAR(20),APELLIDO VARCHAR(20),SUELDO FLOAT)"""
        conexionBBDD(creartabla)
        print("Tabla creada con exito")
    except:
        print("Error al crear la tabla")


def insertarRegistro():
    # Insertar registros a la tabla
    try:

        nom = input("Ingrese nombre: ")
        ape = input("Ingrese apellido: ")
        dni = input("Ingrese DNI: ")
        sueldo = input("Ingrese sueldo: ")
        insertardato = "INSERT INTO PERSONAS VALUES('" + dni + \
            "','" + nom + "','" + ape + "','" + sueldo + "');"
        conexionBBDD(insertardato)
    except:
        print("Error en el ingreso de datos")


def mostrarTabla():
    # Mostrar tabla y obtencion de datos
    mostrartabla = "SELECT * FROM PERSONAS ORDER BY DNI;"
    conexionBBDD(mostrartabla)


def eliminarTabla():
    # Eliminar tabla
    try:
        borrartabla = "DROP TABLE IF EXISTS PERSONAS;"
        conexionBBDD(borrartabla)
        print("Tabla eliminada con exito")
    except pymysql.Error as error:
        print("Error al eliminar tabla " + error)


def mostrarRegistro():
    # Mostrar un solo registro
    try:
        dni = input("Ingrese DNI:")
        mostrar = "SELECT * FROM PERSONAS WHERE DNI='" + dni + "'"
        conexionBBDD(mostrar)
    except pymysql.Error as error:
        print("Error en la busqueda de datos " + error)


def actualizarRegistro():
    # Actualizar registro
    actualizardato = """UPDATE PERSONAS SET NOMBRE="Joaquin" WHERE NOMBRE="Santiago";"""
    conexionBBDD(actualizardato)


def eliminarDatabase():
    # Elimino la base de datos
    eliminarbase = """DROP DATABASE IF EXISTS PRUEBAS"""
    conexionBBDD(eliminarbase)


def mostrarDatabase():
    # Muestra base de datos
    mostrarbase = """SHOW DATABASES"""
    conexionBBDD(mostrarbase)


def vaciarTabla():
    # Vacia la tabla
    vaciartable = """TRUNCATE TABLE PERSONAS"""
    conexionBBDD(vaciartable)


switch = {
    1: crearDatabase,
    2: crearTabla,
    3: insertarRegistro,
    4: mostrarTabla,
    5: mostrarRegistro,
    6: mostrarDatabase,
    7: actualizarRegistro,
    8: vaciarTabla,
    9: eliminarTabla,
    10: eliminarDatabase
}


def ejecutarFuncion(op):
    funcion = switch.get(op)
    return funcion()


# Menu
while True:
    print("Elija una opcion:")
    print("1- Crear DDBB PRUEBAS")
    print("2- Crear Tabla PERSONAS")
    print("3- Insertar registros a la tabla")
    print("4- Mostrar tabla")
    print("5- Mostrar registro de la tabla por DNI")
    print("6- Mostrar bases de datos")
    print("7- Actualizar registro de la tabla")
    print("8- Vaciar tabla")
    print("9- Eliminar tabla")
    print("10- Eliminar DDBB PRUEBAS")
    print("0- Salir del programa")
    opcion = int(input("Ingrese el valor elegido: "))
    if(opcion > 0 and opcion <= 10):
        ejecutarFuncion(opcion)
    elif(opcion == 0):
        break
    else:
        print("Opcion erronea")
    input("Presiona una tecla para continuar")
    os.system('cls')
