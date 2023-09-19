import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_results(before, after):
    plt.figure(figsize=((10, 5)))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(before, cv2.COLOR_BGR2RGB))
    plt.title("antes", fontsize=10)
    plt.subplot(1, 2, 2)
    plt.imshow(after)
    plt.title("depois", fontsize=10)
    plt.show()

# a -> imagem, m -> intervalo, x -> variação
def alterar_faixa_matizes(a, m, x):
    imagem_hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)

    matiz_max = np.mod((m + x) / 2, 180)
    matiz_min = np.mod((m - x) / 2, 180)

    print(f"[Min] {matiz_min} <--> {matiz_max} [Max]")

    if matiz_min < matiz_max:
        # Não precisa de ajustes circulares, pois matiz_min é menor que matiz_max
        imagem_hsv[:, :, 0] = np.where(
            (imagem_hsv[:, :, 0] >= matiz_min) & (imagem_hsv[:, :, 0] <= matiz_max),
            (imagem_hsv[:, :, 0] + 90) % 180,
            imagem_hsv[:, :, 0]
        )
        # imagem_rgb = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2RGB)
        # plot_results(a, imagem_rgb)

    elif matiz_min > matiz_max:
        # Ajuste circular para o caso em que matiz_min é maior que matiz_max
        imagem_hsv[:, :, 0] = np.where(
            ((imagem_hsv[:, :, 0] >= matiz_min) & (imagem_hsv[:, :, 0] <= 179)) |
            ((imagem_hsv[:, :, 0] >= 0) & (imagem_hsv[:, :, 0] <= matiz_max)),
            (imagem_hsv[:, :, 0] + 90) % 180,
            imagem_hsv[:, :, 0]
        )
        
    imagem_rgb = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2RGB)
    plot_results(a, imagem_rgb)

def main():
    imagem_entrada = cv2.imread("circulo_cromatico.jpeg")  
    alterar_faixa_matizes(imagem_entrada, 210, 45)

    imagem_entrada = cv2.imread("circulo.jpg")  
    alterar_faixa_matizes(imagem_entrada, 30, 60)

    imagem_entrada = cv2.imread("circulo2.png")  
    alterar_faixa_matizes(imagem_entrada, 30, 60)

    imagem_entrada = cv2.imread("circulo3.png")  
    alterar_faixa_matizes(imagem_entrada, 30, 60)

    # imagem_entrada = cv2.imread("aves.jpg")  
    # alterar_faixa_matizes(imagem_entrada, 30, 60)


if __name__ == "__main__":
    main()
