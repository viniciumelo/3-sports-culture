import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Yuri Alberto
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Retenção, Pivô e Movimentação)', 
    'Velocidade Máxima<br>(Arrancadas e Rupturas em Profundidade)', 
    'Chances de Gol<br>(Finalizações, Infiltrações e xG)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Yuri Alberto pontua muito bem em velocidade de transição ofensiva e volume de finalização.
valores_grafico = [76, 89, 85]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Participação direta (Média de toques sob pressão e trabalho de pivô)", 
    "33.8 km/h de pico (Excelente explosão em diagonais e contrataques)", 
    "0.62 xG por jogo (Alto volume de finalizações e presença constante na área)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]

# 2. Construção do Gráfico de Radar Interativo
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=valores_grafico_fechados,
    theta=metricas_fechadas,
    fill='toself',
    fillcolor='rgba(0, 0, 0, 0.4)',  # Tom preto/branco clássico (referência ao Corinthians)
    line=dict(color='white', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Yuri Alberto'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Yuri Alberto",
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
        bgcolor='rgb(16, 20, 28)' # Fundo escuro estilo dashboard profissional
    ),
    paper_bgcolor='rgb(16, 20, 28)',
    showlegend=False,
    width=700,
    height=600
)

# 4. Execução do script
if __name__ == '__main__':
    print("Gerando gráfico de desempenho do Yuri Alberto...")
    fig.show()