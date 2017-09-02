'''
推箱子
Author: Frank
Created: 08/27/2017
'''
def Maze():
    #list0-6 and Boxlayout for layout (x 为 纵坐标，y 为横坐标)
    list0=['#','#','#','#','#','#','#','#','#','#']
    list1=['#','#',' ',' ',' ',' ',' ','#','#','#']
    list2=['#','#','O','#','#','#',' ',' ',' ','#']
    list3=['#',' ','S',' ','O',' ',' ','O',' ','#']
    list4=['#',' ','*','*','#',' ','O',' ','#','#']
    list5=['#','#','*','*','#',' ',' ',' ','#','#']
    list6=['#','#','#','#','#','#','#','#','#','#']
    Boxlayout=[list0,list1,list2,list3,list4,list5,list6]

    #   'S'表示工作的小人
    #   '#'表示墙体
    listx=[2,3,3,4]# listx, listy 为箱子'O'的坐标，共四个箱子
    listy=[2,4,7,6]
    
    listxa=[4,4,5,5]#listxa,listys 为最终箱子的位置'*'的坐标，共四个    
    listya=[2,3,2,3]

    Boxesleftout=4  #未推到最终位置的箱子个数

    x=3 #(3,2)为工作小人最初位置
    y=2

    while Boxesleftout!=0:

        for i in range (7):
            for j in range(10):
                print(Boxlayout[i][j],end='')
            print('')

        Order=input()
        #用w 上，s 下， a 左，d 右
        # 表示工作小人的移动方向
        #用x 退出游戏
        #每次输入后需要按回车确认

        if Order=='s':  #向下移动
            if Boxlayout[x+1][y]!='#'and Boxlayout[x+1][y]!='O':    #判断前方格是否是墙体或箱子，如否，则小人前进一格
                Boxlayout[x][y]=' '
                x=x+1
                Boxlayout[x][y]='S'
            elif Boxlayout[x+1][y]=='O'and Boxlayout[x+2][y]!='#'and Boxlayout[x+2][y]!='O':    #判断前方格是否为箱子，且前方第二格不是墙体或另一箱子。如否，则小人前进一格
                Boxlayout[x][y] = ' '
                x = x + 1
                Boxlayout[x][y]='S'
                for i in range (4):
                    if listx[i]==x and listy[i]==y:#判断前方箱子为哪一个箱子
                        Boxlayout[x+1][y]='O'#箱子前进一格，并相应修改listx表示的箱子位置
                        listx[i]=listx[i]+1
        #以上为'S'向下的操作，其他方向同理

        if Order=='w':  #向上移动
            if Boxlayout[x-1][y]!='#'and Boxlayout[x-1][y]!='O':
                Boxlayout[x][y]=' '
                x = x - 1
                Boxlayout[x][y]='S'
            elif Boxlayout[x-1][y]=='O'and Boxlayout[x-2][y]!='#'and Boxlayout[x-2][y]!='O':
                Boxlayout[x][y] = ' '
                x = x - 1
                Boxlayout[x][y] = 'S'
                for i in range (4):
                    if listx[i]==x and listy[i]==y:
                        Boxlayout[x-1][y]='O'
                        listx[i]=listx[i]-1

        if Order=='a':  #向左移动
            if Boxlayout[x][y-1]!='#'and Boxlayout[x][y-1]!='O':
                Boxlayout[x][y]=' '
                y=y-1
                Boxlayout[x][y]='S'
            elif Boxlayout[x][y-1]=='O'and Boxlayout[x][y-2]!='#'and Boxlayout[x][y-2]!='O':
                Boxlayout[x][y] = ' '
                y=y-1
                Boxlayout[x][y]='S'
                for i in range (4):
                    if listx[i]==x and listy[i]==y:
                        Boxlayout[x][y-1] = 'O'
                        listy[i] = listy[i] - 1
        if Order=='d':  #向右移动
            if Boxlayout[x][y+1]!='#'and Boxlayout[x][y+1]!='O':
                Boxlayout[x][y]=' '
                y=y+1
                print(y)
                Boxlayout[x][y]='S'
                print(x,y)
            elif Boxlayout[x][y+1]=='O'and Boxlayout[x][y+2]!='#'and Boxlayout[x][y+2]!='O':
                Boxlayout[x][y] = ' '
                y=y+1
                Boxlayout[x][y]='S'
                for i in range (4):
                    if listx[i]==x and listy[i]==y:
                        Boxlayout[x][y+1]='O'
                        listy[i]=listy[i]+1

        if Order=='x':  #判定是否退出
            break

        # 避免因小人和箱子的移动而覆盖箱子最终位置'*'的显示
        for i in range (4):
            if Boxlayout[listxa[i]][listya[i]]!='O' and Boxlayout[listxa[i]][listya[i]]!='S':
                Boxlayout[listxa[i]][listya[i]]='*'

        #判断箱子是否已经全部被推到最终位置
        Boxesleftout = 4
        for i in range (4):
            for j in range (4):
                if listx[i]==listxa[j] and listy[i]==listya[j]:
                    Boxesleftout=Boxesleftout-1

        #清屏
        print('\n'*30)

    #判断是成功或是中途退出
    if Boxesleftout==0:
        print('congratulation!')
    else:
        print(' Exit by pressing x ')  #print(' \(\>\﹏\<\) ')

#主程序
Maze()