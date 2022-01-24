import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self, ranges, end, player):
        self.wn = tk.Tk()
        self.wn.geometry("720x480")
        self.wn.title("aMAZE-ing GUI!")

        self.ranges = ranges
        self.end = end
        self.player = player

        self.canvas = tk.Canvas(self.wn, bg="blue", height=480, width=720)
        self.canvas.grid(row=0,column=0)

    def update(self):
        inBounds = False
        for range in self.ranges:
            if range[0] < self.player[0] and range[1] > self.player[1]+10 and range[2] > self.player[2] and range[3] < self.player[3]-10:
                inBounds = True
                break
        if not inBounds:
            self.player = [355, 460, 365, 470]
        if self.end[0] < self.player[0] and self.end[1] > self.player[1]+10 and self.end[2] > self.player[2] and self.end[3] < self.player[3]-10:
            tk.messagebox.showinfo("YOU WON!", "CONGRATS")
            self.wn.destroy()
        self.canvas.delete("all")
        self.drawMap()
        self.drawEnd()
        self.drawPlayer()


    def drawMap(self):
        for range in self.ranges:
            self.canvas.create_rectangle(range[0], range[1], range[2], range[3], fill="white", outline="white")

    def drawEnd(self):
        self.canvas.create_rectangle(self.end[0], self.end[1], self.end[2], self.end[3], fill="black")

    def drawPlayer(self):
        self.canvas.create_rectangle(self.player[0], self.player[1], self.player[2], self.player[3], fill="red")

    def startGUI(self):
        self.drawMap()
        self.drawPlayer()
        self.drawEnd()

        self.canvas.grid(row=0,column=0)
        self.wn.mainloop()

    def checkPos(self, player, range):
        pass

    def d(self, event):
        self.player[0] += 4
        self.player[2] += 4
        self.update()

    def a(self, event):
        self.player[0] -= 4
        self.player[2] -= 4
        self.update()

    def s(self, event):
        self.player[1] += 4
        self.player[3] += 4
        self.update()

    def w(self, event):
        self.player[1] -= 4
        self.player[3] -= 4
        self.update()

if __name__ == "__main__":
    global playing
    playing = True
    # the maze
    ranges = [
        [300, 480, 420, 400],
        [350, 420, 370, 360],
        [270, 380, 370, 360],
        [270, 420, 290, 200],
        [240, 270, 400, 250],
        [390, 265, 410, 245],
        [395, 260, 425, 230],
        [410, 245, 430, 100]
    ]
    end = [410, 130, 430, 100]
    player = [355, 460, 365, 470]
    gui = GUI(ranges, end, player)
    gui.wn.bind('<d>', gui.d)
    gui.wn.bind('<w>', gui.w)
    gui.wn.bind('<a>', gui.a)
    gui.wn.bind('<s>', gui.s)
    gui.startGUI()
