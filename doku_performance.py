import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Jérémy Doku
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Dribles, Condução e Retenção)', 
    'Velocidade Máxima<br>(Aceleração e Sprints Explosivos)', 
    'Chances de Gol<br>(Cruzamentos, Key Passes e xA)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Doku registra nota máxima em aceleração/velocidade e números altíssimos em retenção por drible.
valores_grafico = [94, 98, 81]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção por drible (Média de 6.8 dribles certos/jogo e 1v1 dominante)", 
    "35.3 km/h de pico (Explosão e aceleração de elite)", 
    "0.65 xG+xA (Volume alto de assistências e passes para a grande área)"
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
    fillcolor='rgba(135, 206, 235, 0.3)',  # Tom azul celeste (referência ao Man City / Bélgica)
    line=dict(color='deepskyblue', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Jérémy Doku'
))