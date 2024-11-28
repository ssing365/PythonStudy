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