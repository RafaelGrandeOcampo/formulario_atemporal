import sqlite3

class DatabaseHandler:
    def __init__(self, db_name="inmobiliaria.db"):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Crear tabla para las direcciones de los pisos
        self.c.execute('''CREATE TABLE IF NOT EXISTS direccion_piso (
            id INTEGER PRIMARY KEY,
            direccion TEXT UNIQUE
        )''')

        # Crear tabla para los arrendadores
        self.c.execute('''CREATE TABLE IF NOT EXISTS arrendador (
            id INTEGER PRIMARY KEY,
            piso_id INTEGER,
            nombre TEXT,
            dni TEXT,
            canal_captacion TEXT,
            cuenta_bancaria TEXT,
            direccion_facturacion TEXT,
            email TEXT,
            telefono TEXT,
            administracion REAL,
            FOREIGN KEY(piso_id) REFERENCES direccion_piso(id)
        )''')

        # Crear tabla para las características del piso
        self.c.execute('''CREATE TABLE IF NOT EXISTS caracteristicas_piso (
            id INTEGER PRIMARY KEY,
            piso_id INTEGER,
            superficie INTEGER,
            capacidad INTEGER,
            numero_planta INTEGER,
            numero_habitaciones INTEGER,
            numero_habitaciones_suite INTEGER,
            numero_banos INTEGER,
            numero_aseos INTEGER,
            ascensor_escalera TEXT,
            wifi TEXT,
            precio_alquiler REAL,
            consumos REAL,
            fecha_disponibilidad TEXT,
            poblacion TEXT,
            distrito TEXT,
            barrio TEXT,
            ref_catastral TEXT,
            gastos_comunidad_incluidos TEXT,
            orientacion TEXT,
            aislamiento_ventana TEXT,
            acepta_animales TEXT,
            acepta_pet_fee TEXT,
            exterior TEXT,
            acceso_minusvalidos TEXT,
            calefaccion TEXT,
            aire_acondicionado TEXT,
            combustible_calefaccion TEXT,
            agua_caliente TEXT,
            espacio_cocina TEXT,
            tipo_cocina TEXT,
            horno TEXT,
            nevera TEXT,
            lavavajillas TEXT,
            microondas TEXT,
            utensilios TEXT,
            cafetera TEXT,
            tostadora TEXT,
            otros_cocina TEXT,
            armarios_empotrados TEXT,
            lavadora TEXT,
            secadora TEXT,
            tendedero TEXT,
            sofa_cama TEXT,
            smart_tv TEXT,
            ventilador TEXT,
            balcon TEXT,
            patio TEXT,
            terraza TEXT,
            plaza_parking_precio TEXT,
            piscina TEXT,
            trastero_precio TEXT,
            estudio TEXT,
            vestidor TEXT,
            zona_lavado TEXT,
            interfono TEXT,
            portero TEXT,
            video_portero TEXT,
            alarma TEXT,
            piso_larga_estancia TEXT,
            portales_restringidos TEXT,
            otros_comentarios TEXT,
            FOREIGN KEY(piso_id) REFERENCES direccion_piso(id)
        )''')

        # Crear tabla para los arrendatarios
        self.c.execute('''CREATE TABLE IF NOT EXISTS arrendatario (
            id INTEGER PRIMARY KEY,
            piso_id INTEGER,
            nombre TEXT,
            dni TEXT,
            direccion TEXT,
            pais TEXT,
            telefono TEXT,
            email TEXT,
            FOREIGN KEY(piso_id) REFERENCES direccion_piso(id)
        )''')

        self.conn.commit()

    def insert_direccion_piso(self, direccion):
        self.c.execute('''INSERT OR IGNORE INTO direccion_piso (direccion) VALUES (?)''', (direccion,))
        self.conn.commit()
        self.c.execute('SELECT id FROM direccion_piso WHERE direccion = ?', (direccion,))
        return self.c.fetchone()[0]

    def insert_arrendador(self, piso_id, nombre, dni, canal_captacion, cuenta_bancaria, direccion_facturacion, email, telefono, administracion):
        self.c.execute('''INSERT INTO arrendador (piso_id, nombre, dni, canal_captacion, cuenta_bancaria, direccion_facturacion, email, telefono, administracion) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                       (piso_id, nombre, dni, canal_captacion, cuenta_bancaria, direccion_facturacion, email, telefono, administracion))
        self.conn.commit()
        return self.c.lastrowid

    def insert_arrendatario(self, piso_id, nombre, dni, direccion, pais, telefono, email):
        self.c.execute('''INSERT INTO arrendatario (piso_id, nombre, dni, direccion, pais, telefono, email) 
                          VALUES (?, ?, ?, ?, ?, ?, ?)''',
                       (piso_id, nombre, dni, direccion, pais, telefono, email))
        self.conn.commit()

    def insert_caracteristicas_piso(self, piso_id, caracteristicas):
        self.c.execute('''INSERT INTO caracteristicas_piso (piso_id, ...) VALUES (?, ...)''', (piso_id, *caracteristicas))
        self.conn.commit()

    def update_arrendador(self, arrendador_id, piso_id, nombre, dni, canal_captacion, cuenta_bancaria, direccion_facturacion, email, telefono, administracion):
        self.c.execute('''UPDATE arrendador SET piso_id = ?, nombre = ?, dni = ?, canal_captacion = ?, cuenta_bancaria = ?, 
                          direccion_facturacion = ?, email = ?, telefono = ?, administracion = ? 
                          WHERE id = ?''',
                       (piso_id, nombre, dni, canal_captacion, cuenta_bancaria, direccion_facturacion, email, telefono, administracion, arrendador_id))
        self.conn.commit()

    def update_arrendatario(self, arrendatario_id, piso_id, nombre, dni, direccion, pais, telefono, email):
        self.c.execute('''UPDATE arrendatario SET piso_id = ?, nombre = ?, dni = ?, direccion = ?, pais = ?, telefono = ?, email = ? 
                          WHERE id = ?''',
                       (piso_id, nombre, dni, direccion, pais, telefono, email, arrendatario_id))
        self.conn.commit()

    def update_caracteristicas_piso(self, piso_id, caracteristicas):
        self.c.execute('''UPDATE caracteristicas_piso SET ... = ? WHERE id = ?''', (*caracteristicas, piso_id))
        self.conn.commit()

    def delete_arrendador(self, arrendador_id):
        self.c.execute('DELETE FROM arrendador WHERE id = ?', (arrendador_id,))
        self.conn.commit()

    def delete_arrendatario(self, arrendatario_id):
        self.c.execute('DELETE FROM arrendatario WHERE id = ?', (arrendatario_id,))
        self.conn.commit()

    def delete_caracteristicas_piso(self, piso_id):
        self.c.execute('DELETE FROM caracteristicas_piso WHERE id = ?', (piso_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
