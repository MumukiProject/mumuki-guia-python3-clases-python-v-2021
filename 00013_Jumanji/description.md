Lo interesante a la hora de programar con objetos es que cuando les enviamos mensajes, cada objeto le pregunta qué hacer a su clase. Este concepto es conocido como _**method lookup**_, que en castellano sería algo así como "búsqueda del método" :mag_right:. Por ejemplo, si bien todos los animales entienden el mensaje `comer`, cada uno lo hace de forma distinta según el método que hayamos definido en su clase.

¡Veamos si se entiende!

>Suponiendo que tenemos el siguiente código:
>
```python
nano = Caballo(500, "Cuarto De Milla")
pepita = Golondrina(200, "General Las Heras")
theo = Gato(50, 7)
kali = Gato(30, 13)
```
>
> ¿Cuáles de las siguientes afirmaciones son verdaderas?
