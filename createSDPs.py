#!/usr/bin/env python3
import fileinput, csv
checkWords = ("Signal_Name","Red_Source","Red_Video_Sender", "Red_Audio_1_Sender", "Red_Audio_2_Sender", "Red_Ancilliary_Data_Sender","Blue_Source","Blue_Video_Sender", "Blue_Audio_1_Sender", "Blue_Audio_2_Sender", "Blue_Ancilliary_Data_Sender", "Port")
# checkWords = ("SoureceName", "sourceAddressRed","multicastRed","SourceName2","multicastBlue","sourceAddressBlue","port")
replaceWords = []
csvIn = input("Pleae Enter a CSV file name in the same directory you are running this script: ")

with open(csvIn, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csvfile)
    for row in spamreader:
        # print(', '.join(row))
        replaceWords.append(row)

for sender in replaceWords: 
    # print(sender)
    # Create new SDP File
    print(sender[0])
    with fileinput.FileInput("master.sdp") as file:
        myfile = "./SDP_Files/" + sender[0] + ".sdp"
        
        with open(myfile, 'w') as fileout: 
            for line in file:
                for check, rep in zip(checkWords, sender):
                    line = line.replace(check, rep)
                fileout.write(line)
            fileout.close()
        file.close()
