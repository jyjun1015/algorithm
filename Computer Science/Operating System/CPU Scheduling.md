# CPU Scheduling

<br>

## 1. 스케줄링

> CPU 를 잘 사용하기 위해 프로세스를 잘 배정

- 조건 : 오버헤드 ↓ / 사용률 ↑ / 기아 현상 ↓
- 목표
    1. `Batch System`: 가능하면 많은 일을 수행. 시간(time) 보단 처리량(throughout)이 중요
    2. `Interactive System`: 빠른 응답 시간. 적은 대기 시간.
    3. `Real-time System`: 기한(deadline) 맞추기.

## 2. 선점 / 비선점 스케줄링

  ### 선점 (preemptive) : OS가 CPU의 사용권을 선점할 수 있는 경우, 강제 회수하는 경우 (처리시간 예측 어려움)
    - FCFS
    - SJF
    - HRN
  ### 비선점 (nonpreemptive) : 프로세스 종료 or I/O 등의 이벤트가 있을 때까지 실행 보장 (처리시간 예측 용이함)
    - Priority Schediuling
    - Round Robin
    - Multilevel-Queue
