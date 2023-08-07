package baek;

import java.util.Scanner;

public class Baek_2164 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int i = 0;
		double result = Math.pow(2, i);
		double check = 0;
		while (check <= N) {
			check = Math.pow(2, i);
			if (check <= N) {
				result = check;
			}
			i += 1;
		}
		System.out.println((int) result);
	}
}
