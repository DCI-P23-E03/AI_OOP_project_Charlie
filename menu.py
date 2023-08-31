from abc import ABC, abstractmethod
import getch

class Menu(ABC):

    MAX_HORIZONTAL_SIZE=72
    MAX_VERTICAL_SIZE=36

    def __init__(self, list_of_menu_items, W):
        #self.__menu = self._generate_menu(list_of_menu_items, [1])
        self.coords=[1]
        self.W=W
        self.N=len(list_of_menu_items)-1
        self.list_of_menu_items=list_of_menu_items

    @abstractmethod    
    def _generate_menu(self, list_of_menu_items, *args):
        pass
        
    def print_menu(self):
        print(self.__menu)

    def __access_menu_item(self,lst):
        item=self.list_of_menu_items
        for i in lst:
            item=item[i]
        return item
    
    def _move_down_menu(self):
        depth=len(self.coords)
        if depth==1:
            menu_length=self.N
        else:
            menu_length=len(self.__access_menu_item(self.coords[:-1]))-1
        if self.coords[-1]<menu_length:
            self.coords[-1]+=1

    def _move_up_menu(self):
        if self.coords[-1]>1:
            self.coords[-1]-=1
        else:
            self._close_menu_item()

    def _open_menu_item(self):
        if len(self.__access_menu_item(self.coords))>1:
            self.coords.append(1)
        else:
            self.execute(*self.coords)

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
            print(self.coords,self.__access_menu_item(self.coords))



    @abstractmethod
    def execute(self, *args):
        pass

class VerticalMenu(Menu):
    
    def __init__(self, list_of_menu_items, W):
        super().__init__(list_of_menu_items, W)
        if 2*self.N>super().MAX_VERTICAL_SIZE:
            raise ValueError("Menu too large") 
        

    def execute(self, *args):
        s=""
        for i in args:
            if i == -1:
                self.list_of_menu_items.reverse()
                break
            s+=str(self.list_of_menu_items[i])
        print(s)
        return s
    
    def navigate_menu(self):
        while True:
            depth=len(self.coords)
            move=getch.getch()
            if move == "a":
                self._close_menu_item()
            if move == "s":
                self._move_down_menu()
            if move == "w":
                self._move_up_menu()
            if move == "a":
                self._close_menu_item()
            if move == "d" or move == " ":
                self._open_menu_item()
            if move.isdigit():
                self._switch_top_menu_item(int(move))
            if move=="x":
                break
            print(self.coords,self._Menu__access_menu_item(self.coords))

    def _generate_menu(self, list_of_menu_items, *args):
        pass
    
class HorizontalMenu(Menu):

    def __init__(self, list_of_menu_items, W):
        super().__init__(list_of_menu_items, W)
        if self.W*self.N>super().MAX_HORIZONTAL_SIZE:
            raise ValueError("Menu too large")
        
    def navigate_menu(self):
        super().navigate_menu()
        print(self.coords,self._Menu__access_menu_item(self.coords))

    def _generate_menu(self, list_of_menu_items, *args):
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
            ["1.2",
                ["1.2.1"],
                ["1.2.2",
                    ["1.2.2.1"]]],
            ["1.3"]
        ],
        ["2",
            ["2.1"],
            ["2.2",
                ["2.2.1",
                    ["2.2.1.1"]]]
        ],
        ["3"],
        ["4"]
        ]
c=HorizontalMenu(menu_list, 8)
c.navigate_menu()
