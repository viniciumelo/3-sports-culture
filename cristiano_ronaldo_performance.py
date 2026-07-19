import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Cristiano Ronaldo
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Toques na Área/Retenção)', 
    'Velocidade Máxima<br>(Aceleração/Sprints)', 
    'Chances de Gol<br>(Gols Esperados - xG e Volume)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada no perfil analítico do jogador)
# CR7 pontua no topo histórico em finalização e volume de chances, mantendo boa velocidade e menor retenção de bola.
valores_grafico = [68, 88, 97]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Foco em definição (Poucos toques, alta eficiência)", 
    "34.2 km/h de pico (Sprints verticais)", 
    "0.95 xG (Volume extremo de finalizações)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]