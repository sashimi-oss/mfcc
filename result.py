import predict

print (predict.pred.prediction_label[0])
# if(predict.pred.prediction_label[0] == 2):
#     print ('true')

# numbers = input('1から5を入力してください')
# numbers = int(numbers)
numbers = predict.pred.prediction_label[0]

# vcAct = {0:"おじいさん（長塚さん）", 1:"おばあさん（高野先生）", 2:"少年(白上虎太郎)",
#            3:"男の子(月読ショウタ)", 4:"女の子", 5:"少女",
#            6:"青年女", 7:"青年男", 8:"おじさん(ぴたごえ)", 9:"おばさん(ぴたごえ)"}
vcAct = {0:"男の子", 1:"少年", 2:"青年男",
            3:"おじさん", 4:"おじいさん", 5:"女の子",
            6:"少女", 7:"青年女", 8:"おばさん", 9:"おばあさん"}

if numbers in vcAct:
    preVC = vcAct[numbers]
else:
    print("エラー")

print(preVC)
