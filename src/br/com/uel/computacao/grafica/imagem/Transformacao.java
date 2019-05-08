package br.com.uel.computacao.grafica.imagem;

import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;

public class Transformacao {

	private Mat imagem;

	public Transformacao(Mat imagem) {
		this.imagem = imagem;
	}

	public double[][] matrizAngulo(double angulo) {
		double[][] matrix = { { Math.cos(angulo), -1 * (Math.sin(angulo)), 0 },
				{ (Math.sin(angulo)), Math.cos(angulo), 0 }, { 0, 0, 1 } };

		return matrix;
	}

	/*
	 * Constroi a matrix de rotacao | alfa beta (1-alfa) * centroX - beta * centroY
	 * | | -beta alfa beta * centroX + (1-alfa) * centroY | alfa = cos(angulo) beta
	 * = sen(angulo)
	 */
	private  double[][] matrizRotacao(int[] cm, double angulo) {
		double a = (Math.PI / 180) * (360 - angulo);
		double alfa = Math.cos(a);
		double beta = Math.sin(a);
		double[][] matrix = { { alfa, beta, (1 - alfa) * cm[0] - beta * cm[1] },
				{ -1 * beta, alfa, beta * cm[0] + (1 - alfa) * cm[1] } };

		return matrix;
	}

	/* Pega centro de massa e armazena em p(cmx,cmy) */
	public static int[] baricentro(Mat im) {
		int[] ponto = new int[3];
		ponto[0] = im.width() / 2;
		ponto[1] = im.height() / 2;
		ponto[2] = 1;
		return ponto;
	}

	public Mat rotacao(double angulo) {

		
		
		
		
		//Creating an empty matrix to store the result
	      Mat saida  = imagem.clone();
	   
	      //Creating the transformation matrix M
	      Mat matRotacao = Imgproc.getRotationMatrix2D(new Point(0, 0),30,1);

	      //Rotating the given image
	      Imgproc.warpAffine(imagem, saida,matRotacao, new Size(imagem.cols(), imagem.cols()));
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
//		
//		
//		Mat dst = imagem.clone();
//
//		int[] cm = baricentro(imagem);
//		double[][] rotationMatrix = matrizRotacao(cm, angulo);
//
//		for (int i = 0; i < imagem.height(); i++) { // Colocaremos a imagem inteira com o cm no ponto (0,0)
//			for (int j = 0; j < imagem.width(); j++) {
//				
//				double[] rgb = imagem.get(i, j);
//				
//				int[] pLinha = new int[2];
//				pLinha[0] = (int) (rotationMatrix[0][0] * i + rotationMatrix[0][1] * j + rotationMatrix[0][2]);
//				pLinha[1] = (int) (rotationMatrix[1][0] * i + rotationMatrix[1][1] * j + rotationMatrix[1][2]);
//				
//				System.out.println("plinha[0]: "+pLinha[0]+"\tplinha[1]"+pLinha[1]+"["+rgb[0]+"]["+rgb[1]+"]["+rgb[2]+"]");
//				dst.put(pLinha[0], pLinha[1], rgb);
//				
//				if (angulo > 0 && angulo < 90) {
//					dst.put(pLinha[0] + 1, pLinha[1] + 1, rgb);
//					dst.put(pLinha[0] + 2, pLinha[1] + 2, rgb);
//				} else if (angulo > 90 && angulo < 180) {
//					dst.put(pLinha[0] - 1, pLinha[1] - 1, rgb);
//					dst.put(pLinha[0] - 2, pLinha[1] - 2, rgb);
//				} else if (angulo > 180 && angulo < 270) {
//					dst.put(pLinha[0] - 1, pLinha[1] - 1, rgb);
//					dst.put(pLinha[0] + 2, pLinha[1] + 2, rgb);
//				} else if (angulo > 270 && angulo < 360) {
//					dst.put(pLinha[0] + 1, pLinha[1] + 1, rgb);
//					dst.put(pLinha[0] - 2, pLinha[1] - 2, rgb);
//				}
//			}
//		}
		return saida;
	}

	public Mat transfTranslacao(int x, int y) {
		Mat im_tran = new Mat(imagem.rows() * 2, imagem.cols() * 2, imagem.type());

		double[][] matMult = constroiMatrix(imagem, y, x);

		for (int i = 0; i < imagem.height(); i++) { // Percorre a imagem inteira
			for (int j = 0; j < imagem.width(); j++) {

				int[] vet = { i, j, 1 }; // Vetor correspondente ao p = (x,y)
				double[] rgb = imagem.get(i, j); // Pega o RGB

				double[] pLinha = multiplicaMatrix(matMult, vet, i, j); // Pega a posi��o do p'. p' = (x',y')
				im_tran.put((int) pLinha[0], (int) pLinha[1], rgb); // Salva o novo ponto na nova imagem
			}
		}
		return im_tran;
	}

	/*
	 * Constroi e retorna a matrix | 1 0 deltaX | | 0 1 deltaY | | 0 0 1 |
	 */
	private double[][] constroiMatrix(Mat im, int deltaX, int deltaY) {
		double[][] matrix = { { 1, 0, deltaX }, { 0, 1, deltaY }, { 0, 0, 1 } };

		return matrix;
	}

	/*
	 * Multiplica a matrix pelo vetor [x y 1] e armazena o resultado em um vetor [x'
	 * y' 1]
	 */
	private double[] multiplicaMatrix(double[][] matMult, int[] vet, int i, int j) {

		double x = 0;
		int cont = 0;
		double[] vetResp = new double[3];

		// Realiza a multiplica��o da matrix com o vetor
		for (int l = 0; l < 3; l++) {
			x = (matMult[l][0] * vet[0]) + (matMult[l][1] * vet[1]) + (matMult[l][2] * vet[2]);
			vetResp[cont] = x;
			x = 0;
			cont++;
		}

		return vetResp;
	}
	
	public  Mat cinza(Mat imagem) {
		Mat cinza = imagem.clone();
		
		int lin = imagem.height();
		int col = imagem.width();
		
		for(int i = 0 ; i < lin; i++) {
			for(int j = 0; j < col; j++) {
				double []rgb = imagem.get(i, j);
				int media = mediaRGB(rgb);
				rgb[0] = media;
				rgb[1] = media;
				rgb[2] = media;
				cinza.put(i,j, rgb);
			}
		}
		return cinza;
	}
	
	private  int mediaRGB(double[] rgb) {
		double media = (rgb[0] + rgb[1] + rgb[2])/3;
		return (int) media;
	}
}
