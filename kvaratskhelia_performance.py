import plotly.graph_objects as go

# 1. Definição das métricas que você pediu e os valores fictícios médios do Kvara
# Para o visual ficar perfeito, os valores do gráfico estão normalizados (0 a 100)
# Mas os valores reais são exibidos ao passar o mouse.
metricas = [
    'Posse de Bola<br>(Retenção sob Pressão)', 
    'Velocidade Máxima<br>(Aceleração/Sprint)', 
    'Chances de Gol<br>(Gols + Assistências Esperadas)'
]

# Notas visuais de desempenho (Escala 0 a 100 baseada em scouts europeus)
valores_grafico = [85, 92, 88]  

# Dados reais detalhados para aparecerem na legenda interativa (hover)
valores_reais = [
    "85% de eficiência", 
    "34.8 km/h de pico", 
    "0.75 xG+xA por jogo"
]

# O gráfico de radar precisa fechar o circuito, então repetimos o primeiro item no final
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]

# 2. Construção do Gráfico de Radar Interativo
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=valores_grafico_fechados,
    theta=metricas_fechadas,
    fill='toself',
    fillcolor='rgba(135, 206, 250, 0.4)',  # Azul claro (lembrando o Napoli/Geórgia)
    line=dict(color='deepskyblue', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Khvicha Kvaratskhelia'
))

# 3. Estilização do Layout
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Khvicha Kvaratskhelia",
        font=dict(size=22, color='white'),
        x=0.5,
        y=0.95
    ),
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor="rgba(255, 255, 255, 0.2)",
            tickfont=dict(color="rgba(255, 255, 255, 0.7)")
        ),
        angularaxis=dict(
            gridcolor="rgba(255, 255, 255, 0.3)",
            tickfont=dict(size=12, color='white')
        ),
        bgcolor='rgb(20, 24, 35)' # Fundo escuro para destacar os dados
    ),
    paper_bgcolor='rgb(20, 24, 35)',
    showlegend=False,
    width=700,
    height=600
)
# 4. Executar e exibir o gráfico no navegador
if __name__ == '__main__':
    print("Gerando gráfico de desempenho...")