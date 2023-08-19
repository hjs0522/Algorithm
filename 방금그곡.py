def solution(m, musicinfos):
    answer = ''
    m= m.replace('C#','c')
    m=m.replace('D#','d')
    m=m.replace('E#','e')
    m=m.replace('F#','f')
    m=m.replace('G#','g')
    m=m.replace('A#','a')
    max_length = 0
    for music in musicinfos:
        start,end,name,song = music.split(',')
        sh,sm=start.split(':')
        start_time= int(sh)*60+int(sm)
        eh,em = end.split(':')
        end_time = int(eh)*60+int(em)
        song = song.replace('C#','c')
        song = song.replace('D#','d')
        song =song.replace('E#','e')
        song =song.replace('F#','f')
        song =song.replace('G#','g')
        song = song.replace('A#','a')
        len_song = len(song)
        q,r = divmod(end_time-start_time,len_song)
        song = song*q + song[:r]
        if m in song:
            if len(song) > max_length:
                answer = name
                max_length = len(song)
    return "(None)" if answer==''else answer