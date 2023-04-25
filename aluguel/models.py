from django.db import models

# Create your models here.
class Carro(models.Model):
    placa = models.CharField("Carro",max_length=7, primary_key=True)
    marca = models.CharField("Marca",max_length=150)
    ano = models.CharField("Ano",max_length=7)
    modelo = models.CharField("Modelo",max_length=150)
    data_compra = models.DateField("Data de Compra")

    def __str__(self):
        return self.modelo
    


class Cliente(models.Model):
    cpf = models.CharField("CPF",max_length=15, primary_key=True)
    nome = models.CharField("Nome",max_length=250)
    telefone = models.CharField("Telefone",max_length=50)
    data_nascimento = models.DateField("Data de Nascimento")
    endereco = models.CharField("Endereço",max_length=150)

    def __str__(self):
        return "{}".format(self.nome)
    

class Aluguel(models.Model):
    codigo = models.AutoField("Codigo",primary_key=True, unique=True)
    data_alugel = models.DateField()
    data_entrega = models.DateField()
    valor = models.DecimalField("Valor", max_digits=15, decimal_places=2)
    devolucao = models.BooleanField("Devolvido")
    diaria = models.DecimalField("Diaria",max_digits=10, decimal_places=2)
    placa = models.ForeignKey(Carro, on_delete=models.CASCADE, verbose_name="Carro")
    cpf = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, related_name='cliente_alugueis')

    def __str__(self):
        return "{} - {} - {}".format(self.codigo, self.cliente.nome, self.carro.modelo)
    