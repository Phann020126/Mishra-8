# Informe del trabajo de algoritmia de Modelos de Optimización

## Resumen

En el presente trabajo se presenta una solución del problema de **mishra**, utilizando el método **Differential Evolution**, así como una breve explicación de por qué algunos de los métodos estudiados en clase no pueden ser utilizados para resolver el problema.

## Métodos no aceptados

La función de mishra en cuestión no puede ser resuelta por los siguientes métodos:

1. Método de descenso del gradiente
2. Método de Newton
3. Método de Quasi-Newton
4. Método BFGS

#### Método de descenso del gradiente

Este método no puede ser utilizado debido a que el problema en cuestión es no convexo, por lo que el método del gradiente es propenso a quedar atrapado en los óptimos locales. El éxito del método del gradiente dependería por completo de la elección del punto inicial.

#### Método de Newton

El método de Newton no puede ser utilizado porque depende tanto del gradiente como de la matriz Hessiana. Como los términos incluyen valores absolutos y polinomios de alto grado haría que calcular el Hessiano fuera difícil y propenso a errores.

#### Método de Quasi-Newton

Este método sufre los mismos problemas que el método de Newton, ya que a pesar de la construcción aproximada de la matriz Hessiana depende del gradiente de la función, y por tanto es propensa a quedar atrapada en óptimos locales.

#### Método BFGS

El método BFGS es eficaz cuand se trata de funciones suaves y diferenciables, en caso de nustro problema, que es no lineal y no convexo, pordíamos enfrentar problemas de convergencia, quedando atrapado en óptimos locales. 

## Método aceptado

El método con el que se pudo dar solución al problema fue el método **Differential Evolution** de **scipy**, el cual es un método estocastico basado en poblaciones. Mientras recorre la población el algoritmo muta cada una de las soluciones candidatas, mezclandolas con otras soluciones candidatas para crear un candidato de prueba. La estrategia utilizada por defecto es *"***best1bin***"*. En esta estrategia se seleccionan de manera aleatoria dos miembros de la población y su diferencia se utiliza para mutar el mejor miembro. Luego se construye el vector b' = x $_0$ + mutation * (x $_r$ $_0$ - x $_r$ $_1$). Luego se construye un vector de prueba, empezando por un i-esimo valor elegido aleatoriamente, el vector se llena con valores de b' o del candidato original. La elección se realiza utilizando una distribución binomial, se genera un número aleatorio en [0, 1). Si el valor es menor que la constante de recombinación entonces se utiliza el de b', en caso contrario se selecciona del candidato original. El parámetro final siempre se obtiene de b'. Una vez se construye el candidato se realiza una revisión para determinar si mejora la solución, si el candidato es mejor que el original, toma su lugar, y si es mejor que el candidato a solución actual, también lo reemplaza.

Se seleccionó este método debido a que el problema de **mishra** en cuestión es un problema no convexo con múltiples óptimos locales, por lo que debemos desechar las técnicas que puedan quedar atrapadas en un óptimo local. Este algoritmo explora el espacio de búsqueda completo, por lo que aumenta las probabilidades de encontrar el óptimo global. El algoritmo no requiere que la función sea diferenciable o se pueda calcular un gradiente. Al evitar la dependencia del gradiente **Differential Evolution** es más robusto en problemas con funciones irregulares. **Differential Evolution** puede manejar restricciones y dominios complejos de manera eficiente. En el caso de  **Mishra**, donde la función tiene múltiples términos de alta complejidad, el algoritmo puede ajustarse bien para trabajar dentro de estos dominios sin requerir simplificaciones o transformaciones problemáticas.
