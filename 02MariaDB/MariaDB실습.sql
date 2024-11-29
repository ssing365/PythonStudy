/*
블럭 단위 주석은 Java와 동일하게 작성합니다.
*/

#라인단위 주석은 #입니다.

/*
실행 방법
F9 : 현재 문서의 쿼리 전체를 실행한다.
Ctrl + F9 : 블럭으로 지정한 쿼리만 실행한다.
	만약 쿼리의 절반 정도만 선택하면 에러가 발생한다.
Ctrl + Shift + F9 : 현재 쿼리를 실행한다. 단, 마지막에 기술한 세미콜론 안으로 커서를 옮긴 후 실행해야 한다.
*/

/*
테이블 생성하기
제약조건
	PRIMARY KEY : 기본키 지정. 해당 키로 지정된 컬럼은 중복되지 않는 값이 입력되어야 한다.사람으로 따지면 주민번호
	
	AUTO_INCREMENT : 자동증가 컬럼으로 지정한다. 오라클 sequence처럼 1씩 증가하는 순차적인 정수가 자동 입력된다.	
		
	UNSIGNED : 정수형 컬럼으로 지정하는 경우 음수는 사용하지 않고, 양수의 범위만 사용한다. 이 때 양의 범위가 2개로 늘어난다.
*/

#1. 숫자형으로 구성된 테이블
CREATE TABLE tb_int(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	num1 TINYINT UNSIGNED NOT NULL,
	num2 SMALLINT NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	num4 BIGINT,
	fnum1 FLOAT(10,5) NOT NULL,
	fnum2 DOUBLE(20,10)
);
	
DESC tb_int;
	
/*
데이터 입력하기
형식1] insert into 테이블명 (컬럼명) values (값);
*/

#일련번호 컬럼은 insert문에서 제외하는 것이 좋다. 자동증가 컬럼으로 지정되었으므로 순차적인 번호가 자동 부여된다.

INSERT INTO tb_int (num1, num2, num3, num4, fnum1, fnum2)
VALUES (123,12345,1234567,1234567890,12345.12345, 1234567890.1234567890);

/*형식2] insert into 테이블명 values (값)*/
#insert문 작성시 컬럼을 명시하지 않으면 전체컬럼에 대해 입력값을 기술해야 하므로 실행 시 오류가 발생할 수 있다. 권장X
INSERT INTO tb_int VALUES (2, 123, 12345, 1234567, 1234567890,tb_int
12345.12345, 1234567890.1234567890);

SELECT * FROM tb_int;

#2. s날짜형으로 구성된 테이블
/*
current_timestamp : 날짜 형식으로 지정된 컬럼에 디폴트값으로 현재 시각을 입력할 때 사용한다.
				오라클의 sysdate와 동일하다.
NOW() : 날짜형식으로 지정된 컬럼에 현재 시각을 입력한다. 초단위까지의 시간이 입력된다.
*/tb_date
CREATE TABLE tb_date(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	DATE1 DATE NOT NULL,
	DATE2 DATETIME DEFAULT current_timestamp
);
	
DESC tb_date;
	
INSERT INTO tb_date(DATE1, DATE2) VALUES ('2023-02-25', NOW());
INSERT INTO tb_date(DATE1) VALUES ('2023-02-27');

SELECT * FROM tb_date;

#3. 문자형
CREATE TABLE tb_string(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	str1 VARCHAR(30) NOT NULL,
	str2 TEXT
);
DESC tb_string;

INSERT INTO tb_string(str1, str2) VALUES ('난 짧은글3', '난 엄청 긴글3');
INSERT INTO tb_string(str1, str2) VALUES ('난 짧은글2', '난 엄청 긴글2');
INSERT INTO tb_string(str1, str2) VALUES ('난 짧은글1', '난 엄청 긴글1');

/*
레코드 조회시 조건 추가하기
*/
SELECT * FROM tb_string;
SELECT * FROM tb_string WHERE idx = 2;
SELECT * FROM tb_string WHERE idx = 2; AND str1='난 짧은글2';
SELECT * FROM tb_string WHERE idx = 2; AND str1='난 짧은글3';
SELECT * FROM tb_string WHERE idx = 2; or str1='난 짧은글3';

/*
레코드 겁색시 문자열이 포함된 것을 인출하고 싶다면 like절을 사용한다.
*/
SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은%';
SELECT * FROM tb_string WHERE str1 LIKE '난 짧은%';
SELECT * FROM tb_string WHERE str1 LIKE '%난 짧은';

#4. 특수형
CREATE TABLE tb_spec(
	idx INT AUTO_INCREMENT,
	/* 여러 항목 중 1개만 선택할 수 있다. */
	spec1 ENUM('M', 'W', 'T'),
	/* 항목에서 2개 이상 선택할 수 있다. */
	spec2 SET('A', 'B', 'C', 'D'),
	/* 아웃라인 방식으로 컬럼을 먼저 생성한 후 별도로 기본키를 지정한다.*/
	PRIMARY KEY (idx)
);

INSERT INTO tb_spec (spec1, spec2) VALUES ('W', 'A,B,C');#정상입력
INSERT INTO tb_spec (spec1, spec2) VALUES ('X', 'A,B,C');#spec1에러
INSERT INTO tb_spec (spec1, spec2) VALUES ('M', 'X,B,C');#spec2에러
#spec1은 not null로 지정되지 않았으므로 null을 허용하는 컬럼이다.
INSERT INTO tb_spec (spec2) VALUES ('B,C,D'); 
SELECT * FROM tb_spec;

CREATE TABLE board(
	num INT NOT NULL AUTO_INCREMENT, # 일련번호. 자동증가컬럼
	title VARCHAR(200) NOT NULL, #제목 : 짧은 텍스트
	content TEXT NOT NULL, # 내용 : 긴 텍스트 
	id VARCHAR(20) NOT NULL,
	postdate DATETIME DEFAULT CURRENT_TIMESTAMP, #작성일. 현재 시각이 default
	visitcount MEDIUMINT, #조회수 : 대략 800만 이하
	PRIMARY KEY(num) #일련번호 컬럼은 아웃라인 방식으로 pk로 지정
);

#더미데이터 입력
#날짜의 경우 now()함수를 통해 입력한다.
#특히 일련번호 컬럼인 num은 쿼리문에서 생략된 상태로 실행한다.
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목1', '내용1입니다.', 'korea', NOW(), 0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목2', '내용2입니다.', 'korea', NOW(), 0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목3', '내용3입니다.', 'korea', NOW(), 0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목4', '내용4입니다.', 'korea', NOW(), 0);
INSERT INTO board
	(title, content, id, postdate, visitcount)
VALUES ('제목5', '내용5입니다.', 'korea', NOW(), 0);

SELECT * FROM board;
SELECT * FROM board ORDER BY num DESC;
SELECT * FROM board ORDER BY num ASC;
SELECT * FROM board ORDER BY num;
