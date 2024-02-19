formas = [0] * 11
formas[0] = 1
print("Formas de llegar al escalon 0: 0")
for i in range(1, 11):
    formas[i] = formas[i-1] + formas[i-2] + formas[i-3]
    print(f"Formas de llegar al escalon {i}: {formas[i]}")

