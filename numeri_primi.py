import time
# Test di Fermat
# numeri di Carmichael - evitare falsi positivi

# Test di Miller-Rabin
# Si tratta di un metodo di calcolo veloce, che restituisce un numero inferiore di "falsi positivi" rispetto al test di Fermat.
# Un numero "composto" non restituisce mai un "falso positivo" per più di un quarto dei valori assunti da a

def make_prime(num: int, divisore: int= 0) -> list:
    prime_numbers: list= []
    if divisore != 0:
        num//divisore
    
    for i in range(2, (num) +1):
        prime_numbers.append(i)
    c: int= 0
    for x in range(c, len(prime_numbers)):
        popped_nums: int= 0
        for y in range(len(prime_numbers) -1 -c):
            num1: int = prime_numbers[y +1 +c -popped_nums]
            num2: int = prime_numbers[x]
            temp: int = num1%num2
            if  temp == 0:
                prime_numbers.pop(y +1 +c -popped_nums)
                popped_nums += 1
        c += 1
    print(len(prime_numbers))
    return prime_numbers

def make_prime_andrea(n: int) -> None:
    nums: list = list(range(1, n + 1))
    nums[0] = 0
    for num in nums:
        if num != 0:
            for j in range(num ** 2, len(nums), num):
                nums[j - 1] = 0
    primes = list(filter(lambda num: num != 0, nums))
    # print(primes)

def make_prime_gpt(n: int) -> None:
    nums = list(range(2, n + 1))
    primes = []
    for num in nums:
        if num != 0:
            primes.append(num)
            for j in range(num ** 2, n + 1, num):
                nums[j - 2] = 0
            
# start1 = time.time()    
# make_prime_andrea(1_000_000)  
# print(f"{time.time() - start1} -- PRIMA VERSIONE")

start1 = time.time()    
make_prime_gpt(1_000_000_000)  
print(f"{time.time() - start1} -- VERSIONE GPT")
                

        
# start1 = time.time()
# make_prime(100000)
# print(f"{time.time() - start1} -- VERSIONE MIGLIORE")