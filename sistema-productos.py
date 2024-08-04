# CREAR SISTEMA
# Mostrar en una tabla, una lista de productos que tiene un id, descripcion, precio y stock

# crear lista de productos
productos = [
    {"ID": 1, "Descripcion": "Cartera", "Precio": 5.4, "Stock": 100},
    {"ID": 2, "Descripcion": "Perfume", "Precio": 3.9, "Stock": 50},
    {"ID": 3, "Descripcion": "Sacos", "Precio": 60, "Stock": 200},
    {"ID": 4, "Descripcion": "Zapatos", "Precio": 23, "Stock": 67},
    {"ID": 5, "Descripcion": "Cinturones", "Precio": 2.15, "Stock": 93},
    {"ID": 6, "Descripcion": "Polleras", "Precio": 10, "Stock": 150},
    {"ID": 7, "Descripcion": "Camisas", "Precio": 35, "Stock": 300},
    {"ID": 8, "Descripcion": "Remeras", "Precio": 19, "Stock": 150},
    {"ID": 9, "Descripcion": "Sweaters", "Precio": 25, "Stock": 120},
    {"ID": 10, "Descripcion": "Medias", "Precio": 3.9, "Stock": 40},
    {"ID": 11, "Descripcion": "Pulseras", "Precio": 8.0, "Stock": 45},
    {"ID": 12, "Descripcion": "Aros", "Precio": 3.9, "Stock": 78},
    {"ID": 13, "Descripcion": "Jeans", "Precio": 70, "Stock": 130},
    {"ID": 14, "Descripcion": "Shorts", "Precio": 64, "Stock": 110},
    {"ID": 15, "Descripcion": "Poleras", "Precio": 15, "Stock": 35},
    {"ID": 16, "Descripcion": "Camperas", "Precio": 89, "Stock": 50},
    {"ID": 17, "Descripcion": "Buzos", "Precio": 28.9, "Stock": 26},
    {"ID": 18, "Descripcion": "Bufandas", "Precio": 5.9, "Stock": 11},
    {"ID": 19, "Descripcion": "Crema de manos", "Precio": 12, "Stock": 57},
    {"ID": 20, "Descripcion": "Collar", "Precio": 19, "Stock": 11},
]


# Mostrar la lista en una tabla
def mostrar_productos(productos):
    print(f"{'ID':<5} {'Descripcion':<15} {'Precio':<10} {'Stock':<10}")
    print("-" * 45)
    for producto in productos:
        print(
            f"{producto['ID']:<5}{producto['Descripcion']:<15}{producto['Precio']:<10}{producto['Stock']:<10}"
        )


def mostrarOpciones():
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Editar producto")
    print("4. Mostrar productos")
    print("5. Salir")


def agregar_productos(productos):
    descripcion_nueva = input("Agregar nueva descripción al producto: ")
    precio_nuevo = ingresar_float("Ingresar el precio del nuevo producto: ")
    stock = ingresar_entero("Agregar numero de stock del nuevo producto: ")
    productos.append(
        {
            "ID": len(productos) + 1,
            "Descripcion": descripcion_nueva,
            "Precio": precio_nuevo,
            "Stock": stock,
        }
    )
    print("Se ha agregado un nuevo producto")


def eliminar_productos(productos):
    mostrar_productos(productos)
    id_eliminar = ingresar_entero("Ingrese el ID del producto que desea eliminar: ")
    for producto in productos:
        if producto["ID"] == id_eliminar:
            productos.remove(producto)
            print("Se elimino el producto con éxito")
            return  # termina la función eliminar_productos
    print("no existe producto para el ID indicado")


def editar_productos(productos):
    mostrar_productos(productos)
    id_editar = ingresar_entero("Escriba el ID del producto que desee editar: ")
    for producto in productos:
        if producto["ID"] == id_editar:
            producto["Descripcion"] = input(
                "Ingrese la nueva descripción del producto: "
            )
            producto["Precio"] = ingresar_float("Ingrese nuevo precio: ")
            producto["Stock"] = ingresar_entero("Ingresar stock del producto: ")
            print("Se edito el producto")
            return
    print("Producto no encontrado")


def main():
    encendido = True

    while encendido:
        mostrarOpciones()
        opcion = input("ingrese la opción deseada: ")
        if opcion == "1":
            agregar_productos(productos)
        elif opcion == "2":
            eliminar_productos(productos)
        elif opcion == "3":
            editar_productos(productos)
        elif opcion == "4":
            mostrar_productos(productos)
        elif opcion == "5":
            encendido = False
        else:
            print("ingrese una opción valida")


def ingresar_entero(mensaje):
    ingresando = True
    numero_entero = None
    while ingresando:
        try:
            valor = input(mensaje)
            numero = int(valor)
            ingresando = False
            numero_entero = numero
        except ValueError:
            print("error: no ingresaste un numero entero")
    return numero_entero


def ingresar_float(mensaje):
    ingresando = True
    numero_float = None
    while ingresando:
        try:
            valor = input(mensaje)
            numero = float(valor)
            ingresando = False
            numero_float = numero
        except ValueError:
            print("error: no ingresaste un numero con decimales valido")
    return numero_float


main()
