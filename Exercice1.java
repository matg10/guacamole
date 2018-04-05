package tp1;

import java.util.Scanner;

/**
 * Lire grâce à l’entrée standard deux entiers x et y et afficher leur somme : «
 * la somme des entiers x et y vaut : somme »
 * 
 * @author ENSG / DEI
 *
 */
public class Exercice1 {

	public static void main(String[] args) {
		// Création d'un objet Scanner
		Scanner scan = new Scanner(System.in);
		// On demande à saisir le premier entier
		System.out.println("Entier x ?");
		int x = scan.nextInt();
		scan.nextLine(); // pour prendre en compte le saut de ligne (caracère \n associé à la touche entrée)
		
		System.out.println("Entier y ?");
		int y = scan.nextInt();
		scan.nextLine(); 
		
		int somme = x + y;
		System.out.println("La somme des entiers x (" + x + ") et y (" + y + ") vaut " + somme);
		scan.close(); // pour fermer la connection vers l'entrée standard (pour faire propre)
	}

}
