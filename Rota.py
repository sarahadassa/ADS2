class Rota:
    def __init__(self):
        self.pontos = []      # Lista de pontos (PontoRota) na rota
        self.custo_total = 0  # Custo total da rota
        self.tempo_total = 0  # Tempo total da rota em segundos

    def adicionarPonto(self, ponto):
        """Adiciona um novo ponto de parada para o drone"""
        self.pontos.append(ponto)

    def calcularCustoTotal(self, drone):
        """Calcula o custo total incluindo paradas para recarga"""
        custo_total = 0
        for i in range(1, len(self.pontos)):
            origem = self.pontos[i - 1]
            destino = self.pontos[i]
            distancia = origem.calcularDistancia(destino)
            if drone.bateria < distancia:
                custo_total += drone.pousar()  # Adiciona custo de recarga
            drone.bateria -= distancia  # Ajuste da bateria
            custo_total += drone.bateria
        self.custo_total = custo_total
        return self.custo_total

    def calcularTempoTotal(self, drone):
        """Calcula o tempo total de voo e paradas"""
        tempo_total = 0
        for i in range(1, len(self.pontos)):
            origem = self.pontos[i - 1]
            destino = self.pontos[i]
            tempo_voo = origem.calcularDistancia(destino) / drone.velocidade_base * 3600
            if tempo_voo > drone.autonomia_base:
                drone.pousar()
                tempo_total += 60  # Acrescenta tempo de recarga
            tempo_total += tempo_voo
        self.tempo_total = tempo_total
        return self.tempo_total

    class Rota:
        def __init__(self):
            self.pontos = []  # Lista de pontos (PontoRota) na rota
            self.custo_total = 0  # Custo total da rota
            self.tempo_total = 0  # Tempo total da rota em segundos

        def adicionarPonto(self, ponto):
            """Adiciona um novo ponto de parada para o drone"""
            self.pontos.append(ponto)

        def calculoDoCustoTotal(self, drone):
            """Calcula o custo total, incluindo paradas para recarga"""
            custo_total = 0
            for i in range(1, len(self.pontos)):
                origem = self.pontos[i - 1]
                destino = self.pontos[i]
                distancia = origem.calcularDistancia(destino)
                # Cálculo do consumo de bateria para o percurso
                bateria_necessaria = distancia * (drone.bateria / drone.velocidade_base)

                # Verifica se há necessidade de recarga
                if drone.bateria < bateria_necessaria:
                    custo_total += drone.pousar()  # Adiciona o custo de recarga
                drone.bateria -= bateria_necessaria  # Ajuste do nível de bateria após voo

            self.custo_total = custo_total
            return self.custo_total

        def calculoDoTempoTotal(self, drone):
            """Calcula o tempo total de voo e paradas"""
            tempo_total = 0
            for i in range(1, len(self.pontos)):
                origem = self.pontos[i - 1]
                destino = self.pontos[i]
                # Calcula o tempo para o voo
                tempo_voo = origem.calcularDistancia(destino) / drone.velocidade_base * 3600

                # Verifica se precisa pousar para recarregar
                if tempo_voo > drone.bateria:
                    tempo_total += 60  # Tempo de recarga
                    drone.pousar()

                tempo_total += tempo_voo  # Acumula o tempo de voo

            self.tempo_total = tempo_total
            return self.tempo_total
