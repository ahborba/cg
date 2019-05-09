package br.com.uel.computacao.grafica.imagem;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.Scanner;

import org.opencv.core.Mat;

public class Convolucao implements Comparator<Double> {
	public static double limiar;
	private Mat imagem;
	private int[][] sobelR1 = { { -1, -2, -1 }, { 0, 0, 0 }, { 1, 2, 1 } };
	private int[][] sobelR2 = { { -1, 0, 1 }, { -2, 0, 2 }, { -1, 0, 1 } };
	public static int raio = 1;
	private Mat convolucao;
	private int lin, col;
	private boolean erro = false;
	private double[] black = { 0, 0, 0 };
	private double[] white = { 255, 255, 255 };
	private double qtdElementos;

	public Convolucao(Mat imagem) {
		this.imagem = imagem;
		lin = imagem.rows();
		col = imagem.cols();
		qtdElementos = (Math.pow((2 * raio) + 1, 2));
//		System.out.println("linhas: " + lin + "colunas: " + col);
		convolucao = new Mat(lin, col, imagem.type());
	}

	protected Mat convolucao(String metodo) {

		for (int i = 1; i < lin; i++) {
			for (int j = 1; j < col; j++) {
				borda(i, j, metodo);
			}
		}

		if (erro)
			return null;

		return convolucao;
	}

	private void borda(int i, int j, String metodo) {
		switch (metodo) {
		case "sobel":
			sobel(i, j);
			break;
		case "media":
			media(i, j);
			break;
		case "mediana":
			mediana(i, j);
			break;
		default:
			erro = true;
			return;
		}

	}

	private void sobel(int lin, int col) {
		double r1 = 0, r2 = 0;
		for (int k = -1, i = 0; k < 2; k++, i++) {
			if (lin + k == this.lin) {
				break;
			}
			for (int n = -1, j = 0; n < 2; n++, j++) {
//				System.out.println("[i: "+(lin+k)+" col: "+(col+n)+"]");
//				System.out.println("if: "+( col + n > this.col));
				if (col + n >= this.col) {
					break;
				}
				double rgb[] = imagem.get(lin + k, col + n);

//				System.out.print(((rgb[0]+rgb[1]+rgb[2])/3)*sobelR1[i][j]);
				r1 += ((rgb[0] + rgb[1] + rgb[2]) / 3) * sobelR1[i][j];
				r2 += ((rgb[0] + rgb[1] + rgb[2]) / 3) * sobelR2[i][j];

			}
		}
		if (Math.sqrt((r1 * r1) + (r2 * r2)) > limiar) {
			convolucao.put(lin, col, black);
		} else {
			convolucao.put(lin, col, white);
		}
	}

	private void media(int lin, int col) {
		double r = 0, g = 0, b = 0, rgb[] = { 0, 0, 0 };

		for (int i = lin - raio; i <= lin + raio; i++) {
			if (i < 0 || i >= this.lin)
				continue;
			for (int j = col - raio; j <= col + raio; j++) {

				if (j == this.col || j < 0) {
					continue;
				}

				rgb = imagem.get(i, j);
				r += rgb[0] / (qtdElementos);
				g += rgb[1] / (qtdElementos);
				b += rgb[2] / (qtdElementos);
//				System.out.println("\n[i: "+(i)+" col: "+(j)+"]");
//				System.out.println("r: "+rgb[0]+"g: "+rgb[1]+"b: "+rgb[2]);
			}
		}
		rgb[0] = r;
		rgb[1] = g;
		rgb[2] = b;
		convolucao.put(lin, col, rgb);
	}

	private void mediana(int lin, int col) {
		double rgb[] = null;

		LinkedList<Double> r, g, b;
		r = new LinkedList<Double>();
		g = new LinkedList<Double>();
		b = new LinkedList<Double>();

		for (int i = lin - raio; i <= lin + raio; i++) {
			if (i < 0 || i >= this.lin)
				continue;
			for (int j = col - raio; j <= col + raio; j++) {

				if (j == this.col || j < 0) {
					continue;
				}

				rgb = imagem.get(i, j);
				r.add(rgb[0]);
				g.add(rgb[1]);
				b.add(rgb[2]);
//				System.out.println("\n[i: "+(i)+" col: "+(j)+"]");
//				System.out.println("r: "+rgb[0]+"g: "+rgb[1]+"b: "+rgb[2]);
			}
		}
		r.sort(this);
		rgb[0] = r.get(r.size() / 2);
		g.sort(this);
		rgb[1] = g.get(g.size() / 2);
		b.sort(this);
		rgb[2] = b.get(b.size() / 2);

		convolucao.put(lin, col, rgb);
	}

	public int compare(Double i, Double ii) {

		if (i < ii) {
			return 1;
		}
		return 0;
	}
}
