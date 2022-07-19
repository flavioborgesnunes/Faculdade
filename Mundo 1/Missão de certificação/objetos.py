class ferramentas: 
   '''
   Classe ferramentas
   '''
   def __init__(self, Id_ferramentas, descricao, fabricante, volts, number, tamanho, medida, tipo, material, tempo ):
        '''
        Construtor classe ferramentas
        :param Id_ferramentas: código interno, gerado pelo sistema
        :descricao: texto livre contendo principais informações de identificação 
        :fabricante: qual a marca da fabricante
        :volts: voltagem de uso
        :number: número que identifica a ferramenta pelo fabricante 
        :tamanho: informações em número, especifica o tamanho do equipamento
        :medida: unidade de medida, cm, polegadas, metros
        :tipo: tipo de ferramenta elétrica, mecânica, segurança, etc.
        :material: material da ferramenta, ferro, madeira, borracha, plástico etc
        :tempo: tempo máximo de reserva
        '''
        self.Id_ferramentas = Id_ferramentas
        self.descricao = descricao
        self.fabricante = fabricante
        self.volts = volts
        self.number = number
        self.tamanho = tamanho
        self.medida = medida
        self.tipo = tipo
        self.material = material
        self.tempo = tempo