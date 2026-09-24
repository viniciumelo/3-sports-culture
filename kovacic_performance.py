import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Mateo Kovačić
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Condução Progressiva e Retenção)', 
    'Velocidade Máxima<br>(Agilidade e Transição em Condução)', 
    'Chances de Gol<br>(Passes Decisivos e Construção)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Kovačić pontua extremamente alto em retenção e condução de posse sob pressão.
valores_grafico = [93, 84, 68]