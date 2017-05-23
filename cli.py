##CS171 FINAL PROJECT
##TIMOTHY KWONG
##DENNIS FONG
##
##CLI IMPLEMENTATION

MYID = '11111'

ports = [None] * 4
for i in range(4):
    ports[i] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ##ports[0] = map1
    ##ports[1] = map2
    ##ports[0] = reducer
    ##ports[1] = prm/replicator

def setup():
    while True:
        try:
            ports[0].connect((MYID, 5001))
            break
        except Exception:
            pass
    while True:
        try:
            ports[1].connect((MYID, 5002))
            break
        except Exception:
            pass
    while True:
        try:
            ports[2].connect((MYID, 5003))
            break
        except Exception:
            pass
    while True:
        try:
            ports[3].connect((MYID, 5004))
            break
        except Exception:
            pass

def query_print():
    while True:
        try:
            ports[3].sendall('!PRINT!')
            break
        except Exception:
            pass

def query_total(pos1, pos2):
    pos_string = str(pos1) + ' ' + str(pos2)
    while True:
        try:
            ports[3].sendall('!TOTAL! ' + pos_string)
            break
        except Exception:
            pass

def query_merge(

def total(pos1, pos2):
    total_count = 0
    fpos1 = open(pos1, 'r')
    fpos2 = open(pos2, 'r')
    for line in fpos1:
        word = line.split()
        total_count = total_count + int(word[1])
    for line in fpos2:
        word = line.split()
        total_count = total_count + int(word[1])
    return total_count

def merge(pos1, pos2):
    fpos1 = open(pos1, 'r')         #LINE FORMAT: [word] [count]
    fpos2 = open(pos2, 'r')
    output = {}
    for line in fpos1:
        word = line.split()
        if word[0] == 'filename':
            pass
        elif word[0] not in output:   #NEW INSTANCE OF WORD
            output[word[0]] = int(word[1])
        else:                       #WORD ALREADY EXISTS
            output[word[0]] = output[word[0]] + int(word[1])
    for line in fpos2:
        word = line.split()
        if word[0] == 'filename':
            pass
        if word[0] not in output:   #NEW INSTANCE OF WORD
            output[word[0]] = int(word[1])
        else:                       #WORD ALREADY EXISTS
            output[word[0]] = output[word[0]] + int(word[1])
    for index in output:
        print index + ': ' + str(output[index])


