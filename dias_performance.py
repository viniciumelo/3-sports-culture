import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Rúben Dias
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Saída de Bola e Volume de Passe)', 
    'Velocidade Máxima<br>(Recuperação e Cobertura)', 
    'Chances de Gol<br>(Cabeceio e Passes Progressivos)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados analíticos da Premier League)
valores_grafico = [93, 83, 62]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Construção de elite (Média de 85+ toques/jogo e 93% de acerto de passe)", 
    "33.1 km/h de pico (Excelente timing de desarme e recuperação)", 
    "0.18 xG+xA (Presença em escanteios e lançamento longo)"
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
    fillcolor='rgba(100, 149, 237, 0.3)',  # Tom azul celeste (referência ao City e Portugal)
    line=dict(color='royalblue', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Rúben Dias'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Rúben Dias",
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
        bgcolor='rgb(16, 20, 26)' # Fundo escuro estilo dashboard profissional
    ),
    paper_bgcolor='rgb(16, 20, 26)',
    showlegend=False,
    width=700,
    height=600
)

# 4. Execução do script
if __name__ == '__main__':
    print("Gerando gráfico de desempenho do Rúben Dias...")
    fig.show()