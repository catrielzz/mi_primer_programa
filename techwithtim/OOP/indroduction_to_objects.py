# Instancia: Cada vez que creamos un nuevo objeto, se dice que estamos creando una instancia de una clase.
# Por ejemplo, escribir el comando x = 1 se traduce en: crear una nueva instancia de la clase int con el valor 1
# y el nombre x.

# Método: puede pensar en un método como una función específica de ciertos objetos y clases.
# Los métodos se crean dentro de una clase y solo son visibles para las instancias de esa clase.
# Un ejemplo de un método es .strip (). Solo se puede usar en objetos de clase str ya que es específico de la clase str.
# Todos los métodos deben invocarse en una instancia de una clase.
# No podemos simplemente escribir strip () ya que necesitamos incluir una instancia seguida de un punto antes.

x = 5
y = "string"
y.strip()

print(type(x))  # x es una instancia de la clase int <class 'int'>
print(type(y))  # y es una instancia de la clase str <class 'str'>

# Atributos: Un atributo es cualquier cosa que sea específica de un determinado objeto.
# Por ejemplo, el objeto tiene un color de atributo. Podemos cambiar ese color y modificarlo y si creamos un nuevo
# objeto tortuga puede tener un color diferente.






