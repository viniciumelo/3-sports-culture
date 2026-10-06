import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Jonas Urbig
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Jogo com os Pés e Saída Curta)', 
    'Velocidade Máxima<br>(Saídas Explosivas e 1v1)', 
    'Chances de Gol<br>(Prevenção de Gols e xG Prevented)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada no perfil e scout do atleta)
# Urbig é avaliado como um jovem goleiro com excelente técnica com os pés e ótima agilidade.
valores_grafico = [87, 82, 89]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Alta precisão com os pés (Média de 84%+ de acerto na distribuição)", 
]
