# O ângulo 6 P2P1P3 é agudo (vértice em P1);
# Os segmentos P1P2 e P1P3 têm o mesmo comprimento;
# Os pontos P2, P3, P4 e P5 são colineares;
# Os pontos médios dos segmentos P2P3 e P4P5 são coincidentes;
# O segmento P2P3 tem comprimento maior que o segmento P4P5;
# Os segmentos P4P6 e P5P7 são perpendiculares ao segmento P2P3;
# Os segmentos P4P6 e P5P7 têm o mesmo comprimento;
# Os pontos P1 e P6 devem estar separados pela reta que contém o segmento P2P3. Formalmente,
#o segmento P1P6 deve interceptar a reta que contém o segmento P2P3 em um único ponto

#7 linhas, a iesima da entrada contem Xi e Yi

linhas = []
for _ in range(7):
  x,y = map(int,input().split())
  