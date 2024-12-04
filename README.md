# DjangoAIProject

**DjangoAIProject** es una aplicación web desarrollada con **Django**, diseñada como un sitio tipo blog para explorar temas de programación web e inteligencia artificial. Este proyecto fue realizado para las materias de **"Programación Web"** e **"Inteligencia Artificial"**.

---

## 🚀 Funcionalidades principales

- **Menú interactivo con 4 secciones principales**:
  1. **Principal**: Información general sobre las tecnologías utilizadas.
  2. **Web**: Filtros personalizados y visualización de imágenes dinámicas.
  3. **Python**: Tabla conectada a una base de datos (MySQL) con información sobre herramientas de inteligencia artificial, y formularios para consultas GET y POST.
  4. **Inteligencia Artificial**: Sección dedicada a la implementación de modelos de AI (en desarrollo).

- **Integración de bases de datos**:
  - La aplicación utiliza el ORM de Django para interactuar con una base de datos MySQL.

- **Templating**:
  - Uso de plantillas reutilizables para mantener un diseño consistente.

- **Autenticación integrada**:
  - Sistema de usuarios basado en las herramientas de autenticación de Django.

---

## ⚙️ Tecnologías utilizadas

- **Backend**: Django 4.2, Python 3.10
- **Frontend**: HTML5, CSS3, JavaScript
- **Base de datos**: MySQL
- **Otras herramientas**:
  - Django ORM
  - Plantillas reutilizables de Django

---

## 📂 Instalación

### Requisitos previos
- Python >= 3.10
- MySQL
- Virtualenv o similar

### Pasos para la instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/django-ai-project.git
   cd django-ai-project
   ```
2. Crea y activa un entorno virtual:
  ```bash
  python -m venv env
  source env/bin/activate # En Windows: env\Scripts\activate
  ```


```bash
  ```
3. Instala las dependencias del proyecto:
  ```bash
  pip install -r requirements.txt
  ```
4. Aplica las migraciones de la base de datos:
   ```bash
    python manage.py makemigrations
    python manage.py migrate
  ```
5. Ejecuta el servidor de desarrollo:
  ```bash
  python manage.py runserver
  ```
Abre tu navegador en http://127.0.0.1:8000.

Aquí tienes un archivo `README.md` diseñado específicamente para tu proyecto **DjangoAIProject**:

---

### **README.md para "DjangoAIProject"**

```markdown
# DjangoAIProject

**DjangoAIProject** es una aplicación web desarrollada con **Django**, diseñada como un sitio tipo blog para explorar temas de programación web e inteligencia artificial. Este proyecto fue realizado para las materias de **"Programación Web"** e **"Inteligencia Artificial"**.

---

## 🚀 Funcionalidades principales

- **Menú interactivo con 4 secciones principales**:
  1. **Principal**: Información general sobre las tecnologías utilizadas.
  2. **Web**: Filtros personalizados y visualización de imágenes dinámicas.
  3. **Python**: Tabla conectada a una base de datos (MySQL) con información sobre herramientas de inteligencia artificial, y formularios para consultas GET y POST.
  4. **Inteligencia Artificial**: Sección dedicada a la implementación de modelos de AI (en desarrollo).

- **Integración de bases de datos**:
  - La aplicación utiliza el ORM de Django para interactuar con una base de datos MySQL.

- **Templating**:
  - Uso de plantillas reutilizables para mantener un diseño consistente.

- **Autenticación integrada**:
  - Sistema de usuarios basado en las herramientas de autenticación de Django.

---

## ⚙️ Tecnologías utilizadas

- **Backend**: Django 4.2, Python 3.10
- **Frontend**: HTML5, CSS3, JavaScript
- **Base de datos**: MySQL
- **Otras herramientas**:
  - Django ORM
  - Plantillas reutilizables de Django

---

## 📂 Instalación

### Requisitos previos
- Python >= 3.10
- MySQL
- Virtualenv o similar

### Pasos para la instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/django-ai-project.git
   cd django-ai-project
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate # En Windows: env\Scripts\activate
   ```

3. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las credenciales de la base de datos:
   - Renombra el archivo `example.env` a `.env`:
     ```bash
     mv example.env .env
     ```
   - Abre el archivo `.env` y añade tus credenciales de MySQL:
     ```
     DB_NAME=nombre_base_datos
     DB_USER=usuario
     DB_PASSWORD=contraseña
     DB_HOST=localhost
     DB_PORT=3306
     ```

5. Aplica las migraciones de la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

7. Abre tu navegador en `http://127.0.0.1:8000`.

---

## 🚧 Estado del proyecto

- Las secciones **Principal**, **Web**, y **Python** están completamente funcionales.
- La sección **Inteligencia Artificial** está en desarrollo para integrar modelos de AI.

---

## 🤝 Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una rama nueva (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz un push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más información.

---

## 📧 Contacto

Desarrollado por **Felipe de Jesús Duarte Castillo**  
Correo: [fduartecastillo2@gmail.com](mailto:fduartecastillo2@gmail.com)  
Portafolio: [https://felipeduarte2.github.io/portafolio](https://felipeduarte2.netlify.app/)
```

---

### **¿Qué incluye este README.md?**
1. **Introducción**: Explica el propósito del proyecto y las tecnologías utilizadas.
2. **Funcionalidades**: Detalla las características clave.
3. **Guía de instalación**: Proporciona instrucciones paso a paso para configurar y ejecutar el proyecto.
5. **Estado del proyecto**: Indica las partes completadas y las que están en desarrollo.
6. **Contribuciones y licencia**: Facilita la colaboración y define los derechos del proyecto.

---

### **Próximos pasos**
1. **Asegúrate de añadir las imágenes**:
   - Sube capturas relevantes del proyecto y reemplaza las rutas `ruta/de/imagen-*.png` por sus ubicaciones reales.
2. **Súbelo a GitHub**:
   - Guarda el archivo como `README.md` y súbelo a tu repositorio.

¿Te gustaría que trabajemos en otro proyecto o alguna sección específica? 😊



