import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Luka Modrić
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Retenção, Controle e Passe)', 
    'Velocidade Máxima<br>(Aceleração Curta e Agilidade)', 
    'Chances de Gol<br>(Key Passes, Trivelas e xA)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados analíticos)
# Modrić registra topo de elite global em retenção de posse e criação de jogadas.
valores_grafico = [96, 72, 88]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção de elite (Média de 75+ toques/jogo e 91% de acerto de passe)", 
    "31.0 km/h de pico (Inteligência espacial e leitura de jogo)", 
    "0.75 xG+xA (Líder em passes decisivos e quebra de linhas)"
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
))
