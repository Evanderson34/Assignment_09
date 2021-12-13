#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Evan Anderson, 2021-Dec-12, Completed unfinished methods
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        print()
        if strYesNo.lower() == 'yes':
            print('Reloading...\n')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info() # Returns CD input data as tuple
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects) # Assigns tuple values to attributes of new CD object and appends CD object to CD object list
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects) # Shows list of CD Objects
        cd_idx = input('Select the CD / Album index: ') # User inputs CD based on ID
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx) # CD is selected from CD object list based on ID
        while True:
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x':
                break
            elif strChoice == 'a':
                tplTrkInfo = IO.ScreenIO.get_track_info() # Returns track input data as tuple
                PC.DataProcessor.add_track(tplTrkInfo, cd) # Assigns tuple values to attributes of newly created track object and appends track object to the corresponding CD object's track list
                print()
            elif strChoice == 'd':
                IO.ScreenIO.show_tracks(cd) # Displays the selected CD objects track list
            elif strChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                trk_idx = input('Select the Track index: ')
                cd.rmv_track(trk_idx) # removes track from CD object based on inputed ID
            else:
               print('General Error')
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')