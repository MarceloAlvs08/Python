from PIL import image, imageDraw, ImageFront
import os

def criar_imagem_tabuada():
    # 1. Definir as dimensões da imagem
    # Vamos definir um tamanho quadrado, como na imagem referẽncia.
    LARGURA = 600
    ALTURA = 600
    COR_FUNDO = (000, 000, 255)

    # 2. Criar uma nova imagem em branco
    # 'RGB' é o modo de cor, 'COR_FUNDO' define a cor inicial;
    imagem = image.new('RGB', (LARGURA, ALTURA), color=COR_FUNDO)

    # 3. Preparar o objeto de desenho
    # O ImageDraw é como a nossa "caneta" ou "pincel" digital.
    desenho = ImageDraw.Draw(imagem)

    # --- AQUI VAMOS ADICIONAR O CÓDIGO PARA DESENHAR A GRELHA ---

    # 4. Guardar a imagem final
    pasta_saida = "saida_imagens"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    caminho_ficheiro = os.path.join()

    


