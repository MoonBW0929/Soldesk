from Account_DAO import Account_DAO
from Console_Print import ConsolePrint
from Record_Data_DAO import RecordData_DAO


def sub_loop(name):
    while True:
        ch = ConsolePrint.show_sub_menu()
        print("-----------------------------")

        if ch == "1":
            rd = ConsolePrint.show_new_record()
            result = r_dao.insert_new_record(rd, name)
            ConsolePrint.show_result(result)
        if ch == "2":
            start, end = ConsolePrint.show_delete_record()
            result = r_dao.delete_record(name, start, end)
            ConsolePrint.show_result(result)
        if ch == "3":
            list = r_dao.get_all_record(name)
            ConsolePrint.show_all_record(list)
        if ch == "4":
            ch = ConsolePrint.show_analysis_record_menu()
            if ch == "1":
                result = r_dao.analysis_all_record(name)
                if result:
                    best, worst = r_dao.get_bestworst_record(name)
                    ConsolePrint.show_analysis_all_record(r_dao, best, worst)
                else:
                    ConsolePrint.show_result("전적의 개수가 부족합니다 (2개 이상 필요)")
            elif ch == "2":
                champ = ConsolePrint.show_choose_analysis_record()
                result = r_dao.analysis_all_record(name, champ)
                if result:
                    best, worst = r_dao.get_bestworst_record(name, champ)
                    ConsolePrint.show_analysis_all_record(r_dao, best, worst)
                else:
                    ConsolePrint.show_result("전적의 개수가 부족합니다 (2개 이상 필요)")
        if ch == "5":
            break

if __name__ == "__main__":

    r_dao = RecordData_DAO()

    while True:
        ch = ConsolePrint.show_main_menu()
        print("-----------------------------")

        if ch == "1":
            id, pw = ConsolePrint.show_login()
            result = Account_DAO.login_account(id, pw)
            if result:
                ConsolePrint.show_result("로그인 성공")
                name = Account_DAO.get_account_nickname(id, pw)
                sub_loop(name)
            else:
                ConsolePrint.show_result("로그인 실패")
        elif ch == "2":
            ac = ConsolePrint.show_new_account()
            result = Account_DAO.check_create_account(ac)
            if result == 1: 
                result = Account_DAO.create_new_accont(ac)
                ConsolePrint.show_result(result)
            else:
                ConsolePrint.show_result(result)
        elif ch == "3":
            id, pw = ConsolePrint.show_delete_account()
            result = Account_DAO.check_delete_account(id, pw)
            if result == 1:
                result = Account_DAO.delete_accont(id, pw)
                ConsolePrint.show_result(result)
            else:
                ConsolePrint.show_result(result)
        elif ch == "4":
            break