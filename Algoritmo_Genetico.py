import random

class Algoritmo_Genetico:
    def __init__(self, populacao_inicial, taxa_mutacao, taxa_cruzamento):
        self.populacao = populacao_inicial
        self.taxa_mutacao = taxa_mutacao
        self.taxa_cruzamento = taxa_cruzamento

    def gerarPopulacaoInicial(self, pontos_disponiveis, drone):
        """Gera uma população inicial de rotas aleatórias"""
        # Cria rotas aleatórias utilizando os pontos disponíveis
        self.populacao = [self.criarRotaAleatoria(pontos_disponiveis, drone) for _ in range(100)]

    def criarRotaAleatoria(self, pontos, drone):
        """Cria uma rota aleatória para o drone visitar"""
        rota = Rota()
        random.shuffle(pontos)
        for ponto in pontos:
            rota.adicionarPonto(ponto)
        rota.calcularCustoTotal(drone)
        return rota

    def calcularFitness(self, rota):
        """Atribui um valor de fitness com base no custo e tempo total"""
        # Fitness pode ser o inverso do custo + tempo
        fitness = 1 / (rota.calcularCustoTotal() + rota.calcularTempoTotal())
        return fitness

    def selecionar(self):
        """Seleciona rotas com base no fitness para cruzamento"""
        # Implementação da seleção por torneio
        pass

    def cruzar(self, rota1, rota2):
        """Realiza cruzamento entre duas rotas"""
        # Implementa um cruzamento (por exemplo, ponto único)
        pass

    def mutar(self, rota):git ls-remote origin

        """Realiza mutação na rota para alterar a ordem dos pontos"""
        # Implementa uma mutação (troca de dois pontos na rota)
        pass

    import random

    class Algoritmo_Genetico:
        def __init__(self, populacao_inicial, taxa_mutacao=0.1, taxa_cruzamento=0.8):
            self.populacao = populacao_inicial
            self.taxa_mutacao = taxa_mutacao
            self.taxa_cruzamento = taxa_cruzamento

        def calculoFitness(self, rota):
            """Calcula o fitness com base no custo e tempo total (quanto menor, melhor)"""
            return 1 / (rota.custo_total + rota.tempo_total)  # Fitness inversamente proporcional ao custo e tempo

        def selecionar(self):
            """Seleciona rotas da população com base no fitness"""
            # Seleção por torneio
            torneio = random.sample(self.populacao, 5)
            melhor_rota = max(torneio, key=self.calculoFitness)  # Escolhe a melhor rota do torneio
            return melhor_rota

        def cruzar(self, rota1, rota2):
            """Realiza cruzamento entre duas rotas para criar uma nova rota"""
            ponto_corte = len(rota1.pontos) // 2
            nova_rota = Rota()
            nova_rota.pontos = rota1.pontos[:ponto_corte] + rota2.pontos[ponto_corte:]
            return nova_rota

        def mutar(self, rota):
            """Realiza uma mutação trocando dois pontos na rota para manter diversidade"""
            if random.random() < self.taxa_mutacao:
                indice1, indice2 = random.sample(range(len(rota.pontos)), 2)
                # Troca os pontos
                rota.pontos[indice1], rota.pontos[indice2] = rota.pontos[indice2], rota.pontos[indice1]
