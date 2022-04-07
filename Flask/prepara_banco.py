import MySQLdb

print('Conectando...')

conexao = MySQLdb.connect(user='root', passwd='EnsiferuM1', host='127.0.0.1', port=3306)

print('Conectou')

# Descomente se quiser desfazer o banco...
conexao.cursor().execute("DROP DATABASE IF EXISTS `jogoteca`;")
criar_tabelas = '''CREATE DATABASE `jogoteca`;

    USE `jogoteca`;

    CREATE TABLE `jogo` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
    );

    CREATE TABLE `usuario` (
      `id` varchar(8) NOT NULL,
      `nome` varchar(20) NOT NULL,
      `senha` varchar(8) NOT NULL,
      PRIMARY KEY (`id`)
    );
'''

conexao.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conexao.cursor()
cursor.executemany(
    'INSERT INTO jogoteca.usuario (id, nome, senha) VALUES (%s, %s, %s)',
    [
        ('luan', 'Luan Marques', 'flask'),
        ('nico', 'Nico', '7a1'),
        ('danilo', 'Danilo', 'vegas')
    ])

cursor.execute('select * from jogoteca.usuario')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
cursor.executemany(
    'INSERT INTO jogoteca.jogo (nome, categoria, console) VALUES (%s, %s, %s)',
    [
        ('God of War 4', 'Ação', 'PS4'),
        ('NBA 2k18', 'Esporte', 'Xbox One'),
        ('Rayman Legends', 'Indie', 'PS4'),
        ('Super Mario RPG', 'RPG', 'SNES'),
        ('Super Mario Kart', 'Corrida', 'SNES'),
        ('Fire Emblem Echoes', 'Estratégia', '3DS'),
    ])

cursor.execute('select * from jogoteca.jogo')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando senão nada tem efeito
conexao.commit()
cursor.close()
