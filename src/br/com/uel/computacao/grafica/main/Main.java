package br.com.uel.computacao.grafica.main;

import java.util.Scanner;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

import br.com.uel.computacao.grafica.imagem.Imagem;

public class Main {
	public static Mat saida;
	public static String path = "/home/ahborba/workspace/eclipse/cg/.images", nome, extensao;
	public static double angulo;
	public static Mat mat;
	
	public static void main(String[] args) {
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
		lerArquivo();
		
		Imagem imagem = new Imagem(mat);

		
		System.out.println(path+"saida."+extensao);
		Imgcodecs.imwrite(path+"saida"+"."+extensao,saida );
	}

	private static void lerArquivo() {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Digite o diretorio do arquivo: ");
		path = sc.nextLine();
		
		System.out.print("Digite o nome do arquivo: ");
		nome = sc.nextLine();
		extensao = nome.split("\\.")[1];
		
		System.out.print("Digite o angulo: ");
		angulo= Double.parseDouble(sc.nextLine());
		sc.close();
		
		
		if(path.charAt(path.length()-1) != '/') {
			path += "/";			
		}
		System.out.println(path+nome);
		
		mat = Imgcodecs.imread(path + nome);
		
	}
}
