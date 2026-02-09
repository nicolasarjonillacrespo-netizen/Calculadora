import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("%Calculadora de Rebajas")
st.markdown("Bienvenido. Introduce tus datos para calcular la rebaja que usted quiera.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio = st.sidebar.number_input("Precio", min_value=0, max_value=100000, value=0)
rebaja = st.sidebar.slider("La rebaja...", 0, 100, 50)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    rbj = precio*rebaja/100
    precio_final=precio-rbj
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="La rebaja", value=f"{rbj:.2f}")
        st.metric(label="el precio rebajado", value=f"{precio_final:.2f}")
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if rebaja < 18.5:
            st.warning("Poca rebaja")
            st.write("Podria ser mejor no?")
        elif 18.5 <= rebaja < 25:
            st.success("✅ Buen chollo")
            st.balloons() # ¡Premio!
        elif 25 <= rebaja < 60:
            st.success("Chollazo")
            st.write("Eres un gran comprador.")
        else:
            st.write("Tu rebeja es flipante")
            
