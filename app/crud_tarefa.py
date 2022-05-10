from banco import Banco


class Tarefa:
    def __init__(self, descricao="", situacao="", id=None):
        self.descricao = descricao
        self.situacao = situacao
        self.id = id
        self.tabela = 'tarefas'
        self.insere_campos = '(descricao, situacao)'
        self.atualiza_campos = ('descricao', 'situacao')

    def __str__(self):
        return f"{self.situacao}: {self.descricao}"

    def parametros(self):
        return self.__str__().split(": ")

    def inserir(self):
        try:
            banco = Banco()
            self.id = banco.inserir(self.tabela, self.insere_campos, self.parametros())
            banco.fechar_conexao()
        except Exception as e:
            print(f'\n[x] Falha ao inserir registro [x]: {e}\n')

    def deletar(self):
        try:
            banco = Banco()
            banco.deletar(self.tabela, self.id)
            banco.fechar_conexao()
        except Exception as e:
            print(f'\n[x] Falha ao deletar registro [x]: {e}\n')
    
    def atualizar(self):
        try:
            banco = Banco()
            linhas = banco.atualizar(self.tabela, self.atualiza_campos, self.parametros(), self.id)
            banco.fechar_conexao()
            if linhas == 0:
                raise Exception('Não foi possível atualizar')
            else:
                return True
        except Exception as e:
            print(f'\n[x] Falha ao atualizar registro [x]: {e}\n')
    
    def listar(self):
        banco = Banco()
        tarefas = banco.listar(tabela=self.tabela)
        banco.fechar_conexao()
        return tarefas
