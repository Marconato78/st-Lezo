# st-Lezo

Aplicación web desarrollada con **Streamlit** para conmemorar la vida, las hazañas militares y el legado histórico del almirante español **Blas de Lezo y Olavarrieta**.

Conocido como *"Patapalo"* o *"Mediohombre"* debido a las numerosas heridas sufridas en combate, Blas de Lezo es una de las figuras más destacadas de la historia naval española. Su mayor logro fue la defensa de **Cartagena de Indias** en 1741 frente a una enorme flota británica.

La aplicación actúa como un repositorio histórico interactivo que utiliza tecnologías web modernas para presentar información biográfica, estadísticas militares y el legado cultural del almirante.

---

## Características

* 📜 Información histórica sobre la vida de Blas de Lezo.
* ⚔️ Datos sobre la defensa de Cartagena de Indias.
* 📊 Comparativas visuales de fuerzas militares.
* 🖼️ Integración de imágenes y retratos históricos.
* 🌙 Interfaz personalizada con temática oscura inspirada en museos históricos.
* 📑 Navegación organizada mediante pestañas interactivas.

---

## Contexto Histórico

El objetivo principal de la aplicación es divulgar uno de los episodios más importantes de la historia militar española:

### Sitio de Cartagena de Indias (1741)

Blas de Lezo logró defender la ciudad de Cartagena de Indias con:

* **3.000 soldados**
* **6 barcos**

frente a una fuerza británica compuesta por:

* **27.000 hombres**
* **186 barcos**

La aplicación destaca algunas de las estrategias que hicieron posible esta victoria:

* Hundimiento estratégico de barcos para bloquear los canales de acceso.
* Aprovechamiento de la geografía defensiva de la bahía.
* Desgaste del enemigo mediante enfermedades tropicales y condiciones climáticas adversas.
* Coordinación eficiente de recursos extremadamente limitados.

---

## Arquitectura de la Aplicación

El proyecto está implementado como una aplicación Streamlit de un único archivo:

```text
streamlit_app.py
```

Este archivo gestiona:

* Configuración de la aplicación.
* Estilos personalizados.
* Estructura de navegación.
* Presentación del contenido histórico.
* Visualización de métricas e imágenes.

La arquitectura aprovecha el modelo de ejecución reactivo de Streamlit para actualizar dinámicamente la interfaz.

---

## Estructura de la Interfaz

### Sistema de Temas

La aplicación utiliza una estrategia de inyección de CSS personalizada para reemplazar los estilos predeterminados de Streamlit.

Características visuales:

| Elemento        | Color                         |
| --------------- | ----------------------------- |
| Fondo principal | `#0e1117`                     |
| Acentos dorados | `#d4af37`                     |
| Estilo general  | Temática histórica tipo museo |

### Navegación por Pestañas

El contenido está dividido en cuatro secciones principales mediante:

```python
st.tabs()
```

Esto permite una navegación clara entre los distintos aspectos de la vida y legado del almirante.

---

## Componentes Principales

### 1. Información Histórica

Presenta:

* Biografía de Blas de Lezo.
* Principales campañas militares.
* Logros estratégicos.
* Legado histórico.

---

### 2. Visualización de Datos

La aplicación utiliza:

```python
st.metric()
```

para mostrar comparativas numéricas que evidencian la enorme desventaja de las fuerzas españolas durante la defensa de Cartagena de Indias.

Ejemplos:

* Número de soldados.
* Número de barcos.
* Relación de fuerzas entre ambos bandos.

---

### 3. Contenido Multimedia

Las imágenes históricas se integran mediante:

```python
st.image()
```

permitiendo mostrar retratos y material gráfico relacionado con el almirante.

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

| Archivo            | Descripción                    |
| ------------------ | ------------------------------ |
| `streamlit_app.py` | Aplicación principal Streamlit |
| `README.md`        | Documentación del proyecto     |
| `.python-version`  | Versión de Python utilizada    |

---

## Requisitos

* Python 3.x
* Streamlit

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/st-Lezo.git
cd st-Lezo
```

### 2. Crear entorno virtual (opcional)

```bash
python -m venv .venv
```

Activar:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install streamlit
```

o bien:

```bash
pip install -r requirements.txt
```

si existe un archivo de requisitos.

---

## Ejecución

Iniciar la aplicación localmente:

```bash
streamlit run streamlit_app.py
```

Una vez iniciada, Streamlit mostrará una URL similar a:

```text
http://localhost:8501
```

Abrirla en el navegador para acceder a la aplicación.

---

## Tecnologías Utilizadas

* Python
* Streamlit
* HTML/CSS personalizado

---

## Objetivo Educativo

Este proyecto busca acercar al público la figura de Blas de Lezo mediante una experiencia interactiva y visual, facilitando la comprensión de uno de los episodios más relevantes de la historia naval española.

---

## Referencias

* Blas de Lezo y Olavarrieta
* Sitio de Cartagena de Indias (1741)
* Historia Naval Española
* Streamlit
