import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Lamine Yamal
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Dribles e Retenção)', 
    'Velocidade Máxima<br>(Aceleração e Sprints)', 
    'Chances de Gol<br>(Criação de Chances e xG)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
valores_grafico = [92, 86, 90]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Alta retenção (Média de 5.2 dribles tentados/jogo)", 
    "33.5 km/h de pico (Aceleração rápida no 1v1)", 
    "0.82 xG+xA (Líder em passes decisivos da ponta)"
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
    fillcolor='rgba(138, 43, 226, 0.3)',  # Tom azul/roxo vibrante
    line=dict(color='blueviolet', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Lamine Yamal'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Lamine Yamal",
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
        bgcolor='rgb(18, 20, 28)' # Fundo escuro estilo dashboard profissional
    ),
    paper_bgcolor='rgb(18, 20, 28)',
    showlegend=False,
    width=700,
    height=600
)

# 4. Execução do script
if __name__ == '__main__':