import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Blas de Lezo - El Mediohombre", page_icon="⚓", layout="wide")

# Estilos CSS personalizados para Modo Oscuro
st.markdown("""
<style>
    /* Forzar fondo oscuro para toda la app */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .main-title {
        font-family: 'Georgia', serif;
        color: #ffffff;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .subtitle {
        color: #cbd5e1;
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }
    .section-title {
        color: #ffffff;
        border-bottom: 3px solid #d4af37; /* Acento dorado */
        padding-bottom: 5px;
        margin-top: 2rem;
    }
    .quote-box {
        background-color: #1e293b; /* Fondo recuadro oscuro */
        border-left: 6px solid #d4af37;
        padding: 20px;
        font-style: italic;
        font-size: 1.5rem;
        color: #ffffff;
        margin: 2rem 0;
    }
    .card {
        background-color: #1e293b; /* Fondo tarjeta oscura */
        padding: 20px;
        border-radius: 10px;
        border-top: 5px solid #d4af37;
        text-align: center;
        height: 100%;
        color: #ffffff !important;
    }
    .card p, .card h4 {
        color: #ffffff !important;
    }
    /* Asegurar que los textos generales sean blancos */
    p, li, .stMarkdown {
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Título y encabezado
st.markdown('<div class="main-title">Blas de Lezo y Olavarrieta</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">El Invencible "Mediohombre" y la Defensa de Cartagena de Indias</div>', unsafe_allow_html=True)

# Pestañas de navegación
tab1, tab2, tab3, tab4 = st.tabs(["⚓ Biografía", "⚔️ El Mediohombre", "🛡️ Sitio de Cartagena", "📜 Legado"])

with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<h2 class="section-title">Orígenes y Primeros Años</h2>', unsafe_allow_html=True)
        st.write("""
        Nacido en Pasajes (Guipúzcoa) en 1689, Blas de Lezo se enroló en la marina francesa (aliada de España) como guardiamarina a los doce años. 
        
        Su carrera comenzó en plena **Guerra de Sucesión Española**, donde rápidamente demostró un valor y una capacidad estratégica fuera de lo común para su edad. Ascendió rápidamente en el escalafón militar gracias a su audacia en combate y su inteligencia naval.
        
        A lo largo de su carrera, protegió las rutas comerciales del Imperio, luchó contra piratas en el Mar del Sur (Pacífico) y lideró la reconquista de Orán (1732).
        """)
    with col2:
        # Imagen de Wikimedia
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Blas_de_Lezo.jpg/800px-Blas_de_Lezo.jpg", caption="Retrato de Blas de Lezo", use_container_width=True)

with tab2:
    st.markdown('<h2 class="section-title">El Origen de su Apodo: "El Mediohombre"</h2>', unsafe_allow_html=True)
    st.write("Blas de Lezo sacrificó gran parte de su cuerpo en defensa de su nación. Sus legendarias heridas de guerra forjaron su mito:")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="card">
            <h3 style="color:#d4af37; font-size:3rem; margin-bottom:0px;">🦵</h3>
            <h4>La Pierna Izquierda</h4>
            <p><strong>Batalla de Vélez-Málaga (1704):</strong> A los 15 años, una bala de cañón le destrozó la pierna. Le fue amputada por debajo de la rodilla sin anestesia, soportando la cirugía sin proferir una queja.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="card">
            <h3 style="color:#d4af37; font-size:3rem; margin-bottom:0px;">👁️</h3>
            <h4>El Ojo Izquierdo</h4>
            <p><strong>Asedio de Tolón (1707):</strong> Una esquirla de cañón impactó en su rostro, haciéndole perder la visión del ojo izquierdo por completo.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div class="card">
            <h3 style="color:#d4af37; font-size:3rem; margin-bottom:0px;">💪</h3>
            <h4>El Brazo Derecho</h4>
            <p><strong>Sitio de Barcelona (1714):</strong> Recibió un balazo en el antebrazo derecho que le rompió tendones y huesos, dejándolo sin movilidad en el brazo para el resto de su vida.</p>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown('<h2 class="section-title">La Batalla de Cartagena de Indias (1741)</h2>', unsafe_allow_html=True)
    st.write("El almirante inglés Edward Vernon atacó Cartagena de Indias con una flota colosal, buscando asestar el golpe definitivo al Imperio Español en la Guerra del Asiento. La defensa española, liderada estratégicamente por Blas de Lezo, logró la mayor derrota naval de la historia de Gran Bretaña.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.metric(label="🇬🇧 Fuerzas Británicas (Vernon)", value="~27.000 hombres", delta="186 buques y 2.000 cañones", delta_color="off")
    with col_b:
        st.metric(label="🇪🇸 Defensa Española (Lezo)", value="~3.000 hombres", delta="6 navíos", delta_color="off")
    
    st.subheader("La Estrategia Defensiva")
    st.write("""
    Con una inferioridad numérica de **10 a 1**, Blas de Lezo sabía que no podía ganar un combate abierto. Su genio táctico consistió en:
    * **Aprovechar el terreno:** Hundió sus propios barcos en el estrecho de Boca Chica para bloquear la entrada de los buques ingleses.
    * **Retraso y desgaste:** Obligó a los británicos a desembarcar y combatir en zonas pantanosas, exponiéndolos a la fiebre amarilla y la malaria.
    * **Defensa final:** La resistencia en el Castillo de San Felipe de Barajas terminó por colapsar la moral y las fuerzas inglesas, causando unas **18.000 bajas** británicas.
    """)
    st.info("La derrota británica fue tan humillante que el Rey Jorge II prohibió bajo castigo hablar o escribir sobre el tema en Inglaterra. Incluso se habían acuñado monedas prematuras celebrando la victoria británica que nunca ocurrió.")

with tab4:
    st.markdown('<h2 class="section-title">Legado y Sentencia</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="quote-box">
        "Para venir a Cartagena es necesario que el rey de Inglaterra construya otra escuadra mayor, porque esta solo ha quedado para conducir carbón de Irlanda a Londres."<br><br>
        <div style="text-align:right; font-size:1.2rem; font-weight:bold;">— Blas de Lezo, a Edward Vernon</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    **Muerte y Olvido:** Blas de Lezo murió poco después de la batalla, en septiembre de 1741, a causa de las heridas e infecciones contraídas en el asedio. Debido a desacuerdos políticos con el Virrey Eslava, fue enterrado en una fosa común y su figura fue parcialmente olvidada por siglos.
    
    **Reconocimiento Actual:** Hoy en día, Blas de Lezo es considerado uno de los mayores genios militares de la historia naval española. 
    * Cuenta con imponentes estatuas en Madrid (Plaza de Colón) y en Cartagena de Indias.
    * La Armada Española honra su memoria nombrando a uno de sus buques más modernos con su nombre: la **Fragata F-103 "Blas de Lezo"**.
    """)
    
st.markdown("---")
st.caption("Aplicación desarrollada con Streamlit | Información basada en Wikipedia")
