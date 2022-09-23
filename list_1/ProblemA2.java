package first_list;

import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.Collectors;

public class ProblemA2 {
	
	private static boolean stop = false;
	private static long[] out;
	private static long[] array;
	private static long[] possibleSolution;
	private static boolean[] visited;
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int n = input.nextInt();
		input.nextLine();
		
		array = Arrays.stream(input.nextLine().split(" ")).mapToLong(Long::parseLong).toArray();
		
		possibleSolution = new long[n];
		out = new long[n];
		visited = new boolean[n];
		
		// backtracking
		
		for (int pos = 0; pos < n; pos++) {
			out[0] = array[pos];
			solution(1, pos);
			if (stop) {
				break;
			}
		}
		
		// print response
		
		String result = Arrays.stream(out)
		        .mapToObj(String::valueOf)
		        .collect(Collectors.joining(" "));
		
		System.out.println(result);
	}
	
	private static void solution(int index, int pos) {
		
		if (index == array.length) {
			stop = true;
			for (int i = 1; i < array.length; i++) {
				out[i] = possibleSolution[i];
			}
		} else {
			for (int i = 0; i < array.length; i++) {
				if (stop) {
					break;
				} else if (!visited[i]) {
					if(array[pos] * 2 == array[i] || array[i] * 3 == array[pos]){
						visited[i] = true;
						possibleSolution[index] = array[i];
						solution(index + 1, i);
	                    visited[i] = false;
	                }
				}
			}
		}
	}
}
