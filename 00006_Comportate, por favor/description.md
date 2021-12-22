Ya vimos que al enviarle un mensaje a un objeto, este lo puede entender o no. Pero aún no sabemos qué determina si esto sucederá o no. :face_with_monocle:

Para que un objeto entienda un mensaje debemos "enseñarle" cómo hacerlo, y para ello es necesario definir un **método** dentro de la clase a la que pertenece. Un método es, entonces, la descripción de qué hacer cuando se recibe un mensaje del mismo nombre. El conjunto de métodos es lo que provee de comportamiento a las instancias de una clase. 

Por ejemplo, para que nuestra clase `Celular` entienda el mensaje `tiene_bateria_maxima` podría estar definida de la siguiente manera:

```python
class Celular:
  def __init__(self, bateria, saldo):
    self.bateria = bateria
    self.saldo = saldo

  def tiene_bateria_maxima(self):
    return self.bateria == 100
```

Como podemos notar, `self`sigue siendo necesario como primer (y en este caso único) parámetro de nuestros métodos. ¡Y tiene sentido! Recordemos que nos sirve para acceder a los atributos de un objeto. :eyes:

¡Ahora te toca a vos! 

> Definí en la clase `Celular` los métodos `cargar_a_tope` que cargue la batería al 100% y `necesita_saldo` que indique si el celular se quedó sin saldo, es decir, tiene $0.