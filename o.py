'''class Retangulo:
      largura = 10
      altura = 10
      def __init__(self, a, b):
            self.largura = a
            self.altura = b
      def getd(self):
            d = "Largura: {}\nAltura: {}" .format(self.largura, self.altura)
            return d
      def geta(self):
            a = "Aréa: {}" .format(self.largura*self.altura)
            return a
r = Retangulo(5, 3)

print(r.getd()+"\n"+r.geta())

r.altura = 50

print(r.getd()+"\n"+r.geta())
'''

class Conta:
      __saldo = 0
      def __init__ (self):
            self.__saldo = 0
            self.extrato = list()
            self.extrato.append(self.__saldo)
      def depositar(self, a):
            self.__saldo = self.__saldo + a
            self.extrato.append(a)
            return "Depósito realizado."
      def sacar(self, b):
            if b > self.__saldo: 
                  return "Saldo insuficiente."
            else:
                  self.__saldo = self.__saldo - b
                  self.extrato.append(-b)
                  return "Saque realizado."
      def getextrato(self):
            s = list()
            d = list()
            i = self.extrato[0]
            for u in self.extrato:
                  if u > 0:
                        d.append(u)
                  elif u < 0:
                        s.append(u)
            return "Valor inicial: {}\nDepositos: {}\nSaques: {}" .format(i, d, s)

      def getsaldo(self):
            return "Saldo Total: R$ {},00" .format(self.__saldo)

akim_de_paula = Conta()
akim_de_paula.depositar(8000)
akim_de_paula.depositar(50000)
akim_de_paula.sacar(2)
print(akim_de_paula.getsaldo())


