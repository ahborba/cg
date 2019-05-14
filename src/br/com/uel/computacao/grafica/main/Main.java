package br.com.uel.computacao.grafica.main;

import java.util.Scanner;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;

import br.com.uel.computacao.grafica.imagem.Convolucao;
import br.com.uel.computacao.grafica.imagem.Imagem;

public class Main {
	public static Mat saida;
	public static String path = "./.images/", nome = "tony.jpg", extensao = "jpg";
	public static double angulo;
	public static String metodo = "mediana";
	public static Mat mat;
	public static int qtd = 1;
	public static double limiar = 100;

	public static void main(String[] args) {
		System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
			lerArquivo();

			Imagem imagem = new Imagem(mat);

			saida = imagem.convolucao(mat, metodo);
			System.out.println("Resultado salvo em: " + path + metodo +"-"+nome);
			Imgcodecs.imwrite(path + metodo +"-"+nome, saida);
		
	}

	private static void lerArquivo() {
		Scanner sc = new Scanner(System.in);

		System.out.print("Digite o diretorio do arquivo: ");
		path = sc.nextLine();

		System.out.print("Digite o nome do arquivo: ");
		nome = sc.nextLine();
		extensao = nome.split("\\.")[1];

		System.out.print("Escolha o metodo de convolucao: \n - sobel\n - media\n - mediana\nsua escolha: ");
		metodo = sc.nextLine();

		if (metodo.equals("sobel")) {
			System.out.print("Insira o limiar desejado: ");
			Convolucao.limiar = sc.nextDouble();
		}

		sc.close();

		if (path.charAt(path.length() - 1) != '/') {
			path += "/";
		}
		System.out.println("Abrindo a imagem : " + path + nome);
		mat = Imgcodecs.imread(path + nome);

	}
}
