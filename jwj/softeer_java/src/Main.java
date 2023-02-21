import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int result;

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		
		int[][] tree = new int[N+1][N+1]; 
		
		for (int i = 1; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int distance = Integer.parseInt(st.nextToken());
			
			tree[start][end] = distance;
			tree[end][start] = distance;
			}
		
		// dfs를 통해 백트래킹 할 때마다 값을 더해 줘서 모든 거리를 구하겠다.
		for (int i = 1; i <= N; i++) {
			result = 0;
			boolean [] visited = new boolean[N+1];
			visited[i] = true;
			dfs(i, tree, visited, 0);
			System.out.println(result);
		}
		
	}
	
	static void dfs(int start, int tree[][], boolean visited[], int sum) {
		
		for (int i = 1; i <= N; i++) {
			if (tree[start][i] != 0 && ! visited[i]) {
				visited[i] = true;
				result += sum + tree[start][i];
				dfs(i, tree, visited, sum + tree[start][i]);
			}
		}
		
	}

}
