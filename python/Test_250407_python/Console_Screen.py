from datetime import datetime
from snack.snack import Snack
from company.company import Company


class ConsoleScreen:

    def show_menu():
        print("1) 회사 등록")
        print("2) 과자 등록")
        print("3) 회사 전체 조회")
        print("4) 과자 전체 조회")
        print("5) 회사 일부 조회")
        print("6) 과자 일부 조회")
        print("7) 회사 검색")
        print("8) 과자 검색")
        print("9) 과자 회사 조회")
        print("10) 과자 정보 수정")
        print("11) 과자 정보 삭제")
        print("12) 종료")
        print("-----------------------")

        return input("메뉴 선택 : ")

    def show_add_company():
        print("1) 회사 등록")
        name = input("이름 : ")
        addr = input("주소 : ")
        ceo = input("대표명 : ")
        emp = input("직원수 : ")
        print("-----------------------")

        return Company(name, addr, ceo, emp)
    
    def show_add_snack(s_no):
        print("2) 과자 등록")
        name = input("이름 : ")
        date = input("유통기한(YYYY-MM-DD) : ")
        price = input("가격 : ")
        weight = input("무게 : ")
        cp = input("제조사 : ")
        print("-----------------------")

        return Snack(s_no+1, name, date, price, weight, cp)

    def show_choose_page(page):
        c_page = int(input("페이지[1~%d] : " % page))
        print("-----------------------")

        return c_page
    
    def show_companys(list):
        for cp in list:
            print("%s, %s, %s, %d" % (cp.name, cp.addr, cp.ceo, cp.emp))
        print("-----------------------")

    def show_snacks(list):
        for snack in list:
            print("%d, %s, %s, %d, %d, %s" \
            "" % (snack.no, snack.name, datetime.strftime(snack.date, "%Y-%m-%d"), snack.price, snack.weight, snack.cp))
        print("-----------------------")

    def show_result(result):
        print(result)
        print("-----------------------")

    def show_search():
        keyword = input("검색어 입력 : ")
        print("-----------------------")
        return keyword
    
    def show_snacks_info(list):
        # s_no, s_name, s_date, s_price, s_weight, c_name, c_addr, c_ceo, c_employee
        for snack in list:
            print("%s, %s, %d, %d / " \
            "" % (snack.s_name, datetime.strftime(snack.s_date, "%Y-%m-%d"), snack.s_price, snack.s_weight)
            + "%s, %s, %s, %d" % (snack.c_name, snack.c_addr, snack.c_ceo, snack.c_employee))
        
        print("-----------------------")

    def show_update_search():
        keyword = input("업데이트할 과자의 이름 입력 : ")
        print("-----------------------")
        return keyword
    
    def show_choose_update():
        print("1) 이름")
        print("2) 유통기한")
        print("3) 가격")
        print("4) 중량")
        print("5) 제조사")
        print("-----------------------")
        up_num = input("업데이트 할 항목 선택 : ")
        up_data = input("업데이트 할 값 입력 : ")

        return up_num, up_data

    def show_delete_search():
        keyword = input("삭제할 과자의 이름 입력 : ")
        print("-----------------------")
        return keyword