# app.py - Interfaz web para el clasificador de tickets
# Luis Antonio Monsalve Hernández | 2026

from flask import Flask, request, jsonify, render_template_string
from classifier import TicketClassifier

app = Flask(__name__)
classifier = TicketClassifier()

# HTML simple para la interfaz
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clasificador de Tickets con IA</title>
    <style>
        * { box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f7fa; }
        h1 { color: #2c3e50; text-align: center; }
        .card { background: white; border-radius: 10px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }
        textarea { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 16px; rows: 4; }
        button { background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-size: 16px; margin-top: 10px; }
        button:hover { background: #2980b9; }
        .result { margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 6px; }
        .alta { color: #e74c3c; font-weight: bold; }
        .media { color: #f39c12; font-weight: bold; }
        .baja { color: #27ae60; font-weight: bold; }
        .footer { text-align: center; margin-top: 30px; color: #7f8c8d; font-size: 0.9rem; }
    </style>
</head>
<body>
    <h1>🤖 Clasificador de Tickets con IA</h1>
    
    <div class="card">
        <h2>Descripción del Problema</h2>
        <textarea id="ticket-text" placeholder="Ej: Servidor caído, nadie puede trabajar..." rows="4"></textarea>
        <button onclick="classifyTicket()">Clasificar Ticket</button>
    </div>
    
    <div class="card" id="result-card" style="display: none;">
        <h2>Resultado</h2>
        <div id="result-content"></div>
    </div>
    
    <div class="footer">
        <p>Proyecto educativo | Luis Antonio Monsalve Hernández | 2026</p>
        <p>GitHub: github.com/monsa2810/clasificador-tickets-ia-junior</p>
    </div>
    
    <script>
        async function classifyTicket() {
            const text = document.getElementById('ticket-text').value;
            if (!text.trim()) {
                alert('Por favor, describe el problema.');
                return;
            }
            
            const response = await fetch('/classify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: text })
            });
            
            const result = await response.json();
            
            const resultCard = document.getElementById('result-card');
            const resultContent = document.getElementById('result-content');
            
            resultCard.style.display = 'block';
            resultContent.innerHTML = `
                <p><strong>Texto:</strong> ${result.texto}</p>
                <p><strong>Prioridad:</strong> <span class="${result.prioridad}">${result.prioridad.toUpperCase()}</span></p>
                <p><strong>Confianza:</strong> ${result.confianza.toFixed(2)}%</p>
                <p><strong>Probabilidades:</strong></p>
                <ul>
                    ${Object.entries(result.probabilidades).map(([cls, prob]) => 
                        `<li>${cls}: ${(prob * 100).toFixed(2)}%</li>`
                    ).join('')}
                </ul>
            `;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "Texto vacío"}), 400
    
    result = classifier.classify(text)
    return jsonify(result)

if __name__ == '__main__':
    print("🚀 Iniciando servidor...")
    print("📍 Accede a: http://localhost:5000")
    app.run(debug=True, port=5000)
