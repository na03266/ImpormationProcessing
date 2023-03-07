1. 요구사항 확인

1) 소프트웨어 개발 방법론

- 객체지향 설계 원칙(SOLID) : SRP, OCP, LSP, ISP, DIP

- 럼바우(Rumbaugh) 객체지향 분석 모델링
   객체(Object) ER、객체다이어그램 / 동적(Dynamic) 상태 흐름도 / 기능(Functional) 자료 흐름도

- 비용 산정 기법 : Loc(낙관치, 중간치, 비관치), man-mounth, cocomo(organic, semi-detached, embedded), putnam(주기 단계별 인력분포 가정), FP(기능점수)


2) 현행 시스템 분석

- 현행 시스템 파악 절차 : 구성/기능/인터페이스 >> 아키텍처 및 소프트웨어 구성 >> 하드웨어 및 네트워크 구성

- 소프트웨어 아키텍처 패턴 유형
   클라-서버, 계층화, 마스터-슬레이브, 파이프-필터, 피어투피어, 이벤트-버스, MVC, 등

- 디자인 패턴 유형
    생성    객체 인스턴스 생성에 관여, 클래스 정의와 객체 생성 방식을 구조화, 캡슐화 수행
    구조    더 큰 구조 형성 목적으로 클래스나 객체의 조합을 다룸
    행위    클래스나 객체들이 상호작용하는 방법과 역할 분담.
    클래스  클래스간 관련성(상속관계)(컴파일 타임에 정적으로 결정)
    객체    객체 간 관련성을 다루는 패턴(런타임에 동적으로 결정)

 - GoF의 디자인 패턴

    Builder         인스턴스 조립, 생성과 표기를 분리해서 복잡한 객체를 생성
    Prototype       기존 객체를 복제하여 객체를 생성
    Factory Method  상위 클래스에서 생성하는 인터페이스를 정의하고, 하위클래스에서 인스턴스를 생성하도록 하는 방식, 생성할 객체의 클래스를
                    국한하지 않고 객체를 생성
    Abstract Factory구체적인 클래스에 의존하지 않고 서로 관련있는 객체 조합을 만드는 인터페이스를 제공하는 패턴, 구체적인 구현은 Concrete 
                    Product 클래스에서 이루어짐 동일한 주제의 다른 팩토리를 묶음
    Singleton       전역변수를 사용하지 않고 객체를 하나만 생성하고 어디서든지 참조할 수 있도록 하는 패턴, 한클래스에 한 객체만 존재하도록 
                    제한.
    Bridge          기능클래스와 구현 클래스를 연결하고 구현부에서 추상 계층을 분리하여 추상화된 부분과 실제 구현 부분을 독립적으로 확장할 수 
                    있게함,구현 뿐 아니라, 추상화된 부분까지 변경해야 하는 경우 활용
    Decorator       기존에 구현되어 있는 클래스에 필요한 기능을 추가해 나가는 패턴
    Facade          복잡한 시스템에 대해 단순한 인터페이스를 제공해서 결합도를 낮추어 시스템 구조에 대한 파악을 쉽게 하는 패턴, 통합된 
                    인터페이스 제공
    Flyweight       클래스의 경량화를 목적으로 하는 디자인 패턴. 여러개의 가상 인스턴스를 제공
    Proxy           실체 객체에 대한 대리객체, 실체 객체에 대한 접근 이전에 필요한 행동을 취할 수 있게 만듦. 특정 객체로의 접근을 제어하기 
                    위한 용도로 사용
    Composite       객체들의 관계를 트리구조로 구성하여 부분-전체 계층을 표현하는 패턴
                    복합객체와 단일 객체를 동등하게 취급
    Adapter         기존에 생성된 클래스를 재사용할 수 있도록 중간에서 맞춰주는 역할을 하는 인터페이스를 만드는 패턴, 인터페이스가 호환되지 
                    않는 클래스들을 함께 이용할 수 있도록 타 클래스의 인터페이스를 기존 인터페이스에 덧씌움.
    Mediator        객체수가 너무 많으면 중간에 결합을 통제하고 지시하는 역할을 하는 중재자를 두고 중재자에게 모든 것을 요구하여 통신의 
                    빈도수를 줄이는 패턴, 상호작용의 유연한 변경을 지원
    Interpreter     언어의 다양한 해석, 구체적으로 구문을 나누고 각각의 해석을 맡는 클래스를 작성, 문법 자체를 캡슐화해서 사용
    Iterator        컬렉션 구현 방법을 노출시키지 않으면서도 그 집합체 안에 들어있는 모든 항목에 반복자를 사용하여 접근할 수 있는 패턴, 내부 
                    표현 방법을 노출하지 않고 복합객체 원소를 순차적으로 접근 가능하게 함
    Template Methord상위클래스에 추상메서드를 통에 기능의 골격을 제공하고, 하위 클래스에 세부처리를 구체화하는 방식. 상위 작업의 구조를 
                    바꾸지 않으면서 서브클래스로 작업의 일부분을 수행
    Observer        한 객체의 상태가 변하면 종속된 다른 객체에 연락이 가고 자동으로 내용이 갱신되는 방법
    State           객체의 상태에 따라 행위 내용을 변경
    Visitor         각 클래스 데이터 구조로부터 처리기능을 분리하여 별도의 클래스를 만들어 놓고 해당 클래스의 메서드가 각 클래스를 돌아다니며 
                    특정 작업을 수행하게 만드는 패턴
    Command         실행될 기능을 캡슐화 함으로 주어진 여러 기능을 실행할 수 있는 재사용 성이 높은 클래스를 설계하는 패턴
    Strategy        알고리즘 군을 정의하고 같은 알고리즘을 각각 하나의 클래스로 캡슐화한 다음, 필요할 때 서로 교환해서 사용할 수 있게 함
    Memento         클래스 설계 관점에서 객체의 정보를 저장할 필요가 있을 깨 적용하는 디자인 패턴, Undo 기능을 개발할 때 사용하는 패턴

    Chain of Responsibility
                    정적으로 어떤 기능에 대한 처리의 연결이 하드코딩 되어 있을 때 기능 처리의 연결 변경이 불가능한데, 이를 동적으로 연결되어있는 경우에 따라 다르게 처리될 수 있도록 연결한 디자인 패턴

3) 요구사항 확인
- 정형기술 검토 기법

    워크 스루 Work-Through  자료 사전 배포, 작성중에 검토하고 결함 찾기
                            정적, 명세, 결과, 코드 등을 여러 사람이 검토하게 하는 것
    인스펙션 Inspection     저자를 제외하고 전문가가 검사하는 공식적인 법

2. 화면 설계

1) UI 요구사항 확인

- UI 설계원칙 :직관성, 유효성, 학습성, 유연성

- UI 용어
    UX      사용자 경험, 느낌 반응 등
    UI      사용자 인터페이스
    CLI     Command Line Interface 문자열
    GUI     Graphical User Interface 그래픽(아이콘, 버튼, 문자)
    MUI     Menu User Interface 메뉴
    NUI     Natural User Interface 움직임(멀티터치, 동작)

 - UML(Unified Modelling Language)
     개념        객체 지향 시스템 개발을 위한 표준화된 모델링 언어
    구성요소    사물, 관계, 다이어그램
    관계        연관, 집합, 포함, 일반화, 의존, 실체화
    정적(구조적)클래스, 객체, 컴포넌트, 배치, 복합체구조, 패키지
    동적(행위적)유스케이스, 시퀀스, 커뮤니케이션, 상태, 활동, 타이밍

3. 데이터 입출력 구현

1) 논리데이터저장소 확인

- 데이터 모델
    구조        데이터 구조 및 정적 성질을 표현하는 요소
    연산        DB에 저장된 실제 데이터를 처라하는 작업에 대한 명세
    제약조건    DB에 저장 될 수 있는 실제 데이터의 논리적인 제약조건

- 데이터 모델 절차 : 요구사항 분석 >> 개념적 설계 >> 논리적 설계 >> 물리적 설계

- 관계 대수   Select : σ조건(R) // Project : π속성리스트(R) // Join : R⋈S  // Division : R÷S

- X(결정자) → Y(종속자) 

2)물리 데이터 저장소 설계

- 무결성(Integrity) 제약조건
    개체 (Entity)       기본키(Primary key)를 구성하는 모든 속성은 널(Null)이나 중복값을 가지면 안된다. (Unique Index)
    참조(Referential)   외래키(Foreign)는 참조할 수 없는 값을 가질 수 없다
    속성 (Attribute)    속성의 값은 기본값, 널 여부, 도메인이 지정된 규칙을 준수해야함 (Check, null, not null, default)
    사용자 정의         사용자의 의미적 요구사항 준수(Trigger, 사용자정의 데이터타입)
    키 (Key)            같은 킷값을 가진 튜플 허용 x(Unique)


3) 데이터베이스 기초 활용하기

- 시멘틱 웹(semantic web) : 온톨로지를 활용하여 서비스를 기술하고, 온톨로지의 의미적 상호 윤용성을 이용해서 서비스 검색, 조합, 중재 기능을 자동화하는 웹

- 온톨로지(Ontology) : 실세계에 존재하는 모든 개념들과 개념들의 속성, 그리고 개념들 간의 관계를 컴퓨터가 이해할 수 있도록 서술해 놓은 지식 베이스

- 맵리듀스 : 대용량 데이터 처리를 분산 병령 컴퓨팅에서 처리하기위해 제작된 프레임워크		Map : 입력레코드를 읽어 데이터 변형, Reduce : Map의 결과 집계

- Tajo : 맵리듀스 대신 SQL로 분산분석 작업을 하는 하둡 기반 데이터 웨어하우스 시스템

- Hadoop(High-Availability Distributed Object-Oriented Platform) : 구글의 GFS(Google File System)와 맵리듀스 등을 활용하여 구현한 자바 기반 분산 컴퓨팅 플랫폼

- HDFS(Hadoop Distributed File System) : 대용량 데이터 집합을 처리하는 응용 프로그램에 적합하도록 설계된 하둡 분산파일 시스템

- 데이터마이닝 : 대규모 데이터 안에서 자동으로 통계적 규칙이나 패턴을 찾아내는 기술

4. 통합 구현

1) 연계 매커니즘 구성

- 인스턴스 : 객체지향 프로그래밍에서 해당 클래스의 구조로 컴퓨터 저장공간에 할당된 실체

- WSDL(Web Service Description Language) : 웹 서비스명, 제공위치, 메시지 포맷, 프로토콜 정보 등 웹 서비스에 대한 상세 정보가 기술된 XML 형식 언어

- SOAP(Simple Object Access Protocol) : HTTP, HTTPS, SMTP 등을 사용하여 XML 기반메시지를 네트워크상태에서 교환하는 프로토콜

- UDDI(Universal Description, Discovery and Integration) : 웹 서비스에 대한 정보의 공개 및 검색에 대한 방법을 정의하는 XML 기반의 공용 디렉토리 또는 프로토콜의 집합체

- SOA(Service Oriented Architecture) : 서비스 지향 아키텍처(핵심기술 : UDDI, SOAP, WSDL)

- JDBC(Java Database Connectivity) : Java와 DB 연결을 위한 표준 API

2) 내외부 연계 모듈 구현

- EAI(Enterprise Application Integration) : Point to Point, Hub & Spoke, Message Bus, hybrid

- ESB(Enterprise Service Bus) : 느슨한 결합(특정 서비스를 변경하더라도 연결된 다른 서비스에 영향x)

- IPC(Inter Process Communication) : 운영체제에서 프로세스간 데이터를 주고받기 위한 통신기술		메시지큐, 공유메모리, 소켓, 세마포어(프로세스사이에 동기를 맞추는 기능)

5.인터페이스 구현

1) 인터페이스 기능 구현

- JSON (JavaScript Object Notation) : 키-값 쌍 개방형 표준 포멧
- XML(eXtensible Markup Language) : 데이터를 정의하는 규칙을 제공하는 확장가능한 마크업 언어, 					HTML과 달리 DTD가 유동적
- DTD(Document Type Definition) : 문서 형식 정의 <!DOCTYPE html> 
				구성요소 : Element, Attribute, Entity
- AJAX(Asynchronous JavaScript and XML) : 비동기 통신 기술로 클라와 서버간에 XML 통신주요기술 : XML, Javascript, Dom, HTML, CSS, XSLT
- DOM(Document Object Model) :  플랫폼과 언어에 중립적인 인터페이스		Core DOM(모든 문서타입), HTML DOM(HTML타입), XML DOM(XML타입)	

- DB암호화 기법 :  API, Plug-in, TDE, Hybrid

2) 인터페이스 구현 검증
- 인터페이스 구현 검증도구(엑스피 엔셀워)
	xUnit : 다양한 언어를 지원하는 단위테스트 프레임워크
	STAF(Software Testing Automation Framework) : 개방형 테스트 프레임워크, 테스트대상 	 	환경에 데몬을 사용하여 테스트를 진행하고 통합하여 자동화하는 인터페이스 구현 검증 도구
	FitNesse, NTAF, Selerium, watir
- 인터페이스 감시도구 : 스카우터, 제니퍼

6. 프로그래밍 언어 활용

1) 기본 사항
- -1은 2진수로 ~11111111임, 10000~는 –21억 정도 됨
- 식별자는 대소문을 구별함.
- a&&b = a가 False면 b를 실행 안 함. // a||b = a가 True면 b를 실행 안 함.
- break (①for문 탈출 ②case문 탈출)
- switch문은 break가 없을 경우 끝까지 동작함
- for문의 코드가 한줄이면 괄호 생략이 가능함.

- 식별자 표기법
    헝가리안    nScore      식별자 명 접두어
    카멜        totalScore  뒷 단어 대문자
    파스칼      TotalScore  첫 글자 대문자
    스네이크    total_score 단어 사이 _

- 연산자 우선순위 : 증감 산술 시프트  관계 비트  논리 삼항 대입
- 지역변수/ 전역변수, for 문 조건값, 관계연산, return 확인할 것

2)C
- 전역변수는 초기화되지 않으면 정수형은0, 실수형은 0.0, 문자형은 NULL로 초기화된다.
- 전역변수는 프로그램이 시작되면 변수가 생성되고 종료되면 변수가 소멸된다
- 지역변수는 중괄호가 닫히는 시점에 소멸된다.
- static 변수 : 블록 내외부 상관없이 선언할 수 있다. (블록내 선언, 블록안에서만 // 전역선언, 전체)
- 자료형 *포인터 변수명 = &변수명  p=&arr[0], *(p+i) == *(&arr[0]+i) == *(&a[0][i]) == a[0][1]
- 매개변수를 전달하려면 주소값(Reference)로 전달해야함.
- strcat(String Concatenate), strcpy(String Copy), strcmp(String Compare), strlen(String Length), strrev(String Reverse),
- sqrt(양의 제곱근 계산), ceil(소수점올림), floor(소수점내림)
- rand(Random), srand(Seed Random), time(현재시간) atoi(ASCII to integer), itoa(atoi반대)

3)Java
- 클래스 단위 구성
- static변수는 시스템 전체에서 사용이 가능
- for each >> for(제어변수:배열){문장;}
- this는 현재 객체를 가리킴, 클래스내부의 변수와 메서드를 가르킨다. this를 안쓰면 파라미터로 받은 값을 가르키게됨.(why? 함수 안에 있어서 클래스 안에 있는 것 보다 더 가까움)
- 자바는 자식클래스를 생성하면 부모클래스를 먼저 방문하고 그다음에 자식 클래스를 방문함. 파이썬은 자식클래스의 생성자만 방문함.
- 인터페이스 상속 : implement, 클래스상속 : extends

- add(인덱스, 값) : 해당 인덱스에 값을 추가함.
- Math.random() : 0~1 실수형 난수 생성 – 곱하기로 필요한 범위 지정

- HashSet : 중복된 원소를 허용하지 않음
- HashMap : 키와 값으로 구성된 객체를 저장하는 구조.
- 예외처리 : try {} catch(){} finally{}
- throw / throws :  의도적으로 예외를 던짐 / 메서드에서 발생하는 예외를 던짐

4)Python
- 자바는 true/false, 파이썬은 True/False
- 시퀀스 자료형 : 문자열형, list[], 튜플 (), 
- 비시퀀스 자료형 :  세트{}, 딕셔너리{'s'=1, 'j'=2}
- //는 몫을 계산함 c, 자바에서는 주석임

- 파이썬은 입력받을 값 앞에 self를 써야함.
- 파이썬 생성자는 __init__라는 메서드명을 사용함
- 오버로딩 지원x

a={1,2,3} b=a   자료 참조     b[2]의 값을 변경하면 a[2]의 값도 같이 변경됨

values = {1, 2, 3, 4}   a,b, *c = values    다중 대입가능   a= 1, b = 2, c = {3, 4}

7.SQL 응용

1) 데이터베이스 기본
- 트랜잭션(Transaction) : 데이터베이스 시스템에서 하나의 논리적 기능을 정상적으로 수행하기 위한 작업의 기본 단위
    원자성  Atomicity   완전하게 실행되거나 전혀 실행되지 않아야 한다.(Commit, Rollback)
    일관성  Consistency 시스템이 가지고 있는 고정요소는 트랜잭션 수행 전과 트랜잭션 수행 후의 상태가 같아야 한다는 특성 (무결성 제약조건, 동시성 제어)
    격리성  Isolation   동시에 실행되는 트랜잭션들이 서로 영향을 미치지 않아야함.
    영속성  Durability  성공이 완료된 트랜잭션의 결과는 영속적으로 데이터베이스에 저장되어야함.

- 실패(failed),>> Rollback >> 철회(aborted)
- 병행제어 (+ 낙관적 검증, 다중버전 동시성 제어)
 
    로킹        Locking     한 트랜잭션이 데이터를 엑세스 하는 동안 다른 트랜잭션이 접근 못하게 하는 법 (로킹 단위 : 한 번에 로킹 할 수 있는 단위)
    타임 스탬프 Time Stamp  트랜잭션 간의 처리순서를 미리 정하는 법 단점 : 연쇄 복귀(Cascading Rollback)

- DDL 대상 : 도메인, 스키마, 테이블, 뷰, 인덱스

- 스키마 : 구조와 제약조건 등의 정보를 담고있는 기본적인 구조
    외부 스키마 External Schema     사용자의 입장에서 접근할 수 있는 정의를 기술
    개념 스키마 Conceptual Schema   개체 간의 관계, 접근권한, 보안 및 무결성 정의
    내부 스키마 Internal Schema     물리적 저장장치의 관점  레코드형식, 저장 데이터 항목의 표현 방법, 내부 레코드의 물리적 순서 등을 기술

- 뷰 : 논리적 독립성을 갖는 가상 테이블, CREATE문으로 생성, ALTER로 변경 불가
- 인덱스
    순차 접근       저장된 물리적 순서대로 접근(논리 순서가 일치하도록 순차 저장)
    인덱스 접근     값, 주소 쌍으로 표현
    해싱 접근       디스크 블록주소를 레코드의 탐색 값에 대한 해싱함수로 얻는 주소로 직접 접근
    클러스터드      Clustered 한 테이블에 한 개만 설정, 삽입할 때마다 정렬
    넌클러스터드    Non-Clustered 한 테이블에 여러 개 설정 가능

(2)DDL 명령어:CREATE, ALTER, DROP, TRUNCATE(오브젝트내용삭제)
- create table 테이블명(컬럼명 데이터타입 [check(조건식), not null, default, unique, primary key])
- alter table 테이블명 add<modify> 컬럼명 데이터타입 [제약조건]
- alter table 테이블명 drop column 컬럼명  >> 컬럼 삭제
- drop table 테이블명 [cascade|restrict]
- truncate table 테이블명 : 테이블 내의 모든 데이터를 삭제하는 명령

- create[or replace] view 뷰이름 as 조회쿼리;
- drop view 뷰이름;

- create [unique] index 인덱스명 on 테이블명(컬럼명1, 컬럼명2...);
- alter [unique] index 인덱스명 on 테이블명(컬럼명1, 컬럼명2...);
- drop index 인덱스명;

(3) DML : select, insert, update, delete
- select[all|distinct] 속성명1, 속성명2.. from 테이블명, [where][group by][having][order by];
- where 조건 : in(값1, 값2), not in(값1, 값2), like[%,[],_,^], is null, is not null, and, or, not
- select a.컬럼1, b.컬럼1 from 테이블1 a join 테이블 b on 조인조건 [where 검색조건]
- 집합연산자 : union, union all, intersect(교집합), minus
- insert into 테이블명(속성명1,~) values(데이터1, ~);
- update 테이블명 set 속성명=데이터,~ where 조건;
- delete from 테이블명 where 조건;

(4) DCL : grant, revoke
- grant 권한 on 테이블 to 사용자
- revoke 권한 on 테이블 from 사용자

2) 응용 SQL 작성하기
- 다중 행 연산자 : in, any, some, all, exists
- 집계함수 : count, sum, avg, max, min, stddev(표준편차), variance(분산)
- 그룹함수 : rollup, cube, grouping sets

3) SQL활용 및 최적화
- 절차형 sql : 프로시저, 사용자정의함수, 트리거

8. 서버 프로그램 구현

1) 개발환경 구축
- 형상관리 : 변경사항 관리
- 베이스라인 : 산출물들의 검토, 평가, 조정, 처리 등 변화를 통제하는 시점의 기준
- 형상관리 도구 : CVS, CVN, RCS, Bitkeeper, Git, Clear Case

2) 공통 모듈 구현
-응집도 : 모듈의 독립성
    우연    Coincidental    내부 구성요소의 연관관계가 없음
    논리    Logical         유사한 성격을 갖거나 특정 형태로 분류되는 처리 요소가 모인 경우
    시간    Temporal        특정 시간에 처리되는 기능을 모은 경우
    절차    Procedural      다수 기능을 가질 때, 순차적으로 수행할 경우
    통신    Communication   동일한 입력과 출력으로 다른 기능을 수행하는 경우
    순차    Sequential      모듈 내에서 한 활동의 출력값을 다른 활동이 사용하는 경우
    기능    Functional      모듈 내부의 모든 기능 요소들이 한 문제와 연관되어 수행되는 경우

- 결합도 : 외부의 모듈과의 연관도 혹은 모듈간의 상호의존성
    내용    Content     다른 모듈의 내부 기능 및 변수를 다른 모듈에서 사용
    공통    Common      전역변수 참조 및 갱신
    외부    External    외부에서 도입된 데이터 포맷, 통신프로토콜, 인터페이스를 공유
    제어    Control     다른 모듈의 내부 논리 조직 제어목적으로 제어신호를 이용하여 통신
    스탬프  Stamp       모듈간의 인터페이스로 배열이나 객체, 구조 등이 전달되는 경우
    자료    Data        인터페이스로 전달되는 파라미터만으로 상호작용이 일어나는 경우

- JUnit : Java언어를 지원하는 xUnit이라는 이름의 단위테스트 프레임워크 <CppUnit, HttpUnit>

 3) 배치 프로그램 구현
- 이벤트 배치, 온디멘드 배치, 정기 배치
- 배치 스케쥴러 : 스프링 스케쥴러, 쿼츠 스케쥴러(초 분 시 일 월 요 연)(L:마지막 기간, /:시작과 반복간격, ? : 항목 미사용, W : 가장 가까운 평일, -기간)

9. 소프트웨어 개발 보안 구축

1) 소프트웨어 개발 보안 설계
- 개발 보안 구성요소 : 기밀성, 무결성, 가용성, + 자산, 위협, 취약점, 위험
- DoS(Denial of Service) : 시스템 자원을 부족하게 하여 원래 의도된 의도대로 사용하지 못하게 함
- SYN Flooding : syn 패킷만 보내 점유
- UDP Flooding : 대량의 UDP 패킷으로 ICMP를 생성하게 하여 지속해서 자원을 고갈시킴
- Smurf Attack : 출발지 주소를 공격대상의 IP로 설정하여 네트워크 전체에게 ICMP echo 패킷을 직접 브로드캐스팅하여 마비시키는 공격
- 죽음의 핑 : ICMP 패킷을 아주 크게 만들어 전송, 단편화 재조립과정에서 오버플로우 발생
- 랜드 어택 : 출발지 IP를 공격 대상인 목적지 IP와 같게 변조(뺑뺑이시킴)
- 티어드롭 : IP헤더가 조작된 일련의 IP패킷 조각들을 전송
- 봉크 : 분할된 패킷의 번호를 모두 1번으로 해서 보내는 것
- 보잉크 : 패킷 시퀀스 번호를 비정상적으로 바꾸어서 보내는 법

- DDoS(Distributed Dos) : 분산 서비스 거부 공격(공격자 분산배치)
- DRDOS(Distributed  Reflection Dos) : 서버 및 서버 단말까지 공격도구로 사용함.
- 세션하이재킹(Session Hijacking) : ACK Storm 증가, 네트워크 부하 증가
- 어플리케이션 공격 : HTTP GET플러딩, Slowloris, RUDY, Slow Read Attack, Hullk Dos

- 스니핑(Sniffing) : 공격 대상에게 직접 공격은 하지 않고 내용만 몰래봄
- 스누핑(Snooping) : 네트워크상의 중요정보를 몰래 획득하는 해킹수법(IP, ARP)
- 스푸핑(Spoofing) : TCP/IP의 구조적 결함을 이용해서 사용자의 시스템 권한을 획득한 후 신뢰 관계에 있는 IP를 도용하여 정보를 획득하는 수법
- 패스워드 크래킹 : 사전, 무차별, 하이브리드, 레인보우테이블
- 트로이목마 : 정상같은데 실행하면 악성코드 실행

- 버퍼오버플로우 : 프로그램에서 할당된 메모리의 범위를 넘어선 위치에 자료를 읽기 쓰기
- 스택가드/스택쉴드 : 스택 버퍼 오버플로우 공격을 방어하기 위해 값이 변경될 경우, 프로그램 실행을 중단하는 스택 보호 기술
- 버퍼(Buffer) : 데이터를 옮길 때 일시적으로 데이터를 보관하는 메모리영역

 - 백도어 탐지기법
    Backdoor           뒷문, 불법/무단 출입가능하게 만든 트랩 도어
    무결성 검사         침입자에 의해 변경된 파일 존재 검사
    열린 포트 확인      침입자가 실행한 프로세스와 열린 포트 존재 확인
    로그 분석           침입자의 기록을 분석
    SetUID 파일 검사    SetUID 권한 파일 검사
    백도어 탐지 툴사용  백신 등 바이러스 툴 사용

- 보안용어
    봇넷            감염됨 다수의 피씨들이 네트워크로 연결된 형태
    웜              스스로 복제하여 네트워크등의 연결을 통하여 전파하는 프로그램
    APT             Advanced Persistent Threat 지능형 지속 위협 종류 : 제로데이 익스플로잇, 드로퍼, 백도어
    Zero-day        시간적 여유 없이 감행되는 해킹 공격(방어하기 전에 패야함)
    사회 공학       Social Engineering  인간 사이의 기본적 신뢰(심리적 취약점)를 이용,
                    인간 기반 : 휴지통 뒤지기, 어깨너머 훔쳐보기
                    컴퓨터 기반 : 피싱, 파밍, 스미싱 등
    Trust Zone      운영체제를 변조하는 공격행위에 대한 방어
                    스마트폰의 AP(Application Processor) 칩에 적용된 보안 영역
    Typosquatting   타이포스쿼팅, 가짜URL
                    정상과 비슷한 도메인의 이름을 등록해두고 자주 사용하는 사이트의 URL을 교묘하게 바꿔 가짜 사이트로 유도하는 등의 공격기법
    Switch Jamming  패킷을 브로드캐스트함. 스위치 기능을 마비시키는 공격

- 역할기반 접근통제 : MAC, DAC, RBAC
- 3A : Authentication, Authorization, Accounting

- 인증관련기술 : SSO, Kerberos(대칭키 암호화 바탕의 티켓 기반의 인증 프로토콜)
- 접근통제 보호 모델 : 벨-라파듈라(기밀성), 비바(무결성)

- 암호 알고리즘
- 블록 암호 방식 : DES(미국표준64비트 평문블록), AES(고급암호화 표준), SEED(128비트)
- 스트링 암호방식 : RC4
- 일방향 암호 방식(해시암호방식) : MAC, MDC
- 암호화 기법
    공개키 암호화 기법 = 비대칭암호화기법
    RSA, Elgamal 디피-헬만등
    RSA(Rivest Shamir Adleman:각각 만든 사람들 이름임)
    - 큰 소인수의 곱을 인수 분해하는 알고리즘 이용.
    비밀키 암호화 기법 = 단일 키, 대칭 암호화 기법
    DES, 3-DES, AES, SEED, ARIA, MASK 등
    DES(Data Encryption Standard) 데이터 암호화 표준, 64비트의 평문을 46비트의 암호문으로.

- 블록 암호화방식
    IDEA    International Data Encryption Algorithm     PGP(Pretty good Privacy)로 채택된 8라운드 알고리즘
    Skipjack    Clipper 칩에 내장됨 블록 알고리즘 32라운드 음성 암호화에 주로 사용됨

-  해시 암호화 알고리즘 MD5(Message Digest 5) : UNIX에서 일반 계정의 비밀번호 저장 시 사용

-  IPSec : IP 패킷 단위로 암호화, 인증, 키 관리를 통해 보안 서비스를 제공해줌
-  SSL/TLS : IPSec와는 다르게 클라와 서버간에 상호인증, 암호방식에 대해 협상을 거침(443포트)
-  S-HTTP : 클라와 서버간에 전송되는 모든 메시지를 각각 암호화하여 전송(shttp://사용)

2) 소프트웨어 개발 보안 구현
-  XSS(Cross Site Scripting) 웹 페이지에 포함된 부적절한 스크립트 실행
-  SQL Injection : SQL 구문을 어플리케이션에 삽입해서 데이터베이스를 공격
- 네트워크보안 솔루션
    WAF     Web Application Firewall 웹에서 XSS, SQL Injection 등을 탐지하고 차단하는 역할
    SIEM    Security Information Event Management : SIM+SEM
    TKIP    Temporal Key Integrity Protocol 임시 키 무결성 프로토콜
    VPN     Virtual Private Network 가상 사설망, 공중망으로 사설망 효과를 얻기 위한 기술

- 비즈니스 연속성 계획 : BIA, RTO, RPO, DRP, DRS
- DRS유형 : Mirror, Hot, warm, cold

- 보안용어
    트립와이어      (Tripwire)  시스템 파일 등 변조와 추가 등을 MD5, SHA, CRC-32 등을 이용해 검사하는 도구, 백도어 탐지
    SSH Protocol    스니핑의 공격을 막기 위해 개발됨, 22번 포트 사용    유닉스 기반의 데이터 기밀성을 보장할 수 있음
    부인 방지       Non-repudiation     메시지의 송 수신자가 송 수신 사실을 부인하지 못하도록 하는 방법
    SSL             Secure Socket Layer 전송계층 프로토콜, 넷스케이프사가 정한 인터넷 통신 규약 프로토콜
    TLS             Transport Layer Security    SSL을 기반으로 만들어진 인터넷 커뮤니케이션을 위한 암호화 보안 프로토콜 안전한 연결과 압축, 암호화를 담당
    SDN             Software Defined Networking 스위치 라우터 등 하드웨어에 의존하는 네트워크 체계에서 소프트웨어로 네트워크를 제어 관리하기 위해 개발됨
    HSM             Hardware Security Module    USB 형태의 스마트칩을 사용하는 형태(보안토큰)
    Reverse Telnet  서버의 권한을 획득한 후 서버에서 먼저 공격자 PC로 연결하게 하여 공격자가 직접 명령을 입력하여 개인정보를 전송하는 등의 공격

    Digital Forensics   디지털 포렌식   컴퓨터와 인터넷을 기반으로 이루어지는 범죄 수사를 위한 과학수사 방법
    Brute Force Attack  무차별 대입 공격    주어진 경우의 수를 모두 대입하여 암호를 크랙 하는 기법

    Kill Switch     분실한 기기에 저장된 개인정보를 원격으로 삭제   
    ISMS            Information Security Management System 개인정보 관리체계 인증   기술적, 물리적, 관리적 보호조치 등으로 종합적인 정보보호 관리체계에 대한 인증체계
    PMS             Production Information Management System 개인정보보호 관리체계 인증 ISMS 보호조치 기준을 달성하기 위한 위협 정도의 평가 및 대책 수립 및 운영을 위한 인증체계
    ISMS-P          Production Information & Information Security Management System     ISMS + PMS임

10. 어플리케이션 테스트 관리

1) 어플리케이션 테스트 설계
- 살충제 패러독스 : 동일한 테스트케이스 반복사용으로 새로운 문제점을 발견할 수 없다.

- 소프트웨어 테스트 산출물 
    테스트 시나리오 테스트 실행을 위한 일련의 활동  테스트케이스의 동작 순서를 기술한 문서, 
    테스트 하네스   시험을 지원하는 목적으로 생성된 코드와 데이터
                    구성요소:테스트 드라이버, 테스트 스텁, 테스트 케이스, 테스트 스크립트, 목 오브젝트
    테스트 로그     테스트 수행 시 발생한 오류를 시간대별로 기록


- 화이트박스 테스트 (구결조 조변다 기제데루)
    기초 경로 검사      Base Path Testing 흐름도의 기초 집합의 각 경로를 실행
    조건 검사           Condition Testing 모듈 내의 논리적 조건 검사
    루프 검사           Loop Testing 반복 실행을 중심으로 검사
    데이터 흐름 검사    Data Flow Testing 변수의 사용에 따라 검사경로 선택

- 그레이박스 테스트 : 프로그램 내부 구조의 일부만 알고 수행하는 검사

- 블랙박스 테스트 (동경결상 유분페원비오)

    동치 분할 검사      Equivalence Partitioning Testing    입력조건에 중점을 두고 하나의 입력조건에 타당한 값과 그렇지 못한 값을 설정하여  
                    해당 입력 자료에 맞는 결과가 출력되는지 보는 검사
    경계값 분석         Boundary Value Analysis 경계값에서 생기는 오류
    원인-효과그래픽     Cause-Effect Graphic Testing 원인-결과 그래프
    비교 검사           Comparison Testing 여러버전에서 검사값 같은지

- 테스트 종류
    명세 기반 테스트    주어진 명세를 모두 테스트케이스로 구현하고 있는지 확인(블랙)
    구조 기반 테스트    내부 논리 흐름에 맞춰 테스트케이스를 작성하고 확인(화이트)
    경험 기반 테스트    검사자의 경험을 토대로 한 직관과 기술능력을 기반으로 수행하는 검사(블랙)

- 테스트 목적에 따른 분류(회복, 안전 성능 구조 회귀 병행)
    성능 테스트     Performance 실행시간, 응답시간, 경과시간, 처리량, 사용률 등
    스트레스 테스트 Stress 과도한 분량 또는 빈도로 자원을 요청할 때 영향
    회기 테스트     Regression 한 모듈의 수정이 다른 부분에 미치는 영향
    회복 테스트     Recovery 부하를 가중시켜 오류 유도 후 복구

- 테스트 오라클
    참          True    모든 입력값에 대해서
    샘플링      Sampling    특정한 몇 개의 입력값에 대해서
    휴리스틱    Heuristic   특정 입력값에서는 올바른 결과 나머지는 추정으로 처리
    일관성 검사 Consistent  변경 수행 전과 후의 결과 값이 같은지


- 테스트레벨 : 단위 통합 시스템 인수
    단위 테스트     Unit Test   개별 모듈 검사[설계]     정확히 구현되었는지 계획한 기능이 제대로 수행되는지
    통합 테스트     Integration Test    시스템을 구성하는 모듈과 인터페이스의 결합 검사[개발]    상향식(드라이버) 하향식(스텁)
    시스템 테스트   System Test 시스템 전체의 수행을 검사    고객의 요구사항이 완벽히 수행되는지 평가
    인수 테스트     Acceptance Test 고객이 참여하는 검사    알파(Alpha) 테스트(개발자o), 베타(Beta) 테스트(개발자x)
    → 빅뱅 통합 테스트 : 스텁/드라이버 없이 모듈을 한꺼번에 통합하여 테스팅하는 방법

- 빌드 테스트 (BAT or BVT)
    세너티 테스트   테스트 케이스 없이 단위모듈이나 시스템 모듈을 테스트하는 기법 빌드나 릴리즈 전에 진행
    스모크 테스트   각 모듈의 중요한 기능을 검증하기 위한 테스트 빌드나 릴리즈 후에 진행

2) 어플리케이션 통합 테스트
- 드라이버 / 스텁 || 하향식 / 상향식 / 샌드위치

3) 어플리케이션 성능 개선
 - 어플리케이션 성능 측정 지표
    처리량      Throughput 일정 시간 안에 처리하는 일의 양
    응답 시간   Response time 요청 전달 후 도착할 때까지 걸린 시간
    경과 시간   Turn Around Time 작업 의뢰 후 처리 완료까지 걸리는 시간
    자원 사용률 Resource Usage 작업을 처리할 동안 CPU, 메모리, 네트워크 등의 자원 사용률

11. 응용 SW 기초 기술 활용

1) 운영체제 특징
- 메모리 배치 기법 : 반입 / 배치 / 할당 / 교체

- 메모리 할당 기법
    FIFO        First In First Out 비 선점 방식 = FCFS(First Come First Serviced) 
    SJF         Shortest Job First 비 선점 방식
    Priority    비 선점 방식, 프로세스 자체적으로 우선순위를 순위대로 실행, 기아 상태(Starvation)가 유발될 수 있으며 에이징(Aging) 기법사용
    HRN         Highest Response ratio Next (대기시간 + 서비스시간)/서비스시간 큰 숫자 우선
    RR          Round Robin 선점 방식 시분할 시스템(Time Sharing System)을 위해 고려됨, 시간 할당량(Time Slice)에 따라 달라짐
    SRT         Shortest Remaining Time First
    → 에이징(Aging) : 무한 정지 방지 수단, 기다린 시간에 비례하여 프로세스에게 우선순위 부여

- 디스크 스케쥴링  
    FCFS        First Come First Serviced
    SSTF        탐색 거리가 가장 짧은 것
    SCAN        한 방향으로 이동하며 끝에 도착하면 반대 방향으로 스캔 진행
    C-SCAN      항상 밖에서 안으로 움직이면서 가장 짧은 탐색 거리를 갖는 요청을 서비스
    N-step SCAN 새로 추가된 요청은 다음에 서비스하는 것, SCAN의 방식을 사용
    LOOK        양끝을 왕복하지만 움직이는 방향에 요청이 없으면 그 자리에서 방향을 바꿈
    Eschenbach  C-SCAN처럼 움직이면서 모든 실린더가 요청이 있든 없든 전체 트랙이 한 바퀴 회전할 동안의 서비스를 받는 기법

- 교착상태(Deadlock) 해결 기법 : 예방, 회피, 발견, 복구 
    예방(Prevention)    상호 배제, 점유와 대기, 비 선점, 환형 대기가 안 생기게 하는 것
    회피(Avoidance)     은행가 알고리즘(Banker’s Algorithm)
    발견(Detection)     자원할당그래프(Resource - Allocation Graph)
    회복(Recovery)      교착상태에 있는 프로그램을 종료하거나 자원을 선점하여 다른 애한테 줌

2) 네트워크 기초 활용하기
 - OSI(Open System Interconnection) 7 Layer
 
물리
Physical
0과 1의 비트정보를 회선에 보내기위한 전기적신호 변환
RS-232C, v.24/28, Ethernet, FDDI(비트)

데이터링크
Data Link
인접 시스템 간 데이터 전송, 전송오류 제어, 동기화, 흐름제어 등의 전송기능 제공
HDLC, LLC, LAPB, LAPD, PPP, 이더넷(프레임)

네트워크
Network
단말기 간 데이터 전송을 위한 최적화된 경로 제공
X.25, ARP, RARP, IPX, IP, ICMP(패킷)

전송
Transport
신뢰성있는 통신 보장, 데이터의 분할과 재조립, 흐름제어, 오류제어, 혼잡제어 등을 담당.
TCP, UDP (세그먼트)

세션
Session
연결 접속 및 동기 제어
SIP, SDP, RPC, NetBIOS, SSH, TLS (데이터)

표현
Presentation
데이터 형식 설정과 부호교환, 암/복호화
MPEG, SSL, JPEG (데이터)

응용
Application
사용자와 네트워크 간 응용서비스 연결, 데이터 생성
HTTP(80), TELNET(23), FTP(21, 전송은 20), SMTP(25) (데이터)
