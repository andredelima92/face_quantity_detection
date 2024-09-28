# Face Detection Project

Este projeto realiza a **detecção de rostos** em uma imagem e conta quantos rostos foram detectados. Ele utiliza a biblioteca OpenCV e o `dlib` para o reconhecimento facial. 

## Funcionalidades
- Carrega uma imagem e detecta os rostos presentes.
- Exibe a imagem com retângulos ao redor dos rostos detectados.
- Mostra o número de rostos encontrados na imagem.

## Requisitos

Certifique-se de que você tenha instalado o **Python 3.x** no seu sistema. Além disso, você precisará instalar alguns pacotes específicos para rodar este projeto.

### Pacotes Necessários

- `opencv-python`: Usada para manipulação de imagens e detecção facial.
- `dlib`: Usada para detecção de rostos com o algoritmo frontal face detector.
- `CMake`: Necessário para compilar o `dlib`.

### Passos para instalar os pacotes:

1. Instale o `pip` se ainda não o tiver instalado:
```bash
    sudo apt install python3-pip  # Para sistemas Ubuntu/Debian
```

# Instale o CMake

## Ubuntu/Debian

```bash
sudo apt update
sudo apt install cmake
```

## Windows

Baixe e instale o [CMake](https://cmake.org/download/), certificando-se de adicioná-lo ao `PATH` durante a instalação.

## macOS

Instale via Homebrew:

```bash
brew install cmake
```

# Instale os pacotes necessários para o projeto

Após instalar o CMake, instale os pacotes Python necessários com o comando abaixo:

```bash
pip install opencv-python
pip install dlib -vvv
```

# Como Executar o Projeto

## Passo 1: Clone o repositório

Se você estiver utilizando o Git, clone este repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd face-detection
```

## Passo 2: Execute o script de detecção de rostos

Após clonar o projeto e instalar as dependências, você pode rodar o script passando o caminho da imagem que deseja analisar:
O Projeto ja conta com uma imagem de exemplo image.png

```bash
python face_detection.py <caminho_da_imagem>
```

Por exemplo:

```bash
python face_detection.py imagens/image.jpg
```

## Passo 3: Resultado

O script exibirá a imagem em uma janela com retângulos ao redor dos rostos detectados e imprimirá no terminal o número de rostos encontrados.

# Exemplo de Uso

Se você usar a imagem `image.png`, o script exibirá o número de rostos detectados no terminal:

```yaml
Rostos detectados: 7
```

# Observações

- Certifique-se de que o arquivo de imagem fornecido esteja acessível e no formato correto (JPEG, PNG, etc.).
- Se o `dlib` não compilar corretamente devido a problemas com o CMake, siga as instruções de instalação fornecidas nas mensagens de erro.