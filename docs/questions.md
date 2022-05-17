# Requerimientos, Criterios, Casos

# Cuestionario

## Responder:

### 1. ¿Qué es Coding Dojo? Referencia.[^1]

> *Coding Dojo* es un encuentro entre un grupo de desarrolladores que tienen el objetivo de superar un desafío de programación. El objetivo del mismo es **divertirse** y **mejorar sus habilidades**.

### 2. Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia.[^2]

> De forma simple; los requerimientos son las *propiedades* que debe tener el software, los criterios de aceptación son los *jueces* que evalúan si el software cumple con un requisito determinado, y los escenarios de prueba son los *ejemplos* que validan un criterio de aceptación en particular.

> Para los ejemplos, tomemos la aplicación a desarrollar en esta tarea:

> | **Requerimientos** | **Criterios de Aceptación** | **Escenarios de prueba** |
> | --- | --- | --- |
> | La aplicación debe soportar la introducción de *números arábigos* | La aplicación debe cumplir con la *suma de números romanos* | 16 = XVI
> | La aplicación no debe soportar la introducción de *números con parte decimal* | La aplicación debe cumplir con la *resta de números romanos* | 9 = IX


### 3. Dé dos ejemplos de requerimientos no funcionales, y especifique cual es su categoría (seguridad, performance, portabilidad, etc.)

> 1. El tiempo de aprendizaje del usuario debe ser menor a 10 minutos. **_Usabilidad_**
> 2. El software debe ser capaz de soportar 1 operación a la vez. **_Rendimiento_**

### 4. ¿Qué es TDD?[^3][^4]

> *TDD* son las siglas de Test Driven Development, que en español significa Desarrollo Dirigido por Pruebas. TDD es un proceso en el que se escriben las pruebas antes de escribir el código con el objetivo de traer control de calidad tan temprano como sea posible al ciclo de vida de desarrollo de software.

> Al escribir las pruebas antes que el código estamos creando documentación, lo que hará que nuestro código sea más limpio.

### 5. ¿Qué son pruebas unitarias automatizadas?[^5][^6]

> Las pruebas unitarias son pruebas que se hacen a una pequeña parte del código (por esto se llama unitaria, siendo esta pequeña parte una unidad) para comprobar que funciona perfectamente.

> De esta forma, las pruebas unitarias automatizadas consisten en la aplicación de herramientas para automatizar el proceso descrito anteriormente.

### 6. ¿Cual fue el primer framework de pruebas unitarias y para cual lenguaje fue creado?[^7]

> El primer framework de pruebas unitarias fue llamado *JUnit*, para el lenguaje de programación Java. Fue creado en 1997 por Kent Beck.

### 7. Describa los componentes de la arquitectura xUnit.[^8][^9]

> A nivel general, la arquitectura xUnit consta de los siguientes componentes:

> #### Accesorios de prueba
> Son un conjunto de precondiciones necesarias para que se ejecute una prueba

> #### Ejecución de prueba
> Que es algo parecido a lo siguiente:
> ```
> setup();
> ...
> /* Cuerpo de la prueba */
> ...
> teardown()
> ```
> donde setup() y teardown() sirven para inicializar y limpiar dispositivos de prueba.

> Cabe destacar que también existen otros componentes como Corredor de prueba, Caso de prueba, Suites de prueba, Formateador de resultados de prueba y afirmaciones. Sin embargo, los más comunes son los dos explicados anteriormente.

### 8. Indique al menos tres desventajas de las pruebas unitarias automatizadas.[^10]

> 1. Requiere un mayor análisis cuando se encuentra un error.
> 2. Requiere más tiempo de desarrollo.
> 3. Aumenta las necesidades de las herramientas.

### 9. Indique al menos tres ventajas de las pruebas unitarias automatizadas.

> 1. Se automatizan esfuerzos manuales.
> 2. En algunos casos, nos permiten hacer pruebas que un humano no podría.
> 3. Se ahorra tiempos y costos y permite que las personas se concentren en otras tareas.

## Referencias

[^1]: https://lorenzosolano.com/what-is-coding-dojo/

[^2]: https://lorenzosolano.com/requirements-acceptance-criteria-and/

[^3]: https://www.digite.com/es/agile/desarrollo-dirigido-por-pruebas-tdd/

[^4]: https://lorenzosolano.com/test-driven-development-tdd-implementation/

[^5]: https://www.yeeply.com/blog/que-son-pruebas-unitarias/

[^6]: https://www.atlassian.com/es/continuous-delivery/software-testing/automated-testing

[^7]: https://www.techtarget.com/searchsoftwarequality/answer/Is-unit-testing-an-important-aspect-of-software-development

[^8]: https://hmong.es/wiki/XUnit

[^9]: https://es.wikipedia.org/wiki/XUnit

[^10]: https://www.desarrollo-web-br-bd.com/es/testing/cuales-son-las-desventajas-de-las-pruebas-automatizadas/l967273467/