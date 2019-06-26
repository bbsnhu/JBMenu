class JBMenu:
    def __init__(self, username, menuList, style='double'):
        self.style = style
        self.menuList = menuList
        self.username = username
        self.max_width = 40
        self.greeting = 'Welcome, ' + self.username

    def show(self):
        d_div_set = ['╔', '╗', '╝', '╚', '═', '║']
        s_div_set = ['┌', '┐', '┘', '└', '─', '│']
        div_set = d_div_set
        if self.style == 'single':
            div_set = s_div_set
        print(div_set[0]+div_set[4] * (self.max_width-2) + div_set[1])
        print(div_set[5]+self.greeting.center(self.max_width-2) + div_set[5])
        print(div_set[3]+div_set[4] * (self.max_width-2) + div_set[2])
        for i, j in enumerate(self.menuList, 1):
            print("  " + div_set[5] + " " + str(i) + ': ' + j)
        print(div_set[0]+div_set[4] * (self.max_width-2) + div_set[1])
        print(
            div_set[5]+"Press 'q' to quit..".center(self.max_width-2) + div_set[5])
        print(div_set[3]+div_set[4] * (self.max_width-2) + div_set[2])


testList = ["Menu Item One",
            "Menu Item Two",
            "Menu Item Three",
            "Menu Item Four",
            "Menu Item Five"]
