codigo = int(input("Qual o código do produto: "))
quantidadeComprada = int(input("Quantidade comprada: "))


if codigo >= 1 and codigo <= 10:
preco = 10
totalNota = quantidadeComprada * preco
  if totalNota <= 250:
    precoFinal = totalNota * 0.95
    print("O preço final é: R$", precoFinal)
  else:
    print("O preço final é: R$", totalNota)

elif codigo >= 11 and codigo <= 20:
  preco = 15
  totalNota = quantidadeComprada * preco
  if totalNota >= 250 and totalNota <= 500:
    precoFinal = totalNota * 0.90
    print("O preço final é: R$", precoFinal)
  else:
    print("O preço final é: R$", totalNota)

elif codigo >= 21 and codigo <= 30:
  preco = 20
  totalNota = quantidadeComprada * preco
  if totalNota > 500:
    precoFinal = totalNota * 0.85
    print("O preço final é: R$", precoFinal)
  else:
    print("O preço final é: R$", totalNota)

else:
  preco = 30
  totalNota = quantidadeComprada * preco
  print("O preço final é de: R$", totalNota)