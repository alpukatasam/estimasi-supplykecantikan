import pickle
import streamlit as st

model = pickle.load(open('estimasisupply.sav', 'rb'))

st.title('Estimasi harga supply')
##'Availability','Number of products sold','Stock levels','Lead times','Revenue generated','Order quantities'
##      55    ,           802      ,            58      ,       7    ,  8661.996792392383 , 96
Ketersediaan = st.number_input('Availability Example(55)')
Banyaknya_produk_terjual = st.number_input('Number of products sold Example(802)')
Level_stok = st.number_input('Stock levels Example(58)')
Jumlah_memimpin = st.number_input('Lead times Example(7)')
Pendapatan_dihasilkan= st.number_input('Revenue generated Example(8661.996792392383)')
Banyaknya_permintaan = st.number_input('Order quantities Example(96)')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[Ketersediaan, Banyaknya_produk_terjual, Level_stok, Jumlah_memimpin, Pendapatan_dihasilkan,Banyaknya_permintaan]]
    )
    st.write ('Estimasi Harga : ', predict)