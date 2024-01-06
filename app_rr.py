import pandas as pd
import streamlit as st
import webbrowser as wb


df=pd.read_excel('produtos_rr.xlsx')
df.head(1)

tipos=df['Tipo'].unique()
tipo=st.selectbox(label='Combo, Salgada ou Copinho?',
                  options=tipos)
df_tipo=df[df['Tipo']==tipo]


produtos=df_tipo['Produto'].unique()
produto=st.selectbox('Qual sabor você quer?',
                     options=produtos)
df_produto=df_tipo[df_tipo['Produto']==produto].iloc[0]

link_produto=df_produto['links']

st.image(df_produto['fotos'])

st.title(df_produto['Produto'])

st.markdown(df_produto['descrição'])

if st.button(label='Ver no cardápio',type='secondary'):
    wb.open(link_produto)

st.progress(df_produto['Preferência dos Clientes'],
            text='Quanto essa esfiha é pedida no nosso cardápio')

col1,col2,col3=st.columns(3)


col1.metric(label='Preço',value=f"{df_produto['Preço']:.2f}")
col2.metric(label='Melhor Preço',value=f"{df_produto['Melhor Preço']:.2f}")

col3.subheader(f"Melhor dia pra compra : {df_produto['Melhor Dia pra Compra']}")

st.sidebar.image('img/RR Esfihas - Logotipo A.png')

if st.sidebar.button(label='Cardápio Digital',type='primary'):
    wb.open('https://app.cardapioweb.com/rr_esfihas')
