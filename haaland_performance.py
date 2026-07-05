import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Haaland
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Toques na Área/Retenção)', 
    'Velocidade Máxima<br>(Sprints de Explosão)', 
    'Chances de Gol<br>(Gols Esperados - xG)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados reais da Premier League)
# Haaland se destaca absurdamente em finalização e velocidade, tendo menos participação na posse.
valores_grafico = [65, 95, 98]  

# Dados reais detalhados que aparecem ao passar o mouse
valores_reais = [
    "Poucos toques (Geralmente < 25 por jogo)", 
    "36.2 km/h de pico", 
    "0.98 xG (Chances claras por jogo)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]

