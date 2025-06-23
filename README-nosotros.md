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

Posteriormente se implementa un gestor de contexto (with #code as #code ) para manejar las respuestas de la API para que al finalizar las consultas los recursos utilizados se liberen .

dentro de este se encuentra un ejecutor (ThreadPoolExecutor) realiza varias funciones al mismo tiempo.
Posteriormente se utiliza el método .map del executor que especifica la función a realizar y las iteraciones 


luego solicita los datos a la  api , mediante la Funcion **fetch_pokemon(id)**
evalua si la respuesta de la api es satisfactoria . si response contiene  error , esa card se carga con error.

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
        "id": raw_data["id"],
        "name": raw_data["name"],
        "url": f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{raw_data['id']}.png",
        "height": raw_data["height"],
        "weight": raw_data["weight"],
        "base": raw_data["base_experience"],
        "types": raw_data["types"],
        "hp": raw_data["stats"][0]["base_stat"]
    }

    name    : retorna el nombre .
    url     : devuelve la ruta de la imagen por defecto del pokemon solicitado mediante su id.
    height  : retorna su altura.
    weight  : retorna el peso.
    base    : retorna el nivel base de experiencia.
    type    : retorna los tipos ("fuego , aire") (pueden ser mas de un solo tipo)
    hp      : puntos de salud base 
    
Ese elemento / ejementos JSON son los que contienen la variable images de la sección views.py
Luego se le envía a la función render() esta variable :

return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

Se agregó un borde de color dinámico en la tarjeta del Pokémon dentro de home.html
que cambia según su tipo: Fuego, Agua o Planta.

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
 Mejoras en la funcionalidad de favoritos:
Se corrigieron errores relacionados con el modelo Favourite.
Se actualizaron las migraciones para reflejar estos cambios en la base de datos.
Se agregó la lógica de guardado de favoritos:
Los usuarios autenticados ahora pueden agregar Pokémon a favoritos desde la interfaz principal.
Se implementó la vista saveFavourite, usando get_or_create para evitar duplicados por usuario.
Se actualizó la interfaz para mostrar el estado actual: si un Pokémon ya está en favoritos, se muestra un botón deshabilitado.
Se mejoró el diseño de los botones de tipo (FUEGO, AGUA, PLANTA):
Ahora usan clases Bootstrap para diferenciarse visualmente según el tipo.
Se organizó mejor el layout de estas opciones.

# Loading Spinner* para la carga de imágenes

 Se crea una plantilla llamada 'spinner.html'.
 Esta se utiliza como pantalla intermedia al ingresar a la sección de galería.
 Al renderizarse, muestra un GIF de carga centrado (spinner),
 y automáticamente redirige al usuario hacia la vista de la Pokédex ('pokedex') tras unos segundos.


