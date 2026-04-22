import streamlit as st
brut = st.number_input("Brüt Geliri Giriniz: ")

v190 = 190000 * 0.15
v400 = 210000 * 0.20
v1500 = 1100000 * 0.27
v5300 = 3800000 * 0.35
if brut < 190000:
  vergi = v190 + (brut * 0.15)

elif brut < 400000:
  vergi = v190 + v400 + ((brut - 190000) * 0.20)

elif brut < 1500000:
  vergi = v190 + v400 + v1500 + ((brut - 400000) * 0.27)

elif brut < 5300000:
  vergi = v190 + v400 + v1500 + ((brut - 1500000) * 0.35)

else:
  vergi = v190 + v400 + v1500 + v5300 + ((brut - 5300000) * 0.40)

net = brut - vergi
aylik_brut = brut / 12
aylik_net = net / 12

st.write("Yıllık Brüt", brut)
st.write("Yıllık Net", net)
st.write("Toplam Vergi", vergi)
st.write("Aylık Net", aylik_net)
st.write("Aylık Brüt", aylik_brut)