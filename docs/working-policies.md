# EGC - mantecao-hub

# Metodología de Trabajo

## Historial de versiones
| Nombre de la versión | Cambios |
|-------------------------|-------------------------|
| v1.0 | Documento inicial |
| v1.1 | Revisión para el M3 |

## Índice
  - [Contribuyentes](#contribuyentes)
  - [Introducción](#introducción)
  - [Acta Fundacional](#acta-fundacional)
  - [Política de gestión de commits](#política-de-gestión-de-commits)
    - [Commits atómicos](#commits-atómicos)
      - [Definición de Commit Atómico](#definición-de-commit-atómico)
      - [Procedimiento para realizar Commits Atómicos](#procedimiento-para-realizar-commits-atómicos)
    - [Revisiones, fixes y pull request](#revisiones-fixes-y-pull-request)
    - [Hotfixes](#hotfixes)
  - [Política de gestión de issues](#política-de-gestión-de-issues)
    - [Titulos y descripciones](#titulos-y-descripciones)
    - [Etiquetado básico](#etiquetado-básico)
    - [Asignación de responsables](#asignación-de-responsables)
    - [Milestones](#milestones)
    - [Asignación a proyectos y tableros](#asignación-a-proyectos-y-tableros)
    - [Seguimiento y actualización](#seguimiento-y-actualización)
    - [Cierre de issues](#cierre-de-issues)
  - [Política de gestión de ramas](#política-de-gestión-de-ramas)
    - [GitFlow como Estrategia de Gestión de Ramas](#gitflow-como-estrategia-de-gestión-de-ramas)
    - [Ramas Principales](#ramas-principales)
    - [Ramas de Soporte](#ramas-de-soporte)

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

A continuación se presenta el documento de las políticas del trabajo en el proyecto, en el cual se va a especificar y explicar los procedimientos que se han de seguir en el proyecto a la hora de trabajar de forma ideal, este a su vez funciona como acta fundacional al incluirla

## Acta fundacional

Reunidos:

Los arriba contribuyentes, integrantes del equipo de trabajo, acuerdan formalizar el presente **Acta Fundacional** que regirá el funcionamiento y conducta del grupo durante el desarrollo del proyecto.

### **Acuerdos del grupo:**

1. **Responsabilidad y cumplimiento**: Cada miembro se compromete a cumplir con las tareas asignadas y los plazos establecidos, asegurando que se entregue el trabajo con la calidad esperada.
2. **Comunicación efectiva**: Se mantendrá una comunicación abierta, respetuosa y directa entre los miembros. Las decisiones importantes se tomarán por consenso y se deberán documentar en un acta de reunión cuando sea necesario.
3. *Participación activa**: Todos los miembros deberán participar activamente en las reuniones, aportando ideas, soluciones y retroalimentación para mejorar el trabajo en equipo.
4. **Resolución de conflictos**: Ante la aparición de un conflicto, se buscará una solución interna mediante diálogo entre las partes afectadas. Si el conflicto se considera grave o no se resuelve internamente, se acudirá al coordinador de proyectos de la asignatura.
5. **Revisión del acta**: El presente acta podrá ser revisada y modificada únicamente por acuerdo unánime de todos los miembros, de manera excepcional.


### **Sanciones por incumplimiento:**
1. **Retrasos en la entrega de tareas**: La primera falta será advertida verbalmente. Si se repite, se asignará una tarea adicional o se deberá compensar de acuerdo a la decisión del grupo.
2. **Falta de participación o asistencia**: Se hará un llamado de atención y, en caso de reincidencia, se informará al coordinador de proyectos para que intervenga de acuerdo con las normativas de la asignatura.
3. **Conducta irrespetuosa**: En caso de conductas inapropiadas o irrespetuosas hacia otros miembros, se abordará el problema en reunión de equipo. Si persiste, se solicitará la intervención del coordinador de proyectos.
4. **Incumplimiento de los acuerdos**: La reincidencia en el incumplimiento de las responsabilidades acordadas será motivo de una advertencia formal por parte del grupo y, en última instancia, la notificación al coordinador de proyectos para evaluar posibles consecuencias.

### **Tipos de conflictos frecuentes:**
- **Diferencias de opinión en la toma de decisiones**: Se buscará consenso mediante el diálogo. En caso de no llegar a un acuerdo, se someterá a votación y se respetará la mayoría.
- **Distribución desigual del trabajo**: Se revisarán las responsabilidades asignadas y se reestructurará la carga de trabajo en función de las habilidades y tiempo disponible de cada miembro.
- **Incumplimiento de plazos o calidad**: Se plantearán medidas correctivas para cumplir con los objetivos y se tomarán acciones disciplinarias de acuerdo a las sanciones descritas anteriormente.


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
En el caso específico de las revisiones, siempre en el footer del commit hemos de colocar nuestro nombre precedido por "Reviewed-by:", adicionalmente si se trata de un fix o similar es importante colocar en el footer "Refs:#Número-de-la-issue", considerando que dicho número ha de hacer referencia a la issue relacionada

En el caso de las pull request se espera tanto el reviewer con "Reviewed-by:" como una descripción clara de lo comprobado independientemente de que sea exitosa o no la revisión de la misma de cara a la aceptación de cambios.

### Hotfixes
En el caso específico de que la rama principal presente errores urgentes se hará un "commit hotfix", estos han de inidicar claramente su issue referida usando "Refs:#Número-de-la-issue" en el mensaje, y describir los cambios y ser acompañados posteriormente por un segundo commit de revisión considerando que en el primero todo se encontraba en estado funcional y solventado donde se indique tanto la issue con "Refs:#Número-de-la-issue" como el reviewer con  el footer "Reviewed-by:"

---

## Política de gestión de issues
Esta política define cómo gestionar las issues en el proyecto utilizando **GitHub**. El objetivo es organizar, priorizar y dar seguimiento eficiente a cada tarea dentro del ciclo de desarrollo.

### Titulos y descripciones
Cada **issue** debe contar con el siguiente formato dependiendo de su **categoría**, se ha de recalcar que ningún campo opcional ah de venir provisto de formato de mediante "#":
#### Features
  - Título: ⭐️ feat: <"nombre de la feat">
  - Descripción: Se crearán al menos 3 apartados:
    - Descripción General (obligatorio): Se ha de indicar un breve descripción de lo que trata
    - Detalles (Obligatorio): Se realiza una descripción más exacta de la feature
        - Listado de módulos (opcional):Se han de listar los módulos de la apliación que se han de alterar como una lista de cuadrículas
    - Orientación (opcional): Si se puede incluir una orientación breve de como arreglar la issue
    - Política de Ítems (Obligatorio): Se incluirá una casilla que verifique que la issue cumple con la política

Aquí se aporta un ejemplo:

---

### ⭐️ feat: fakenodo
### Descripción General

Hacer un mock de la API de Zenodo

### Detalles

Esta tarea esta enfocada principalmente al entorno de desarrollo, de manera que se pueda trabajar como desarrollador con Fakenodo y con Zenodo en producción. De esta forma, aseguramos que se pueda probar correctamente la integración con Zenodo.

No se especifican los módulos que se deben de tocar, pero principalmente necesitarían modificación aquellos módulos que hagan uso de la API de Zenodo.

### Política de Ítems

- [ ] Esto de acuerdo con la política indicada

---

#### Enhancements
  - Título: ✨ enhancement <"nombre del enhancement">
  - Descripción: Se crearán al menos 3 apartados:
    - Descripción General (obligatorio): Se ha de indicar un breve descripción de lo que trata
    - Detalles (Obligatorio): Se realiza una descripción más exacta del enhacement
        - Listado de módulos (opcional):Se han de listar los módulos de la apliación que se han de alterar como una lista de cuadrículas
    - Orientación (opcional): Si se puede incluir una orientación breve de como arreglar la issue
    - Política de Ítems (Obligatorio): Se incluirá una casilla que verifique que la issue cumple con la política

Aquí se aporta un ejemplo:

---

### Título: ✨ enhancement: testing fakenodo
### Descripción General

Llevar a cabo los tests de Fakenodo

### Detalles

Se tienen que realizar un número suficiente de tests de manera que se cubran la mayoría de las casuísticas de Fakenodo. Hay que tener en cuenta que los tests de interfaz se refieren a las páginas donde se utilice la API de Fakenodo/Zenodo y comprobar que la API haga las operaciones correctas.
- [ ] Tests unitarios
- [ ] Tests de carga con Locust
- [ ] Tests de interfaz con Selenium

### Política de Ítems

- [ ] Esto de acuerdo con la política indicada

---

#### Fixes
  - Título: 🔧 fix <"nombre del fix">
  - Descripción: Se crearán al menos 3 apartados:
    - Descripción General (obligatorio): Se ha de indicar un breve descripción de lo que trata
    - Detalles (Obligatorio): Se realiza una descripción más exacta del fix
        - Error encontrado (Obligatorio): Expresar el error y su método de reproducción si aplica
        - Listado de módulos (opcional):Se han de listar los módulos de la apliación que se han de alterar como una lista de cuadrículas
        - Orientación (opcional): Si se puede incluir una orientación breve de como arreglar la issue
    - Política de Ítems (Obligatorio): Se incluirá una casilla que verifique que la issue cumple con la política

Aquí se aporta un ejemplo:

---

### Título: 🔧 fix: arreglar el workflow
### Descripción General
Necesario ajuste del workflow de release

### Detalles
#### Error encontrado
Es necesario ajustar el workflow de las releases para que haga una release en cada push a main, ya que no se pueden hacer releases a partir de Pull Requests como se indica en la imagen de abajo. Se puede aprovechar el hecho de que no hace releases en Pull Requests para las pruebas.

![imagen](https://github.com/user-attachments/assets/bccfcb7d-c103-46ac-bbd4-1c9b3bd55f8d)

Como no se puede hacer por PRs, revisar alguna forma de que detecte de cual rama proviene para realizar la release en función del nombre de la rama, como esta configurado ahora.

Si se trata de algo complejo y no da tiempo a terminarlo en este milestone, cerrar la issue como no terminada y eliminar el workflow de la release.

### Política de Ítems

- [ ] Esto de acuerdo con la política indicada

---

#### Bugs
  - Título: 🐞 bug <"nombre del bug">
  - Descripción: Se crearán al menos 3 apartados:
    - Descripción General (obligatorio): Se ha de indicar un breve descripción de lo que trata
    - Detalles (Obligatorio): Se realiza una descripción más exacta del bug
        - Error encontrado (Obligatorio): Expresar el error y su método de reproducción si aplica
        - Listado de módulos (opcional):Se han de listar los módulos de la apliación que se han de alterar como una lista de cuadrículas
        - Orientación (opcional): Si se puede incluir una orientación breve de como arreglar la issue
    - Política de Ítems (Obligatorio): Se incluirá una casilla que verifique que la issue cumple con la política

Aquí se aporta un ejemplo:

---

### Título: 🐞 bug: error en test
### Descripción General
La ejecución de los tests de selenium del modulo auth no funcionan correctamente

### Detalles
#### Error encontrado
Al realizar el comando rosemary selenium test me encuentro con un error en los drivers del proyecto que me impide su correcto funcionamiento "Añado la imagen"
El resultado no deberái de dar errores en la ejecución

Posiblemente sea un problema de la instalación de Firefox, pero actualmente no tengo herramientas para solventarlo

### Política de Ítems

- [ ] Esto de acuerdo con la política indicada

---


### Etiquetado básico
Cada **issue** debe contar con al menos las siguientes etiquetas:
- **Tipo de issue:**
  - `feature`: Para nuevas funcionalidades.
  - `enhancement`: Para mejoras a funcionalidades existentes.
  - `fix`: Para correciones de funcionalidades ya hechas
  - `hotfix`: Para correciones urgentes en la rama principal
  - `bug`: Para reportes de errores.
  - `fix`: Para correciones de funcionalidades ya hechas
  - `hotfix`: Para correciones urgentes en la rama principal
  - `bug`: Para reportes de errores.
  - `documentation`: Para tareas de documentación.

### Asignación de responsables
- **Cada issue** debe tener **dos personas asignadas**: Esto asegura revisión y cooperación en cada tarea.

### Milestones
- Todas las **issues** deben estar vinculadas a una **milestone** específica que coincida con el período de trabajo que se determine en la organicación de la asignatura.

### Asignación a proyectos y tableros
- Cada issue debe estar vinculada a uno de los **proyectos** de GitHub definidos para el equipo. Esto permite visibilidad clara en el tablero del proyecto y facilita el seguimiento en conjunto.
Para organizarlas existen **dos tableros**:
  - **Tablero de desarrollo**: Para gestionar el desarrollo general de las features y nuevas funcionalidades.
Donde se establecen los siguientes campos:
    - `Prioridad`: con valores {P0,P1,P2}, dónde P0 es la de mayor prioridad y P2 la de menos. Las prioridades deben ser claramente definidas para asegurar que las tareas críticas o bloqueantes sean atendidas primero.
    - `Tamaño`: con valores {XS,S,M,L,XL}. Indican el tamaño de la issue, su alcance o en su defecto su envergadura.
    - `Estimación`: en horas totales a invertir idealmente
    - `Fecha inicio`: en que fecha pasa a estar en progreso.
    - `Fecha fin`: en que fecha pasa a estar hecha.
  - **Tablero de bugs**: Exclusivo para la gestión y resolución de errores. Posee los mismos campos que el tablero de desarrollo.
  
  Las issues deben ser asignados al **tablero correspondiente** según su tipo (feature/documentation/enhacement o bug/fix).

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

### Rama Principal
Las siguientes ramas serán permanentes y existirán a lo largo del proyecto:
- `main`: Contiene el código en estado **estable** que ha sido lanzado a producción.

### Ramas de Soporte
GitFlow utiliza ramas adicionales para gestionar características específicas, correcciones de errores y versiones. Las principales ramas de soporte son:

- **Feature**: Para el desarrollo de nuevas funcionalidades. Cada nueva funcionalidad o tarea debe desarrollarse en una rama de característica (feature branch). El nombre de la rama debe seguir el siguiente formato:

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

- **Enhancement**: Para la mejoría de partes del sistema ya existentes (adición de tests, optimización de scripts...). Cada nueva mejoría debe desarrollarse en una rama de característica (enhancement branch). El nombre de la rama debe seguir el siguiente formato:

```
Enhancement-N/Nombre-de-la-issue
```

Donde:
- `N` es el número de la issue asignada en el sistema de seguimiento de GitHub.
- `Nombre-de-la-issue` es una descripción breve pero clara de la funcionalidad que se va a desarrollar.

Si se está desarrollando la mejoría relacionada con la issue #3 llamada "Crear test para buscador", la rama se llamaría:
```
Enhancement-3/Crear-test-para-buscador
```

- **Fix**: Para el cambio de funcionalidades ya hechas. Cada arreglo debe desarrollarse en una rama de característica (fix branch). El nombre de la rama debe seguir el siguiente formato:

```
Fix-N-M/Nombre-del-fix
```

Donde:
- `N` es el número de la issue que corresponde a lo que se está arreglando en el sistema de seguimiento de GitHub.
- `M` es el número de la issue asignada en el sistema de seguimiento de GitHub donde quedan registrado el arreglo.
- `Nombre-del-fix` es una descripción breve pero clara del arreglo que se va a realizar.

Si se está arreglado la funcionalidad relacionada con la issue #3, y es la primera rama de arreglo que se crea, la rama se llamaría:
```
Fix-3-1/Fallo-de-inicio
```

- **Bug**: Para cambios no urgentes del proyecto. Debe desarrollarse en una rama de característica (bug branch). El nombre de la rama debe seguir el siguiente formato:

```
Bug-N/Nombre-del-bug
```

Donde:
- `N` es el número de la issue asignada en el sistema de seguimiento de GitHub donde quedan registrado el arreglo.
- `Nombre-del-bug` es una descripción breve pero clara del arreglo que se va a realizar.

Si se está solventando el bug relacionado con la issue #3, la rama se llamaría:
```
Bug-3-1/Usuario-en-formato-desconocido

```