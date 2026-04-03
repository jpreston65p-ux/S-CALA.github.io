from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
# Permitir que el HTML se comunique con este servidor
CORS(app) 

# Configurar tu API Key de Google 
# (PON AQUÍ LA NUEVA CLAVE QUE CREES, ¡NO LA COMPARTAS!)
genai.configure(api_key="AIzaSyByYxYYMVeeyoLE9mW0kkGhNA9S89-JWI4")

# Volvemos a la versión 1.5-flash que funciona perfecto y rápido
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/chat', methods=['POST'])
def responder_chat():
    datos = request.json
    mensaje_usuario = datos.get('mensaje')
    
    # Personalidad del Pastor SCala con la regla de respuestas cortas
    instruccion_completa = f"""
    Eres el 'Pastor SCala', un asistente de IA avanzado diseñado para un ministerio. 
    Tu objetivo es brindar orientación, reflexión profunda y crecimiento personal. 
    Tu tono debe ser compasivo, muy profesional, maduro y alineado con valores cristianos y bíblicos.
    
    REGLA ESTRICTA: Tus respuestas deben ser precisas, directas y fáciles de entender. 
    Responde en un máximo de 1 a 3 párrafos muy cortos. Nunca te extiendas demasiado.
    
    Mensaje del usuario: {mensaje_usuario}
    """
    
    try:
        respuesta = model.generate_content(instruccion_completa)
        return jsonify({"respuesta": respuesta.text})
    except Exception as e:
        # Si algo falla, esto lo imprimirá en tu pantalla negra
        print(f"\n❌ ERROR DE LA IA: {e}\n")
        return jsonify({"respuesta": "Lo siento, estoy teniendo dificultades técnicas en este momento."}), 500

if __name__ == '__main__':
    print("=========================================")
    print(" SERVIDOR PASTOR SCALA INICIADO (Backend)")
    print("=========================================")
    app.run(port=5000)