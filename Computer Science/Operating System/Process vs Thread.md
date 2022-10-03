### 프로세스 & 스레드
> 프로세스 : 프로그램을 메모리 상에서 실행중인 작업
> 스레드 : 프로세스 안에서 실행되는 여러 흐름 단위

기본적으로 프로세스마다 최소 1개의 스레드를 소유 

#### 프로세스 
* Code : 코드 자체를 구성하는 메모리 영역(프로그램 명령)
* Data : 전역변수, 정적변수, 배열 등
  * 초기화 된 데이터는 Data 영역에 저장
  * 초기화 되지 않은 데이터는 bss 영역에 저장 
* Heap : 동적 할당 시 사용(new(), malloc() 등)
* Stack : 지역변수, 매개변수, 리턴 값 (임시 메모리 영역) 

#### 스레드
* 스레드는 Stack만 각각 할당 받고 나머지 영역은 공유

 => 프로세스는 고유 공간과 자원을 할당받아 사용하지만 스레드는 공간과 자원을 공유하면서 사용하는 차이 존재 

#### 멀티프로세스 
> 하나의 컴퓨터에 여러 CPU 장착 -> 하나 이상의 프로세스들을 동시에 처리(병렬)
**장점** : 안전성 (메모리 침범 문제를 OS 에서 해결)**
**단점** : 독립된 메모리 영역을 갖고 있어, 작업량이 많을수록 오버헤드 발생, Context Switching으로 인한 성능 저하
 * Context Switching : 프로세스의 상태 정보를 저장하고 복원하는 일련의 과정(캐시 메모리 초기화)

#### 멀티스레드
> 하나의 응용 프로그램에서 여러 스레드를 구성해 각 스레드가 하나의 작업을 처리
**장점** : 공유 메모리만큼의 시간, 자원 손실이 감소하여 전역 변수와 정적 변수에 대한 자료 공유 가능
**단점** : 하나의 스레드가 데이터 공간을 망가뜨리면, 모든 스레드가 작동 불능 상태
 * Critical Section 기법 사용 : 하나의 스레드가 공유 데이터 값을 변경하는 시점에 다른 스레드가 그 값을 읽으려할 때 발생하는 문제를 해결하기 위한 동기화 과정 