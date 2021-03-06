# Definicao da classe Ocorrencia
class Ocorrencia(object):
    def __init__(self, nomeOcorrencia, tipo, prioridade, status, resumo):
        self.nomeOcorrencia = nomeOcorrencia
        self.tipo = tipo
        self.prioridade = prioridade
        self.status = status
        self.resumo = resumo
        self.responsavel = None
        self.ID = 0

    def __del__(self):
        return 1

    def getNomeOcorrencia(self):
        return self.nomeOcorrencia

    def getTipoOcorrencia(self):
        return self.tipo

    def getPrioridade(self):
        return self.prioridade

    def getStatus(self):
        return self.status

    def getResumo(self):
        return self.resumo

    def getResponsavel(self):
        return self.responsavel

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def setResponsavel(self,funcionario):
        if(self.status == "Aberta"):
            self.responsavel = funcionario

    def setPrioridadeBaixa(self):
        if(self.status == "Aberta"):
            self.prioridade = "Baixa"

    def setPrioridadeMedia(self):
        if(self.status == "Aberta"):
            self.prioridade = "Media"

    def setPrioridadeAlta(self):
        if(self.status == "Aberta"):
            self.prioridade = "Alta"

    def finalizaOcorrencia(self):
        self.status = "Fechada"