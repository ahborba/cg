package br.com.uel.computacao.grafica.imagem;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;

import org.opencv.core.Mat;

public class Convolucao implements Comparator<Pixel> {
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

		for (int i = 0; i < lin; i++) {
			for (int j = 0; j < col; j++) {
//				System.out.println("pixel: ["+i+","+j+"]");
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
			sobel(i+1, j+1);
			break;
		case "media":
			media(i+1, j+1);
			break;
		case "mediana":
			mediana(i, j);
			break;
		default:
			erro = true;
			return;
		}
//		System.out.println("===========================================================================");
	}

	private void sobel(int lin, int col) {
		double r1, r2;
		r1 = r2 = 0;
		double r_R1, r_R2, g_R1, g_R2, b_R1, b_R2;

		r_R1 = r_R2 = g_R1 = g_R2 = b_R1 = b_R2 = 0;

		for (int k = -1, i = 0; k < 2; k++, i++) {
			if (lin + k == this.lin) {
				break;
			}
			for (int n = -1, j = 0; n < 2; n++, j++) {
//				System.out.println("if: "+( col + n > this.col));
				if (col + n >= this.col) {
					break;
				}
				double rgb[] = imagem.get(lin + k, col + n);

//				System.out.print("R1: ["+rgb[0]+","+rgb[1]+","+rgb[2]+"] ->"+"["+ rgb[0] * sobelR1[i][j]+","+rgb[1]* sobelR1[i][j]+","+rgb[2]* sobelR1[i][j]+"]");
//				System.out.print("R2: ["+rgb[0]+","+rgb[1]+","+rgb[2]+"] ->"+"["+ rgb[0] * sobelR2[i][j]+","+rgb[1]* sobelR2[i][j]+","+rgb[2]* sobelR2[i][j]+"]");
				r_R1 += rgb[0] * sobelR1[i][j];
				r_R2 += rgb[0] * sobelR2[i][j];
				g_R1 += rgb[1] * sobelR1[i][j];
				g_R2 += rgb[1] * sobelR2[i][j];
				b_R1 += rgb[2] * sobelR1[i][j];
				b_R2 += rgb[2] * sobelR2[i][j];

			}
//			System.out.println();
		}

		r1 = (r_R1 + g_R1 + b_R1) / 3;
		r2 = (r_R2 + g_R2 + b_R2) / 3;
//		System.out.println("R1="+r1+"\tR2="+r2);

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
		
		double lista[] = new double[9];

		// percorre a vizinhança do pixel
		for (int i = lin - raio; i <= lin + raio; i++) {
			if (i < 0 || i >= this.lin)
				continue;
			for (int j = col - raio; j <= col + raio; j++) {

				if (j == this.col || j < 0) {
					continue;
				}
				Arrays.fill(lista,(int)rgb[0]+rgb[1]+rgb[2]);
				rgb = imagem.get(i, j);
//				lista.add((int)rgb[0]+rgb[1]+rgb[2]);
//				System.out.print("i: "+i+"[r:"+lista.get(lista.size()-1).r+","+"g:"+lista.get(lista.size()-1).g+",b:"+lista.get(lista.size()-1).b+"]");
//				System.out.print("[i: "+(i)+" col: "+(j)+"]");
			}
//			System.out.println();
		}
		Arrays.sort(lista);

		
//		System.out.println("\n[r:"+lista.get(lista.size()/2).r+","+"g:"+lista.get(lista.size()/2).g+",b:"+lista.get(lista.size()/2).b+"]");
//		System.out.println(lista.size()/2);	
//		Pixel pixel = lista.get(lista.size()/2);
//		rgb = imagem.get(pixel.x,pixel.y);
		convolucao.put(lin, col, rgb);
	}


	@SuppressWarnings("unused")
	private void distanciaCor(int lin, int col) {
		double r1, r2;
		r1 = r2 = 0;
		double r_R1, r_R2, g_R1, g_R2, b_R1, b_R2;

		r_R1 = r_R2 = g_R1 = g_R2 = b_R1 = b_R2 = 0;

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

				r_R1 += rgb[0] * sobelR1[i][j];
				r_R2 += rgb[0] * sobelR2[i][j];
				g_R1 += rgb[1] * sobelR1[i][j];
				g_R2 += rgb[1] * sobelR2[i][j];
				b_R1 += rgb[2] * sobelR1[i][j];
				b_R2 += rgb[2] * sobelR2[i][j];

//				r1 += ((rgb[0] + rgb[1] + rgb[2]) / 3) * sobelR1[i][j];
//				r2 += ((rgb[0] + rgb[1] + rgb[2]) / 3) * sobelR2[i][j];

			}
		}
	}

	@Override
	public int compare(Pixel p1, Pixel p2) {

		if(p1.r + p1.g + p1.b > p2.r +p2.g + p2.b) {
		return 0;			
	}else {
		return 1;
	}
		
//		if(p1.r > p2.r && p1.g > p2.g && p1.b > p2.b) {
//			return 0;			
//		}else {
//			return 1;
//		}
	}
}
