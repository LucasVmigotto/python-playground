# Print para exibição em console
print("Hello World")

# Alocação de valor a variável
hello = "Hello World"
print(hello)

# Recebimento de input do usuário
print("Type a message:")
message = input()
print(message)

# Exibição de mensagem com variáveis por concatenação em String
## Usa-se o operador %f para valores de Double
double = 3.14
print("The pi value it's almost %f" %(double))

## Usa-se o operador %s para valores de String
string = "text"
print("String it's usually used to print %s" %(string))

## Usa-se o operador %d para valores de Integer
integer = 7
print("I was born in February %dth" %(integer))

# Condicionais
## If simples
isTrue = 2 > 1
if isTrue:
    print("If the math stills the same, you should see this...")

## If + Else
if not(isTrue):
    print("If the math stills the same, you should see this...")
else:
    print("Bad news... Someone broke the math...")

## If composto
if 1 > 2:
    print("1 it's greater than 2 (Something is wrong)")
elif 1 == 2:
    print("2 it's equal to 1 (Something still wrong...)")
else:
    print("1 it's less than 2 (Now you got it)")

# Loop
## While loop
i = 0
while i < 10:
    print("%d it's less than 10, this will be logged" %(i))
    i += 1

## For loop
for count in range(1, 10):
    print("Step %d" %(count))

# Arrays, Lists e Estruturas de Dados
## Arrays

### Arrays em Python são zero-indexados
myFirstArray = [
    1, 2, 3, 4, 5, 6, 7
]

### Exibição de valores de array
print("The first element of the array should be 1: %d"%(myFirstArray[0]))

## Listas com chave-valor (key-value)
person = {
    "name": "John Doe",
    "age": 21,
    "phone": "9999-9999"
}

### Consumo de valores
print("Hello, my name is %s" %(person["name"]))
print("I'm %d years old" %(person["age"]))
print("My phone is %s" %(person["phone"]))

for key, value in person.items():
    print("Attribute: %s --> Key: %s" %(key, value))
