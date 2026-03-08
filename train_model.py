# train_model.py - Entrenamiento del modelo de clasificación de tickets
# Luis Antonio Monsalve Hernández | 2026

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Dataset de entrenamiento (datos simulados para fines educativos)
tickets = [
    # Alta prioridad
    ("Servidor caído, nadie puede trabajar", "alta"),
    ("Problema de conectividad en toda la oficina", "alta"),
    ("Sistema de producción no responde", "alta"),
    ("Brecha de seguridad detectada", "alta"),
    ("Base de datos corrupta, datos perdidos", "alta"),
    ("Red interna no funciona", "alta"),
    ("Correo electrónico no envía ni recibe", "alta"),
    ("Sistema lento, imposible trabajar", "alta"),
    ("Error crítico en aplicación principal", "alta"),
    ("Firewall bloquea todo el tráfico", "alta"),
    
    # Media prioridad
    ("Impresora no conecta a la red", "media"),
    ("Software no abre correctamente", "media"),
    ("Necesito instalar programa nuevo", "media"),
    ("Configuración de correo no funciona", "media"),
    ("Pantalla azul ocasional", "media"),
    ("WiFi lento en algunas áreas", "media"),
    ("Actualización de sistema fallida", "media"),
    ("Problema con periféricos USB", "media"),
    ("Aplicación se cierra inesperadamente", "media"),
    ("Error en reporte mensual", "media"),
    
    # Baja prioridad
    ("Consulta sobre uso de sistema", "baja"),
    ("Necesito guía de usuario", "baja"),
    ("Solicitud de acceso nuevo", "baja"),
    ("Pregunta sobre funcionalidad", "baja"),
    ("Recomendación de software", "baja"),
    ("Consulta de horario de soporte", "baja"),
    ("Solicitud de capacitación", "baja"),
    ("Pregunta sobre políticas IT", "baja"),
    ("Feedback sobre sistema", "baja"),
    ("Solicitud de documentación", "baja"),
]

# Expandir dataset para mejor entrenamiento
tickets_expanded = tickets * 5  # 150 ejemplos

# Separar datos y etiquetas
texts = [ticket[0] for ticket in tickets_expanded]
labels = [ticket[1] for ticket in tickets_expanded]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Crear pipeline: TF-IDF + Naive Bayes
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

# Entrenar modelo
model.fit(X_train, y_train)

# Evaluar modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Modelo entrenado exitosamente")
print(f"📊 Precisión: {accuracy * 100:.2f}%")
print(f"\n📋 Reporte de clasificación:")
print(classification_report(y_test, y_pred))

# Guardar modelo
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print(f"\n💾 Modelo guardado como 'model.pkl'")
print(f"🎯 Proyecto: Clasificador de Tickets de Soporte con IA Básica")
print(f"👤 Autor: Luis Antonio Monsalve Hernández")
