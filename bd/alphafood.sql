USE alphafood;
CREATE TABLE Usuario (
    ID_usuario VARCHAR(10) PRIMARY KEY NOT NULL,
    Nombre VARCHAR(30) NOT NULL,
    Apellido VARCHAR(30) NOT NULL,
    Direccion VARCHAR(50) NOT NULL,
    Telefono VARCHAR(15) NOT NULL
);

CREATE TABLE Productos (
    Codigo_producto INT PRIMARY KEY NOT NULL,
    Nombre VARCHAR(50) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    Cantidad_stock INT NOT NULL
);

CREATE TABLE Pedido (
    ID_pedido INT PRIMARY KEY NOT NULL,
    ID_usuario VARCHAR(10) NOT NULL,  -- Agregamos la columna ID_usuario
    Codigo_producto INT NOT NULL,
    Fecha_pedido DATE NOT NULL,
    Monto_total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ID_usuario) REFERENCES Usuario(ID_usuario),
    FOREIGN KEY (Codigo_producto) REFERENCES Productos(Codigo_producto)
);


