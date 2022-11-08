from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/XD")
def XD():
    return render_template("XD.html")

@app.route("/SiAct")
def SiAct():
    return render_template("dedicacion.html")

# Tabla Area

@app.route("/area")
def area():
    conn = pymysql.connect(host="host="Fandite.mysql.pythonanywhere-services.com"", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from area")
    reg = cursor.fetchall()
    Num=len(reg)
    return render_template("area.html", areas=reg, NumA=Num)

@app.route("/area_agr")
def area_agr():
    return render_template("area_agr.html")

@app.route("/inser_area", methods=["POST"])
def inser_are():
    if request.method == "POST":
        area = request.form["area"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("select max(idArea) from area")
        Dat = cursor.fetchall()
        DatIDA = Dat[0]
        idA = DatIDA[0] + 1

        cursor.execute("insert into area(idArea, descrp) values (%s, %s)", (idA, area))
        conn.commit()
    return redirect(url_for('area'))

@app.route("/area_edi/<string:idArea>")
def area_edi(idArea):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from area where idArea = %s", (idArea))
    reg = cursor.fetchall()
    return render_template("area_edi.html", area = reg[0])

@app.route("/upt_area/<string:idArea>", methods=["POST"])
def upt_are(idArea):
    if request.method == "POST":
        area = request.form["area"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update area set descrp = %s where idArea=%s", (area, idArea))
        conn.commit()
    return redirect(url_for('area'))

@app.route("/area_bor/<string:idArea>")
def area_bor(idArea):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from area where idArea=%s", (idArea))
    conn.commit()
    return redirect(url_for('area'))

# Tabla Carrera

@app.route("/carrera")
def carrera():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from carrera")
    reg = cursor.fetchall()
    return render_template("carrera.html", carreras=reg)

@app.route("/carrera_agr")
def carrera_agr():
    return render_template("carrera_agr.html")

@app.route("/inser_carrera", methods=["POST"])
def inser_carrera():
    if request.method == "POST":
        carrera = request.form["carrera"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("insert into carrera(descrp) values (%s)", (carrera))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route("/carrera_edi/<string:idCarrera>")
def carrera_edi(idCarrera):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from carrera where idCarrera = %s", (idCarrera))
    reg = cursor.fetchall()
    return render_template("carrera_edi.html", carrera = reg[0])

@app.route("/upt_carrera/<string:idCarrera>", methods=["POST"])
def upt_Carrera(idCarrera):
    if request.method == "POST":
        carrera = request.form["carrera"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update carrera set descrp = %s where idCarrera=%s", (carrera, idCarrera))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route("/carrera_bor/<string:idCarrera>")
def carrera_bor(idCarrera):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from carrera where idCarrera=%s", (idCarrera))
    conn.commit()
    return redirect(url_for('carrera'))

# Tabla Escolaridad

@app.route("/escolaridad")
def escolaridad():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from escolaridad")
    reg = cursor.fetchall()
    return render_template("escolaridad.html", escos=reg)

@app.route("/escolaridad_agr")
def escolaridad_agr():
    return render_template("escolaridad_agr.html")

@app.route("/inser_esco", methods=["POST"])
def inser_escol():
    if request.method == "POST":
        escolaridad = request.form["esco"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("insert into escolaridad(descrp) values (%s)", (escolaridad))
        conn.commit()
    return redirect(url_for('escolaridad'))

@app.route("/escolaridad_edi/<string:idEscolaridad>")
def escolaridad_edi(idEscolaridad):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from escolaridad where idEscolaridad = %s", (idEscolaridad))
    reg = cursor.fetchall()
    return render_template("escolaridad_edi.html", escol = reg[0])

@app.route("/upt_esco/<string:idEscolaridad>", methods=["POST"])
def upt_escolaridad(idEscolaridad):
    if request.method == "POST":
        escolaridad = request.form["esco"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update escolaridad set descrp = %s where idEscolaridad=%s", (escolaridad, idEscolaridad))
        conn.commit()
    return redirect(url_for('escolaridad'))

@app.route("/escolaridad_bor/<string:idEscolaridad>")
def escolaridad_bor(idEscolaridad):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from escolaridad where idEscolaridad=%s", (idEscolaridad))
    conn.commit()
    return redirect(url_for('escolaridad'))

# Tabla Estado Civil

@app.route("/estadoci")
def estadoci():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from EstadoCiv")
    reg = cursor.fetchall()
    return render_template("estadoci.html", ests=reg)

@app.route("/estadoci_agr")
def estadoci_agr():
    return render_template("estadoci_agr.html")

@app.route("/inser_est", methods=["POST"])
def inser_est():
    if request.method == "POST":
        est = request.form["est"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("insert into EstadoCiv(descrp) values (%s)", (est))
        conn.commit()
    return redirect(url_for('estadoci'))

@app.route("/estadoci_edi/<string:idEstadoC>")
def estadoci_edi(idEstadoC):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from EstadoCiv where idEstadoCiv = %s", (idEstadoC))
    reg = cursor.fetchall()
    return render_template("estadoci_edi.html", est = reg[0])

@app.route("/upt_est/<string:idEstadoC>", methods=["POST"])
def upt_est(idEstadoC):
    if request.method == "POST":
        est = request.form["est"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update EstadoCiv set descrp = %s where idEstadoCiv=%s", (est, idEstadoC))
        conn.commit()
    return redirect(url_for('estadoci'))

@app.route("/estadoci_bor/<string:idEstadoC>")
def estadoci_bor(idEstadoC):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from EstadoCiv where idEstadoCiv=%s", (idEstadoC))
    conn.commit()
    return redirect(url_for('estadoci'))

# Tabla Grado de Avance

@app.route("/grado")
def grado():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from GradoAv")
    reg = cursor.fetchall()
    return render_template("grado.html", grados=reg)

@app.route("/grado_agr")
def grado_agr():
    return render_template("grado_agr.html")

@app.route("/inser_grado", methods=["POST"])
def inser_grado():
    if request.method == "POST":
        grado = request.form["grado"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("insert into GradoAv(descrp) values (%s)", (grado))
        conn.commit()
    return redirect(url_for('grado'))

@app.route("/grado_edi/<string:idGra>")
def grado_edi(idGra):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from GradoAv where idGradoAv = %s", (idGra))
    reg = cursor.fetchall()
    return render_template("grado_edi.html", grado = reg[0])

@app.route("/upt_grado/<string:idGra>", methods=["POST"])
def upt_grado(idGra):
    if request.method == "POST":
        grado = request.form["grado"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update GradoAv set descrp = %s where idGradoAv=%s", (grado, idGra))
        conn.commit()
    return redirect(url_for('grado'))

@app.route("/grado_bor/<string:idGra>")
def grado_bor(idGra):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from GradoAv where idGradoAv=%s", (idGra))
    conn.commit()
    return redirect(url_for('grado'))

# Tabla Habilidades

@app.route("/hab")
def hab():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from Habilidades")
    reg = cursor.fetchall()
    return render_template("habilidades.html", habs=reg)

@app.route("/hab_agr")
def hab_agr():
    return render_template("habilidades_agr.html")

@app.route("/inser_hab", methods=["POST"])
def inser_hab():
    if request.method == "POST":
        hab = request.form["hab"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("insert into Habilidades(descrp) values (%s)", (hab))
        conn.commit()
    return redirect(url_for('hab'))

@app.route("/hab_edi/<string:idHab>")
def hab_edi(idHab):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from Habilidades where idHabili = %s", (idHab))
    reg = cursor.fetchall()
    return render_template("habilidades_edi.html", hab = reg[0])

@app.route("/upt_hab/<string:idHab>", methods=["POST"])
def upt_hab(idHab):
    if request.method == "POST":
        hab = request.form["hab"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update Habilidades set descrp = %s where idHabili=%s", (hab, idHab))
        conn.commit()
    return redirect(url_for('hab'))

@app.route("/hab_bor/<string:idHab>")
def hab_bor(idHab):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from Habilidades where idHabili=%s", (idHab))
    conn.commit()
    return redirect(url_for('hab'))

# Tabla Idiomas

@app.route("/idioma")
def idioma():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from Idioma")
    reg = cursor.fetchall()
    return render_template("idioma.html", idiomas=reg)

@app.route("/idioma_agr")
def idioma_agr():
    return render_template("idioma_agr.html")

@app.route("/inser_idi", methods=["POST"])
def inser_idi():
    if request.method == "POST":
        idi = request.form["idi"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("insert into Idioma(descrp) values (%s)", (idi))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route("/idioma_edi/<string:idIdi>")
def idioma_edi(idIdi):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from Idioma where idIdioma = %s", (idIdi))
    reg = cursor.fetchall()
    return render_template("idioma_edi.html", idioma = reg[0])

@app.route("/upt_idi/<string:idIdi>", methods=["POST"])
def upt_idi(idIdi):
    if request.method == "POST":
        idi = request.form["idi"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update Idioma set descrp = %s where idIdioma=%s", (idi, idIdi))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route("/idioma_bor/<string:idIdi>")
def idioma_bor(idIdi):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from Idioma where idIdioma=%s", (idIdi))
    conn.commit()
    return redirect(url_for('idioma'))

# Tabla Medio de Publicidad

@app.route("/med")
def med():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from MedioPub")
    reg = cursor.fetchall()
    return render_template("mediopub.html", medios=reg)

@app.route("/med_agr")
def med_agr():
    return render_template("mediopub_agr.html")

@app.route("/inser_med", methods=["POST"])
def inser_med():
    if request.method == "POST":
        med = request.form["medio"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("insert into MedioPub(descrp) values (%s)", (med))
        conn.commit()
    return redirect(url_for('med'))

@app.route("/med_edi/<string:idMed>")
def med_edi(idMed):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from MedioPub where idMedioPub = %s", (idMed))
    reg = cursor.fetchall()
    return render_template("mediopub_edi.html", medio = reg[0])

@app.route("/upt_med/<string:idMed>", methods=["POST"])
def upt_med(idMed):
    if request.method == "POST":
        med = request.form["medio"]
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update MedioPub set descrp = %s where idMedioPub=%s", (med, idMed))
        conn.commit()
    return redirect(url_for('med'))

@app.route("/med_bor/<string:idMed>")
def med_bor(idMed):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from MedioPub where idMedioPub=%s", (idMed))
    conn.commit()
    return redirect(url_for('med'))

@app.route("/puesto")
def puesto():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select idPuesto, nomPuesto from puesto")
    datos = cursor.fetchall()
    return render_template("puesto.html", pue=datos, D = ' ', A = ' ', C = ' ', E = ' ', EC = ' ', G = ' ')

@app.route("/puesto_agr")
def puesto_agr():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select * from area")
    datosA = cursor.fetchall()
    cursor.execute("select * from carrera")
    datosC = cursor.fetchall()
    cursor.execute("select * from escolaridad")
    datosE = cursor.fetchall()
    cursor.execute("select * from EstadoCiv")
    datosEC = cursor.fetchall()
    cursor.execute("select * from GradoAv")
    datosG = cursor.fetchall()
    cursor.execute("select * from Habilidades")
    datosH = cursor.fetchall()
    cursor.execute("select * from Idioma")
    datosI = cursor.fetchall()
    return render_template("puesto_agr.html", area = datosA, carrera=datosC, esco=datosE, ec=datosEC, grado=datosG, hab=datosH, idioma=datosI)

@app.route("/puesto_agregar", methods=["POST"])
def puesto_agregar():
    if request.method=="POST":
        Nom = request.form["NomPuesto"]
        Cod = request.form["CodPuesto"]
        Jefe = request.form["JefeSup"]
        Jornada = request.form["Jornada"]
        Remu = request.form["Remu"]
        Presta = request.form["Presta"]
        Desc = request.form["DescGral"]
        Func = request.form["Funciones"]
        Edad = request.form["Edad"]
        Exp = request.form["Exp"]
        Conoc = request.form["Conocimiento"]
        ManE = request.form["ManEquip"]
        ReqF = request.form["ReqFis"]
        ReqP = request.form["ReqPsi"]
        Resp = request.form["Resp"]
        ConTr = request.form["ConTr"]

        if 'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'

        if 'idEc' in request.form:
            idEC = request.form['idEC']
        else:
            idEC = '1'
        
        if 'idEsco' in request.form:
            idEsco = request.form['idEsco']
        else:
            idEsco = '1'
        
        if 'idGrA' in request.form:
            idGrA = request.form['idGrA']
        else:
            idGrA = '1'
        
        if 'idCar' in request.form:
            idCar = request.form['idCar']
        else:
            idCar = '1'

        if 'Sexo' in request.form:
            Sex = request.form['Sexo']
        else:
            Sex = '1'

        
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("insert into puesto(codPuesto, idArea, nomPuesto, puestoJefeSup," 
        "jornada, remunMensual, prestaciones, descripcionGeneral, funciones, edad, sexo, "
        "idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, experiencia, conocimientos, "
        "manejoEquipo, reqFisicos, reqPsicologicos, responsabilidades, condicionesTrabajo)"
        " values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
        "%s, %s, %s)", (Cod, idAr, Nom, Jefe, Jornada, Remu, Presta, Desc, Func, Edad, Sex, idEC, 
        idEsco, idGrA, idCar, Exp, Conoc, ManE, ReqF, ReqP, Resp, ConTr))
        conn.commit()

        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) from puesto)')
        dato=cursor.fetchall()
        idpue = dato[0]
        idP = idpue[0]
        cursor.execute('select count(*) from idioma ')
        dato = cursor.fetchall()
        nidio = dato[0]
        ni = nidio[0] + 1

        for i in range(1, ni):
            idio = 'idi' + str(i)
            if idio in request.form:
                conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
                cursor = conn.cursor()
                cursor.execute("insert into puesto_has_idiomas(idPuesto, idIdioma) values (%s, %s)", (idP, i))
                conn.commit()

        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute('select idPuesto, nomPuesto from puesto where idPuesto=(select max(idPuesto) from puesto)')
        dato=cursor.fetchall()
        idpue = dato[0]
        idP = idpue[0]
        cursor.execute('select count(*) from habilidades ')
        dato = cursor.fetchall()
        habilis = dato[0]
        habs = habilis[0] + 1

        for i in range(1, habs):
            hab = 'h' + str(i)
            if hab in request.form:
                conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
                cursor = conn.cursor()
                cursor.execute("insert into puesto_has_habilidades(idPuesto, idHabili) values (%s, %s)", (idP, i))
                conn.commit()
        
        print(idP)
        print(habs)

    return redirect(url_for('puesto'))

@app.route("/puesto_edi/<string:id>")
def puesto_edi(id):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute('select * from puesto where idPuesto= %s', (id))
    datos=cursor.fetchall()

    cursor.execute("select a.idArea, a.descrp from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s", (id))
    area = cursor.fetchall()

    cursor.execute("select a.idCarrera, a.descrp from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s", (id))
    carrera = cursor.fetchall()

    cursor.execute("select a.idEstadoCiv, a.descrp from estadociv a, puesto b where a.idEstadoCiv = b.idEstadoCivil and b.idPuesto = %s", (id))
    estc = cursor.fetchall()

    cursor.execute("select a.idEscolaridad, a.descrp from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s", (id))
    escolaridad = cursor.fetchall()

    cursor.execute("select a.idGradoAv, a.descrp from gradoav a, puesto b where a.idGradoAv = b.idGradoAvance and b.idPuesto = %s", (id))
    grado = cursor.fetchall()

    cursor.execute("select a.idIdioma, a.descrp from idioma a, puesto_has_idiomas b where a.idIdioma = b.idIdioma and b.idPuesto = %s", (id))
    idioma = cursor.fetchall()

    cursor.execute("select a.idHabili, a.descrp from habilidades a, puesto_has_habilidades b where a.idHabili = b.idHabili and b.idPuesto = %s", (id))
    habs = cursor.fetchall()
    
    cursor.execute("select * from area")
    datosA = cursor.fetchall()
    cursor.execute("select * from carrera")
    datosC = cursor.fetchall()
    cursor.execute("select * from escolaridad")
    datosE = cursor.fetchall()
    cursor.execute("select * from EstadoCiv")
    datosEC = cursor.fetchall()
    cursor.execute("select * from GradoAv")
    datosG = cursor.fetchall()
    cursor.execute("select * from Habilidades")
    datosH = cursor.fetchall()
    cursor.execute("select * from Idioma")
    datosI = cursor.fetchall()

    print(datos)
    return render_template("puesto_edi.html", A = area[0], C = carrera[0], E = escolaridad[0], EC = estc[0], G = grado[0], D = datos[0], I = idioma, H = habs, area = datosA, carrera=datosC, esco=datosE, ec=datosEC, grado=datosG, hab=datosH, idioma=datosI)

@app.route("/puesto_editarac/<string:id>", methods=["POST"])
def puesto_editarac(id):
    if request.method=="POST":
        Nom = request.form["NomPuesto"]
        Cod = request.form["CodPuesto"]
        Jefe = request.form["JefeSup"]
        Jornada = request.form["Jornada"]
        Remu = request.form["Remu"]
        Presta = request.form["Presta"]
        Desc = request.form["DescGral"]
        Func = request.form["Funciones"]
        Edad = request.form["Edad"]
        Exp = request.form["Exp"]
        Conoc = request.form["Conocimiento"]
        ManE = request.form["ManEquip"]
        ReqF = request.form["ReqFis"]
        ReqP = request.form["ReqPsi"]
        Resp = request.form["Resp"]
        ConTr = request.form["ConTr"]

        if 'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'

        if 'idEc' in request.form:
            idEC = request.form['idEC']
        else:
            idEC = '1'
        
        if 'idEsco' in request.form:
            idEsco = request.form['idEsco']
        else:
            idEsco = '1'
        
        if 'idGrA' in request.form:
            idGrA = request.form['idGrA']
        else:
            idGrA = '1'
        
        if 'idCar' in request.form:
            idCar = request.form['idCar']
        else:
            idCar = '1'

        if 'Sexo' in request.form:
            Sex = request.form['Sexo']
        else:
            Sex = '1'

        
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update puesto set codPuesto=%s, idArea=%s, nomPuesto=%s, puestoJefeSup=%s," 
        "jornada=%s, remunMensual=%s, prestaciones=%s, descripcionGeneral=%s, funciones=%s, edad=%s,"
        "sexo=%s, idEstadoCivil=%s, idEscolaridad=%s, idGradoAvance=%s, idCarrera=%s, experiencia=%s,"
        "conocimientos=%s, manejoEquipo=%s, reqFisicos=%s, reqPsicologicos=%s, responsabilidades=%s,"
        "condicionesTrabajo=%s where idPuesto = %s",(Cod, idAr, Nom, Jefe, Jornada, Remu, Presta, Desc,
        Func, Edad, Sex, idEC, idEsco, idGrA, idCar, Exp, Conoc, ManE, ReqF, ReqP, Resp, ConTr, id))
        conn.commit()

        cursor.execute('select count(*) from idioma ')
        dato = cursor.fetchall()
        nidio = dato[0]
        ni = nidio[0] + 1
        cursor.execute("select a.idIdioma, a.descrp from idioma a, puesto_has_idiomas b where a.idIdioma = b.idIdioma and b.idPuesto = %s", (id))
        idioma = cursor.fetchall()

        for i in range(1, ni):
            idio = 'idi' + str(i)
            if idio in request.form:
                B = False
                for c in idioma:
                    if i == c[0]:
                        B = True
                if B == False:
                    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
                    cursor = conn.cursor()
                    cursor.execute("insert into puesto_has_idiomas(idPuesto, idIdioma) values (%s, %s)", (id, i))
                    conn.commit()
            else:
                conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
                cursor = conn.cursor()
                cursor.execute("delete from puesto_has_idiomas where idPuesto = %s and idIdioma = %s", (id, i))
                conn.commit()

        cursor.execute('select count(*) from habilidades ')
        dato = cursor.fetchall()
        habilis = dato[0]
        habs = habilis[0] + 1
        cursor.execute("select a.idHabili, a.descrp from habilidades a, puesto_has_habilidades b where a.idHabili = b.idHabili and b.idPuesto = %s", (id))
        habilidades = cursor.fetchall()

        for i in range(1, habs):
            hab = 'h' + str(i)
            if hab in request.form:
                B = False
                for c in habilidades:
                    if i == c[0]:
                        B = True
                if B == False:
                    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
                    cursor = conn.cursor()
                    cursor.execute("insert into puesto_has_habilidades(idPuesto, idHabili) values (%s, %s)", (id, i))
                    conn.commit()
            else:
                conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
                cursor = conn.cursor()
                cursor.execute("delete from puesto_has_habilidades where idPuesto = %s and idHabili = %s", (id, i))
                conn.commit()

        return redirect(url_for('puesto'))

@app.route("/puesto_det/<string:id>", methods=['GET'])
def puesto_det(id):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute('select * from puesto where idPuesto= %s', (id))
    datos=cursor.fetchall()

    cursor.execute("select a.idArea, a.descrp from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s", (id))
    area = cursor.fetchall()

    cursor.execute("select a.idCarrera, a.descrp from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s", (id))
    carrera = cursor.fetchall()

    cursor.execute("select a.idEstadoCiv, a.descrp from estadociv a, puesto b where a.idEstadoCiv = b.idEstadoCivil and b.idPuesto = %s", (id))
    estc = cursor.fetchall()

    cursor.execute("select a.idEscolaridad, a.descrp from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s", (id))
    escolaridad = cursor.fetchall()

    cursor.execute("select a.idGradoAv, a.descrp from gradoav a, puesto b where a.idGradoAv = b.idGradoAvance and b.idPuesto = %s", (id))
    grado = cursor.fetchall()

    cursor.execute("select a.idIdioma, a.descrp from idioma a, puesto_has_idiomas b where a.idIdioma = b.idIdioma and b.idPuesto = %s", (id))
    idioma = cursor.fetchall()

    cursor.execute("select a.idHabili, a.descrp from habilidades a, puesto_has_habilidades b where a.idHabili = b.idHabili and b.idPuesto = %s", (id))
    habs = cursor.fetchall()

    cursor.execute("select idPuesto, nomPuesto from puesto")
    dato = cursor.fetchall()

    return render_template("puesto.html",pue = dato, A = area[0], C = carrera[0], E = escolaridad[0], EC = estc[0], G = grado[0], I = idioma, H = habs, D = datos[0])

@app.route("/puesto_bor/<string:id>")
def puesto_bor(id):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()

    cursor.execute("delete from puesto_has_idiomas where idPuesto = %s", (id))
    conn.commit()

    cursor.execute("delete from puesto_has_habilidades where idPuesto = %s", (id))
    conn.commit()

    cursor.execute("delete from puesto where idPuesto = %s", (id))
    conn.commit()

    return redirect(url_for('puesto'))

#Nueva Requisicion

@app.route("/requisicion_agr")
def requisicion_agr():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select idArea, descrp from area")
    Area = cursor.fetchall()
    cursor.execute("select idPuesto, nomPuesto from puesto")
    Puesto = cursor.fetchall()
    return render_template("requisicion_agr.html", Ar = Area, Pue = Puesto)

@app.route("/requisicion_fagr", methods=["POST"])
def requisicion_fagr():
    if request.method == "POST":
        if "idArea" in request.form:
            Area = request.form["idArea"]
        else:
            Area = "1"
        if "idPuesto" in request.form:
            Puesto = request.form["idPuesto"]
        else:
            Puesto = "1"
        if "Tipo" in request.form:
            TipoV = request.form["Tipo"]
        else:
            TipoV = "1"
        Folio = request.form["Folio"]
        Soli = request.form["NomPueS"]
        Elab = request.form["FechaE"]
        Inicio = request.form["FechaIn"]
        Reclu = request.form["FechaRec"]
        Motivo = request.form["motReq"]
        MotivoEspe = request.form["motReqEsp"]
         
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()

        cursor.execute("insert into requisicion(Folio, idArea, FechaElab, idPuesto, NomSol, FechaRec, "
        "FechaIni, TipoVac, MotivoReq, MotivoEspe, Autorizar) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0)", 
        (Folio, Area, Elab, Puesto, Soli, Reclu, Inicio, TipoV, Motivo, MotivoEspe))
        conn.commit()
        return redirect(url_for('requisicion'))

# Requisiciones Pendientes por Autorizar

@app.route("/requisicion")
def requisicion():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select a.idReq, a.Autorizar, a.Folio, b.nomPuesto from requisicion a inner join Puesto b on a.idPuesto = b.idPuesto")
    dat = cursor.fetchall()

    return render_template("requisicion.html", datosR = dat, P = "", Ar="", R = "")


@app.route("/req_autori/<string:id>")
def req_autori(id):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select a.idReq, a.folio, b.nomPuesto from requisicion a inner join puesto b on a.idPuesto = b.idPuesto and idReq = %s", (id))
    datos = cursor.fetchall()
    return render_template("req_autorizar.html", D = datos[0])

@app.route("/req_autorizar/<string:id>", methods = ["POST"])
def req_autorizar(id):
    if request.method == "POST":
        Revisado = request.form['Revisado']
        Autorizado = request.form['Autorizado']
        conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
        cursor = conn.cursor()
        cursor.execute("update requisicion set NomRev=%s, NomAutoriza=%s, Autorizar=1 where idReq = %s", (Revisado, Autorizado, id))
        conn.commit()
    return redirect(url_for('req_autorizadas'))
        
@app.route("/req_det/<string:id>", methods=["GET"])
def req_det(id):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select Folio, FechaElab, NomSol, FechaRec, FechaIni, TipoVac, MotivoReq, MotivoEspe, Autorizar from requisicion where idReq = %s", (id))
    Req = cursor.fetchall()
    cursor.execute("select descrp from area a inner join requisicion b on a.idArea = b.idArea and b.idReq = %s", (id))
    Area = cursor.fetchall()
    cursor.execute("select b.nomPuesto, c.descrp, b.puestoJefeSup, b.jornada, b.remunMensual, b.descripcionGeneral, b.funciones, d.descrp, b.edad, b.sexo, b.edad, e.descrp from requisicion a inner join puesto b inner join area c inner join escolaridad d inner join estadociv e on a.idPuesto = b.idPuesto and c.idArea = b.idArea and d.idEscolaridad = b.idEscolaridad and e.idEstadoCiv = b.idEstadoCivil and a.idReq = %s;", (id))
    Puesto = cursor.fetchall()
    cursor.execute("select a.idReq, a.Autorizar, a.Folio, b.nomPuesto from requisicion a inner join Puesto b on a.idPuesto = b.idPuesto")
    dat = cursor.fetchall()
    print(dat)
    print(Puesto)
    print(Area)
    print(Req)
    return render_template("requisicion.html", datosR = dat, P = Puesto[0], Ar = Area[0], R = Req[0])

@app.route("/req_bor/<string:id>")
def req_bor(id):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("delete from requisicion where idReq = %s", (id))
    return redirect(url_for("requisicion"))

#Requisiciones Autorizadas

@app.route("/req_autorizadas")
def req_autorizadas():
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select a.idReq, a.Autorizar, a.Folio, b.nomPuesto from requisicion a inner join Puesto b on a.idPuesto = b.idPuesto")
    datos = cursor.fetchall()
    return render_template("req_autorizadas.html", dat = datos, Re = "", Pu = "", Are = "")

@app.route("/autori_det/<string:id>")
def autori_det(id):
    conn = pymysql.connect(host="Fandite.mysql.pythonanywhere-services.com", user="Fandite", passwd="Fandatos18", db="Fandite$default")
    cursor = conn.cursor()
    cursor.execute("select a.idReq, a.Autorizar, a.Folio, b.nomPuesto from requisicion a inner join Puesto b on a.idPuesto = b.idPuesto")
    datos = cursor.fetchall()
    cursor.execute("select Folio, FechaElab, NomSol, FechaRec, FechaIni, TipoVac, MotivoReq, MotivoEspe, Autorizar, NomRev, NomAutoriza from requisicion where idReq = %s", (id))
    Req = cursor.fetchall()
    cursor.execute("select descrp from area a inner join requisicion b on a.idArea = b.idArea and b.idReq = %s", (id))
    Area = cursor.fetchall()
    cursor.execute("select b.nomPuesto, c.descrp, b.puestoJefeSup, b.jornada, b.remunMensual, b.descripcionGeneral, b.funciones, d.descrp, b.edad, b.sexo, b.edad, e.descrp from requisicion a inner join puesto b inner join area c inner join escolaridad d inner join estadociv e on a.idPuesto = b.idPuesto and c.idArea = b.idArea and d.idEscolaridad = b.idEscolaridad and e.idEstadoCiv = b.idEstadoCivil and a.idReq = %s;", (id))
    Puesto = cursor.fetchall()
    return render_template("req_autorizadas.html", dat = datos, Re = Req[0], Are = Area[0], Pu = Puesto[0])

if __name__ == "__main__":
    app.run(debug=True)