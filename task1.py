learin_rate = 0.01
x1,x2=0.0,0.0
total = 1e-6
for s in range (1,6):
    grade_x1=-7
    grade_x2=-4
    
    new_x1 = x1-learin_rate*grade_x1
    new_x2 = x2-learin_rate*grade_x2
    up_nor= (new_x1-x1)*2+(new_x2-x2)*0.5
    if up_nor < total:
        print(f'stop iteration{s}due to small parameter {up_nor}')
        break
        
    x1,x2=new_x1,new_x2
    print(f'step{s}:x1= {x1:.3f}, x2: {x2:.3f}')
    print(f'Profit: {7*x1+4*x2:.2f}')
    print ('----'*20)