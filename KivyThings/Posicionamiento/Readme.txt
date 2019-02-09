#Instruduccion a Kivy Lang

Objetivo:
Separar el codigo de interface visual del codigo de logica de negocio

Caracteristicas:
>Lenguaje de marcacion
>Semejante a QML, XML, JSON
>Construccion de Interfaces Graficas

Estructura:

<ClassName>:
    LayoutType:
        WidgetType:
            pos: 10, 10
            size: .5, .5

    LayoutType2:
        font_size: 70
        center_x: root.width / 4
        top: root.top - 5
        Text: "0"



  ClassName
 -------------------------------------
 |            LayoutType             |
 |    ----------------------------   |
 |    |       -------------       |  |
 |    |       | widgetType |      |  |
 |    |       -------------       |  |
 |    ----------------------------   |
 |                                   |
 |            LayoutType2            |
 |    ----------------------------   |
 |    |            0              |  |
 |    ----------------------------   |
 |                                   |
 -------------------------------------


#Propiedades de medida y posicionamiento:

Sufijo Hint:
Significa que sus valores deben ser definidos
en valores porcentuales (0.0 y 1.0)

Ejemplo:
- pos_hint: Espera un diccionario con los ejes x e y en %
-> pos_hint: {"x": .1, "y": .1}

- size_hint: Espera una tupla con width y height en %
