Downloader e Converter by Solarion
GitHub Python PyQt5 FFmpeg

O Downloader e Converter by Solarion é uma aplicação desktop desenvolvida em Python que permite baixar vídeos de diversas plataformas (YouTube, Instagram, TikTok, Facebook, etc.) e convertê-los para formatos populares como MP4, MP3, MKV, AVI, MOV, FLV e WAV. A interface é construída com PyQt5, oferecendo uma experiência moderna e responsiva, com suporte a temas escuros e múltiplos idiomas.

Recursos Principais
Download de Vídeos:

Suporta plataformas como YouTube, Instagram, TikTok, Facebook, Twitch, Twitter e Pinterest.

Escolha a resolução do vídeo (de 144p até 4K).

Baixe vídeos individuais ou playlists.

Conversão de Formatos:

Converta vídeos para MP4, MKV, AVI, MOV, FLV.

Extraia áudio em formatos MP3 ou WAV.

Ajuste a resolução e a taxa de bits do áudio.

Interface Moderna:

Interface gráfica intuitiva e responsiva.

Suporte a temas escuros.

Tradução para múltiplos idiomas (Português, Inglês, Espanhol, Russo, Chinês, Japonês, Francês, Italiano, Alemão e Coreano).

Funcionalidades Avançadas:

Limite de largura de banda para downloads.

Suporte a proxies.

Atualizações automáticas (em desenvolvimento).

Pré-requisitos
Antes de executar o programa, certifique-se de ter os seguintes requisitos instalados:

Python 3.8 ou superior:

Baixe Python.

FFmpeg:

O FFmpeg é necessário para conversão de vídeos e áudios.

Instale o FFmpeg.

Bibliotecas Python:

Instale as dependências usando o requirements.txt:

bash
Copy
pip install -r requirements.txt
Instalação
Siga os passos abaixo para configurar e executar o programa:

Clone o repositório:

bash
Copy
git clone https://github.com/seu-usuario/downloader-converter-solarion.git
cd downloader-converter-solarion
Instale as dependências:

bash
Copy
pip install -r requirements.txt
Execute o programa:

bash
Copy
python "Downloader e Converter by Solarion 1.0.py"
Como Usar
Interface Principal:

Insira a URL do vídeo no campo "Video URL".

Escolha a pasta de destino no campo "Save Folder".

Selecione o formato de saída (MP4, MP3, MKV, etc.).

Escolha a resolução do vídeo ou a taxa de bits do áudio.

Clique em "Start Download" para iniciar o download e a conversão.

Configurações Avançadas:

Acesse a aba "Advanced Settings" para:

Definir o número máximo de threads.

Limitar a largura de banda.

Configurar um proxy (opcional).

Temas e Idiomas:

Ative o Modo Escuro no checkbox "Dark Mode".

Altere o idioma no menu suspenso "Language".

Capturas de Tela
Interface Principal
Interface Principal

Modo Escuro
Modo Escuro

Configurações Avançadas
Configurações Avançadas

Estrutura do Projeto
Copy
downloader-converter-solarion/
├── Downloader e Converter by Solarion 1.0.py  # Código principal
├── requirements.txt                           # Dependências do projeto
├── screenshots/                               # Capturas de tela
├── README.md                                  # Este arquivo
└── icon.png                                   # Ícone do aplicativo
Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

Faça um Fork do repositório.

Crie uma Branch para sua feature ou correção:

bash
Copy
git checkout -b minha-feature
Faça Commit das suas alterações:

bash
Copy
git commit -m "Adicionando nova funcionalidade"
Envie as Alterações:

bash
Copy
git push origin minha-feature
Abra um Pull Request no repositório original.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Autor
Solarion

GitHub: @solarion

Email: seu-email@example.com

Agradecimentos
À comunidade PyQt5 por fornecer uma biblioteca poderosa para interfaces gráficas.

Ao FFmpeg por possibilitar a conversão de vídeos e áudios.

Aos colaboradores e testadores que ajudaram a melhorar o projeto.

Problemas Conhecidos
A conversão para formatos como AVI e FLV pode ser lenta em hardware menos potente.

O suporte a playlists ainda está em desenvolvimento.

Futuras Melhorias
Adicionar suporte a mais plataformas (Vimeo, Dailymotion, etc.).

Implementar download de playlists.

Adicionar suporte a legendas (subtitles).

Melhorar a aceleração por hardware (GPU).

Se você gostou do projeto, não se esqueça de deixar uma ⭐ no repositório! 😊
