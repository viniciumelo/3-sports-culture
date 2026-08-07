mport plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Manuel Neuer
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Jogo com os Pés e Saída)', 
    'Velocidade Máxima<br>(Cobertura Fora da Área)', 
    'Chances de Gol<br>(Gols Evitados e Lançamentos)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada no histórico do atleta)
# Neuer revolucionou a posição com notas altíssimas para um goleiro em passe e saídas da área.
valores_grafico = [92, 80, 94]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Precisão de passe de linha (Média de 88% de acerto no passe)", 
    "31.2 km/h de pico (Ação como líbero/sweeper)", 
    "Elite em xG Evitado (Altíssima taxa de defesas difíceis)"
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
    fillcolor='rgba(46, 139, 87, 0.3)',  # Tom verde (referência ao Bayern e Alemanha)
    line=dict(color='seagreen', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Manuel Neuer'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Manuel Neuer",
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
        bgcolor='rgb(15, 22, 18)' # Fundo escuro focado no tema verde
    ),
)
