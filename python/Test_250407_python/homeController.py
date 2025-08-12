from Console_Screen import ConsoleScreen
from company.companyDAO import CompanyDAO
from snack.snackDAO import SnackDAO


if __name__ == "__main__":

    s_dao = SnackDAO()
    c_dao = CompanyDAO()

    while True:
        choice = ConsoleScreen.show_menu()
        print("-----------------------")

        if choice == "1":
            cp = ConsoleScreen.show_add_company()
            result = c_dao.add_company_db(cp)
            ConsoleScreen.show_result(result)
        elif choice == "2":
            s_no = s_dao.get_snack_lastNum_db()
            sn = ConsoleScreen.show_add_snack(s_no)
            result = s_dao.add_snack_db(sn)
            ConsoleScreen.show_result(result)
        elif choice == "3":
            list = c_dao.get_all_company_db()
            ConsoleScreen.show_companys(list)
        elif choice == "4":
            list = s_dao.get_all_snack_db()
            ConsoleScreen.show_snacks(list)
        elif choice == "5":
            page = c_dao.get_company_page_db("")
            c_page = ConsoleScreen.show_choose_page(page)
            list = c_dao.get_company_db(c_page, "")
            ConsoleScreen.show_companys(list)
        elif choice == "6":
            page = s_dao.get_snack_page_db("")
            c_page = ConsoleScreen.show_choose_page(page)
            list = s_dao.get_snack_db(c_page, "")
            ConsoleScreen.show_snacks(list)
        elif choice == "7":
            keyword = ConsoleScreen.show_search()
            page = c_dao.get_company_page_db(keyword)
            if page == 0:
                print("해당 회사를 찾지 못했습니다")
                print("-----------------------")
                continue
            else:
                c_page = ConsoleScreen.show_choose_page(page)
                list = c_dao.get_company_db(c_page, keyword)
                ConsoleScreen.show_companys(list)
        elif choice == "8":
            keyword = ConsoleScreen.show_search()
            page = s_dao.get_snack_page_db(keyword)
            if page == 0:
                print("해당 과자를 찾지 못했습니다")
                print("-----------------------")
                continue
            else:
                c_page = ConsoleScreen.show_choose_page(page)
                list = s_dao.get_snack_db(c_page, keyword)
                ConsoleScreen.show_snacks(list)
        elif choice == "9":
            keyword = ConsoleScreen.show_search()
            page = s_dao.get_snack_page_db(keyword)
            if page == 0:
                print("해당 과자를 찾지 못했습니다")
                print("-----------------------")
                continue
            else:
                c_page = ConsoleScreen.show_choose_page(page)
                list = s_dao.get_snack_info_db(c_page, keyword)
                ConsoleScreen.show_snacks_info(list)
        elif choice == "10":
            keyword = ConsoleScreen.show_update_search()
            up_num, up_data = ConsoleScreen.show_choose_update()
            result = s_dao.update_snack_db(keyword, up_num, up_data)
            ConsoleScreen.show_result(result)
        elif choice == "11":
            keyword = ConsoleScreen.show_delete_search()
            result = s_dao.delete_snack_db(keyword)
            ConsoleScreen.show_result(result)
        elif choice == "12": break