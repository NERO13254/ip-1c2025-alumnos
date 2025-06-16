# Galería de imágenes carga adecuadamente.**
 En la ruta de app->views.py
 se encuentra la función **home**
 la cual tiene 2 variables , images y fauvorite_list .
 Luego retorna la función renderer 
 
renderer() :
 Proviene de django/shortcuts

 es la encargada de imprimir por pantalla todas las cards , pero para que las cards se puedan imprimir por pantalla primero hay que pasarle cada card de la API en formato json.

getAllImages()  :
 provinene de layers/transport/transport
 la función se encarga de solicitar las cards especificadas , en formato JSON

En la variable definida como "images" se le asigna la función getAllImages : 
 images = getAllImages()

De esta forma la variable images contenga la información necesaria para que la funcion renderer pueda imprimir las cards en el HTML de home

¿Como funciona getAllImages?
comienza estableciendo una variable denominadoa json_collection = [] , la cual va a ser la encargada de almaacenar las cards , de la api.
al finalizar la función se retorna esta variable 

luego se implementa un bucle for que comienza desd del 1 hasta el 20 , este bucle sirve para limitar los resultados de la api , si queremos modificar cuantas cards traer podemos modificar el for , por ejemplo , si queremos traer 100 cards solo debemos cambiar el rango :

    --for i in range(1 , 101 ) : 

luego solicita los datos a la  api , mediante la variable **response** 
posteriormente evalua si la respuesta de la api es satisfactoria . si response contiene  error , esa card se carga con error lanzando el mensaje 
"error al obtener datos para el id" , o lo mismo si no encuentra el pokemon "Pokémon con id {id} no encontrado"

luego transforma la respuesta de la api en formato JSON , para que pueda ser manipulable : 
 raw_data = response.json()

una vez transformado en formato JSON , hay una función que se encarga de agrupar los datos de la API llamada fromRequestIntoCard()
 
 **fromRequestIntoCard()**
 proviene de utilities/translator.py 

 recibe el elemento JSON y almacena los datos en una variable denominada Card , la cual almacena un objeto JSON con los datos 

    pero no utilicé esta función debido a que no se cargan los datos de la imagen ni el "tipo" de pokemon , por ejemplo 
    tipo fuego volador

    por ende tuve que hacerlo yo mismo al elemento JSON que devuelve la función , para eso corroboré los datos provenientes de la api 
    https://pokeapi.co/

    En su web podemos ver un ejemplo de los datos que retorna la api con sus claves , la sección se llama "Resource for ditto" 

    basandome en el ejemplo brindado creé el objeto :

    {
        "name": raw_data["name"] , 
        "url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+str(raw_data["id"] )+".png",
        "height": raw_data["height"],
        "weight": raw_data["weight"],
        "base": raw_data["base_experience"],
        "types" : raw_data["types"]
    }

    name    : retorna el nombre .
    url     : devuelve la ruta de la imagen por defecto del pokemon solicitado mediante su id.
    height  : retorna su altura.
    weight  : retorna el peso.
    base    : retorna el nivel base de experiencia.
    type    : retorna los tipos ("fuego , aire") (pueden ser mas de un solo tipo)

Ese elemento / ejementos JSON son los que contienen la variable images de la sección views.py
Luego se le envía a la función render() esta variable :

return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })



# Buscador I (según el nombre del pokémon)
Dentro de views.py se encuentra la función  **search**

comineza con una variable llamada : name 
que es la que  contiene el valor tipeado por el usuario ejemplo : "ditto"

luego evalua si e lnombre contiene algo , en caso de no contener nada , se redirige a la secicon home para cargar los datos
por defecto . 

pero en caso de que contenga información llama a la función filterByCharacter() y le pasa como parametro el nombre

**filterByCharacter()**
    se encuentra en services.py 
    receorre todas las imagenes obtenidas de la API y evalua si el nombre de coincide con el de la card que se está iterando , de ser el caso , se agrega a una variable 

luego se encapsula el resultado de la funcion en una variable y se le envía a renderer() para que imprima por pantalla los datos coincidientes

# Buscador II (filtro según tipo fuego, agua o planta)
 El buscador de tipos funciona de la misma manera pero implementa la función filterByType(type)


# Favoritos
 FALTA RESOLVER
# ALTA de nuevos usuarios
 FALTA RESOLVER
# Loading Spinner* para la carga de imágenes
 FALTA RESOLVER
# Renovar interfaz gráfica 
 FALTA RESOLVER