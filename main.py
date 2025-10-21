import whisper
import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import torch # Importamos o torch para checar a GPU

# -----------------------------------------------------------------
# TAREFA BE-1 (Parcial): Configuração da Aplicação FastAPI
# -----------------------------------------------------------------
app = FastAPI()

# -----------------------------------------------------------------
# TAREFA BE-4: Configuração do CORS (ESSENCIAL!)
# -----------------------------------------------------------------
# Permite que seu front-end (ex: localhost:5173) se conecte
origins = [
    "http://localhost:5173", # Endereço padrão do Vite
    "http://localhost:3000", # Endereço padrão do create-react-app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------
# TAREFA BE-1 (Parcial): Carregamento Otimizado do Modelo Whisper
# -----------------------------------------------------------------
# Detectar automaticamente o melhor dispositivo (GPU do Mac, NVIDIA, ou CPU)
if torch.backends.mps.is_available():
    DEVICE = "mps"
    print("Usando GPU do Mac (MPS).")
elif torch.cuda.is_available():
    DEVICE = "cuda"
    print("Usando GPU NVIDIA (CUDA).")
else:
    DEVICE = "cpu"
    print("Usando CPU.")

# Pega a configuração do seu script original
MODEL_SIZE = "base" 
print(f"Carregando o modelo Whisper ({MODEL_SIZE})... Isso pode demorar.")

try:
    # Carrega o modelo no dispositivo detectado (ex: "mps")
    model = whisper.load_model(MODEL_SIZE, device=DEVICE) 
    print(f"Modelo Whisper '{MODEL_SIZE}' carregado com sucesso em '{DEVICE}'.")
except Exception as e:
    print(f"Erro ao carregar o modelo Whisper: {e}")
    print("Certifique-se de que o FFmpeg está instalado (brew install ffmpeg).")
    exit()


# -----------------------------------------------------------------
# TAREFA BE-3: Endpoint HTTP Mockado (Equipamentos)
# -----------------------------------------------------------------
@app.get("/api/equipments")
async def get_equipments():
    """
    Endpoint HTTP GET para a equipe de front-end buscar os equipamentos.
    Por enquanto, retorna dados FALSOS (mockados).
    """
    print("Endpoint /api/equipments foi chamado.")
    return [
        {"id": 1, "name": "Impressora 3D (Ender 3)", "status": "disponivel"},
        {"id": 2, "name": "Cortadora a Laser (LaserTech)", "status": "em_uso"},
        {"id": 3, "name": "Fresa CNC (Router 3000)", "status": "manutencao"},
        {"id": 4, "name": "Prototipadora de PCB", "status": "disponivel"},
    ]

# -----------------------------------------------------------------
# TAREFA BE-2: Endpoint WebSocket Mockado (Transcrição)
# -----------------------------------------------------------------
@app.websocket("/ws/transcribe")
async def websocket_endpoint(websocket: WebSocket):
    """
    Endpoint WebSocket para comunicação em tempo real (áudio).
    """
    await websocket.accept()
    print("Cliente WebSocket conectado!")
    try:
        while True:
            # Recebe os dados de áudio em bytes do front-end
            audio_data_bytes = await websocket.receive_bytes()
            
            # POR ENQUANTO (Fase 1), vamos apenas logar que recebemos.
            print(f"Recebidos {len(audio_data_bytes)} bytes de áudio do cliente.")
            
            # Na Fase 2, vamos pegar esses bytes, converter e passar para
            # o `model.transcribe()` que você já tem a lógica.

    except WebSocketDisconnect:
        print("Cliente WebSocket desconectado.")
    except Exception as e:
        print(f"Ocorreu um erro no WebSocket: {e}")

# -----------------------------------------------------------------
# Ponto de entrada para rodar o servidor
# -----------------------------------------------------------------
if __name__ == "__main__":
    print("Iniciando servidor FastAPI em http://localhost:8000")
    # Rode o servidor
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)