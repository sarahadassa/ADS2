import math

class pontoDaRota:
    def __init__(self, cep, latitude, longitude):
        self.cep = cep
        self.latitude = latitude
        self.longitude = longitude

    def calcularDistancia(self, outro_ponto):
        """Calcula a distância entre dois pontos (em km) usando a fórmula de Haversine"""
        # Implementa a fórmula de Haversine para calcular distância entre coordenadas
        R = 6371  # Raio da Terra em km
        lat1, lon1 = math.radians(self.latitude), math.radians(self.longitude)
        lat2, lon2 = math.radians(outro_ponto.latitude), math.radians(outro_ponto.longitude)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distancia = R * c
        return distancia
