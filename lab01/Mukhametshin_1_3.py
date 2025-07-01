name = "John Smith"
amount = 350_000
result = 376_250
n = result / amount * 100 - 100
print("Client name: {}\n"
      "Initial deposit amount: {} $\n"
      "Interest rate: {:.2f} % per annum and total deposit amount: {} $".format(name, amount, n, result))