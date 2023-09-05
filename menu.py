from abc import ABC, abstractmethod
from os import system as x
from termcolor import colored

import getch

class Menu(ABC):

    MAX_HORIZONTAL_SIZE=72
    MAX_VERTICAL_SIZE=36

    def __init__(self, list_of_menu_items, W):
        
        self.coords=[1,2,2,1]
        self.selected=set()
        self.W=W
        self.N=len(list_of_menu_items)-1
        self.list_of_menu_items=list_of_menu_items
        self._menu = self._generate_menu()
        self.print_menu()
        

    #@abstractmethod    
    #def _generate_menu(self):
    #    pass
        
    def print_menu(self):
        #x("clear")
        print(self._menu)

    def _access_menu_item(self,lst):
        item=self.list_of_menu_items
        for i in lst:
            item=item[i]
        return item
    
    def _move_down_menu(self):
        depth=len(self.coords)
        if depth==1:
            menu_length=self.N
        else:
            menu_length=len(self._access_menu_item(self.coords[:-1]))-1
        if self.coords[-1]<menu_length:
            self.coords[-1]+=1

    def _move_up_menu(self):
        if self.coords[-1]>1:
            self.coords[-1]-=1
        #else:
        #    self._close_menu_item()

    def _open_menu_item(self):
        if len(self._access_menu_item(self.coords))>1:
            self.coords.append(1)
        else:
            return self.execute(*self.coords)

    def _close_menu_item(self):
        if len(self.coords)>1:
            self.coords.pop(-1)

    def _switch_top_menu_item(self,i):
        if isinstance(i,int) and i>0 and i<=self.N:
            self.coords=[i]
            if len(self.list_of_menu_items[i])>1:
                self.coords.append(1)

    


    @abstractmethod
    def navigate_menu(self):
        while True:
            depth=len(self.coords)
            move=getch.getch()
            if depth == 1:
                if move == "a":
                    self._move_up_menu()
                if move == "d":
                    self._move_down_menu()
                if move == "s" or move == " ":
                    self._open_menu_item()
            if depth > 1:
                if move == "s":
                    self._move_down_menu()
                if move == "w":
                    self._move_up_menu()
                if move == "a":
                    self._close_menu_item()
                if move == "d" or move == " ":
                    self._open_menu_item()
            if move=="x":
                break
            print(self.coords,self._access_menu_item(self.coords))



    @abstractmethod
    def execute(self, *args):
        pass

    

class VerticalMenu(Menu):
    
    def __init__(self, list_of_menu_items, W):
        super().__init__(list_of_menu_items, W)
        #self.selected=set()
        
        if 2*self.N>super().MAX_VERTICAL_SIZE:
            raise ValueError("Menu too large") 
        if self.W<6:
            raise ValueError("Menu items too small")
        

    def execute(self, *args):
        
        print(self.selected)
        return getch.getch()
    
    def _select_menu_item(self):
        
        if len(self._access_menu_item(self.coords))==1:
            if self.coords[-1] not in self.selected:
                self.selected.add(self.coords[-1])
                
            else:
                self.selected.discard(self.coords[-1])
                

    def _close_menu_item(self):
        super()._close_menu_item()
        self.selected.clear()

    def _open_menu_item(self):
        if len(self._access_menu_item(self.coords))>1:
            self.coords.append(1)
            self.selected.clear()
        else:
            return self.execute(*self.coords)

    
    def navigate_menu(self):
        
        while True:
            x("clear")
            self._menu = self._generate_menu()
            self.print_menu()
            #depth=len(self.coords)
            move=getch.getch()
            if move == "a":
                self._close_menu_item()
            if move == "s":
                self._move_down_menu()
            if move == "w":
                self._move_up_menu()
            if move.isdigit():
                self._switch_top_menu_item(int(move))
            if move=="f":
                self._select_menu_item()
            if move == "d" or move == " ":
                move = self._open_menu_item()
            
            if move=="x":
                break
            #print(self.coords,self._access_menu_item(self.coords))

    def _chop_menu_entry(self,menu_entry):
        if len(menu_entry)>self.W-2:
            return menu_entry[:self.W-3]+"…"
        return menu_entry

    def _generate_menu(self):
        #sizes=[self.N]
        items=self.list_of_menu_items
        max_vert_size=self.N
        depth=len(self.coords)
        cur_vert_position=1
        top_of_menu=[1]
        bottom_of_menu=[self.N]
        for i in self.coords[:-1]:
            items=items[i]
            #sizes.append(len(items)-1)
            cur_vert_position+=i-1
            top_of_menu.append(cur_vert_position)
            bottom_of_menu.append(cur_vert_position+len(items)-2)
            max_vert_size=max(max_vert_size,bottom_of_menu[-1])
        #print(top_of_menu)
        #print(bottom_of_menu)
        #print(self.coords)
        filled=[]
        len_cur_item=len(self._access_menu_item(self.coords)[0])
        #print(len_cur_item)
        long_menu_item=len_cur_item>self.W-2
        
        for _ in range(max_vert_size):
            filled.append([])
        
        #print(self.selected)

        for i in range(depth):
            for j in range(max_vert_size):
                if j>=top_of_menu[i]-1 and j<bottom_of_menu[i]:
                    cur_entry=self._access_menu_item(self.coords[:i])[j+2-top_of_menu[i]]
                    #if len(cur_entry[0])<self.W-2:
                    
                    filled[j].append(self._chop_menu_entry(cur_entry[0]).ljust(self.W-2)+int(len(cur_entry)>1)*" →"
                                     +int(j+2-top_of_menu[i] in self.selected and i==depth-1)*" ✓")
                    #else:
                    #    filled[j].append(cur_entry[0][:self.W-3]+"…"+int(len(cur_entry)>1)*" →")
                else:
                    filled[j].append(0)
        #print(filled,depth,max_vert_size)

        hline=self.W*"─"
        blank=self.W*" "
        vline="│"
        tlline="┌"+hline
        tcline="┬"+hline
        mlline="├"+hline
        blline="└"+hline
        mcline="┼"+hline
        bcline="┴"+hline
        tend="┐"
        mend="┤"
        bend="┘"

        print_menu=""
        bottom_line=""
        
        for j in range(max_vert_size):
            menu_content=""
            
            for i in range(depth):
                w = i!=0 and bool(filled[j][i-1])
                nw = i!=0 and j!=0 and bool(filled[j-1][i-1])
                n = j!=0 and bool(filled[j-1][i])
                o = bool(filled[j][i])
                #print(j,i,w,nw,n,o)
                if (o and nw) or (w and n):
                    print_menu+=mcline
                elif nw:
                    if n:
                        print_menu+=bcline
                    elif w:
                        print_menu+=mend+blank
                    else:
                        print_menu+=bend+blank
                elif o:
                    if n:
                        print_menu+=mlline
                    elif w:
                        print_menu+=tcline
                    else:
                        print_menu+=tlline
                elif n:
                    print_menu+=blline
                elif w:
                    print_menu+=tend+blank
                else:
                    print_menu+=" "+blank
                
                if o:
                    if self.coords[i]==j+2-top_of_menu[i]:
                        if i==depth-1:
                            len_cur_menu=max(self.W,len_cur_item+2)
                            #menu_content+=vline+colored(filled[j][i].ljust(self.W),"blue")
                            menu_content+=vline+colored((self._access_menu_item(self.coords)[0].ljust(len_cur_menu-2)+int(len(self._access_menu_item(self.coords))>1)*" →"+int(j+2-top_of_menu[i] in self.selected and i==depth-1)*" ✓").ljust(len_cur_menu),"blue")
                        else:
                            menu_content+=vline+colored(filled[j][i].ljust(self.W),"green")
                    else:
                        menu_content+=vline+filled[j][i].ljust(self.W)
                elif w:
                    menu_content+=vline+blank
                else:
                    menu_content+=" "+blank

                if j==max_vert_size-1:
                    if w:
                        if o:
                            bottom_line+=bcline
                        else:
                            bottom_line+=bend+blank
                    elif o:
                        bottom_line+=blline
                    else:
                        bottom_line+=" "+blank

            if o:
                menu_content+=vline+"\n"
                if self.coords[-1]==j+2-top_of_menu[-1] and long_menu_item:
                    if n:
                        print_menu+="┴"+(len_cur_menu-self.W-1)*"─"+tend+"\n"
                    else: 
                        print_menu+=(len_cur_menu-self.W)*"─"+tend+"\n"
                elif self.coords[-1]==j+1-top_of_menu[-1] and long_menu_item:
                    print_menu+="┬"+(len_cur_menu-self.W-1)*"─"+bend+"\n"
                    
                elif n:
                    print_menu+=mend+"\n"
                else:
                    print_menu+=tend+"\n"
            elif n:
                if self.coords[-1]==j+1-top_of_menu[-1] and long_menu_item:
                    print_menu+=(len_cur_menu-self.W)*"─"+bend+"\n"
                else:
                    print_menu+=bend+"\n"
                menu_content+=" "+"\n"
            else:
                print_menu+=" "+"\n"
                menu_content+=" "+"\n"


            print_menu+=menu_content
        if o:
            if self.coords[-1]==max_vert_size+1-top_of_menu[-1] and long_menu_item:
                bottom_line+=(len_cur_menu-self.W)*"─"+bend
            else:
                bottom_line+=bend
        else:
            bottom_line+=" "
        
        return print_menu+bottom_line

                           



    
class HorizontalMenu(Menu):

    def __init__(self, list_of_menu_items, W):
        super().__init__(list_of_menu_items, W)
        if self.W*self.N>super().MAX_HORIZONTAL_SIZE:
            raise ValueError("Menu too large")
        
    def navigate_menu(self):
        super().navigate_menu()
        print(self.coords,self._access_menu_item(self.coords))

    def _move_up_menu(self):
        if self.coords[-1]==1:
            self._close_menu_item()
            return None
        super()._move_up_menu()

    def _generate_menu(self):
        pass

    def execute(self, *args):
        s=""
        for i in args:
            if i == -1:
                self.list_of_menu_items.reverse()
                break
            s+=str(self.list_of_menu_items[i]) 
        print(s)
        return s
    

menu_list=[
    "Menu",[
        "1",
            ["1.1"],
            ["1.2 lalalalalala",
                ["1.2.1"],
                ["1.2.2",
                    ["1.2.2.1 lalalala"]]],
            ["1.3"]
        ],
        ["2",
            ["2.1 laaaawaaaaa"],
            ["2.2",
                ["2.2.1",
                    ["2.2.1.1"]]]
        ],
        ["3"],
        ["4lalalalalala"]
        ]
c=VerticalMenu(menu_list, 10)
c.navigate_menu()
