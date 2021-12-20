Hasta el momento estuvimos enviando mensajes a distintos objetos.
Por ejemplo el `celular_de_eli` entendía los siguientes:

```python
ム celular_de_eli.necesita_saldo()
ム celular_de_eli.tiene_bateria_maxima()
ム celular_de_eli.cargar_a_tope()
```

Pero.... Para consultar y modificar `saldo` y `bateria` deberíamos tener sus valores guardados en alguna parte ¿no? :face_with_monocle:

En objetos tenemos a los **atributos** que también son objetos, y nos permiten guardar valores y representar caracteristicas del objeto que los posea.
Los objetos pueden tener múltiples atributos y al conjunto de los mismos se lo denomina **estado**.

> Veamos si se entiende, probá en la consola los siguientes comandos:
>
```python
ム celular_de_eli.bateria
ム celular_de_eli.saldo
```