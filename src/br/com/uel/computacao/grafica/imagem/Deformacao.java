package br.com.uel.computacao.grafica.imagem;

import java.util.ArrayList;
import java.util.Scanner;

import org.opencv.core.Mat;

public class Deformacao {
	public static final int DESCER = 0, SUBIR = 1, DIREITA = 2, ESQUERDA = 3;
	private Mat imagem;
	int lin, col;
	private double[] cor = new double[3];
	int distancia;
	ArrayList<Pixel> pilha  = new ArrayList<Pixel>(); 	

	public Deformacao(Mat imagem, int distancia, double[] cor) {
		this.imagem = imagem;
		this.cor = cor;
		this.distancia = distancia;
		lin = imagem.rows();
		col = imagem.cols();
	}

	public Mat preenchimentoRecursivo(int x, int y, int direcao) {
		@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
		sc.nextLine();
		boolean pintar = false;
		System.out.println("[x: " + x + "][y: " + y + "]");

		if (x > 0 && mesmaCor(x, y, x - 1, y) && direcao != SUBIR) {
			pintar = true;
			System.out.println(" SOBE [i: " + (x - 1) + "][j: " + y + "]");
			preenchimentoRecursivo(x - 1, y, DESCER);
		}
		if (y < col - 1 && mesmaCor(x, y, x, y + 1) && direcao != DIREITA) {
			pintar = true;
			System.out.println(" DIREITA [i: " + x + "][j: " + (y + 1) + "]");
			preenchimentoRecursivo(x, y + 1, ESQUERDA);
		}
		if (x < lin - 1 && mesmaCor(x, y, x + 1, y) && direcao != DESCER) {
			pintar = true;
			System.out.println(" DESCE [i: " + (x + 1) + "][j: " + y + "]");
			preenchimentoRecursivo(x + 1, y, SUBIR);
		}
		if (y > 0 && mesmaCor(x, y, x, y - 1) && direcao != ESQUERDA) {
			pintar = true;
			System.out.println("ESQUERDA [i: " + x + "][j: " + (y - 1) + "]");
			preenchimentoRecursivo(x, y - 1, DIREITA);
		}
		if (pintar) {
			imagem.put(lin, col, cor);
		}

		return imagem;
	}

	public Mat preenchimento(int x, int y) {
		int i = 0, j = 0;
		recursaoCima();
		while (mesmaCor(x, y, i, j)) {

		}

		return imagem;
	}

	public void recursaoCima(int x, int y) {
		this.xAtual = x;
		this.yAtual = y;
		if(mesmaCor(x,y,x-1,y)) {
			
			preenchimentoRecursivo(x - 1, y, DESCER);
		}
	}

	public void recursaoBaixo() {

	}

	public void recursaoDireita() {

	}

	public void recursaoEsquerda() {

	}

	public boolean mesmaCor(int x, int y, int i, int j) {
		
		if(i < 0 || j < 0 || i >= lin || j >= col)
			return false;
	
		double[] rgbXY = imagem.get(x, y);
		double[] rgbIJ = imagem.get(i, j);
//		System.out.println("rgb1: ["+rgbXY[0]+"]["+rgbXY[1]+"]["+rgbXY[2]+"]");
//		System.out.println("rgb2: ["+rgbIJ[0]+"]["+rgbIJ[1]+"]["+rgbIJ[2]+"]");		

		if (rgbXY[0] - rgbIJ[0] < distancia) {
			if (rgbXY[1] - rgbIJ[1] < distancia) {
				if (rgbXY[2] - rgbIJ[2] < distancia) {
					System.out.println(true);
					return true;
				}
			}
		}
		return false;
	}

}
