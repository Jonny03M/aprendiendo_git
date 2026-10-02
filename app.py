import streamlit as st

st.title("Conversor de temperaturas")
st.write("Creado por Jonny")
opciones = [
    "Celsius a Fahrenheit",
    "Fahrenheit a Celsius",
    "Celsius a Kelvin",
    "Kelvin a Celsius"
]

modo = st.radio("Conversor de:", opciones)
valor = st.number_input("Valor", value=0.0, format="%.2f")

if modo == "Celsius a Fahrenheit":
    resultado = (valor * 9 / 5) + 32
    st.success(f"**{round(resultado,2)} °F")
    st.caption(f"{valor} °C convertidos a Fahrenheit")
    
elif modo == "Fahrenheit a Celsius":
    resultado = (valor - 32) * 5 / 9
    st.success(f"**{round(resultado,2)} °C")
    st.caption(f"{valor} °F convertidos a Celsius")
    
elif modo == "Celsius a Kelvin":
    resultado = valor + 273.15
    st.success(f"**{round(resultado,2)} °K")
    st.caption(f"{valor} °C convertidos a Kelvin")        
elif modo == "Kelvin a Celsius":
    resultado = valor - 273.15
    st.success(f"**{round(resultado,2)} °C")
    st.caption(f"{valor} °K convertidos a Celsius")
