class Stats:
    def __init__(self):
        self.player1shot=0
        self.player1hit=0
        self.player2shot=0
        self.player2hit=0
        if self.player1shot!=0:
            self.player1acc=self.player1hit/self.player1shot
        if self.player2shot!=0:
            self.player2acc=self.player2hit/self.player2shot
        self.player1health=0
        self.player2health=0
        self.player1manaspent=0
        self.player2manaspent=0
        self.player1spec=0
        self.player2spec=0