# Projeto TCC: Assistente Virtual InovFabLab - Módulo de Transcrição de Voz (Whisper)

Este repositório contém o protótipo inicial do módulo de transcrição de voz para o projeto de TCC do Assistente Virtual do InovFabLab. Utiliza o modelo de Inteligência Artificial [Whisper da OpenAI](https://openai.com/research/whisper) para converter fala em tempo real (capturada via microfone) em texto.

Este script é uma peça fundamental para a interação por voz do assistente, permitindo que os usuários agendem equipamentos ou façam perguntas falando diretamente com o sistema.

## 🚀 Funcionalidades

-   **Captura de Áudio:** Grava fragmentos de áudio diretamente do microfone padrão do sistema.
-   **Transcrição Multilíngue:** Utiliza o modelo Whisper para transcrever o áudio em texto.
-   **Suporte a Português:** Configurado para transcrever especificamente em português, garantindo alta precisão para usuários brasileiros.
-   **Loop de Interação:** Continua ouvindo e transcrevendo em ciclos, simulando uma conversa contínua.
-   **Execução em CPU:** Otimizado para rodar em processadores sem a necessidade inicial de uma placa de vídeo dedicada (embora uma GPU melhore drasticamente a performance).

## 💻 Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes softwares instalados em seu sistema:

-   **Python 3.x:** (Recomendado 3.8+)
-   **FFmpeg:** Uma ferramenta essencial para processamento de áudio/vídeo que o Whisper utiliza.
-   **Microfone:** Um microfone conectado e funcionando em seu sistema.

### Instalação de Pré-requisitos por Sistema Operacional

#### **Linux (Ubuntu/Debian)**

Abra o terminal e execute os seguintes comandos:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv ffmpeg libportaudio2
