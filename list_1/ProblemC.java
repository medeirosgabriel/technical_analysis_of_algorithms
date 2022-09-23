package first_list;

import java.util.Arrays;
import java.util.Scanner;

public class ProblemC {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int tests = input.nextInt();
		input.nextLine();
		
		for (int i = 0; i < tests; i++) {
			long[] ns = Arrays.stream(input.nextLine().split(" ")).mapToLong(Long::parseLong).toArray();
			long n = ns[0], steps = ns[1];
			long[] florest = Arrays.stream(input.nextLine().split(" ")).mapToLong(Long::parseLong).toArray();
			long sum = 0, result = 0;
			if (steps < n) {
				for (int j = 0; j < steps; j++) {
					sum += florest[j];
				}
				result = sum;
				for (long j = steps; j < n; j++) {
					sum += florest[(int) j];
					sum -= florest[(int) (j - steps)];
					result = Math.max(result, sum);
				}
				result += (steps*(steps-1))/2; // (n * (n - 1))/2 = a0 + a1 + a2 + a3 + ... + an
				System.out.println(result);
			} else {
				result = (n*(steps-n)) + ((n*(n-1))/2);
				for (int j = 0; j < n; j++) {
					result += florest[j];
				}
				System.out.println(result);
			}
		}
	}
}
