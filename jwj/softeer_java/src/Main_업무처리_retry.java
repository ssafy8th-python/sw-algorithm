import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_업무처리_retry {
	static int H;
	static int K;
	static int R;
	
	static Tree [] tree;
	
	static int answer;
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		H = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		
		tree = new Tree[(int)Math.pow(2, H+1)];
		
		init(1, 0);
		
		for (int i = (int)Math.pow(2, H); i < (int)Math.pow(2, H+1); i++) {
			st = new StringTokenizer(br.readLine());
			for (int k = 0; k < K; k++) {
				tree[i].job.offer(Integer.parseInt(st.nextToken()));
			}
		}
		
		answer = 0;
		
		for (int r = 1; r <= R; r++) {
			work(1, r, 0);
		}
		
		System.out.println(answer);
		
	}
	
	static void work(int index, int r, int depth) {
		if (depth > H) return;
		
		Tree worker = tree[index];
		
		if (depth == H && !worker.job.isEmpty()) {
			int job = worker.job.poll();
			if (index % 2 == 0) tree[index / 2].leftJob.offer(job);
			else tree[index / 2].rightJob.offer(job);
		} else if (depth < H && r % 2 == 0 && !worker.rightJob.isEmpty()) {
			int job = worker.rightJob.poll();
			if (index == 1) {
				answer += job;
			} else {
				if (index % 2 == 0) tree[index / 2].leftJob.offer(job);
				else tree[index / 2].rightJob.offer(job);
			}
			
		} else if (depth < H && r % 2 == 1 && !worker.leftJob.isEmpty()) {
			int job = worker.leftJob.poll();
			if (index == 1) {
				answer += job;
			} else {
				if (index % 2 == 0) tree[index / 2].leftJob.offer(job);
				else tree[index / 2].rightJob.offer(job);
			}
		}
		
		work(index * 2, r, depth + 1);
		work(index * 2 + 1, r, depth + 1);
	}
	
	static void init(int index, int depth) {
		if (depth > H) return;
		
		tree[index] = new Tree(depth);
		
		init(index * 2, depth + 1);
		init(index * 2 + 1, depth + 1);
	}
	
	
	static class Tree {
		int depth;
		Queue<Integer> job;
		Queue<Integer> leftJob;
		Queue<Integer> rightJob;
		
		Tree(int depth){
			this.depth = depth;
			
			initJob();
		}
		
		void initJob(){
			if (depth == H) {
				job = new LinkedList<>();
			} else {
				leftJob = new LinkedList<>();
				rightJob = new LinkedList<>();
			}
			
		}
		
		
	}

}
