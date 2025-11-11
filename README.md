# 🧠 Task Tracker CLI

Un sencillo **administrador de tareas desde la línea de comandos (CLI)** escrito en **Python**, que te permite agregar, actualizar, eliminar y cambiar el estado de tus tareas, guardándolas en un archivo JSON local.

---

## 🚀 Características

✅ Agregar tareas nuevas  
✅ Actualizar descripciones  
✅ Eliminar tareas  
✅ Marcar tareas como **todo**, **in-progress** o **done**  
✅ Listar tareas (todas o filtradas por estado)  
✅ Persistencia automática en un archivo `tasks.json`

---

## 🧩 Requisitos

- Python **3.8 o superior**
- No necesita librerías externas (solo módulos estándar)

---

## ⚙️ Instalación

1. Clona este repositorio o copia el archivo `task_cli.py`:
   ```bash
   git clone https://github.com/MikeRider27/task_tracker.git
   cd task_tracker
   ```

2. Asegúrate de que el archivo tenga permisos de ejecución:
   ```bash
   chmod +x task_cli.py
   ```

3. (Opcional) Coloca el script en tu PATH para usarlo como comando global:
   ```bash
   sudo cp task_cli.py /usr/local/bin/task-cli
   ```

   Luego podrás ejecutarlo como:
   ```bash
   task-cli add "Mi nueva tarea"
   ```

---

## 🧠 Uso

El programa utiliza **subcomandos** para las distintas operaciones.

### 🟢 Agregar una nueva tarea
```bash
python task_cli.py add "Comprar leche"
```
📤 **Salida:**
```
Task added successfully (ID: 1)
```

---

### 🟡 Actualizar una tarea
```bash
python task_cli.py update 1 "Comprar leche y pan"
```
📤 **Salida:**
```
Task 1 updated successfully
```

---

### 🔴 Eliminar una tarea
```bash
python task_cli.py delete 1
```
📤 **Salida:**
```
Task 1 deleted successfully
```

---

### 🔵 Marcar una tarea como “en progreso”
```bash
python task_cli.py mark-in-progress 2
```

### 🟣 Marcar una tarea como “hecha”
```bash
python task_cli.py mark-done 2
```

---

### 📋 Listar tareas
#### Todas las tareas:
```bash
python task_cli.py list
```

#### Solo las completadas:
```bash
python task_cli.py list done
```

#### Solo las pendientes:
```bash
python task_cli.py list todo
```

#### Solo las en progreso:
```bash
python task_cli.py list in-progress
```

📤 **Ejemplo de salida:**
```
ID: 2, Description: Comprar leche y pan, Status: done, Created: 2025-11-11T10:23:41, Updated: 2025-11-11T10:30:10
```

---

## 📁 Estructura del proyecto

```
task-tracker-cli/
│
├── task_cli.py     # Script principal
├── tasks.json          # Archivo de datos (se crea automáticamente)
└── README.md           # Documentación
```

---

## 💾 Ejemplo del archivo `tasks.json`

```json
[
  {
    "id": 1,
    "description": "Comprar leche",
    "status": "done",
    "createdAt": "2025-11-11T10:23:41.123456",
    "updatedAt": "2025-11-11T10:30:10.789012"
  }
]
```

---

## ⚠️ Notas

- Si el archivo `tasks.json` no existe, se crea automáticamente.
- Si el archivo está corrupto o vacío, el sistema lo reiniciará como una lista vacía.
- Todos los datos se guardan en el mismo directorio donde ejecutas el script.

---

## 🧑‍💻 Autor

**Miguel Villalba**  
💻 Proyecto educativo inspirado en ejercicios de CLI Task Tracker
