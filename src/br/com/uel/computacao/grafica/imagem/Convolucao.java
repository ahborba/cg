package br.com.uel.computacao.grafica.imagem;

import org.opencv.core.Mat;

public class Convolucao {
	private double limiar;
	private Mat imagem;
	private int[][] sobelR1 = { { -1, -2, -1 }, { 0, 0, 0 }, { 1, 2, 1 } };
	private int[][] sobelR2 = { { -1, 0, 1 }, { -2, 0, 2 }, { -1, 0, 1 } };
	private Mat convolucao;
	private int lin, col;
	private boolean erro = false;
	private double[] black = {0,0,0};
	private double[] white = {255,255,255};

	
	public Convolucao(double limiar,Mat img) {
		this.imagem = img;
		this.limiar = limiar;
		convolucao = new Mat(imagem.rows(), imagem.cols(), imagem.type());
	}

	protected Mat convolucao(String metodo) {
		lin = imagem.rows();
		col = imagem.cols();

		for (int i = 1; i < lin; i++) {
			for (int j = 1; j < col; j++) {
				borda(i,j,metodo);
			}
		}

		if (erro)
			return null;
		return convolucao;
	}

	private void borda(int i, int j, String metodo) {
		switch (metodo) {
			case "sobel": sobel(i,j);
			case "media": media(i,j);
			case "mediana":mediana(i,j);
			default:
				erro = true;
				return;
		}

	}
	private void sobel(int i, int j) {
		double r1,r2;
		for(int k = 0; k < 3;k++) {
			for (int n = 0; n < 3 ; n++) {

			}
		}
		if(Math.sqrt(r1+r2) > limiar){
			convolucao.put(i,j,black);
		}else {
			convolucao.put(i, j,white);
		}
	}


	private void media(int i, int j) {
		// TODO Auto-generated method stub
		
	}
	private void mediana(int i, int j) {
		
	}


}
