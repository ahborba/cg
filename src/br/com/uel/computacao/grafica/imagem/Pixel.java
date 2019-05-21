package br.com.uel.computacao.grafica.imagem;

public class Pixel {
	public int x;
	public int y;
	private double[] rgb = new double [3];	
	public Pixel(int x , int y ,double [] rgb) {
		this.x = x ;
		this.y = y;
		this.rgb = rgb;
	}
	public Pixel() {}
	public int getX() {
		return x;
	}
	public void setX(int x) {
		this.x = x;
	}
	public int getY() {
		return y;
	}
	public void setY(int y) {
		this.y = y;
	}
	public double getR() {
		return rgb[0];
	}
	public double getG() {
		return rgb[1];
	}
	public double getB() {
		return rgb[2];
	}
	public void setR(double r) {
		this.rgb[0] = r;
	}
	public void setG(double g) {
		this.rgb[1] = g;
	}
	public void setB(double b) {
		this.rgb[2] = b;
	}
	
}
