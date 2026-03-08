# classifier.py - Módulo de clasificación de tickets
# Luis Antonio Monsalve Hernández | 2026

import pickle

class TicketClassifier:
    def __init__(self, model_path='model.pkl'):
        """Cargar el modelo entrenado"""
        try:
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
            self.loaded = True
        except FileNotFoundError:
            print("❌ Error: Modelo no encontrado. Ejecuta train_model.py primero.")
            self.loaded = False
    
    def classify(self, text):
        """Clasificar un ticket por prioridad"""
        if not self.loaded:
            return {"error": "Modelo no cargado"}
        
        prediction = self.model.predict([text])[0]
        probabilities = self.model.predict_proba([text])[0]
        
        # Mapear clases a probabilidades
        classes = self.model.classes_
        prob_dict = {cls: float(prob) for cls, prob in zip(classes, probabilities)}
        
        return {
            "texto": text,
            "prioridad": prediction,
            "probabilidades": prob_dict,
            "confianza": max(probabilities) * 100
        }
    
    def classify_batch(self, texts):
        """Clasificar múltiples tickets"""
        results = []
        for text in texts:
            results.append(self.classify(text))
        return results

# Ejemplo de uso
if __name__ == "__main__":
    classifier = TicketClassifier()
    
    # Tickets de prueba
    test_tickets = [
        "Servidor caído, nadie puede trabajar",
        "Impresora no conecta",
        "Consulta sobre uso de sistema"
    ]
    
    print("🔍 Clasificación de Tickets de Prueba\n")
    for ticket in test_tickets:
        result = classifier.classify(ticket)
        print(f"📝 Ticket: {result['texto']}")
        print(f"🎯 Prioridad: {result['prioridad'].upper()}")
        print(f"📊 Confianza: {result['confianza']:.2f}%")
        print(f"📈 Probabilidades: {result['probabilidades']}")
        print("-" * 50)
