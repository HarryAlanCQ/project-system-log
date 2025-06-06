import hashlib
import json

#PARA REGISTRARSE
usuario = input('Introduce un usuario: ')
contraseña = input('Introduce una contraseña: ')

hash = hashlib.sha512(contraseña.encode()).hexdigest()

todo = [
    {'Usuario':usuario, 'Hash': hash}
]

with open('../../Desktop/usuarios.json', 'w+') as f:
    json.dump(todo, f, indent=4)

#PARA LOGEARSE
registro_usuario = input('Introduce tu usuario: ')
registro_contraseña = input('Introduce tu contraseña: ')

registro_hash = hashlib.sha512(registro_contraseña.encode()).hexdigest()

acceso_concedido = False

with open('../../Desktop/usuarios.json', 'r') as f:
    todo = json.load(f)
    
    for usuario_data in todo:
        if usuario_data['Usuario'] == registro_usuario and usuario_data['Hash'] == registro_hash:
            acceso_concedido = True
            break

if acceso_concedido:
    print('Acceso concedido')
else:
    print('Acceso denegado')
    
    