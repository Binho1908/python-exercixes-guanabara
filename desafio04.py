e = input('Digite algo = ')
print(f'Typo primitivo {type(e)}')
print(f'Só tem espaços? {e.isspace()}')
print(f'É um número? {e.isnumeric()}')
print(f'É alfabetio? {e.isalpha()}')
print(f'É alfanumerico? {e.isalnum()}')
print(f'Está maiúsculo? {e.isupper()}')
print(f'Está minúsculo? {e.islower()}')
print(f'Está capitalizado? {e.istitle()}')
