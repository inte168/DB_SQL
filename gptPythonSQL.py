import pymysql

# 서버 연결
connection = pymysql.connect(
    host='192.168.56.101',
    port=4567,
    user='jyheo',
    password='hjy0618',
    database='madang'
)

# MySQL 연결 객체에서 커서 생성
cursor = connection.cursor()

while True:
    print("===============")
    print("1. 데이터 삽입")
    print("2. 데이터 삭제")
    print("3. 데이터 검색")
    print("4. 종료")
    print("===============")
    
    choice = input("원하는 작업을 선택하시오(1/2/3/4): ")
    
    if choice == '4':
        break
    try:
        table_name = input("작업할 데이터가 있는 테이블의 이름을 입력하세요: ")

        print("해당 테이블의 정보는 다음과 같습니다.")
        cursor.execute("SHOW COLUMNS FROM "+ table_name)
        results = cursor.fetchall()
        for row in results:
            print(row)

                
        if choice == '1':
            # 데이터 삽입
            columns = input("어떤 열에 삽입할지 입력하세요: ")
            columns = "(" + columns + ")"
            values = input("어떤 값을 삽입할지 입력하세요: ")
            values = "(" + values + ")"
            insert_query = f"INSERT INTO {table_name} {columns} VALUES {values}"
            cursor.execute(insert_query)
            connection.commit()
            print("데이터가 삽입되었습니다.")
        
        elif choice == '2':
            # 데이터 삭제
            condition = input("삭제할 데이터를 식별하는 조건을 입력하세요: ")
            condition = ("WHERE " + condition) if len(condition) else ""
            delete_query = f"DELETE FROM {table_name} " + condition
            cursor.execute(delete_query)
            connection.commit()
            print("데이터가 삭제되었습니다.")
        
        elif choice == '3':
            # 데이터 검색 및 출력
            col = input("검색할 열 이름을 입력하세요.(전체는 *): ")
            condition = input("검색할 조건을 입력하세요 (여러 조건은 AND로 연결하세요): ")
            condition = ("WHERE " + condition) if len(condition) else ""
            select_query = f"SELECT {col} FROM {table_name} " + condition
            cursor.execute(select_query)
            results = cursor.fetchall()
            for row in results:
                print(row)
    except:
        print("Error: 다시 시도하세요")

# 커서와 연결 닫기
cursor.close()
connection.close()
