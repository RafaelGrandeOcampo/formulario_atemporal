import streamlit as st
from data import barrios_por_distrito, distritos_por_poblacion
from bd import DatabaseHandler

tab1, tab2, tab3 = st.tabs(["Datos del Arrendador", "Datos del Arrendatario", "Características Piso"])
col1, col2, col3 = st.columns([6, 2, 2])

db = DatabaseHandler()
logo = "aTemporal_negativo_claim.png"
st.sidebar.image(logo, use_column_width=True)

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
gestor = st.sidebar.selectbox("Gestor del Piso", ["Rafael Grande"])
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
if st.sidebar.button("Generar Contrato"):
    st.write("El contrato ha sido generado.")


if st.sidebar.button("Generar Ficha Piso"):
    st.write("La ficha del piso ha sido generada.")

if st.sidebar.button("Generar Mandato"):
    st.write("La ficha del piso ha sido generada.")



with tab1:
    st.subheader("DATOS ARRENDADOR")
    tipo_arrendador = st.selectbox("¿Persona fisica o juridica?", ["", "Fisica", "Juridica"])
    if tipo_arrendador == "Fisica":
        nombre_arrendador = st.text_input("Nombre del Arrendador")
        dni_arrendador = st.text_input("DNI del Arrendador")

    if tipo_arrendador == "Juridica":
        empresa_arrendador = st.text_input("Empresa del Arrendador")
        cif_arrendador = st.text_input("DNI/CIF")
        administrador = st.text_input("Representante legal")
        dni_administrador = st.text_input("DNI")
    canal_arrendador = st.text_input("Canal de Captación")
    cuenta_bancaria_arrendador = st.text_input("Cuenta Bancaria del Arrendador")
    direccion_facturacion_arrendador = st.text_area("Dirección de Facturación")
    email_arrendador = st.text_input("Email del Arrendador")
    telefono_arrendador = st.text_input("Teléfono del Arrendador")
    administracion_arrendador = st.number_input("Administración del Arrendador (%)", min_value=0.0, max_value=6.5, value=6.5, step=0.1, format="%.1f")


with tab2:
    st.subheader(f"Datos de la Reserva")
    fecha_check_in = st.date_input("Fecha de entrada", value=None)
    fecha_check_ou = st.date_input("Fecha de salida", value=None)
    renta_mensual = st.number_input("Introduce un número con dos decimales", format="%.2f", step=0.1)
    direccion_arrendatario = st.text_input(f"Motivo de la instancia")

    numero_arrendatarios = st.number_input("Número de Arrendatarios", min_value=1, value=1)

    # Generación dinámica de campos para cada arrendatario
    for i in range(1, numero_arrendatarios + 1):
        st.subheader(f"ARRENDATARIO {i}")
        nombre_arrendatario = st.text_input(f"Nombre del Arrendatario", key=f"nombre_arrendatario_{i}")
        ascensor_escalera = st.selectbox("DNI/ID/PASAPORTE", ["", "DNI", "ID", "PASAPORTE"], key=f"dni_id_pasaporte_{i}")
        dni_cif_arrendatario = st.text_input(f"DNI/ID/PASAPORTE", key=f"dni_cif_arrendatario_{i}")
        direccion_arrendatario = st.text_input(f"Dirección", key=f"direccion_arrendatario_{i}")
        pais = st.text_input(f"País", key=f"pais_arrendatario_{i}")
        telefono_arrendatario = st.text_input(f"Teléfono", key=f"telefono_arrendatario_{i}")
        email_arrendatario = st.text_input(f"Email", key=f"email_arrendatario_{i}")



with tab3:
    st.subheader("PISO")
    superficie = st.number_input("Superficie (m²)", min_value=0, value=0)
    capacidad = st.number_input("Capacidad", min_value=0, value=0)
    numero_planta = st.number_input("Número de planta", min_value=0, value=0)
    numero_habitaciones = st.number_input("Número de habitaciones", min_value=0, value=0)
    numero_habitaciones_suite = st.number_input("Número de habitaciones suite", min_value=0, value=0)
    numero_banos = st.number_input("Número de baños", min_value=0, value=0)
    numero_aseos = st.number_input("Número de aseos", min_value=0, value=0)
    ascensor_escalera = st.selectbox("Ascensor / escalera", ["", "Ascensor", "Escalera"])
    wifi = st.selectbox("Wifi", ["", "Sí", "No"])

    st.subheader("UBICACIÓN")
    precio_alquiler = st.number_input("Precio alquiler", step=0.1)
    consumos = st.number_input("Consumos", value= 100, step=10)
    fecha_disponibilidad = st.date_input("Fecha de disponibilidad", value=None)
    direccion_completa = st.text_input("Dirección")
    poblacion = st.selectbox("Población", ["", "Madrid", "Barcelona"])
    distritos = distritos_por_poblacion.get(poblacion, [])
    distrito = st.selectbox("Distrito", distritos)
    barrios = barrios_por_distrito.get(distrito, [])
    barrio = st.selectbox("Barrio", barrios)
    ref_catastral = st.text_input("REF. CATASTRAL")

    st.subheader("GENERAL")
    gastos_comunidad_incluidos = st.selectbox("Gastos de comunidad incluidos", ["", "Sí", "No"])
    orientacion = st.text_input("Orientación")
    aislamiento_ventana = st.selectbox("Aislamiento ventana", ["", "Sí", "No"])
    acepta_animales = st.selectbox("Acepta animales", ["", "Sí", "No"])
    acepta_pet_fee = st.selectbox("Acepta Pet fee", ["", "Sí", "No"])
    exterior = st.selectbox("Exterior", ["", "Sí", "No"])
    acceso_minusvalidos = st.selectbox("Acceso minusválidos", ["", "Sí", "No"])
    calefaccion = st.selectbox("Calefacción", ["", "Individual", "Central"])
    aire_acondicionado = st.selectbox("Aire acondicionado", ["", "Sí", "No"])
    combustible_calefaccion = st.selectbox("Combustible calefacción", ["", "Gas natural", "Electricidad", "Otro"])
    agua_caliente = st.selectbox("Agua caliente", ["", "Electricidad", "Gas natural", "Otro"])

    st.subheader("COCINA")
    espacio_cocina = st.selectbox("Espacio cocina", ["", "Integrada", "Independiente"])
    tipo_cocina = st.selectbox("Tipo cocina", ["", "Vitro", "Gas", "Inducción"])
    horno = st.selectbox("Horno", ["", "Sí", "No"])
    nevera = st.selectbox("Nevera", ["", "Sí", "No"])
    lavavajillas = st.selectbox("Lavavajillas", ["", "Sí", "No"])
    microondas = st.selectbox("Microondas", ["", "Sí", "No"])
    utensilios = st.selectbox("Utensilios", ["", "Sí", "No"])
    cafetera = st.selectbox("Cafetera", ["", "Sí", "No"])
    tostadora = st.selectbox("Tostadora", ["", "Sí", "No"])
    otros_cocina = st.text_area("Otros (especificar)")

    st.subheader("DOTACIÓN")
    armarios_empotrados = st.selectbox("Armarios empotrados", ["", "Sí", "No"])
    lavadora = st.selectbox("Lavadora", ["", "Sí", "No"])
    secadora = st.selectbox("Secadora", ["", "Sí", "No"])
    tendedero = st.selectbox("Tendedero", ["", "Sí", "No"])
    sofa_cama = st.selectbox("Sofá cama", ["", "Sí", "No"])
    smart_tv = st.selectbox("Smart TV", ["", "Sí", "No"])
    ventilador = st.selectbox("Ventilador", ["", "Sí", "No"])

    st.subheader("OTROS ESPACIOS")
    balcon = st.selectbox("Balcón", ["", "Sí", "No"])
    patio = st.selectbox("Patio", ["", "Sí", "No"])
    terraza = st.selectbox("Terraza", ["", "Sí", "No"])
    plaza_parking_precio = st.text_input("Plaza de parking (precio)")
    piscina = st.selectbox("Piscina", ["", "Sí", "No"])
    trastero_precio = st.text_input("Trastero (precio)")
    estudio = st.selectbox("Estudio", ["", "Sí", "No"])
    vestidor = st.selectbox("Vestidor", ["", "Sí", "No"])
    zona_lavado = st.selectbox("Zona de lavado", ["", "Sí", "No"])

    st.subheader("COMUNIDAD")
    interfono = st.selectbox("Interfono", ["", "Sí", "No"])
    portero = st.selectbox("Portero", ["", "Sí", "No"])
    video_portero = st.selectbox("Video portero", ["", "Sí", "No"])
    alarma = st.selectbox("Alarma", ["", "Sí", "No"])

    for i in range(1, numero_habitaciones + 1):
        st.subheader(f"HABITACIÓN {i}")
        habitacion_suite = st.selectbox(f"Habitación {i} suite", ["", "Sí", "No"])
        tipo_cama = st.selectbox(f"Tipo cama Habitación {i}", ["", "Individual", "Doble", "Queen", "King"])
        armarios = st.selectbox(f"Armarios en Habitación {i}", ["", "Sí", "No"])
        sabanas = st.selectbox(f"Sábanas en Habitación {i}", ["", "Sí", "No"])

    # Generación dinámica de campos para los baños
    for i in range(1, numero_banos + 1):
        st.subheader(f"BAÑO {i}")
        bano_suite = st.selectbox(f"Baño {i} en suite", ["", "Sí", "No"])
        tipo_ducha = st.selectbox(f"Tipo de ducha en Baño {i}", ["", "Ducha", "Bañera"])
        toallas = st.selectbox(f"Toallas en Baño {i}", ["", "Sí", "No"])

    # Generación dinámica de campos para los aseos
    for i in range(1, numero_aseos + 1):
        st.subheader(f"ASEO {i}")
        aseo_toallas = st.selectbox(f"Toallas en Aseo {i}", ["", "Sí", "No"])

    st.subheader("COMENTARIOS")
    piso_larga_estancia = st.selectbox("Piso larga estancia", ["", "Sí", "No"])
    portales_restringidos = st.text_input("Portales (restringidos) a publicar")
    otros_comentarios = st.text_area("Otros (títulos, descripción, etc.)")


with col3:
    if st.button("Guardar"):
        # Insertar o recuperar el ID de la dirección del piso
        piso_id = db.insert_direccion_piso(direccion_completa)

        # Guardar datos del arrendador
        if tipo_arrendador == "Fisica":
            arrendador_id = db.insert_arrendador(piso_id, nombre_arrendador, dni_arrendador, canal_arrendador, cuenta_bancaria_arrendador,
                                                 direccion_facturacion_arrendador, email_arrendador, telefono_arrendador, administracion_arrendador)
        elif tipo_arrendador == "Juridica":
            arrendador_id = db.insert_arrendador(piso_id, empresa_arrendador, cif_arrendador, canal_arrendador, cuenta_bancaria_arrendador,
                                                 direccion_facturacion_arrendador, email_arrendador, telefono_arrendador, administracion_arrendador)

        # Guardar datos de los arrendatarios
        for i in range(1, numero_arrendatarios + 1):
            db.insert_arrendatario(piso_id, st.session_state[f"nombre_arrendatario_{i}"], st.session_state[f"dni_cif_arrendatario_{i}"],
                                   st.session_state[f"direccion_arrendatario_{i}"], st.session_state[f"pais_arrendatario_{i}"],
                                   st.session_state[f"telefono_arrendatario_{i}"], st.session_state[f"email_arrendatario_{i}"])

        # Guardar las características del piso
        caracteristicas = (
            superficie, capacidad, numero_planta, numero_habitaciones, numero_habitaciones_suite, numero_banos, numero_aseos, ascensor_escalera,
            wifi, precio_alquiler, consumos, fecha_disponibilidad, direccion_completa, poblacion, distrito, barrio, ref_catastral,
            gastos_comunidad_incluidos, orientacion, aislamiento_ventana, acepta_animales, acepta_pet_fee, exterior, acceso_minusvalidos,
            calefaccion, aire_acondicionado, combustible_calefaccion, agua_caliente, espacio_cocina, tipo_cocina, horno, nevera, lavavajillas,
            microondas, utensilios, cafetera, tostadora, otros_cocina, armarios_empotrados, lavadora, secadora, tendedero, sofa_cama, smart_tv,
            ventilador, balcon, patio, terraza, plaza_parking_precio, piscina, trastero_precio, estudio, vestidor, zona_lavado, interfono,
            portero, video_portero, alarma, piso_larga_estancia, portales_restringidos, otros_comentarios
        )
        db.insert_caracteristicas_piso(piso_id, caracteristicas)

        st.success("Datos guardados exitosamente")

        # Cerrar la conexión cuando termines
        db.close()
