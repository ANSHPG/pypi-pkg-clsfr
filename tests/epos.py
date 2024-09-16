def loop(num):
    k=1
    
    # for epo in range(num):
    #     rem = ((int)(num))%10
    #     # print(f'{rem} - {int(num/10)}')
    #     if(epo%((num/10))==0):
    #     #  print(f'{k}-{epo}')
    #      k+=1
    #     #  print(f'{rem} - {int(num/10)}')
    #     # epo+=num/10

    for epo in range(1,num*10):
        if(epo%((num*10)/10)==0):
            k+=1

    print(f'diff[{num}]: {(num/10)} ,k:{k}')
for iter in range(0,11):
    # loop(iter)
    pass
def epos(steps):
    diff = steps/10
    print(f'diff[{steps}->{diff}]')
    for epo in range(1,steps):
            # loss = train(val_true,inputs)
            # print(f'epo: {epo*10},diff: {diff*10}')
            if(((epo*10)%(diff*10))==0):
                print(epo)

# epos(552)

def new(steps):
    diff = (steps)/10
    rem = steps%10
    print(f'diff[{steps}->{diff}] rem: {rem}')
    k=1
    m=1
    for epo in range(1,steps):
            # loss = train(val_true,inputs)
            # print(f'epo: {epo*10},diff: {diff*10}')
            # if((epo%diff)==0):
            #     pass
                # print(epo)
            if(((steps-rem)%epo)==0):
                #  pass
                # print(f'2nd Loop : {epo}  ,{steps-rem} ,{(steps-rem)%epo}')
                k+=1
            print(f'3rd loop: {epo}, {epo%diff}')
            if(epo%diff==0):
                #  print(f'3rd loop: {epo}, {epo%diff}')
                 m+=1
    print(f'{steps}->K:{k}, M:{m}')

for iter in range(1,10):
    new(iter)