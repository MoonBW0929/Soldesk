# 버블 정렬

def bubble_sort(ls):

    for j in range(len(ls)-1):
        for i in range(len(ls)-j-1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]

ls_1 = [234, 12, 1, 54 ,567, 45, 23 ,8]
ls_2 = [70, 49, 8, 54, 1, 5]
ls_3 = [6, 195, 51, 84, 30 ,26, 1, 94, 51, 48]

# bubble_sort(ls_1)
# print(ls_1)
# bubble_sort(ls_2)
# print(ls_2)
# bubble_sort(ls_3)
# print(ls_3)


def select_sort(ls):

    for j in range(len(ls)-1):

        min = ls[j]
        idx = j
        for i in range(j+1, len(ls)):
            if min > ls[i]:
                min = ls[i]
                idx = i
                
        ls[j], ls[idx] = ls[idx], ls[j]

select_sort(ls_1)
print(ls_1)
select_sort(ls_2)
print(ls_2)
select_sort(ls_3)
print(ls_3)