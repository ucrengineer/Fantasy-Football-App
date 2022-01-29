import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import psycopg2 
import pandas.io.sql as psql
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np


class LoginScreen(tk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.password = tk.StringVar()
        self.username = tk.StringVar()
        self.confirmation = tk.StringVar()
        self.confirmation.set('Submit')
       # self.img = PhotoImage(file='football.gif')
       # self.background = ttk.Label(self, image =self.img)

        self.user_label = ttk.Label(self,text='Username:')
        self.user_login = ttk.Entry(self,textvariable=self.username)
        self.pass_label = ttk.Label(self,text='Password:')
        self.user_password = ttk.Entry(self,textvariable=self.password,show='*')
        self.submit_button = ttk.Button(self,textvariable=self.confirmation,command=self.verify)
        self.help = ttk.Label(self, text='email ucrengineerpy@gmail.com to reset username/password')
    
       # self.background.pack()
        self.user_label.pack()
        self.user_login.pack()
        self.pass_label.pack()
        self.user_password.pack()
        self.submit_button.pack()
        self.help.pack()
        print('LoginScreen')
    """Main Function"""
    def verify(self):
        if self.username.get() == 'admin':
            if self.password.get() ==  'admin':
                self.confirmation.set('Loading..')
                LoginScreen.answer(self)
                LoginScreen.clear_screen(self)
                LoginScreen.newscreen(self)
                LoginScreen.Load_team_data(self)
                LoginScreen.Load_player_data(self)
                LoginScreen.Choose_Teams(self)

                """Make ComboBoxes"""
                

            else:
                self.confirmation.set('Wrong password')
        else:
            self.confirmation.set('Wrong username')
            
    def answer(self):
        print('hi')

    def clear_screen(self):
        #self.background.pack_forget()
        self.user_label.pack_forget()
        self.user_login.pack_forget()
        self.pass_label.pack_forget()
        self.user_password.pack_forget()
        self.submit_button.pack_forget()
        self.help.pack_forget()

    def newscreen(self):
        label = ttk.Label(self,text='Choose two(2) Teams',font=90)
        label.pack()
        
 
    def Load_team_data(self):
        try:
       DB_NAME = "db"
            DB_USER = "dbname"
            DB_PASS = "dbpass"
            DB_HOST = "raja.db.elephantsql.com"
            DB_PORT = "port#"

            self.conn_team = psycopg2.connect(database = DB_NAME, user = DB_USER,
                            password=DB_PASS, host= DB_HOST,port=DB_PORT)
            print('Team load successfull')
        except:
            print('Error connecting to database')
        #notice = ttk.Label(self,text='Team database connected successfully',font=90)
        #notice.pack()
        

    def Load_player_data(self):
        try:
            
       DB_NAME = "db"
            DB_USER = "dbname"
            DB_PASS = "dbpass"
            DB_HOST = "raja.db.elephantsql.com"
            DB_PORT = "port#"

            self.conn_player = psycopg2.connect(database = DB_NAME, user = DB_USER,
                            password=DB_PASS, host= DB_HOST,port=DB_PORT)
            print('Player load successfull')
        #notice_2 = ttk.Label(self,text='Player database connected successfully',font=90)
        #notice_2.pack()
        except:
            print('Error with connecting to database')

    def Choose_Teams(self):
        self.logic = 'True'
        self.team_1 = tk.StringVar()
        self.team_2 = tk.StringVar()
        

        self.name_teams = ['ARI','ATL','BAL','BUF','CAR','CHI','CIN','CLE','DAL','DEN','DET','GB','HOU','IND',\
                      'JAX','KC','LAC','LAR','MIA','MIN','NE','NO','NYG','NYJ','OAK','PHI','PIT',\
                      'SEA','SF','TB','TEN','WAS'] 

        combobox_team_1 = ttk.Combobox(self,textvariable=self.team_1,values=self.name_teams)
        combobox_team_1.pack()
        combobox_team_2 = ttk.Combobox(self,textvariable=self.team_2,values=self.name_teams)
        combobox_team_2.pack()
        
        Done = ttk.Button(self,text='Show Team Stats',command=self.graph_team)
        Done.pack()
     



    def graph_team(self):
        
        self.Load_team_data()

        df_1 = psql.read_sql("SELECT * FROM fantasy_points_allowed\
        WHERE team = '{}'".format(self.team_1.get()), self.conn_team)
        
        df_2 = psql.read_sql("SELECT * FROM fantasy_points_allowed\
        WHERE team = '{}'".format(self.team_2.get()), self.conn_team)
        
        
        self.qb_ranks_1 = df_1['qb_rank']
        self.rb_ranks_1 = df_1['rb_rank']
        
        self.qb_ranks_2 = df_2['qb_rank']
        self.rb_ranks_2 = df_2['rb_rank']
        
        
        self.rbppr_ranks_1 = df_1['rbppr_rank']
        self.rbppr_ranks_2 = df_2['rbppr_rank']
        
        
        self.wr_ranks_1 = df_1['wr_rank']
        self.wr_ranks_2 = df_2['wr_rank']
        
        self.wrppr_ranks_1 = df_1['wrppr_rank']
        self.wrppr_ranks_2 = df_2['wrppr_rank']
        
        self.te_ranks_1 = df_1['te_rank']
        self.te_ranks_2 = df_2['te_rank']
        
        self.teppr_ranks_1 = df_1['teppr_rank']
        self.teppr_ranks_2 = df_2['teppr_rank']
        
        self.def_ranks_1 = df_1['def_ranks']
        self.def_ranks_2 = df_2['def_ranks']
        
        self.dfl_1 = df_1['dfl']
        self.dfl_2 = df_2['dfl']
        
        self.ofl_1 = df_1['ofl']
        self.ofl_2 = df_2['ofl']
        
        self.short_1 = df_1['short']
        self.short_2 = df_2['short']
        
        self.deep_1 = df_1['deep']
        self.deep_2 = df_2['deep']

        self.off_pace_1 = df_1['off_pace']
        self.off_pace_2 = df_2['off_pace']
      

        bar_width = .35   
        fig = Figure(figsize=(7,6),dpi=100)
        self.top_fig = tk.Toplevel()
        t = np.arange(13)
        team1 = (int(self.qb_ranks_1),int(self.rb_ranks_1),int(self.rbppr_ranks_1),int(self.wr_ranks_1),\
                int(self.wrppr_ranks_1),int(self.te_ranks_1),int(self.teppr_ranks_1),int(self.def_ranks_1),\
                int(self.dfl_1),int(self.ofl_1),int(self.short_1),int(self.deep_1),int(self.off_pace_1))
        team2 = (int(self.qb_ranks_2),int(self.rb_ranks_2),int(self.rbppr_ranks_2),int(self.wr_ranks_2),\
                int(self.wrppr_ranks_2),int(self.te_ranks_2),int(self.teppr_ranks_2),int(self.def_ranks_2),\
                int(self.dfl_2),int(self.ofl_2),int(self.short_2),int(self.deep_2),int(self.off_pace_2))
                 
        fig.add_subplot(111).bar(t,team1,bar_width,alpha = .4,color='b')          
        fig.add_subplot(111).bar(t+bar_width,team2,bar_width,alpha = .4,color = 'r')       
        self.canvas = FigureCanvasTkAgg(fig,master = self.top_fig)
        self.canvas.draw()
        fig.add_subplot(111).set_xticks(t + bar_width / 2)
        fig.add_subplot(111).tick_params(axis='x', which='major',labelsize=10,labelrotation=45)
        fig.add_subplot(111).set_xticklabels(['QB','RB','RB-PPR','WR','WR-PPR','TE','TE-PPR','DEF','DFL','OFL','SHORT','DEEP','OFF. PACE'])
        fig.add_subplot(111).set_ylabel("Rank")
        fig.add_subplot(111).set_title("Team's Fantasy Football Points Allowed & Offensive Pace")
        fig.add_subplot(111).legend([self.team_1.get(),self.team_2.get()])
        
        self.canvas.get_tk_widget().pack()#grid(row=3,column=1,sticky=(tk.E+tk.W+tk.N+tk.S))
        #self.columnconfigure(1,weight=1)
        #self.rowconfigure(3,weight=1)
        
        if self.logic == 'True':
            player_activate = ttk.Button(self,text="Search Players",command=self.player_search_app)
            player_activate.pack()

        self.logic = 'false'
        self.conn_team.close()
    def player_search_app(self): 
        
        """Player Search Application"""
        self.team_choice = tk.StringVar()
        self.pos_choice = tk.StringVar()
        
        label_pos = ttk.Label(self,text="Choose Team and Position",font=20)
        combobox_team_plyr = ttk.Combobox(self,textvariable=self.team_choice,values=self.name_teams)
        pos_button = ttk.Combobox(self,textvariable=self.pos_choice,values = ['QB','RB','WR','TE'])
        search = ttk.Button(self,text="Seach",command=self.show_player)
       
        label_pos.pack()
        combobox_team_plyr.pack()
        pos_button.pack()
        search.pack()
        

    def show_player(self):
        self.Load_player_data()
        players_list = tk.StringVar()

        player_data = psql.read_sql("SELECT name,team,pos,tchs_atts FROM nfl_player\
        WHERE pos= '{0}' AND team = '{1}'".format(self.pos_choice.get(),self.team_choice.get()),self.conn_player)   
        
        players_list = player_data.head()
        players = ttk.Label(self,text=players_list)
        players.pack()

        

        self.conn_player.close()

        


       

      
class MyApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("800x750")
        self.title("Fantasy Football Winner")
        LoginScreen(self).pack()
      
        





if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
