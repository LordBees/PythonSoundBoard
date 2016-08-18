import os,sys
from pygame import mixer
from tkinter import *
#from winsound import *

cwd = os.getcwd()

class SoundHandler:##add music handler to allow for sfx to be played over mus## EDIT nearly done this.2:37,18/08/2016
    mixer.init()
    formatlist = ['.ogg','.wav','.mp3']
    LoadedTracks = []
    Music_FLAG = False
    LoadedSound = mixer.Sound
    LoadedTrack =  mixer.music

    def __init__(self):
        self.SLoad()##setup for auto getting tracks for init
    ##get sounds
    def resetpath(self):
        os.chdir(cwd)
    def Get_Loaded(self):
        return self.LoadedTracks
    def Get_tracks(self):
        global cwd
        os.chdir('DATA')
        validfiles = []
        for x in os.listdir():
            if x[-4:] in self.formatlist:
                validfiles.append(x)
        os.chdir(cwd)
        return validfiles
    
    def SLoad(self):
        self.LoadedTracks = self.Get_tracks()
    def Clearloaded(self):##clear tracks
        self.LoadedTracks = []

    ##pygame mixer
    def LoadSND(self,sDAT):
        self.Music_FLAG = False
        self.LoadedSound = mixer.Sound('DATA//'+str(sDAT))
    def PlaySND(self):
        if self.LoadedSound == None:# or self.Music_FLAG == True:
            pass
        else:
            mixer.Sound.play(self.LoadedSound)
    def StopSND(self):
        if self.LoadedSound == None:# or self.Music_FLAG == True:
            pass
        else:
            #mixer.Sound.stop()
            self.LoadedSound.stop()
            
    def LoadMUS(self,mDAT):
        self.Music_FLAG = True
        #self.LoadedSound = mixer.music
        self.LoadedTrack.load('DATA//'+str(mDAT))
    def PlayMUS(self,TIMES= -1):
        if self.LoadedTrack == None:# or self.Music_FLAG == False:
            print('track MUS is None!')
        else:
            self.LoadedTrack.play(TIMES)
    def StopMUS(self):
        if self.LoadedTrack == None:# or self.Music_FLAG == False:
            print('track MUS is None!')
        else:
            self.LoadedTrack.stop()
    def PausMUS(self):
        if self.LoadedTrack == None:# or self.Music_FLAG == False:
            print('track MUS is None!')
        else:
            self.LoadedTrack.pause()
    def UpausMUS(self):
        if self.LoadedTrack == None:# or self.Music_FLAG == False:
            print('track MUS is None!')
        else:
            self.LoadedTrack.unpause()
    def TS(self):
        self.SLoad()
        self.LoadSND(self.LoadedTracks[1])
        self.PlaySND()
    def TM(self):
        self.SLoad()
        self.LoadMUS((self.LoadedTracks[0]))
        self.PlayMUS()
        
        
class Board_main():
    win = Tk()
    ##vars
    opt_CTK_MUS = StringVar()
    opt_CTK_SFX = StringVar()
    opt_MUS_VOL = DoubleVar()

    opt_CTK_SFX.set('Current SFX:')
    opt_CTK_MUS.set('Current track:')

    sel_LF = LabelFrame(win,text = 'Browse Files')
    scrollbar = Scrollbar(sel_LF)
    scrollbar.pack( side = RIGHT, fill=Y )
    sound_list_Listbox = Listbox(sel_LF,yscrollcommand = scrollbar.set )
    scrollbar.config( command = sound_list_Listbox.yview )
    sel_LF.pack()

    def __init__(self):
        #win = Tk()
        self.win.geometry('640x480')
        self.win.title('D&D Soundboard - BEES')
        
        load_data_Button = Button(self.win,text = 'Load',command = self.ldB).pack()
        #self.sound_list_Listbox = Listbox(self.win).pack()
        self.sound_list_Listbox.pack()
        #self.sound_list_Listbox.insert(END,'ttt')

        opt_LB = LabelFrame(self.win,text = 'playback options')
        opt_MUS_LB = LabelFrame(opt_LB,text = 'music playback')
        opt_SFX_LB = LabelFrame(opt_LB,text = 'effect playback')
        opt_play_CTK_MUS_Label  = Label (opt_LB,textvariable = self.opt_CTK_MUS).pack()##current track MUS
        opt_play_CTK_SFX_Label  = Label (opt_LB,textvariable = self.opt_CTK_SFX).pack()##current track SFX
        opt_play_SFX_Button = Button(opt_SFX_LB,text = 'PLAY as SFX',command = self.SFX_play).pack()
        opt_play_MUS_Button = Button(opt_MUS_LB,text = 'PLAY as MUS',command = self.MUS_play).pack()
        opt_play_STP_ALL_Button = Button(opt_LB,text = 'STOP-ALL',command = self.STOPPLAY).pack()
        opt_play_STP_SFX_Button = Button(opt_SFX_LB,text = 'STOP-SFX',command = self.STOPSFX).pack()
        opt_play_STP_MUS_Button = Button(opt_MUS_LB,text = 'STOP-MUS',command = self.STOPMUS).pack()
        opt_play_PUS_Button = Button(opt_MUS_LB,text = 'PAUSE',command = self.PMUS).pack()
        opt_play_UPS_Button = Button(opt_MUS_LB,text = 'UNPAUSE',command = self.UPMUS).pack()
        opt_MUS_VOL_SC =  Scale(opt_MUS_LB, variable = self.opt_MUS_VOL ).pack()
        opt_LB.pack()
        opt_MUS_LB.pack()
        opt_SFX_LB.pack()
        ##post init loads
        self.ldB()##for initial listbox population
        #TkLoop
        self.win.after(1000,self.EVENT_ALT_LOOP)
        self.win.mainloop()
        
    def clearLB(self):
        self.sound_list_Listbox.delete(0,self.sound_list_Listbox.size())
    def insertLB(self,data,ARRAY = True):##array of items
        for x in data:
            self.sound_list_Listbox.insert(END,x)
    def insertposLB(self,data,ARRAY = True):
        pass##not implemented
    def RefreshLB(self,data):
        self.clearLB()
        self.insertLB(data)
    ## button procedures    
    def ldB(self):##load data Button ##refreshes list and array
##        h.TS()
##        self.clearLB()
        h.SLoad()
        self.RefreshLB(h.Get_Loaded())
    def SFX_play(self):
        track = self.getLBsel()
        self.opt_SFX_updatelabel(track)
        h.LoadSND(track)
        h.PlaySND()
    def MUS_play(self):
        track = self.getLBsel()
        self.opt_MUS_updatelabel(track)
        h.LoadMUS(track)
        h.PlayMUS()
    def STOPPLAY(self):
        ##if h.LoadedSound.get_busy() == True:
##        if h.Music_FLAG == True:
##            h.StopMUS()
##        else:
##            h.StopSND()
        try:
            h.StopMUS()
        except:
            print('failed stopping snd')
        try:
            h.StopSND()
        except:
            print('failed stopping snd')
        
##        h.StopSND()
##        h.StopMUS()
    def STOPSFX(self):
        h.StopSND()
    def STOPMUS(self):
        h.StopMUS()
    def PMUS(self):
        #if h.Music_FLAG == True:
        h.PausMUS()
    def UPMUS(self):
        #if h.Music_FLAG == True:
        h.UpausMUS()
            
    ###playback button related functions
    def opt_SFX_clearlabel(self):
        self.opt_CTK_SFX.set('')
    def opt_SFX_insertlabel(self,data):
        self.opt_CTK_SFX.set(str(data))
    def opt_SFX_updatelabel(self,data):
        self.opt_SFX_clearlabel()
        self.opt_CTK_SFX.set('Current SFX:\n'+str(data))
    def xt_SFX(self):
        self.opt_SFX_updatelabel('test')
        print(self.opt_CTK_SFX.get())

    def opt_MUS_clearlabel(self):
        self.opt_CTK_MUS.set('')
    def opt_MUS_insertlabel(self,data):
        self.opt_CTK_MUS.set(str(data))
    def opt_MUS_updatelabel(self,data):
        self.opt_MUS_clearlabel()
        self.opt_CTK_MUS.set('Current track:\n'+str(data))
    def xt_MUS(self):
        self.opt_updatelabel('test')
        print(self.opt_CTK_MUS.get())
    def getLBsel(self):
        try:
            sel = self.sound_list_Listbox.get(self.sound_list_Listbox.curselection())
        except:
            sel = None
        if sel == None:
            return [0]
        else:
            return sel
    ###END playback functions########
    ##misc functions
    def getsounds(self):
        pass
    def no(self):## null function
        pass
    
    def EVENT_ALT_LOOP(self):##custom event loop
        ##event code here##

        ##volume slider check
        if h.LoadedTrack == None:# or self.Music_FLAG == False:
            print('track MUS is None vol not adjustable!')
        else:
            h.LoadedTrack.set_volume((self.opt_MUS_VOL.get()/100))
        ##
        ##END EVENT CODE##
        self.win.after(500, self.EVENT_ALT_LOOP)

##functions/procs
def Fcheck():##fs integrity checker
    if os.path.isdir('DATA'):
        pass
    else:
        print('|creating DATA folder')
        os.mkdir('DATA') 
##init
####
Fcheck()
#mixer.init()
h = SoundHandler()        
##tkloop
print('starting win')
win_B = Board_main()
#Board_main = Tk()

#Board_main.mainloop()
##end
