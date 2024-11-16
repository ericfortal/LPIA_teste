def area_triangulo(a, b, c):
  """Calcula a área de um triângulo utilizando a fórmula de Heron.

  Args:
    a: Comprimento do primeiro lado.
    b: Comprimento do segundo lado.
    c: Comprimento do terceiro lado.

  Returns:
    A área do triângulo, ou uma mensagem de erro caso os lados não formem um triângulo.
  """

  # Verificando se os lados formam um triângulo
  if a + b <= c or a + c <= b or b + c <= a:
    return "Os lados não formam um triângulo."

  # Calculando o semiperímetro
  s = (a + b + c) / 2

  # Calculando a área (usando a operação de exponenciação **0.5 para simular a raiz quadrada)
  area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

  return area

# Pedindo as medidas dos lados ao usuário
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Calculando e imprimindo a área
resultado = area_triangulo(lado1, lado2, lado3)
print("A área do triângulo é:", resultado)