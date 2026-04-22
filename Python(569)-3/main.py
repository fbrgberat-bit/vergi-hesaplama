import streamlit as st

yas = st.number_input("Yaşınızı giriniz")
st.balloons()
if yas < 16:
    st.error("Ehliyet Alamaz")
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmJ2azlkeWd1dWFmcnMzYjJrNTR1OHI5N284NzQzdGRvaTVnZ282ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PcMXQqcsn2Fz2/giphy.gif")
elif yas < 18:
    st.warning("Motor Ehliyeti Alabilir")
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWtrNzA3MzVnbGoxdGxtNWE5ZmRic213dDFheGt0dXl6N2p1NzE5NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GiXRtlrK55gNDtw1cV/giphy.gif")
elif yas < 25:
    st.success("Motor ve Otomobil Ehliyeti labilir")
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWJqYzJhcnRyb2JkejF5MGFxaDJndjg4ODhrdml6NnFsb3RiMmVtZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Vfhj19PusenfO/giphy.gif")
else:
    st.success("Motor, Otomobil ve Otobüs Ehliyeti Albilir")
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWIzczd6NHRncnJtbXFkYmVsZmszOGY0em9odnZleDlycGUxZDZxcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/B5BfWWr1UnVrG/giphy.gif")
