package br.com.uel.computacao.grafica.imagem;

import org.opencv.core.Mat;

public class Esqueletizacao {
	


	private boolean verificaImagemCorroida(Mat im) {
		boolean pixelBranco = false;
		for (int i = 1; i < im.height() - 1; i++) {
			for (int j = 0; j < im.width(); j++) {
				double[] rgb = im.get(i, j);
				pixelBranco = verificaRgb(rgb, 255);
				if (pixelBranco == true)
					return false;
			}
		}
		return true;
	}

	public Mat erosao(Mat imagem) {
		Mat erosao = imagem.clone();
		
		double[] white = { 255, 255, 255 };
		double[] black = { 0, 0, 0 };
		
		
		int lin,col;
		lin = imagem.height();
		col = imagem.width();
		erosao = imagemBranca(erosao);

		for (int i = 1; i < lin - 1; i++) {
			for (int j = 1; j < col - 1; j++) {
				// *
				//***
				// *
				double[] rgb1 = imagem.get(i - 1, j);
				double[] rgb2 = imagem.get(i, j);
				double[] rgb3 = imagem.get(i + 1, j);
				double[] rgb4 = imagem.get(i, j - 1);
				double[] rgb5 = imagem.get(i, j + 1);

				if (verificaRgb(rgb1, 255) && verificaRgb(rgb2, 255) && verificaRgb(rgb3, 255)
						&& verificaRgb(rgb4, 255) && verificaRgb(rgb5, 255) && i - 1 != 0
						&& i + 1 != imagem.height() && j - 1 != 0 && j + 1 != imagem.width()) {
					erosao.put(i, j, black);

				} else {
					erosao.put(i, j, white);
				}
			}
		}
		return erosao;
	}

	public static boolean difCores(double[] rgb, double[] rgbAb) {
		if (rgb[0] != rgbAb[0]) {
			return true;
		} else {
			return false;
		}
	}

	public static void diferencaImagem(Mat im,Mat imAb) {
//		Mat imDif = im.clone();
		Mat imDif = new Mat(im.rows() , im.cols() , im.type());
		double []white = {255,255,255};
		for(int i = 0; i < im.height(); i++) {
			for(int j = 0 ; j < im.width(); j++) {
				imDif.put(i, j, white);
			}
		}
	}

	private boolean verificaRgb(double[] rgb, int valorCor) {
		if (rgb[0] != valorCor || rgb[1] != valorCor || rgb[2] != valorCor) {
			return true; // � diferente de branco!
		} else {
			return false; // � igual a branco!
		}
	}

	public Mat dilatacao(Mat imagem) {
		Mat dilatacao = imagem.clone();
		double[] black = { 0, 0, 0 };

		dilatacao = imagemBranca(dilatacao);

		for (int i = 1; i < imagem.height() - 1; i++) {
			for (int j = 1; j < imagem.width() - 1; j++) {
				double[] rgb2 = imagem.get(i, j);

				if (verificaRgb(rgb2, 255)) {
					dilatacao.put(i, j, black);

					dilatacao.put(i - 1, j, black);
					dilatacao.put(i + 1, j, black);
					dilatacao.put(i, j - 1, black);
					dilatacao.put(i, j + 1, black);

				} else {

				}
			}
		}
		return dilatacao;
	}

	public Mat abertura(Mat imagem) {
		Mat abertura = imagem.clone();
		abertura = erosao(abertura);
		abertura = dilatacao(abertura);
		return abertura;
	}

	public Mat fechamento(Mat imagem) {
		Mat fechamento = imagem.clone();
		fechamento = dilatacao(fechamento);
		fechamento = erosao(fechamento);
		return fechamento;
	}


	
	
	public Mat esqueletoLantueJoul(Mat imagem) {
		
		
		
		Mat esqueleto = imagem.clone();
		int i = 0;
		do {
			System.out.println("iniciando: "+ i++);

			Mat abertura = abertura(esqueleto);

			System.out.println("realizada a abertura.");
			diferencaImagem(esqueleto, abertura);
			System.out.println("imagem diferenciada");
			esqueleto = erosao(esqueleto);
			System.out.println("realizada a corosao");
		}while (verificaImagemCorroida(esqueleto));
		
		
		return esqueleto;

	}
	
	
	private Mat imagemBranca(Mat imagem) {

		double[] white = { 255, 255, 255 };
		for (int i = 0; i < imagem.height(); i++) {
			for (int j = 0; j < imagem.width(); j++) {
				imagem.put(i, j, white);
			}
		}
		return imagem;
	}
}
