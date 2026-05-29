# PawFamily - API REST Backend

El núcleo lógico de este sistema ha sido desarrollado como una API REST modular utilizando Python 3 y Flask, conectada a una base de datos relacional MySQL distribuida en red.

## Tecnologías y Herramientas Utilizadas

*   **Lenguaje:** Python 3
*   **Framework:** Flask (organizado mediante Blueprints)
*   **Conector de Base de Datos:** PyMySQL (utilizando DictCursor para mapeo JSON)
*   **Seguridad:** Flask-CORS (Políticas de intercambio de origen cruzado) y Python-dotenv
*   **Testing:** Pytest (Unit & Integration) y automatización E2E[cite: 4]

## Arquitectura del Proyecto

El código fuente está separado por carpetas para que sea más limpio y ordenado[cite: 4]:

*   **`config/`**: Guarda la configuración y la conexión con la base de datos MySQL[cite: 4].
*   **`routes/`**: Recibe las peticiones de la web y devuelve las respuestas en JSON[cite: 4].
*   **`services/`**: Comprueba que los datos sean correctos antes de guardarlos[cite: 4].
*   **`repositories/`**: Se conecta directamente a la base de datos para hacer las consultas (JOINs)[cite: 4].

## Instalación y Ejecución Local

Sigue estos pasos para levantar el servidor de desarrollo en tu entorno local[cite: 4]:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/pawfamily.git](https://github.com/tu-usuario/pawfamily.git)
cd pawfamily/backend

2. Crear y activar un entorno virtual (Recomendado)
En Windows:

python -m venv venv
    .\venv\Scripts\activate
    ```
*   **En macOS/Linux:**
```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Instalar las dependencias obligatorias
```bash
pip install -r requirements.txt

 

4. Configurar las Variables de Entorno 

Crea un archivo llamado .env en la raíz de la carpeta backend/ para configurar las credenciales de tu base de datos de manera segura:

DB_HOST=192.168.116.20   # IP estática de tu Windows Server o Localhost
DB_USER=tu_usuario       # Usuario creado en MySQL
DB_PASSWORD=Monlau2025   # Contraseña de acceso
DB_NAME=paw_family       # Nombre de tu esquema
DB_PORT=3306             # Puerto de escucha del Firewall

 

5. Iniciar el servidor de Flask 

python app.py
 

La API comenzará a escuchar peticiones en el puerto local de desarrollo: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

 

Ejecución de Pruebas (Testing) 

El proyecto cuenta con una suite completa de pruebas unitarias e integración. Para ejecutarlas de forma automatizada, simplemente escribe en la terminal:  

pytest

Documentación de Endpoints y Evidencias 

Para consultar la estructura completa de los esquemas JSON de intercambio de datos (Requests y Responses), la gestión de errores HTTP y las pruebas de validación efectuadas con Postman, por favor, remítase a la Sección 9.2 ("Backend") de la Memoria del Proyecto. 