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
]
