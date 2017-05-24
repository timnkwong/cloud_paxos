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
port_nums = [5001, 5002, 5003, 5004]

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

def cli_main(arg):
    message = arg
    if (arg == 'map'):
        process_map(sys.argv[2])
        return
    elif (arg == 'reduce'):
        for i in range(2, len(sys.argv)):
            if(i < len(sys.argv) - 1):
                message = message + sys.argv[i] + ','
            else:
                message = message + sys.argv[i]
        process_reduce(message)
        return
    elif (arg == 'replicate'):
        message = message + ',' + sys.argv[2]
    elif (arg == 'stop'):
        pass
    elif (arg == 'resume'):
        pass
    elif (arg == 'total'):
        for i in range(2, len(sys.argv)):
            if(i < len(sys.argv) - 1):
                message = message + sys.argv[i] + ','
            else:
                message = message + sys.argv[i]    
        query_total(in_str)
    elif (arg == 'print'):
        pass
    elif (arg == 'merge'):
        message = message + ',' + sys.argv[2] + ',' + sys.argv[3]
    else:
        print 'Invalid argument!'
        return
    while True:
        try:
            ports[3].sendall(message)
            break
        except Exception:
            pass

##########################

def replicate(filename):
## placeholders for code referencing ##
    PRM_logs = {} 
    PRM_logs[log_number] = {}       ##log_number = whichever log the file is stored in order
    PRM_logs[log_number]['words'] = {}
    PRM_logs[log_number]['name'] = filename
## end of placeholders ##
    for line in filename:
        word = line.split()[0]      #word
        wc = int(line.split()[1])   #word count
        if word in PRM_logs[filename]['words']:     #word already exists in logged dict
            PRM_logs[log_number]['words'][word] = PRM_logs[filename]['words'][word] + wc 
        else:                                       #word doens't exist, add it
            PRM_logs[log_number]['words'][word] = wc
    rep_log = PRM_logs[log_number]
    #send rep_log to other PRMs to replicate
    
            
##########################

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

def print_log():
    for filename in logs:
        print filename

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


