# YouTube Vídeo ou Playlist Downloader

Este script permite baixar vídeos ou *playlists* do *YouTube* e converter vídeos baixados em arquivos de áudio MP3. Ele utiliza as bibliotecas `pytube` para baixar vídeos do *YouTube* e `moviepy` para converter vídeos em arquivos de áudio.



## Pré-requisitos

1. **Python e Bibliotecas Necessárias**: Certifique-se de ter o Python instalado. Instale as bibliotecas necessárias com o seguinte comando:

   ```sh
   pip install pytube3 moviepy
   ```

2. **FFmpeg**: Vá para o site oficial do [FFmpeg](https://ffmpeg.org/download.html) e baixe a versão para Windows. Extraia os arquivos baixados e mova-os para `C:\Program Files`. Adicione o caminho da pasta `bin` do FFmpeg às variáveis de ambiente do sistema para que o FFmpeg possa ser chamado a partir de qualquer lugar no Prompt de Comando. Certifique-se de que o FFmpeg está instalado e configurado corretamente no seu sistema. Você pode verificar isso executando o seguinte comando no Prompt de Comando:

   ```sh
   ffmpeg -version
   ```



## Configurações e Funcionamento

### Funções Principais

#### `download_video(url, download_path=".")`

Esta função baixa um vídeo do *YouTube*.

- Parâmetros
  - `url` (str): A URL do vídeo do *YouTube* que deseja baixar.
  - `download_path` (str, opcional): O caminho onde o vídeo será salvo. O padrão é o diretório atual.
- Retorna
  - `output_path` (str): O caminho completo do vídeo baixado.
  - `None` em caso de falha no download.

#### `convert_to_mp3(video_path, output_path=".")`

Esta função converte um vídeo baixado em um arquivo de áudio MP3.

- Parâmetros
  - `video_path` (str): O caminho do vídeo que deseja converter.
  - `output_path` (str, opcional): O caminho onde o arquivo MP3 será salvo. O padrão é o diretório atual.
- Retorna
  - `audio_file` (str): O caminho completo do arquivo MP3 convertido.
  - `None` em caso de falha na conversão.



### Uso

Ao executar o script, você será solicitado a escolher entre baixar um vídeo ou uma *playlist*.

1. **Escolha de download**:
   - **Vídeo**: Digite `v`.
   - **Playlist**: Digite `p`.
2. **URL do Vídeo ou Playlist**:
   - Forneça a URL do vídeo ou da *playlist* que deseja baixar.
3. **Conversão para MP3**:
   - Se deseja converter os vídeos para MP3, digite `s`.
   - Caso contrário, digite `n`.



### Exemplos de Uso

#### Baixar um Vídeo

1. Execute o script:

   ```sh
   python nome_do_script.py
   ```

2. Escolha baixar um vídeo:

   ```sh
   Deseja baixar um vídeo ou uma playlist? (V/P): v
   ```

3. Digite a URL do vídeo:

   ```sh
   Digite o URL do vídeo que deseja baixar: https://www.youtube.com/watch?v=example
   ```

4. Escolha se deseja converter para MP3:

   ```sh
   Deseja converter o vídeo para MP3? (S/N): s
   ```

5. O vídeo será baixado e convertido para MP3, se selecionado.

#### Baixar uma Playlist

1. Execute o script:

   ```sh
   python nome_do_script.py
   ```

2. Escolha baixar uma *playlist*:

   ```sh
   Deseja baixar um vídeo ou uma playlist? (V/P): p
   ```

3. Digite a URL da *playlist*:

   ```sh
   Digite o URL da playlist que deseja baixar: https://www.youtube.com/playlist?list=example
   ```

4. Escolha se deseja converter os vídeos para MP3:

   ```sh
   Deseja converter os vídeos para MP3? (S/N): s
   ```

5. Todos os vídeos da *playlist* serão baixados e convertidos para MP3, se selecionado.

### Observações

- Certifique-se de fornecer *URLs* válidas para vídeos ou *playlists* do *YouTube*.
- O caminho de download padrão é `"C:/Users/SEU_USUARIO/Music"`, mas pode ser alterado conforme necessário.
- O vídeo original será removido após a conversão para MP3.

### Erros Comuns

- **Erro ao baixar o vídeo**: Certifique-se de que a URL do vídeo é válida e que você tem uma conexão estável com a internet.
- **Erro na conversão para MP3**: Verifique se o caminho do vídeo está correto e se você tem as dependências necessárias instaladas.

------

Este é um guia detalhado sobre como configurar e utilizar o script para baixar e converter vídeos do YouTube. Certifique-se de seguir todas as instruções e ajustar os caminhos conforme necessário para sua máquina.
