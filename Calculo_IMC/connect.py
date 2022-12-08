from tinydb import TinyDB
from model import IMC

bd = TinyDB("Resultado.json")

def inserir(model : IMC):
    bd.insert({"Peso":model.peso,
               "Altura":model.altura,
               "Resultado":model.resultado})
