
class digitsToText:
        global ahaad,taash,ashrat,myaat,olouf,tenOlouf,value
        # this contains the dictionaries were the numbers will be converted into words
        ahaad = {0:"صفر", 
                1:"واحد", 2:"اثنين", 3:"ثلاثة", 4:"اربعة", 5:"خمسة",
                6:"ستة",
                7:"سبعة"
                , 8:"ثمانية"
                , 9:"تسعة"
                }

        taash = { 11:"احدعش", 12:"اثنعش", 13:"ثلاثطعش", 14:"اربعطعش", 15:"خمسطعش", 16:"ستطعش",
                17:"سبعطعش", 18:"ثمانطعش", 19:"تسعطعش",
                10 : "عشرة"}


        ashrat = {20:"عشرين", 
                50:"خمسين", 30:"ثلاثين",40:"اربعين", 50:"خمسين",
                60:"ستين",
                70:"سبعين"
                , 80:"ثمانين"
                , 90:"تسعين"
                
                }

        myaat = {100:"مية", 
                200:"ميتين"
                , 300:"ثلاثمية"
                ,400:"اربعمية"
                , 500:"خمسمية",
                600:"ستمية",
                700:"سبعمية"
                , 800:"ثمانمية"
                , 900:"تسعمية"
                }

        olouf = {1000:"الف", 
                2000:"الفين"
                , 3000:" ثلاث آلاف"
                ,4000:"اربع آلاف"
                , 5000:"خمس آلاف",
                6000:"ست آلاف",
                7000:"سبع آلاف"
                , 8000:"ثمان آلاف"
                , 9000:"تسع آلاف"
                }

        tenOlouf = {10000:"عشر آلاف", 
                20000:"عشرين ألف"
                , 30000:" ثلاثين ألف"
                ,40000:"اربعين ألف"
                , 50000:"خمسين ألف",
                60000:"ستين ألف",
                70000:"سبعين ألف"
                , 80000:"ثمانين ألف"
                , 90000:"تسعين ألف"
                }
        value=""
        flag= "" 

        def tens(self,num):

                num = str(num)#convert number to string 

                #test if number dosn't countain any tens
                if num[0]=="0":
                        if num[1] != "0":
                                return ahaad[int(num[1])]
                #if it dose have tens then check if it belongs to teens
                elif num[0] == "1":
                        return taash[int(num)]
                
                elif num[1] == "0": 
                        return ashrat[int(num)]
                        
                else:#if it containes a number then print it and take the values from the dictionary above 
                        return (ahaad[int(num[len(num)-1])]+" و " + ashrat[int(num[len(num)-2]+"0")])


        def hundrands(self,num):
                num = str(num)#convert number to string 
                #test if number dosn't countain any hunderds

                if num[0]=='0':
                        return self.tens(num[1:])

                elif (num[1]=="0" and num[2]=="0"):#100, 200, 300, ...
                        return myaat[int(num)]
                        
                elif num[1]=="0" and num[2]!='0':#102,103,205,...
                        return myaat[int(num[0:2]+"0")]+" و " +ahaad[int(num[2])]
                
                elif num[1]=="1" :#112, 212, 114, ...
                        return myaat[int(num[0]+"00")]+" و " +taash[int(num[1]+num[2])] 
                
                elif num[2]=='0':#120, 230, 130, ...
                        return myaat[int(num[0]+"00")]+" و " +ashrat[int(num[1]+"0")]
                
                else :
                        return myaat[int(num[0]+"00")]+" و "+self.tens(num[1:])

        def thousands(self,num):
                global value
                num = str(num)#convert number to string 
                #test if number dosn't countain any thousands
                

                #thousands
                
                if len(num) == 4:
                        if num[0]=='0' :
                                return self.hundrands(num[1:])
                        elif num[1:] == "000":
                                return olouf[int(num)]
                        else:
                                return olouf[int(num[0]+"000")]+" و "+self.hundrands(num[1:])
                
                #ten thousands
                elif len(num)==5:
                        if num[0]=='0' :
                                return self.thousands(num[1:])
                        if(num[1:]=='0000'):
                                return tenOlouf[int(num)]
                        elif num[1] =="0":
                                return tenOlouf[int(num[0]+"0000")]+" و "+self.hundrands(num[2:])
                        elif num[1] != "0" and num[2:]=="000":
                                return self.tens(num[:2])+" الف  "
                        elif num[1] != "0" :
                                return self.tens(num[:2])+" الف و "+self.hundrands(num[2:])


                #hundred thousand
                elif len(num)==6:
                        if num[0]=='0' :
                                return self.thousands(num[1:])
                        if(num[1:]=='00000'):
                                return myaat[int(num[:3])]+" الف "
                        elif num[0] !="0" and num[3:] == '000':
                                return self.hundrands(num[:3])+" الف "+self.hundrands(num[3:])
                        else:
                                return self.hundrands(num[:3])+" الف و "+self.hundrands(num[3:])

        def millions(self,num):
                global value
                num = str(num)
                        
                # 1000000 one million
                if len(num) == 7:
                        if num[0]=='0' :
                                return self.thousands(num[1:])
                        if num[1:] == "000000":
                                if num[0] == '1':
                                        return "مليون"
                                elif num[0] == '2':
                                        return "مليونين"
                                else:
                                        return ahaad[int(num[0])]+" مليون "
                        else:
                                return  ahaad[int(num[0])]+" مليون و " + self.thousands(num[1:])

                # 10000000 ten million
                elif len(num) == 8:
                        if num[0]=='0' :
                                return self.millions(num[1:])
                        if num[1:] == "0000000":
                                return self.tens(num[:2]) + " مليون "
                        else :
                                return  self.tens(num[:2])  +" مليون و " + self.thousands(num[2:])

                # 100000000 one hundred million
                elif len(num) == 9:
                        if num[0]=='0' :
                                return self.millions(num[1:])
                        if num[1:] == "00000000":
                                return self.hundrands(num[:3]) + " مليون "
                        else:
                                return  self.hundrands(num[:3])  +" مليون و " + self.thousands(num[3:])

        def billions (self,num):
                num = str(num)
                
                #1000000000 one billion
                if len(num) == 10:
                        if num[0]=='0' :
                                return self.millions(num[1:])
                        elif num[1:] == "000000000":
                                if num[0] == '1':
                                        return "مليار"
                                elif num[0] == '2':
                                        return "مليارين"
                                else:
                                        return ahaad[int(num[0])]+" مليار "
                        else:
                                return  ahaad[int(num[0])]+" مليار و " + self.millions(num[1:])

                #10000000000 ten billion
                elif len(num) == 11:
                        if num[0]=='0' :
                                return self.billions(num[1:])
                        elif num[1:] == "0000000000":
                                return self.tens(num[:2])+" مليار "
                        else:
                                return self.tens(num[:2]) +" مليار و " + self.millions(num[2:])
                        
                #100000000000 one hundred billion
                elif len(num) == 12:
                        if num[0]=='0' :
                                return self.billions(num[1:])
                        elif num[1:] == "00000000000":
                                return self.hundrands(num[:3])+" مليار "
                        else:
                                return  self.hundrands(num[:3])  +" مليار و " + self.millions(num[3:])

        def trilions(self,num):
                num = str(num)


                #1000000000000 one trillion
                if len(num) == 13:
                        if num[0]=='0' :
                                return self.billions(num[1:])
                        elif num[1:] == "000000000000":
                                if num[0] == '1':
                                        return "بليون"
                                elif num[0] == '2':
                                        return "بليونين"
                                else:
                                        return ahaad[int(num[0])]+" بليون "
                        else:
                                return  ahaad[int(num[0])]+" بليون و " + self.billions(num[1:])

                #10000000000000 ten trillion
                elif len(num) == 14:
                        if num[0]=='0' :
                                return self.trilions(num[1:])
                        elif num[1:] == "0000000000000":
                                return self.tens(num[:2])+" بليون "
                        else:
                                return self.tens(num[:2]) +" بليون و " + self.billions(num[2:])
                        
                #10000000000000 one trillion billion
                elif len(num) == 15:
                        if num[0]=='0' :
                                return self.trilions(num[1:])
                        elif num[1:] == "00000000000000":
                                return self.hundrands(num[:3])+" بليون "
                        else:
                                return  self.hundrands(num[:3])  +" بليون و " + self.billions(num[3:])

        def quadrillion(self,num):

                num = str(num)

                #1000000000000000 one quadrillion
                if len(num) == 16:
                        if num[0]=='0' :
                                return self.trilions(num[1:])
                        elif num[1:] == "000000000000000":
                                if num[0] == '1':
                                        return " بليار "
                                elif num[0] == '2':
                                        return " بليارين "
                                else:
                                        return ahaad[int(num[0])]+" بليار "
                        else:
                                if num[0] == '1':
                                        return " بليار و "+ self.trilions(num[1:]) 
                                elif num[0] == '2':
                                        return " بليارين و "+ self.trilions(num[1:]) 
                                else:
                                        return  ahaad[int(num[0])]+" بليار و " + self.trilions(num[1:])   

                #10000000000000000 ten quadrillion
                elif len(num) == 17:
                        if num[0]=='0' :
                                return self.quadrillion(num[1:])
                        elif num[1:] == "0000000000000000":
                                return self.tens(num[:2])+" بليار "
                        else:
                                return self.tens(num[:2]) +" بليار و " + self.trilions(num[2:])

                        
                #100000000000000000 hundered quadrillion
                elif len(num) == 18:
                        if num[0]=='0' :
                                return self.quadrillion(num[1:])
                        elif num[1:] == "00000000000000000":
                                return self.hundrands(num[:3])+" بليار "
                        else:
                                return self.hundrands(num[:3])  +" بليار و " + self.trilions(num[3:])

        def quintillion(self,num):
                
                num = str(num)

                #1000000000000000000 one quadrillion
                if len(num) == 19:
                        if num[0]=='0' :
                                return self.quadrillion(num[1:])
                        elif num[1:] == "000000000000000000":
                                if num[0] == '1':
                                        return " تريليون "
                                elif num[0] == '2':
                                        return "  تريليونين  "
                                else:
                                        return ahaad[int(num[0])]+" تريليون "
                        else:
                                return  ahaad[int(num[0])]+" تريليون و " + self.quadrillion(num[1:])   

                #10000000000000000000 ten quadrillion
                elif len(num) == 20:
                        if num[0]=='0' :
                                return self.quintillion(num[1:])
                        if num[1:] == "0000000000000000000":
                                return self.tens(num[:2])+" تريليون "
                        else:
                                return self.tens(num[:2]) +" تريليون و " + self.quadrillion(num[2:])

                        
                #100000000000000000000 hundered quadrillion
                elif len(num) == 21:
                        if num[0]=='0' :
                                return self.quintillion(num[1:])
                        if num[1:] == "00000000000000000000":
                                return self.hundrands(num[:3])+" تريليون "
                        else:
                                return  self.hundrands(num[:3])  +" تريليون و " + self.quadrillion(num[3:])

        def sextillion(self,num):

                num = str(num)
                #1000000000000000000000 one sextillion
                if len(num) == 22:
                        if num[1:] == "000000000000000000000":
                                if num[0] == '1':
                                        return " التلريار "
                                elif num[0] == '2':
                                        return "  التلريارين  "
                                else:
                                        return ahaad[int(num[0])]+" التلريار "
                        else:
                                return  ahaad[int(num[0])]+" التلريار و " + self.quintillion(num[1:])   

                #10000000000000000000000 ten sextillion
                elif len(num) == 23:
                        if num[1:] == "0000000000000000000000":
                                return self.tens(num[:2])+" التلريار "
                        else:
                                return self.tens(num[:2]) +" التلريار و " + self.quintillion(num[2:])

                        
                #100000000000000000000000 hundered sextillion
                elif len(num) == 24:
                        if num[1:] == "00000000000000000000000":
                                return self.hundrands(num[:3])+" التلريار "
                        else:
                                return  self.hundrands(num[:3])  +" التلريار و " + self.quintillion(num[3:])

        
        def numeric2Txt(self,num):

    
            if type(num) is int or type(num) is float:
                num = str(num)

                if num.find('.')>-1:
                        value= self.numeric2Txt(num[: num.find('.')])+' فاصلة '+self.numeric2Txt(num[num.find('.')+1:] )
                        return value

                elif len(num) == 1 : 
                        value= ahaad[int(num)]

                elif len(num)==2:
                        value=self.tens(num)
    
                elif len(num)==3:
                        value=self.hundrands(num)
        
                elif len(num)>= 4 and len(num)<= 6:
                        value=self.thousands(num)
    
                elif len(num) >=7 and len(num)<=9:
                        value=self.millions(num)

                elif len(num) >=10 and len(num)<=12:
                        value=self.billions(num)

                elif len(num) >=13 and len(num) <=15:
                        value=self.trilions(num)

                elif len(num) >=16 and len(num) <=18:
                        value=self.quadrillion(num)

                elif len(num) >=19 and len(num) <=21:
                        value=self.quintillion(num)

                elif len(num) >=22 and len(num) <=24:
                        value=self.sextillion(num)

                return value