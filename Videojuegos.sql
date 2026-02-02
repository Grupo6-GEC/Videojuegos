CREATE DATABASE IF NOT EXISTS videojuegos_db;
USE videojuegos_db;
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(100) NOT NULL,
    clave VARCHAR(255) NOT NULL,
    perfil ENUM('admin', 'user') NOT NULL DEFAULT 'user'
 );

CREATE TABLE videojuegos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    foto VARCHAR(255), -- ruta de la foto o URL
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    creador VARCHAR(100),
    ruta_foto VARCHAR(255),
    tienda VARCHAR(100)
);

CREATE TABLE comentarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_videojuego INT NOT NULL,
    id_usuario INT NOT NULL,
    contenido TEXT NOT NULL,
    FOREIGN KEY (id_videojuego) REFERENCES videojuegos(id) ON DELETE CASCADE,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE lista_token_baneado (
    token_hash CHAR(64) PRIMARY KEY,
    token TEXT NOT NULL,
    expiracion TIMESTAMP NOT NULL
);
INSERT INTO usuarios (usuario, clave, perfil) VALUES
('alice', 'alice123', 'user'),
('bob', 'bob123', 'user'),
('charlie', 'charlie123', 'user'),
('diana', 'diana123', 'user'),
('eve', 'eve123', 'user'),
('root','/somosunoschulos$123', 'admin');

INSERT INTO videojuegos (nombre, foto, descripcion, precio, creador, ruta_foto, tienda) VALUES
('Elden Ring', 'eldenring.jpg', 'RPG de mundo abierto con mucha exploración', 59.99, 'FromSoftware', '/imagenes/eldenring.jpg', 'Steam'),
('Minecraft', 'minecraft.jpg', 'Juego de construcción y supervivencia en mundo abierto', 26.95, 'Mojang', '/imagenes/minecraft.jpg', 'Microsoft Store'),
('The Witcher 3', 'witcher3.jpg', 'RPG con narrativa profunda y mundo abierto', 39.99, 'CD Projekt', '/imagenes/witcher3.jpg', 'GOG'),
('Among Us', 'amongus.jpg', 'Juego de deducción social multijugador', 4.99, 'InnerSloth', '/imagenes/amongus.jpg', 'Steam'),
('Fortnite', 'fortnite.jpg', 'Battle Royale con construcción y eventos en vivo', 0.00, 'Epic Games', '/imagenes/fortnite.jpg', 'Epic Games Store');

INSERT INTO comentarios (id_videojuego, id_usuario, contenido) VALUES
(1, 2, '¡Este juego es increíble! Me encantan los jefes finales.'),
(2, 3, 'Minecraft es perfecto para pasar el tiempo construyendo cosas.'),
(3, 4, 'La historia de Geralt es épica, me atrapó por completo.'),
(4, 5, 'Me encanta jugar Among Us con mis amigos.'),
(5, 1, 'Fortnite es muy divertido, aunque competitivo.');

