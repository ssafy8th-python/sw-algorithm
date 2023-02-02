import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_업무처리 {
	static int H;
	static int K;
	static int R;
	static Worker [] worker;
	static int answer;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		H = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());
		
		worker = new Worker[(int)Math.pow(2, H+1)];
		
		//	인원 배치
		init(1, 0);
		
		// 말단 직원에게 작업 할당
		for (int i = (int)Math.pow(2, H); i< (int)Math.pow(2, H+1); i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < K; j++) {
				worker[i].jobs.offer(Integer.parseInt(st.nextToken()));
			}
		}
		
		
		answer = 0;
		// 작업 시작
		for(int i = 1; i <= R; i++) {
			work(1, i, 0);
		}
		
		System.out.println(answer);

	}
	
	static void work(int index, int day, int depth) {
		if (depth > H) return;
		
		Worker cur = worker[index];
		
		if (depth == H && !cur.jobs.isEmpty()) {
			int job = cur.jobs.poll();
			// index가 짝수면 왼쪽 작업에 할당
			// 홀수이면 오른쪽 작업에 할당
			if(index % 2 == 0) worker[index / 2].leftJobs.offer(job);
			else worker[index / 2].rightJobs.offer(job);
		} else if (depth < H && day % 2 == 0 && !cur.rightJobs.isEmpty()) {
			int job = cur.rightJobs.poll();
			if (index == 1) answer += job;
			else {
				if(index % 2 == 0) worker[index / 2].leftJobs.offer(job);
				else worker[index / 2].rightJobs.offer(job);
			}
		} else if (depth < H && day % 2 == 1 && !cur.leftJobs.isEmpty()) {
			int job = cur.leftJobs.poll();
			if (index == 1) answer += job;
			else {
				if(index % 2 == 0) worker[index / 2].leftJobs.offer(job);
				else worker[index / 2].rightJobs.offer(job);
			}
		}
		
		work(index * 2, day, depth + 1);
		work(index * 2 + 1, day, depth + 1);		
	}
	
	static void init(int index, int depth) {
		
		if(depth > H) return;
		
		worker[index] = new Worker(depth);
		
		init(index * 2, depth + 1);
		init(index * 2 + 1, depth + 1);
	}
	
	static class Worker {
		Queue<Integer> jobs;
		Queue<Integer> leftJobs;
		Queue<Integer> rightJobs;

		public Worker(int depth) {
			// 말단 노드면 업무를 저장할 큐 정의			
			// 말단이 아니면 왼쪽과 오른쪽에 업무를 저장할 큐 정의
			if (depth == H) {
				jobs = new LinkedList<>();
			} else {
				leftJobs = new LinkedList<>();
				rightJobs = new LinkedList<>();
			}		
		}
		
	}

}
