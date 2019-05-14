package br.com.uel.computacao.grafica.imagem;

public class Pixel {
	public Pixel(double r, double g, double b,int x, int y) {
		this.r = (int) r;
		this.g = (int)g;
		this.b = (int)b;
		this.x = x;
		this.y = y;
	}
	public Pixel() {}
	public int soma;
	public int x;
	public int y;
	public int r;
	public int g;
	public int b;
}
