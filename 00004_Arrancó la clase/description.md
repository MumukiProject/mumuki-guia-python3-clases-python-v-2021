Los celulares con los que venimos trabajando, los creamos utilizando `Celular`. 

`Celular` es un molde que nos permite crear objetos. Estos moldes se denominan **clases** y cada objeto que creamos a partir de ellas es una **instancia**. Por ejemplo, en el siguiente código:

```python
cancion_favorita_de_gus = Cancion("Cinema Verité", "Serú Girán")
```

* `Cancion` es una clase;
* `Cancion("Cinema Verité", "Serú Girán")` nos permite instanciar un objeto de la clase `Cancion` con el título `"Cinema Verité"` y la banda `"Serú Girán"`; 
* `cancion_favorita_de_gus` es una referencia a esa instancia para que podamos acceder a ella.

Y la clase está definida de la siguiente manera:

```python
class Cancion:
  def __init__(self, un_titulo, una_banda):
    self.titulo = un_titulo
    self.banda = una_banda
```

Donde `titulo` y `banda` son atributos de sus instancias. Pero... ¿qué es ese `init` con dos guiones bajos de cada lado?¿Ese parámetro `self` para qué está? :thought_balloon:

Estas son preguntas que serán respondidas a la brevedad, pero antes… 

> Definí la clase `Celular` que nos permita crear instancias con una batería y un saldo inicial.