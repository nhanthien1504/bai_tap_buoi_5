'''
Viết chương trình tìm từ dài nhất trong một câu nhập vào từ bàn phím.
input
chào bạn mình là thiên
'''
# str = input('mời nhập một câu: ')
# char = max(str.split(' ')) #max list
# print(char)


'''
    Cho list sau: ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"].
    Viết chương trình để in ra hậu tố (vn, org, net, com) trong các tên miền website trong list trên.
'''
# lst = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
# lst_1 = []
# for i in lst:
#     a_str = i.split('.')[-1]
#     lst_1.append(a_str)
# print(lst_1)

'''
Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.
'''

# tupl = (1, 1.2, 5.6, 9, 3.5)
# tong = 0
# for i in tupl:
#     tong = tong + float(i)
# print(tong)
# max_tup = max(tupl)
# print(max_tup)

'''
Viết chương trình kiểm tra xem tất cả các phần tử trong tuple có giống nhau hay không.
'''
# tupl = (1, 1.2, 5.6, 9, 3.5, 8, 0)
#
# set_1 = set(tupl)
#
# if len(tupl) == len(set_1):
#     print('không có kí tự trùng lặp')
# else:
#     print('có kí tự trùng lặp')

'''
Viết chương trình kiểm tra 2 tuple có phần tử chung hay không.
'''
# tupl_A = (1, 1.2, 5.6, 9, 3.5, 1.5, 0)
# tupl_B = (0, 1.5, 6, 9, 5, 8.2, 0.3)
# set_A = set(tupl_A)
#
# set_B = set(tupl_B)
#
# if set_A & set_B:
#     print('các phần tử chung: ',tuple(set_A & set_B))
# else:
#     print('khong co phan tu trung lap')

'''
Viết chương trình in ra phần tử thứ 4 và phần tử thứ 4 từ cuối lên trong một tuple.
'''
# tupl_A = (1, 1.2, 5.6, 9, 3.5, 1.5, 0)
# if len(tupl_A) < 4:
#     print('chuỗi phải dài hơn 4 kí tự')
# else:
#     print(tupl_A[3])
#     print(tupl_A[-4])

'''
Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
'''
# lst = [(1, 1.2), (5.6, 9), (3.5, 1.5, 0)]
# lst_1 = []
# for i in lst:
#     if len(i)<2:
#         print('nhâp các tuple có số lượng index >2')
#     else:
#         j = i[1]
#         lst_1.append(j)
# print(min(lst_1))

'''
Cho 1 list chứa các tuple không rỗng.
Viết chương trình sắp xếp list đó theo chiều tăng dần của phần tử cuối trong mỗi tuple.
Input: [(2, 5), (4, 1), (0, 0)] 
Output: [(0, 0), (4, 1), (2, 5)]
'''
# lst = [(2, 5), (4, 1), (0, 0)]
# for i in lst:
#     for j in range(len(lst)):
#         print('chuoi :',j,'=',i)




'''
Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.

'''

# lst = [1,2,3,4,(1,5,6)]
# ctr = 0
# for n in lst:
#     if isinstance(n,tuple):
#         break
#     ctr +=1
# print(ctr)


'''
Viết chương trình đảo ngược một tuple
'''

# tupl_A = (1, 1.2, 5.6, 9, 3.5, 1.5, 0)
# re_tupl_A = tupl_A[::-1]
# print(re_tupl_A)

'''
Viết chương trình chuyển một tuple sang thành list và ngược lại từ list sang tuple
'''
# tupl_A = (1, 1.2, 5.6, 9, 3.5, 1.5, 0)
# re_tupl_A = list(tupl_A)
# print(re_tupl_A)
#

'''
Viết chương trình sinh một tuple chứa các phần tử có các kiểu dữ liệu khác nhau.
 Sau đó, unpack các phần tử trong một tuple
'''

# x = ("99", 20, "!##$")
# company, emp, profile = x
# print(company)
# print(emp)
# print(profile)