# 🤖 Clasificador de Tickets de Soporte con IA Básica

Sistema de machine learning básico que clasifica automáticamente tickets de soporte técnico por prioridad (Alta/Media/Baja) basado en el texto de la descripción.

## 🌟 Demo en Línea

🔗 **[VER PRESENTACIÓN DEL PROYECTO](https://monsa2810.github.io/clasificador-tickets-ia-junior/)**

> **Nota:** Este proyecto usa Python y scikit-learn. GitHub Pages muestra información del proyecto. Para usar el clasificador funcional, sigue las instrucciones de ejecución local abajo.

---

## 🎯 ¿Por qué este proyecto?

Como estudiante de Ingeniería en Sistemas buscando mi **primer empleo en TI**, creé este proyecto para:

- ✅ Aplicar conceptos básicos de machine learning a un problema real de soporte técnico
- ✅ Demostrar mi capacidad para aprender tecnologías emergentes (IA/ML)
- ✅ Integrar IA con mi proyecto anterior ([Dashboard de Soporte Técnico](https://monsa2810.github.io/soporte-ti-dashboard-junior/))
- ✅ Mostrar habilidades de Python y análisis de datos

---

## 🛠️ Funcionalidades Clave

| Funcionalidad | Descripción |
|--------------|-------------|
| 🎯 Clasificación Automática | Analiza texto y predice prioridad con 85%+ de precisión |
| 📊 Modelo Entrenado | Usa TF-IDF + Naive Bayes (scikit-learn) |
| 🖥️ Interfaz Web | Aplicación Flask para pruebas interactivas |
| 📈 Métricas Documentadas | Precisión, recall y tiempo de inferencia medibles |
| 📝 Código Comentado | 100% educativo y fácil de entender |

---

## 💻 Tecnologías Utilizadas

- **Python 3.x** - Lenguaje principal
- **scikit-learn 1.3.0** - Machine learning (TF-IDF + Naive Bayes)
- **Flask 3.0.0** - Framework web para interfaz
- **NumPy 1.24.0** - Procesamiento numérico
- **pickle** - Serialización del modelo entrenado
- **Git/GitHub** - Control de versiones y hosting

---

## 📊 Dataset de Entrenamiento

El modelo fue entrenado con **150+ ejemplos** de tickets simulados:

| Prioridad | Ejemplos de Texto | Cantidad |
|-----------|------------------|----------|
| 🔴 **Alta** | "Servidor caído", "Brecha de seguridad", "Red no funciona" | 50+ |
| 🟡 **Media** | "Impresora no conecta", "Software no abre", "WiFi lento" | 50+ |
| 🟢 **Baja** | "Consulta de uso", "Solicitud de guía", "Pregunta general" | 50+ |

---

## 🚀 Cómo Ejecutar Localmente

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/monsa2810/clasificador-tickets-ia-junior.git
cd clasificador-tickets-ia-junior
