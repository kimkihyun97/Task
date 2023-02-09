import string
class ChangeType():

    def change_de(self,num,de=[]):

        if num ==0 :
            de.append(0)
            return
        elif num ==1 :
            de.append(1)
            return
        else :
            de.append(num%2)
            num = num//2
            self.change_de(num,de)
        return int(''.join(list(map(str,de[::-1]))))

    def change_ox(self,num,ox=[]):
        if num==0:
            ox.append(0)
            return
        elif num<8 :
            ox.append(num)
            return
        else :
            ox.append(num%8)
            num = num//8
            self.change_ox(num,ox)
        return int(''.join(list(map(str, ox[::-1]))))

    def change_hx(self,num,hx=[]):
        lst=[i for i in string.ascii_uppercase[:6]]
        if num==0 :
            hx.append(0)
            return
        elif num <10 :
            hx.append(num)
            return
        elif num <16 :
            hx.append(lst[num-10])
            return
        else :
            if num//16 >=10 :
                hx.append(lst[num//16-10])
            else : hx.append(num//16)
            num = num%16
            self.change_hx(num,hx)

        return (''.join(list(map(str, hx))))



if __name__ == "__main__" :
    num_c = ChangeType()
    print(num_c.change_de(255))
    print(num_c.change_ox(255))
    print(num_c.change_hx(255))

