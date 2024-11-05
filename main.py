from Drone import Drone
from pontoDaRota import pontoDaRota
from Rota import Rota
from Algoritmo_Genetico import Algoritmo_Genetico

if __name__ == "__main__":
    # Instanciar um drone
    drone = Drone()

    # Instanciar pontos de rota
    ponto1 = pontoDaRota("82821020", -25.4284, -49.2733)
    ponto2 = pontoDaRota("80010010", -25.4429, -49.2769)

    # Calcular distância entre dois pontos
    distancia = ponto1.calcularDistancia(ponto2)
    print(f"Distância entre ponto1 e ponto2: {distancia:.2f} km")

    # Criar uma rota e adicionar pontos
    rota = Rota()
    rota.adicionarPonto(ponto1)
    rota.adicionarPonto(ponto2)

    # Calcular custo e tempo da rota (métodos a serem completados)
    custo = rota.calcularCustoTotal(drone)
    tempo = rota.calcularTempoTotal(drone)
    print(f"Custo total da rota: R${custo}")
    print(f"Tempo total da rota: {tempo} segundos")




