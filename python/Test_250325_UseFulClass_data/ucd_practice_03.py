
chats_data = open("C:\moon\KakaoTalkChats.txt", "r", encoding="utf-8")

word_dict = {}
skip_word = ["이모티콘", "<사진 읽지 않음>", "https",
             "톡게시판", "삭제된 메시지입니다", ".jpg",
             ".png", ".pdf"]
skip = False

for i in range(5):
    chat_line = chats_data.readline()

while True:
    chat_line = chats_data.readline()
    if not chat_line: break

    chat_line = chat_line.replace("\n", "")
    chat_line2 = chat_line

    if (not chat_line.startswith("20")) and (chat_line != ""):
        pass
    else:
        start_w = chat_line.find(":", 20)
        if start_w == -1: continue

        chat_line = chat_line[start_w+2:len(chat_line)]

    for i in skip_word:
        if chat_line.find(i) != -1:
            skip = True

    if skip :
        skip = False
        continue

    words = chat_line.strip().split(" ")

    for w in words:
        if w == "":
            continue
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

chats_data.close()

word_dict = dict(sorted(word_dict.items(), key=lambda x : x[1], reverse=True))

log_data = open("C:\\moon\\0326.txt", "a", encoding="utf-8")

i = 0
for w, v in word_dict.items():
    i += 1
    if i == 100: break
    print(w, v)

for w, v in word_dict.items():
    log_data.write(w + "\t" + str(v) + "\r\n")

log_data.close()