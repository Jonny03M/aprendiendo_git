import streamlit as st
st.title("Conversor de temperaturas")

modo = st.radio("Conversor de :",["Celsius a Fahrenheit", "Fahrenheit a Celsius"])
valor = st.number_input("Valor")
if modo == "Celsius a Fahrenheit":
    resultado = valor * 9/ 5+32
    st.success(f"**{round(resultado,2)} °F")
    st.caption(f"{valor} °C convertidos a Fahrenheit")
else: 
    resultado = (valor -32) * 5 / 9
    st.success(f"**{round(resultado,2)} °C")
    st.caption(f"{valor} °F convertidos a Celsius")