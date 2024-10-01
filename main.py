import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(layout="wide")
st.title("Coffee Shop Sales☕")



# Qual a catedoria de produto que traz a maior receita? ok
# Qual o produto mais vendido? ok 
# Qual a receita media por cada tipo de produto? e por região?
# Quais lojas que trazem mais ou menos receita?

# Adicionando CSS personalizado para mudar a cor de fundo para marrom claro

df= pd.read_excel("CoffeeShopSales.xlsx")


col1, col2 = st.columns(2)
col3, col4,col5 = st.columns(3)
marrom_palette = ['#8B4513', '#A0522D', '#D2691E', '#DEB887']

# Qual a catedoria de produto que traz a maior receita? 
fig_cate = px.bar(df, x="product_category", y="transaction_qty", title="Faturamento por categoria",color_discrete_sequence = marrom_palette)
col1.plotly_chart(fig_cate, use_container_width=True)

# Qual o produto mais vendido?

qtd_venda_produto = df.groupby("product_type")["transaction_qty"].sum()

top_3_produtos = qtd_venda_produto.sort_values(ascending= False).head(3).reset_index()

fig_top3 = px.bar(top_3_produtos, x= "product_type", y = "transaction_qty",
 title = "Top 3 produtos mais vendido", color_discrete_sequence = marrom_palette )
col2.plotly_chart(fig_top3,use_container_width=True )


# Qual a receita media por cada tipo de produto?  

df["receita"]= df["transaction_qty"]*df["unit_price"]
receita_media_produto = df.groupby("product_type")["receita"].mean().reset_index()
fig_media_prod = px.bar(receita_media_produto, x= "product_type", y= "receita", title= "Receita média por tipo de produto", color_discrete_sequence= marrom_palette)
col3.plotly_chart(fig_media_prod, use_container_width=True)

# e por região?

receita_media_regiao = df.groupby("store_location")["receita"].mean().reset_index()
fig_media_regiao = px.bar(receita_media_regiao, x = "store_location", y ="receita", title="Receita média por Região", color= "store_location",color_discrete_sequence= marrom_palette)
col5.plotly_chart(fig_media_regiao, use_container_width=True)

# Quais lojas que trazem mais ou menos receita?

total_receita_loja = df.groupby("store_location")["receita"].sum().reset_index()
fig_receita_loja = px.pie(total_receita_loja, values= "receita", names= "store_location", title= "Distribuição da Receita Total por Loja", color_discrete_sequence= marrom_palette)
col4.plotly_chart(fig_receita_loja, use_container_width=True)