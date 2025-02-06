class FilaDeImpressao: 

    def configurar_inicial(self): 
        self.fila=[]

    def adicionar_trabalho(self, trabalho):
        self.fila.append(trabalho)
        print (f"trabalho '{trabalho}' adicionando a fila de impressao ")

    def processar_trabalho(self): 
        if not self.esta_vazia():
            trabalho = self.fila.pop(0) #remove o 1 da fila
            print(f"o trabalho '{trabalho}' esta sendo processado")
        else:
            print ("a fila esta vazia!")

    def mostrar_fila(self):
        if self.esta_vazia():
            print("A fila esta vazia!")
        else: 
            print ("fila atual de impressao:")
            for trabalho in self.fila:
                print(f"-{trabalho}")  

    def esta_vazia(self): 
        return len(self.fila) == 0              


def menu():
    fila_impressao=FilaDeImpressao()
    fila_impressao.configurar_inicial()

    while True:
        print ("opcoes:")
        print ("1 adicionarum trabalho na fila de impressao")
        print ("2 imprimir o proximo trabalho da fila")
        print ("3 Mostrar a fila de impressao")
        print ("4 sair")
        escolha=input("escolha uma opcao 1-4")
        #aqui vai ser lido a escolha do usuario

        if escolha=="1":
           trabalho = input ("digite o nome do trabalho a ser impresso")
           fila_impressao.adicionar_trabalho(trabalho)
        elif escolha=="2":     
            fila_impressao.processar_trabalho()
        elif escolha=="3":
            fila_impressao.mostrar_fila()
        elif escolha=="4" :
            print("saindo do programa")
            break
        else:          
            print ("opcao invalida")

menu()