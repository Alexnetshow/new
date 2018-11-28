print("此程式為計算任意三角形面積的程式，請依照提示，分別輸入三角形的三邊長")
side_a,side_b,side_c=float(input("請輸入邊長一:")),float(input("請輸入邊長二:")),float(input("請輸入邊長三:"))

'''此程式利用海龍公式來計算三角形面積'''



if side_a+side_b>side_c and side_b+side_c>side_a and side_a+side_c>side_b:
    s=(side_a+side_b+side_c)/2
    area=(s*(s-side_a)*(s-side_b)*(s-side_c))**0.5
    print("此三角形面積為",area,"平方單位")
    print("*****此簡易程式由Alexander提供支持*****")
    print("請按Enter鍵離開離開")
    end=str(input())
    print(end)

else:
    print("此數值非合理的三角形邊長!")
    print("請按Enter鍵離開")
    end=str(input())
    print(end)
    #this is new for git

