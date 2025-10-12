import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time

# --- Configurações ---
MODEL_SIZE = "base"  # Modelos: "tiny", "base", "small", "medium". "base" é um bom começo.
SAMPLE_RATE = 16000  # Taxa de amostragem. Whisper foi treinado com 16kHz.
RECORD_SECONDS = 5   # Duração de cada gravação em segundos.
FILENAME = "temp_audio.wav" # Nome do arquivo de áudio temporário

# Carrega o modelo Whisper uma única vez
print("Carregando o modelo Whisper...")
try:
    model = whisper.load_model(MODEL_SIZE)
    print(f"Modelo '{MODEL_SIZE}' carregado com sucesso.")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    print("Certifique-se de que o FFmpeg está instalado e no PATH do sistema.")
    exit()

def record_audio():
    """Grava áudio do microfone padrão."""
    print(f"\nOuvindo por {RECORD_SECONDS} segundos... Fale agora!")
    
    # Grava o áudio
    recording = sd.rec(int(RECORD_SECONDS * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype=np.int16)
    sd.wait()  # Espera a gravação terminar
    
    # Salva o áudio em um arquivo WAV
    write(FILENAME, SAMPLE_RATE, recording)
    
    print("Gravação finalizada.")

def transcribe_audio():
    """Transcreve o áudio do arquivo salvo."""
    print("Transcrevendo áudio...")
    
    try:
        # Tenta transcrever. O fp16=False é importante para rodar em CPU.
        result = model.transcribe(FILENAME, language='pt', fp16=False)
        transcribed_text = result['text']
        
        if transcribed_text:
            print(">> Texto Transcrito:", transcribed_text)
        else:
            print(">> Não foi possível detectar fala.")
            
    except Exception as e:
        print(f"Ocorreu um erro na transcrição: {e}")

# --- Loop Principal da Aplicação ---
if __name__ == "__main__":
    print("Aplicação de transcrição em tempo real iniciada.")
    print("Pressione Ctrl+C para sair.")
    
    try:
        while True:
            record_audio()
            transcribe_audio()
            time.sleep(1) # Pequena pausa antes de começar de novo
            
    except KeyboardInterrupt:
        print("\nAplicação encerrada.")