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
