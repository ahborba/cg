package br.com.uel.computacao.grafica.imagem;

import org.opencv.core.Mat;
import org.opencv.imgproc.Imgproc;

public class Contraste {
	private double[] histograma;
	private Mat resposta;
	private Mat cinza;
	private Mat colorida;
	private int linha, coluna;
	private Mat imagem;
	
	public Contraste(Mat normal) {
		this.imagem = normal;
		histograma = new double[256];
	}
	
	public Mat obterContrasteCinza() {
		resposta = new Mat(imagem.height(),imagem.width(),imagem.type());
		cinza = imagem.clone();
		Imgproc.cvtColor(imagem, cinza, Imgproc.COLOR_RGB2GRAY);
		linha = cinza.rows();
		coluna = cinza.cols();
		obterHistograma(linha,coluna);
		obterHistogramaProbabilidade(linha*coluna);
		obterSomaProbabilidade();
		obterHistogramaFinal();
		converterImagemCinza(linha,coluna);
		return resposta;

	}
	public Mat obterContrasteColorido() {
		colorida = imagem.clone();
		Imgproc.cvtColor(imagem, colorida, Imgproc.COLOR_BGR2YUV);
		resposta = new Mat(colorida.height(),colorida.width(),colorida.type());
		
		linha = colorida.rows();
		coluna = colorida.cols();
		
		obterHistogramaCor(linha,coluna);
		obterHistogramaProbabilidade(linha*coluna);
		obterSomaProbabilidade();
		obterHistogramaFinal();
		converterImagemColorida(linha,coluna);
		Imgproc.cvtColor(resposta, colorida, Imgproc.COLOR_YUV2BGR);
		return colorida;
	}
	private void converterImagemColorida(int linha, int coluna) {
		for(int m = 0 ; m < linha ; m++) {
			for(int n = 0 ; n < coluna ; n++) {
				double[]yuv = colorida.get(m, n);
				yuv[0] = histograma [(int) yuv[0]];
				resposta.put(m, n, yuv);
			}
		}
	}
	private void obterHistograma(int linha, int coluna) {
		for(int m = 0 ; m < linha ; m++) {
			for(int n = 0 ; n < coluna ; n++) {
				double[]rgb  = cinza.get(m, n);
				histograma[(int) rgb[0]] = histograma[(int) rgb[0]] + 1;
			}
		}
	}
	private void obterHistogramaProbabilidade(int total) {
		for (int i = 0 ; i < 256 ; i++) {
			histograma[i] = histograma[i] / total;

		}
	}
	private void obterSomaProbabilidade() {
		for (int i = 1 ; i < 256 ; i++) {
			histograma[i] = histograma[i] + histograma[i-1];
		}
		
	}
	private void obterHistogramaFinal() {
		for (int i = 1 ; i < 256 ; i++) {
			histograma[i] = histograma[i] * 255;
		}
	}
	private void converterImagemCinza(int linha, int coluna) {
		System.out.println();
		for(int m = 0 ; m < imagem.height() ; m++) {
			for(int n = 0 ; n < imagem.width() ; n++) {
				double[]rgb = imagem.get(m, n);
				rgb[0] = histograma[(int) rgb[0]];
				rgb[1] = histograma[(int) rgb[1]];
				rgb[2] = histograma[(int) rgb[2]];
				resposta.put(m, n,rgb);
			}
		}
	}
	
	public void obterHistogramaCor(int linha, int coluna) {		
		//fazendo a contagem de cada quantidade de cor
		for(int m = 0; m < linha; m++) {
			for(int n = 0; n < coluna; n++) {
				double[] yuv = colorida.get(m,n);
				histograma[(int)yuv[0]] = histograma[(int)yuv[0]] + 1;	
			}
		}					
	}
	
}
