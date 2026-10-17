import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Erling Haaland (Champions 2026)
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Retenção Direta, Pivô e Eficiência)', 
    'Velocidade Máxima<br>(Arrancadas em Transição e Pique)', 
    'Chances de Gol<br>(Finalizações, Conversão e xG na UCL)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados da Champions League 2026)
# Haaland atinge pontuação máxima em conversão de chances e destaque físico em velocidade.
valores_grafico = [74, 95, 99]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção objetiva (Foco em poucos toques, proteção de corpo e tabelas rápidas)", 
    "35.8 km/h de pico (Velocidade devastadora em contra-ataques na Europa)", 
    "1.34 xG por jogo (Líder em volume de finalizações e conversão letal na Champions)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]

# 2. Construção do Gráfico de Radar Interativo
fig = go.Figure()

