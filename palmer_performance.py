import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Cole Palmer
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Passe, Retenção e Controle)', 
    'Velocidade Máxima<br>(Aceleração e Deslocamento)', 
    'Chances de Gol<br>(Gols, Assistências e xG+xA)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Palmer registra notas altíssimas em criação/conversão de chances e retenção, com velocidade moderada.
valores_grafico = [90, 78, 95]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção de elite (Média de 55+ toques e controle de ritmo)", 
    "32.8 km/h de pico (Foco em leitura espacial)", 
    "0.88 xG+xA (Volume absurdo de participação em gols)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]