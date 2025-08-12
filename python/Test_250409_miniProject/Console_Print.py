from datetime import datetime
from math import ceil
from Account import Account
from Record_Data import RecordData


class ConsolePrint:

    def show_main_menu():
        print("1) 로그인")
        print("2) 신규 계정 생성")
        print("3) 기존 계정 삭제")
        print("4) 종료")
        print("-----------------------------")
        ch = input("▷  ")

        return ch

    def show_login():
        print("계정 정보 입력")
        id = input("ID : ")
        pw = input("PassWord : ")
        print("-----------------------------")

        return id, pw
    
    def show_new_account():
        print("신규 계정 정보 입력")
        id = input("ID : ")
        pw = input("PassWord : ")
        name = input("NickName : ")
        print("-----------------------------")

        return Account(id, pw, name)
    
    def show_delete_account():
        print("삭제할 계정의 정보 입력")
        id = input("ID : ")
        pw = input("PassWord : ")
        print("-----------------------------")

        return id, pw

    def show_sub_menu():
        print("1) 전적 추가")
        print("2) 전적 삭제")
        print("3) 전적 조회")
        print("4) 전적 분석")
        print("5) 메인으로 돌아가기 (로그아웃)")
        print("-----------------------------")
        ch = input("▷  ")

        return ch

    def show_result(result):
        print(result)
        print("-----------------------------")

    def show_new_record():
        print("추가할 전적 입력")
        vd = input("승/패 : ")
        date = input("날짜(YYYYMMDD:HHMI) : ")
        champ = input("사용 챔피언 : ")
        k = input("킬 : ")
        d = input("데스 : ")
        a = input("어시 : ")
        print("-----------------------------")

        return RecordData(0, "", vd, date, champ, k, d, a)
    
    def show_delete_record():
        print("원하는 삭제 범위를 입력")
        start = input("시작(YYYYMMDD:HHMI) : ")
        end = input("끝(YYYYMMDD:HHMI) : ")

        return start, end
    
    def show_all_record(list):
        cnt = 0
        page = ceil(len(list) / 5)
        for rd in list:
            print("%s, %s, %s, %d/%d/%d" \
            "" % (rd.vd, datetime.strftime(rd.date, "%Y%m%d:%H%M"), rd.champ, rd.kill, rd.death, rd.assist))
            
            cnt += 1

            if cnt % 5 == 0:
                print("[%d/%d]" % (cnt // 5, page), end="")
                input()
                print("-----------------------------")
            elif cnt == len(list):
                print("[%d/%d]" % (page, page), end="")
                input()
                print("-----------------------------")

    def show_analysis_record_menu():
        print("1) 전체 전적 분석")
        print("2) 특정 챔피언 전적 분석")
        print("-----------------------------")
        ch = input("▷  ")
        print("-----------------------------")

        return ch
    
    def show_analysis_all_record(rd, best, worst, champ=None):

        if champ == None:
            analysis_title = "  전체 전적 통계"
        else:
            analysis_title = "  %s 챔피언 전적 통계" % champ

        print("\n######################################################################################")
        print(analysis_title)
        print("  총 승리 수 : %d / 총 패배 수 %d / 전체 승률 %.1f%%" % (rd.wins, rd.loses, rd.win_rate))
        print("  평균 킬 수 : %.1f / 평균 데스 수 : %.1f / 평균 어시 수 : %.1f / KDA 평균 : %.1f" \
        "" % (rd.kill_avg, rd.death_avg, rd.assist_avg, rd.kda_avg))
        print("#------------------------------------------------------------------------------------#")

        if best.death == 0:
            print("  Best Play")
            print("  %s, 날짜 : %s, 챔피언 : %s, 킬 : %d, 데스 : %d, 어시 : %d / KDA : %s" \
                "" % (best.vd, datetime.strftime(best.date, "%Y%m%d:%H%M"), best.champ, best.kill, best.death, best.assist, "perfect"))
        else:
            print("  Best Play")
            print("  %s, 날짜 : %s, 챔피언 : %s, 킬 : %d, 데스 : %d, 어시 : %d / KDA : %.1f" \
                "" % (best.vd, datetime.strftime(best.date, "%Y%m%d:%H%M"), best.champ, best.kill, best.death, best.assist, (best.kill + best.assist) / best.death))

        print("#------------------------------------------------------------------------------------#")

        if worst.death == 0:
            print("  Worst Play")
            print("  %s, 날짜 : %s, 챔피언 : %s, 킬 : %d, 데스 : %d, 어시 : %d / KDA : %s" \
                "" % (worst.vd, datetime.strftime(worst.date, "%Y%m%d:%H%M"), worst.champ, worst.kill, worst.death, worst.assist, "perfect"))
        else:
            print("  Worst Play")
            print("  %s, 날짜 : %s, 챔피언 : %s, 킬 : %d, 데스 : %d, 어시 : %d / KDA : %.1f" \
                "" % (worst.vd, datetime.strftime(worst.date, "%Y%m%d:%H%M"), worst.champ, worst.kill, worst.death, worst.assist, (worst.kill + worst.assist) / worst.death))  

        print("######################################################################################")
        print("\n-----------------------------")

    def show_choose_analysis_record():
        print("분석을 원하는 챔피언의 이름을 입력")
        champ = input("▷  ")
        print("-----------------------------")

        return champ
    
    def show_analysis_record():
        pass