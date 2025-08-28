'''to create the file and write the content'''
# f=open('ac.txt','w')
# f.write('hello veeresh,this is ram,how are you')
# print('date is entered')
# f.close()
'''to read the file '''
# f=open('ac.txt','r')
# data=f.read()
# print(data)
# f.close()
'''to dead only 10 characters  '''
# f=open('ac.txt','r')
# data=f.read(10)
# print(data)
# f.close()
'''again add the content '''
# f=open('ac.txt','w')
# f.write('your very clever boy......')
# print('data is fulled..')
# f.close()
# f=open('ac.txt','r')
# data=f.read()
# print(data)
# f.close()
'''use      with      statement'''
# with open('ad.txt','w') as f:
#     f.write('veeresh is great boy')
#     f.write('you have a greate future')
#     f.write('this is a good dessesion')
#     print('content is clear')
# print(f.close())    
'''tell() method'''
# f=open('ad.txt','r')
# print(f.tell())               first the cursor is pointing to 0 index
# print(f.read(3))
# print(f.tell())               now the cursor is pointing to 3rd index

# start=int(input('Enter the year:'))
# end=int(input('Enter the year:'))
# for year in range(start,end):
#     if(year%4==0 and year%100!=0) or(year%400==0):
#         print(year,'leap year')
#     else:
#         print(year,'not a leap year')    
# for i in range(0,20):
#     if i%2==1:
#         print(i)
