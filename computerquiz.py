def main():
    print("*** Kuiz Komputer ***") # Memaparkan tajuk

    playing = input("Adakah anda berminat untuk sertai kuiz ini? Taip 'ya' untuk teruskan atau 'tidak' untuk keluar:  ")

    if playing.lower() != "ya": # Penggunaan .lower akan menukarkan secara automatik kepada huruf kecil
        quit()

    print("\nOkay! Jom kita mulakan ;)")
    score = 0 # Set untuk pemarkahan/jawapan yang betul

    answer = input("\nCPU adalah singkatan bagi - ")
    if answer.lower() == "central processing unit":
       print('Tahniah! Jawapan anda betul ;)')
       score += 1

    else:
      print('Jawapan anda salah :(')

    answer = input("\nGPU adalah singkatan bagi - ")
    if answer.lower() == "graphic processing unit":
        print('Tahniah! Jawapan anda betul ;)')
        score += 1

    else:
        print('Jawapan anda salah :(')

    answer = input("\nRAM adalah singkatan bagi - ")
    if answer.lower() == "random access memory":
        print('Tahniah! Jawapan anda betul ;)')
        score += 1

    else:
       print('Jawapan anda salah :(')

    answer = input("\nGUI adalah singkatan bagi - ")
    if answer.lower() == "graphical user interface":
        print('Tahniah! Jawapan anda betul ;)')
        score += 1

    else:
       print('Jawapan anda salah :(')

    answer = input("\nPerisian apakah yang digunakan untuk menaip laporan dan teks? ")
    if answer.lower() == "microsoft word" or "word":
      print('Tahniah! Jawapan anda betul ;)')
      score += 1

    else:
      print('Jawapan anda salah :(')

    answer = input("\nROM adalah singkatan bagi - ")
    if answer.lower() == "read only memory":
        print('Tahniah! Jawapan anda betul ;)')
        score += 1

    else:
       print('Jawapan anda salah :(')

    jum = (score / 6) * 100 # Penggiraan peratus bagi jumlah jawapan yang betul

    # Memaparkan output - jumlah soalan yang dijawab dengan betul & peratus
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("\n\tAnda telah menjawab " + str(score) + " soalan dengan betul!")
    print("\tMarkah anda ialah " , round(jum,2) , " %")
    print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")

main()
