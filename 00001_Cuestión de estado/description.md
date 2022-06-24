Hasta el momento estuvimos enviando mensajes a distintos objetos. Por ejemplo, el `celular_de_eli` entendía los siguientes:

```python
ム celular_de_eli.necesita_saldo()
ム celular_de_eli.tiene_bateria_maxima()
ム celular_de_eli.cargar_a_tope()
```

Pero… ¿cómo sabemos si el celular necesita saldo o si tiene la batería máxima?¿qué sucede cuando lo cargamos a tope? Para hacer consultas y modificar al `celular_de_eli` deberíamos tener su saldo y batería guardados en alguna parte, ¿no? :face_with_monocle:

¡Exacto! Los objetos tienen **atributos** y al conjunto de los mismos se los denomina **estado**. Los atributos también son objetos y nos permiten guardar valores y representar características del objeto que los posea. 

Para conocer el estado de un objeto, podemos acceder a cada uno de sus atributos escribiendo `objeto.atributo`, habrás notado que, a diferencia de cuando envíamos un mensaje, al acceder a un atributo no vamos a usar paréntesis.

> Probá en la consola los siguientes comandos para saber el saldo y la batería del `celular_de_eli`:
>
>```python
ムcelular_de_eli.bateria
```
>
>```python
ムcelular_de_eli.saldo
```