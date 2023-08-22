"""Documentação do Módulo

Blá-Blá-Blá

"""

# Função que calcula montante e juros em um regime de juros simples
#Type Hint: MyPy (MONITORES VÃO TRABALHAR COM ISSO)
def juros_simples(capital: int, taxa: int, tempo: int) ->tuple :
  """Cálculo de Juros Simples
  Parametros
  ----------
  capital: int
    bábábá
  taxa: float
    bábábá
  tempo: int
    bábábá
  """
  juros = capital * (taxa/100) * tempo
  montante = capital + juros

  # TODO: alterar estrutura de dados de retorno para lista
  # FIXME & BUG:

  return (montante, juros)

def juros_compostos(capital, taxa, tempo):
  """Cálculo de Juros Compostos
  Parametros
  ----------
  capital: int
    bábábá
  taxa: float
    bábábá
  tempo: int
    bábábá
  """
  montante = capital *(pow((1 + taxa/100), tempo))
  juros = montante - capital

  return (round(montante,2), round(juros,2))