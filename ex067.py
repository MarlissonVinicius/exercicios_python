while True:
    num = int(input("\nDigite um valor para ver sua tabuada: ",))
    if num <=0:
        break
    for i in range(1,11):
           print(f"{num}x{i}={num*i}")
     