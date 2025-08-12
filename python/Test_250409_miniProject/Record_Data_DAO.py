from Record_Data import RecordData
from moon_library.moon_DBManager import MoonDBManager


class RecordData_DAO:
    def __init__(self):
        self.get_count_all_record()

    def get_count_all_record(self):
        try:
            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql =   "SELECT count(*) " \
                    "FROM apr09_record_data"

            db_cur.execute(sql)
            
            count = None
            for i in db_cur:
                count = i[0]

            self.record_count = count

        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def insert_new_record(self, rd, name):
        try:

            rd.no = self.record_count + 1
            rd.name = name

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql =   "INSERT INTO apr09_record_data " \
                    "VALUES(%d, '%s', '%s', to_date('%s', 'YYYYMMDD:HH24MI'), '%s', " \
                    "%d, %d, %d)" % (rd.no, rd.name, rd.vd, rd.date, rd.champ, rd.kill, rd.death, rd.assist)

            db_cur.execute(sql)
            
            if db_cur.rowcount == 1:
                self.record_count += 1
                db_con.commit()
                return "전적 추가 성공"
            else:
                return "전적 추가 실패"

        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def delete_record(self, name, start, end):
        try:

            if int(start) > int(end):
                start, end = end, start

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql =   "DELETE FROM apr09_record_data " \
                    "WHERE r_name = '%s' AND r_date >= to_date('%s', 'YYYYMMDD:HH24MI') " \
                    "AND r_date <= to_date('%s', 'YYYYMMDD:HH24MI')" % (name, start, end)

            db_cur.execute(sql)
            
            self.record_count -= db_cur.rowcount

            db_con.commit()

            return "%d개의 전적 삭제 성공" % db_cur.rowcount

        except Exception as e:
            print("전적 삭제 실패")
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_all_record(self, name):
        try:

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql =   "SELECT * " \
                    "FROM apr09_record_data " \
                    "WHERE r_name = '%s' " \
                    "ORDER BY r_date" % (name)

            db_cur.execute(sql)
            
            list = []
            for no, name, vd, date, champ, kill, death, assist in db_cur:
                list.append(RecordData(no, name, vd, date, champ, kill, death, assist))

            return list

        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def analysis_all_record(self, name, champ = None):
        try:

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            if champ == None:
                sql =   "SELECT * " \
                        "FROM apr09_record_data " \
                        "WHERE r_name = '%s' " \
                        "ORDER BY r_date" % (name)
            else:
                sql =   "SELECT * " \
                        "FROM apr09_record_data " \
                        "WHERE r_name = '%s' AND r_champ = '%s' " \
                        "ORDER BY r_date" % (name, champ)

            db_cur.execute(sql)
            
            wins = 0
            loses = 0
            k = 0
            d = 0
            a = 0
            cnt = 0

            for _, name, vd, _, _, kill, death, assist in db_cur:
                if vd == '승':
                    wins += 1
                else:
                    loses += 1

                k += kill
                d += death
                a += assist
                cnt += 1

            if cnt < 2:
                return False
            else:
                self.win_rate = wins / cnt * 100
                self.wins = wins
                self.loses = loses
                self.kill_avg = k / cnt
                self.death_avg = d / cnt
                self.assist_avg = a / cnt
                self.kda_avg = (self.kill_avg + self.assist_avg) / self.death_avg

                return True

        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    def get_bestworst_record(self, name, champ = None):
        try:

            if champ == None:
                champ_use = ""
            else:
                champ_use = "AND r_champ = '%s' " % champ

            db_con, db_cur = MoonDBManager.db_connect("moon0929/ansquddnr4545@195.168.9.124:1521/xe")

            sql1 =  "SELECT * " \
                    "FROM (" \
                        "SELECT * " \
                        "FROM apr09_record_data " \
                        "WHERE r_death > 0 AND r_name = '%s' %s" \
                    ") " \
                    "WHERE ((r_kill + r_assist) / r_death) = (" \
                        "SELECT max((r_kill + r_assist) / r_death) " \
                        "FROM apr09_record_data " \
                        "WHERE r_death > 0 %s" \
                    ")" % (name, champ_use, champ_use)
            
            sql2 =  "SELECT * " \
                    "FROM (" \
                        "SELECT * " \
                        "FROM apr09_record_data " \
                        "WHERE r_death > 0 AND r_name = '%s' %s" \
                    ") " \
                    "WHERE ((r_kill + r_assist) / r_death) = (" \
                        "SELECT min((r_kill + r_assist) / r_death) " \
                        "FROM apr09_record_data " \
                        "WHERE r_death > 0 %s" \
                    ")" % (name, champ_use, champ_use)
            
            sql3 =  "SELECT * " \
                    "FROM apr09_record_data " \
                    "WHERE r_name = '%s' AND r_death = 0 AND (r_kill + r_assist) = (" \
                        "SELECT MAX(r_kill + r_assist) " \
                        "FROM apr09_record_data " \
                        "WHERE r_death = 0 %s" \
                    ")" % (name, champ_use)

            db_cur.execute(sql1)
            
            list1 = [] # best
            for no, name, vd, date, champ, kill, death, assist in db_cur:
                list1.append(RecordData(no, name, vd, date, champ, kill, death, assist))


            db_cur.execute(sql2)

            list2 = [] # worst
            for no, name, vd, date, champ, kill, death, assist in db_cur:
                list2.append(RecordData(no, name, vd, date, champ, kill, death, assist))


            db_cur.execute(sql3)
            
            list3 = [] # best and 0 death (perfect)
            for no, name, vd, date, champ, kill, death, assist in db_cur:
                list3.append(RecordData(no, name, vd, date, champ, kill, death, assist))

            if list3 == []:
                return list1[0], list2[0]
            else:
                if ((list1[0].kill + list1[0].assist) / list1[0].death) > (list3[0].kill + list3[0].assist):
                    return list1[0], list2[0]
                else:
                    return list3[0], list2[0]

        except Exception as e:
            print(e)
        
        finally:
            MoonDBManager.db_disconnect(db_con, db_cur)

    