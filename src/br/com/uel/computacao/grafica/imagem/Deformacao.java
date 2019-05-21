package br.com.uel.computacao.grafica.imagem;


import org.opencv.core.Mat;

public class Deformacao {
	public static final int BAIXO = 0, CIMA = 1, DIREITA = 2, ESQUERDA = 3;
	private Mat imagem;
	int lin, col;
//	private Pixel origem;
	private double[] cor = new double[3];
	int distancia;
//	private LinkedList<Pixel> pilha  = new LinkedList<Pixel>(); 	
//	private LinkedList<Pixel> pintar  = new LinkedList<Pixel>(); 	

	public Deformacao(Mat imagem, int distancia, double[] cor,Pixel o) {
//		this.origem = o;
//		pilha.add(origem);
		this.imagem = imagem;
		this.cor = cor;
		this.distancia = distancia;
		lin = imagem.rows() - 1;
		col = imagem.cols() - 1;
//		System.out.println("Linhas: "+lin);
//		System.out.println("Colunas: "+col);
	}

	public Mat preenchimentoRecursivo(int x, int y,double [] rgb) {
		if(x > lin || y > col || x < 0 || y < 0 )
			return imagem;
		double[] rgbXY = imagem.get(x,y);
		if(rgbXY == null)
			return imagem;
		
		if(mesmaCor(rgbXY,rgb)) {
			imagem.put(x, y,cor);
			preenchimentoRecursivo(x - 1, y,rgb);
			preenchimentoRecursivo(x, y + 1,rgb);
			preenchimentoRecursivo(x + 1, y,rgb);
			preenchimentoRecursivo(x, y - 1,rgb);
		}
		return imagem;
	}

	public boolean mesmaCor(double[] rgbXY,double [] rgb) {
		if(	(rgbXY[0] >= rgb[0] - distancia) && (rgbXY[0] <= rgb[0] + distancia)){
			if(	(rgbXY[1] >= rgb[1] - distancia) && (rgbXY[1] <= rgb[1] + distancia)){
				if(	(rgbXY[2] >= rgb[2] - distancia) && (rgbXY[2] <= rgb[2] + distancia)){
					return true;
				}
			}
		}
		return false;
	}

}
