package first_list;

import java.util.Arrays;
import java.util.Scanner;

public class ProblemB {
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		long[] array = Arrays.stream(input.nextLine().split(" ")).mapToLong(Long::parseLong).toArray();
		long n = array[0], total = array[1], r = 0, i = 0;
		
		while (total > 0) {
			if (n <= total) {
				total -= n;
				r += 1;
			} else {
				n -= 1;
			}
		}
		
		System.out.println(r);
		
		/*
		if (total % n == 0) {
			System.out.println(total/n);
		} else {
			System.out.println(total/n + 1);
		}
		*/
	}
}
