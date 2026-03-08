# Clasificador de Tickets de Soporte con IA Básica

Sistema de machine learning básico para clasificar automáticamente tickets de soporte técnico por prioridad (Alta/Media/Baja) basado en el texto de la descripción.

## 🌟 Demo en Línea

🔗 **[VER DEMO COMPLETO AQUÍ](https://monsa2810.github.io/clasificador-tickets-ia-junior)**

> **Nota**: Este proyecto usa Python y scikit-learn. Para ejecutar localmente, sigue las instrucciones abajo.

---

## 🎯 ¿Por qué este proyecto?

Como estudiante de Ingeniería en Sistemas buscando mi primer empleo en TI, creé este proyecto para:
- Aplicar conceptos básicos de machine learning a un problema real de soporte técnico
- Demostrar mi capacidad para aprender tecnologías emergentes (IA/ML)
- Integrar IA con mi proyecto anterior (Dashboard de Soporte Técnico)
- Mostrar habilidades de Python y análisis de datos

## 🛠️ Funcionalidades clave

- ✅ **Clasificación automática** de tickets por prioridad (Alta/Media/Baja)
- ✅ **Modelo de machine learning** entrenado con datos simulados
- ✅ **Interfaz web simple** para probar el clasificador
- ✅ **Precisión del modelo** documentada y medible
- ✅ **Código limpio y comentado** para fines educativos

## 💻 Tecnologías utilizadas

- **Python 3.x**: Lenguaje principal
- **scikit-learn**: Librería de machine learning
- **Flask**: Framework web para la interfaz (opcional)
- **pickle**: Para guardar/cargar el modelo entrenado
- **GitHub Pages**: Documentación del proyecto

## 📊 Dataset de Entrenamiento

El modelo fue entrenado con 150+ ejemplos de tickets de soporte técnico simulados, categorizados por:
- **Alta**: Problemas de conectividad, servidores caídos, seguridad
- **Media**: Problemas de software, configuración, rendimiento
- **Baja**: Consultas generales, actualizaciones, documentación

## 🚀 Cómo usar este proyecto

### Opción 1: Ver demo en línea (RECOMENDADO)
🔗 **[Acceder al demo](https://monsa2810.github.io/clasificador-tickets-ia-junior)**

### Opción 2: Ejecutar localmente
```bash
# 1. Clona el repositorio
git clone https://github.com/monsa2810/clasificador-tickets-ia-junior.git

# 2. Navega al directorio
cd clasificador-tickets-ia-junior

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Entrena el modelo (si no existe)
python train_model.py

# 5. Ejecuta la aplicación
python app.py
