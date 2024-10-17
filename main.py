from objet.CArreraReturnToolKit import*

def main():
    screen = Tk()
    arreraToolKit = CArreraReturnToolKit("debugConf.json")
    arreraToolKit.active()
    screen.mainloop()

if __name__ == "__main__":
    main()