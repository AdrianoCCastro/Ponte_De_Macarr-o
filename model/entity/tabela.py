# import things
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    identificador = Col('#')
    tipo = Col('Tipo de Esforço')
    esforco_interno = Col('Esforco Interno')
    comprimento = Col('Comprimento')
    qtd_fios = Col('Qtd de fios')

# Get some objects
class Barra(object):
    def __init__(self,identificador, tipo, esforco_interno,comprimento ,qtd_fios):
        self.identificador = identificador
        self.tipo = tipo
        self.esforco_interno = esforco_interno
        self.comprimento = comprimento
        self.qtd_fios = qtd_fios





          