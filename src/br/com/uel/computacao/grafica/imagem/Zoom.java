package br.com.uel.computacao.grafica.imagem;

import org.opencv.core.Mat;

public class Zoom {
	private Mat imagem;
	private int lin, col;
	
	
	public Zoom(Mat imagem) {
		this.imagem = imagem;
		
	}

	public  Mat zoomOutLinear() {
		lin = imagem.rows() ;
		col = imagem.cols() ;
		Mat zoom = new Mat(lin/2,col/2,imagem.type());
		
		for(int m = 0 ; m + 1 < lin ; m+=2){
			for(int n = 0 ; n + 1  < col ; n+=2) {
				
				double rgb[] = calcularQuadrado(m,n);
				
				zoom.put(m/2, n/2, rgb);
			}
		}
		return zoom;		
	}
	public  Mat zoomOutQuadrado() {
		int lin = imagem.rows() ;
		int col = imagem.cols() ;
		Mat zoom = new Mat(lin/2,col/2,imagem.type());
		
		for(int m = 0 ; m <lin ; m+=2){
			for(int n = 0 ; n < col ; n+=2) {
				zoom.put(m/2,n/2,imagem.get(m,n));

			}
		}
		return zoom;
	}
	public Mat zoomInQuadrado() {
		lin = imagem.rows() ;
		col = imagem.cols() ;
		Mat zoom = new Mat(lin*2,col*2,imagem.type());
		
		for(int m = 0 ; m <lin ; m++){
			for(int n = 0 ; n < col ; n++) {
				zoom.put(2*m,2*n,imagem.get(m,n));
				zoom.put(2*m+1,2*n,imagem.get(m,n));
				zoom.put(2*m,2*n+1,imagem.get(m,n));
				zoom.put(2*m+1,2*n+1,imagem.get(m,n));

			}
		}
		return zoom;
	}
	public Mat zoomInLinear() {
		lin = imagem.rows() ;
		col = imagem.cols() ;
		Mat zoom = new Mat(lin*2,col*2,imagem.type());
		for(int i = 0 ; i <lin ; i++){
			for(int j = 0 ; j < col ; j++) {
				zoom.put(2*i,2*j,imagem.get(i,j));
			}
		}
		lin *=2;
		col *=2;
		
		for(int i = 0 ; i < lin  ; i += 2) {
			for (int j = 0 ; j < col ; j += 2) {
				if(j+2< col ) {
					double rgb1[] = zoom.get(i,j);
					double rgb2[] = zoom.get(i, j+2);
					rgb1[0] = ( rgb1[0] + rgb2[0] ) / 2;
					rgb1[1] = ( rgb1[1] + rgb2[1] ) / 2;
					rgb1[2] = ( rgb1[2] + rgb2[2] ) / 2;
					zoom.put(i, j +1,zoom.get(i,j));
					zoom.put(i,j+2 ,rgb1);
					continue;
				}
				if( j + 1 < col) {
					zoom.put(i, j +1,zoom.get(i,j));
					continue;
				}
				
				
			}
		}
		
		for(int j = 0 ; j < col; j += 1) {
			for (int i = 0 ; i < lin ; i += 2) {
				if(i + 2 < lin) {
					double rgb1[] = zoom.get(i,j);
					double rgb2[] = zoom.get(i+2,j);
					rgb1[0] = ( rgb1[0] + rgb2[0] ) / 2;
					rgb1[1] = ( rgb1[1] + rgb2[1] ) / 2;
					rgb1[2] = ( rgb1[2] + rgb2[2] ) / 2;
					zoom.put(i+1,j,zoom.get(i,j));
					zoom.put(i+2,j ,rgb1);
				}
				else if( i + 1 < lin) {
					zoom.put(i+2,j,zoom.get(i,j));
					continue;
				}
			}
		}
		return zoom;
		
	}
	private double[] calcularQuadrado(int m, int n) {
		double rgbI[]= imagem.get(m , n);
		double rgbII[] = imagem.get(m+1 , n);
		double rgbIII[] = imagem.get(m , n+1);
		double rgbIV[] = imagem.get(m+1, n+1);
		double resp[] = imagem.get(m,n);
		resp[0] = ( rgbI[0]+ rgbII[0] + rgbIII[0]+rgbIV[0] ) / 4;
		resp[1] = ( rgbI[1]+ rgbII[1] + rgbIII[1]+rgbIV[1] ) / 4;
		resp[2] = ( rgbI[2]+ rgbII[2] + rgbIII[2]+rgbIV[2] ) / 4;
		return resp;
	}
	
}


