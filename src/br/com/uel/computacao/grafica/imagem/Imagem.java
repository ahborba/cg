package br.com.uel.computacao.grafica.imagem;

import java.util.Scanner;

import org.opencv.core.Mat;

public class Imagem {

	private Contraste contraste;
	private Zoom zoom;
	private Esqueletizacao esqueleto;
	private Transformacao transformacao;
	private Convolucao conv;
	int linha, coluna;

	public Imagem(Mat img) {
	}

	public Mat ZoomInLinear(Mat imagem) {
		zoom = new Zoom(imagem);
		return zoom.zoomInLinear();
	}

	public Mat ZoomOutLinear(Mat imagem) {
		zoom = new Zoom(imagem);
		return zoom.zoomOutLinear();
	}

	public Mat ZoomInQuadrado(Mat imagem) {
		zoom = new Zoom(imagem);
		return zoom.zoomInQuadrado();
	}

	public Mat ZoomOutQuadrado(Mat imagem) {
		zoom = new Zoom(imagem);
		return zoom.zoomInQuadrado();
	}

	public Mat contrasteCinza(Mat imagem) {
		contraste = new Contraste(imagem);
		return contraste.obterContrasteCinza();
	}

	public Mat contrasteColorido(Mat imagem) {
		contraste = new Contraste(imagem);
		return contraste.obterContrasteColorido();
	}

	public Mat esqueletizacao(Mat imagem) {
		esqueleto = new Esqueletizacao();
		return esqueleto.esqueletoLantueJoul(imagem);
	}

	public Mat abertura(Mat imagem) {
		esqueleto = new Esqueletizacao();
		return esqueleto.abertura(imagem);
	}

	public Mat fechamento(Mat imagem) {
		esqueleto = new Esqueletizacao();
		return esqueleto.fechamento(imagem);
	}

	public Mat rotacao(Mat imagem, double angulo) {
		transformacao = new Transformacao(imagem);
		return transformacao.rotacao(angulo);
	}

	public Mat translacao(Mat imagem, int x, int y) {
		transformacao = new Transformacao(imagem);
		return transformacao.transfTranslacao(x, y);
	}

	public Mat cinza(Mat imagem) {
		transformacao = new Transformacao(imagem);
		return transformacao.cinza(imagem);
	}

	public Mat erosao(Mat imagem) {
		esqueleto = new Esqueletizacao();
		return esqueleto.erosao(imagem);
	}

	public Mat dilatacao(Mat imagem) {
		esqueleto = new Esqueletizacao();
		return esqueleto.dilatacao(imagem);
	}

	public Mat convolucao(Mat imagem, String metodo) {
		conv = new Convolucao(imagem);
		return conv.convolucao(metodo);

	}
}
