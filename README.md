# st-Lezo
https://st-lezo-2o66uycqbsn7mmfeps2xbz.streamlit.app/

Aplicación web desarrollada con **Streamlit**.

## Descripción

Este proyecto consiste en una aplicación web implementada mediante el framework Streamlit. La aplicación está estructurada como una solución ligera de una sola página, utilizando un único archivo Python para gestionar la configuración, el diseño visual, la navegación y la presentación de contenido.

La arquitectura aprovecha el modelo de ejecución reactivo de Streamlit para actualizar dinámicamente la interfaz de usuario.

---

## Arquitectura

La aplicación sigue una arquitectura simple basada en un único archivo principal:

```text
streamlit_app.py
```

Responsabilidades principales:

* Configuración de la aplicación.
* Personalización de estilos mediante CSS.
* Definición de la estructura de navegación.
* Renderizado de componentes visuales.
* Gestión del flujo de ejecución de Streamlit.

---

## Características Técnicas

### Personalización Visual

La interfaz utiliza inyección de CSS personalizada para sobrescribir los estilos predeterminados de Streamlit.

Características implementadas:

* Tema oscuro personalizado.
* Colores de acento definidos mediante CSS.
* Ajustes de tipografía y presentación visual.
* Estilización de componentes nativos de Streamlit.

---

### Navegación

La aplicación organiza la información mediante pestañas utilizando:

```python
st.tabs()
```

Este enfoque permite dividir la interfaz en secciones independientes manteniendo una experiencia de usuario sencilla.

---

### Componentes Utilizados

Entre los componentes principales empleados se encuentran:

```python
st.tabs()
st.metric()
st.image()
st.markdown()
```

Estos componentes permiten construir interfaces interactivas sin necesidad de frameworks frontend adicionales.

---

## Estructura del Proyecto

```text
st-Lezo/
│
├── streamlit_app.py
├── README.md
└── .python-version
```

### Archivos principales

| Archivo            | Descripción                                                |
| ------------------ | ---------------------------------------------------------- |
| `streamlit_app.py` | Aplicación principal                                       |
| `README.md`        | Documentación del proyecto                                 |
| `.python-version`  | Versión de Python utilizada para garantizar compatibilidad |

---

## Requisitos

* Python 3.x
* Streamlit

---

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/usuario/st-Lezo.git
cd st-Lezo
```

### Crear entorno virtual (opcional)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

### Instalar dependencias

```bash
pip install streamlit
```

o:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Iniciar la aplicación localmente:

```bash
streamlit run streamlit_app.py
```

Por defecto, Streamlit expondrá la aplicación en:

```text
http://localhost:8501
```

---

## Tecnologías Utilizadas

* Python
* Streamlit
* CSS personalizado

---

## Consideraciones de Compatibilidad

El proyecto incluye un archivo `.python-version` para fijar la versión de Python y asegurar un comportamiento consistente entre entornos de desarrollo y despliegue.

La aplicación no requiere:

* Frameworks JavaScript externos.
* Bases de datos.
* Servidores backend adicionales.

Todo el procesamiento y renderizado se realiza mediante Streamlit.
