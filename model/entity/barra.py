class Barra():
    def __init__(self,esforco_interno,tipo ,comprimento) -> None:
        self.esforco_interno = esforco_interno
        self.tipo = tipo
        self.comprimento = self.converte_em_centimetro(comprimento)
        self.qts_fios_de_macarrao = 0

    def converte_em_centimetro(self,comprimento):
        return comprimento * 10
        