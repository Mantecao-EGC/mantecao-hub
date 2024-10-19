# EGC - mantecao-hub

# Metodología de Trabajo

## Historial de versiones
| Nombre de la versión | Cambios |
|-------------------------|-------------------------|
| v1.0 | Documento inicial |

## Índice

1. [Contribuyentes](##contribuyentes)
2. [Introducción](##introducción)
3. [ Política de gestión de commits](##política-de-gestión-de-commits)
    3.1 [ Commits atómicos](##commits-atómicos)
        3.1.1 [ Definición de Commit Atómico](###definición-de-commit-atómico)
        3.1.2 [ Procedimiento para realizar Commits Atómicos](###procedimiento-para-realizar-commits-atómicos)
4. [ Política de gestión de issues](##política-de-gestión-de-issues)
    4.1 [ Etiquetado básico](###etiquetado-básico)
    4.2 [ Asignación de responsables](###asignación-de-responsables)
    4.3 [ Milestones](###milestones)
    4.4 [ Asignación a proyectos y tableros](###asignación-a-proyectos-y-tableros)
    4.5 [ Seguimiento y actualización](###seguimiento-y-actualización)
    4.6 [ Cierre de issues](###cierre-de-issues)
5. [ Política de gestión de ramas](##política-de-gestión-de-ramas)
    5.1 [ GitFlow como Estrategia de Gestión de Ramas](###gitflow-como-estrategia-de-gestión-de-ramas)
    5.2 [ Ramas principales](###ramas-principales)
    5.3 [ Ramas de soporte](###ramas-de-soporte)
6. [ Procedimiento en caso de no cumplimiento](##procedimiento-en-caso-de-no-cumplimiento)

## Contribuyentes
| Nombre del contribuyente |
|-------------------------|
| Samuel Albalat Ortiz | 
| Pablo Alcántara Bernal |
| Adrián García Chavero |
| Álvaro Hidalgo Rodríguez |
| Nerea Jiménez Adorna |
| Santiago Rosado Raya |

## Introducción

A continuación se presenta el documento de las políticas del trabajo en el proyecto, en el cual se va a especificar y explicar los procedimientos que se han de seguir en el proyecto a la hora de trabajar de forma ideal.

## Política de gestión de commits

Como política de gestión de commits emplearemos como base la metodología de **Conventional Commits** especificada en el siguiente documento: [**Conventional Commits** en español](https://www.conventionalcommits.org/es/v1.0.0/). 

Además, hemos decidido extender nuestras políticas para facilitar aún más la gestión del proyecto. Los añadidos se especifican a continuación.

### Commits atómicos

#### Definición de Commit Atómico
Un commit atómico es aquel que representa un único cambio o, en su defecto, conjunto de cambios relacionados entre sí, realizado en un repositorio de código, de manera que:
- Soluciona un problema específico o agrega una funcionalidad independiente.
- No incluye cambios innecesarios ni mezclados con otros cambios que resuelvan problemas distintos.
- Facilita la revisión del código, revertir cambios si es necesario y mantener el historial del proyecto claro y legible.

#### Procedimiento para realizar Commits Atómicos
- **Cambios pequeños y enfocados**: Cada commit debe contener solo los cambios necesarios para solucionar un problema o agregar una funcionalidad específica.
- **No mezclar tipos de cambios**: Evitar combinar cambios que resuelvan problemas distintos, como correcciones de bugs junto con nuevas funcionalidades.
- **Mensajes de commit descriptivos**: El mensaje de cada commit debe explicar claramente qué cambios se realizaron y por qué.
- **Testear antes de commitear**: Asegurarse de que el código compila correctamente y pasa todas las pruebas antes de hacer un commit. Esto garantiza que cada commit sea un estado funcional del código.
- **Frecuencia de commits**: Se recomienda hacer commits frecuentemente para que los cambios puedan ser revisados y revertidos fácilmente, en lugar de acumular grandes cantidades de código en un solo commit.

### Revisiones, fixes y pull request
En el caso específico de las revisiones, siempre en el footer del commit hemos de colocar nuestro nombre precedido por "Reviewed-by:", adicionalmente si se trata de un fix o similar es importante colocar en el footer "Refs:#Número-de-la-issue".

En el caso de las pull request se espera tanto el reviewer como una descripción clara de lo comprobado independientemente de que sea exitosa o no.

---

## Política de gestión de issues
Esta política define cómo gestionar las issues en el proyecto utilizando **GitHub**. El objetivo es organizar, priorizar y dar seguimiento eficiente a cada tarea dentro del ciclo de desarrollo.

### Etiquetado básico
Cada **issue** debe contar con al menos las siguientes etiquetas:
- **Tipo de issue:**
  - `feature`: Para nuevas funcionalidades.
  - `bug`: Para reportes de errores.
  - `documentation`: Para tareas de documentación.
  - `enhancement`: Para mejoras a funcionalidades existentes.

### Asignación de responsables
- **Cada issue** debe tener **dos personas asignadas**: Esto asegura revisión y cooperación en cada tarea.

### Milestones
- Todas las **issues** deben estar vinculadas a una **milestone** específica que coincida con el período de trabajo que se determine en la organicación de la asignatura.

### Asignación a proyectos y tableros
- Cada issue debe estar vinculada a uno de los **proyectos** de GitHub definidos para el equipo. Esto permite visibilidad clara en el tablero del proyecto y facilita el seguimiento en conjunto.
Para organizarlas existen **dos tableros**:
  - **Tablero de desarrollo**: Para gestionar el desarrollo general de las features y nuevas funcionalidades.
Donde se establecen los siguientes campos:
    - `Prioridad`: con valores {P0,P1,P2}, dónde P0 es la de mayor prioridad y P2 la de menos. Las prioridades deben ser claramente definidas para asegurar que las tareas críticas sean atendidas primero.
    - `Tamaño`:con valores {XS,S,M,L,XL}. Indican el tamaño de la issue.
    - `Estimación`: en horas totales a invertir.
    - `Fecha inicio`: donde pasa a estar en progreso.
    - `Fecha fin`: donde pasa a estar hecha.
  - **Tablero de bugs**: Exclusivo para la gestión y resolución de errores. Posee los mismos campos que el tablero de desarrollo.
  
  Las issues deben ser asignados al **tablero correspondiente** según su tipo (feature o bug).

### Seguimiento y actualización
- Los responsables deben actualizar las **issues** de manera regular con comentarios y avances. 

### Cierre de issues
- Una issue se considera cerrada cuando:
  - Se ha completado la tarea y se ha revisado el código.
  - Se han actualizado los tableros y se ha movido la issue a `Hecho`.

---

## Política de gestión de ramas
### GitFlow como Estrategia de Gestión de Ramas
Este proyecto sigue la estrategia de ramificación **GitFlow**, que define un flujo de trabajo claro para el desarrollo de nuevas funcionalidades, corrección de bugs y despliegues de producción. El uso de GitFlow asegura que las ramas estén organizadas y que cada etapa del ciclo de desarrollo esté bien delimitada.

### Ramas Principales
Las siguientes ramas serán permanentes y existirán a lo largo del proyecto:
- `main`: Contiene el código en estado **estable** que ha sido lanzado a producción.
- `develop`: Ramas destinadas al **desarrollo** y contienen el código que está listo para ser probado antes de pasar a producción.

![image](https://hackmd.io/_uploads/H1ArNmZlJl.png)

### Ramas de Soporte
GitFlow utiliza ramas adicionales para gestionar características específicas, correcciones de errores y versiones. Las principales ramas de soporte son:
- **Feature/Fix/Hotfix/Bug branches**: Para el desarrollo de nuevas funcionalidades. Cada nueva funcionalidad o tarea debe desarrollarse en una rama de característica (feature branch). El nombre de la rama debe seguir el siguiente formato:

```
Feat-N/Nombre-de-la-issue
```

Donde:
- `N` es el número de la issue asignada en el sistema de seguimiento de GitHub.
- `Nombre-de-la-issue` es una descripción breve pero clara de la funcionalidad que se va a desarrollar.

Si se está desarrollando la funcionalidad relacionada con la issue #3 llamada "Diseñar las políticas de gestión", la rama se llamaría:
```
Feat-3/Diseñar-las-politicas-de-gestión
```

---

## Procedimiento en caso de no cumplimiento

El cumplimiento de estas políticas será monitoreado mediante revisiones de código (pull requests). Cada miembro del equipo debe adherirse a estas políticas. En caso de no cumplirlas se considerarán como errores y tendrán que ser solucionados en el menor tiempo posible, con una prioridad P2.