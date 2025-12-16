from time import sleep
class Timer:
    
    def __init__(self, format, start, end, direction):
        self.format = format
        start_split = start.split(':')
        end_split = end.split(':')
        self.direction = direction
        self.start_hh = int(start_split[0])
        self.start_mm = int(start_split[1])
        self.start_ss = int(start_split[2])
        self.end_hh = int(end_split[0])
        self.end_mm = int(end_split[1])
        self.end_ss = int(end_split[2])
        

    def display_time(self):
        sep = ':' if self.format == 'hh:mm:ss' else '.'
        print(f"{self.cur_hh:02d}{sep}{self.cur_mm:02d}{sep}{self.cur_ss:02d}")

    def shrink_time(self):
        self.cur_ss -= 1
        if self.cur_ss == -1:
            self.cur_ss = 59
            self.cur_mm -=1
        if self.cur_mm == -1:
            self.cur_mm = 59
            self.cur_hh -= 1
        if self.cur_hh == -1:
            self.cur_hh = 23

    def expand_time(self):
        self.cur_ss += 1
        if self.cur_ss == 60:
            self.cur_ss = 0
            self.cur_mm +=1
        if self.cur_mm == 60:
            self.cur_mm = 0
            self.cur_hh += 1
        if self.cur_hh == 24:
            self.cur_hh = 0

    #fix 59->0 0->59
    def countdown(self):
        ##total_seconds = (self.end_hh - self.start_hh)*3600 + (self.end_mm - self.start_mm)*60 + (self.end_ss - self.start_ss)
        start_total = self.start_hh*3600 + self.start_mm*60 + self.start_ss
        end_total   = self.end_hh*3600   + self.end_mm*60   + self.end_ss
        total_seconds = abs(end_total - start_total)
        print(f'Starting the timer ({total_seconds} seconds)')
        if self.direction.lower() == 'up':
            self.cur_hh = self.start_hh
            self.cur_mm = self.start_mm
            self.cur_ss = self.start_ss
            self.target_hh = self.end_hh
            self.target_mm = self.end_mm
            self.target_ss = self.end_ss
            while not (self.cur_hh == self.target_hh and
                       self.cur_mm == self.target_mm and
                       self.cur_ss == self.target_ss):
                self.expand_time()
                sleep(1)
                self.display_time()
            print('Finish counting up')
        elif self.direction.lower() == 'down':
            self.cur_hh = self.end_hh
            self.cur_mm = self.end_mm
            self.cur_ss = self.end_ss
            self.target_hh = self.start_hh
            self.target_mm = self.start_mm
            self.target_ss = self.start_ss
            while not (self.cur_hh == self.target_hh and
                       self.cur_mm == self.target_mm and
                       self.cur_ss == self.target_ss):
                self.shrink_time()
                sleep(1)
                self.display_time()
            print('Finish counting down')
                
    def start(self):
        self.countdown()

t = Timer('hh:mm:ss', '22:33:55', '22:34:10', "up")
t.start()