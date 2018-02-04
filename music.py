import subprocess as sb

def loadMPD():
    try:
        print (sb.check_output(['mpd']))
    except sb.CalledProcessError as e:
        pass

def setMusic():
    p = sb.Popen(['mpc','-q', 'load'], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT)
    sb.check_output(['mpc','clear'])
    grep_stdout = p.communicate(input=b'retro.m3u')[0]
    print (grep_stdout.decode())
    sb.check_output(['mpc','-q', 'shuffle'])
    sb.check_output(['mpc','-q', 'play'])

def pauseMusic(switch):
    if(switch):
        sb.check_output(['mpc','-q','pause'])
    else:
        sb.check_output(['mpc', '-q', 'play'])

def nextSong():
    sb.check_output(['mpc', '-q', 'next'])
    
def prevSong():
    sb.check_output(['mpc', '-q', 'prev'])

def terminateMusic():
    sb.check_output(['mpc', 'clear'])
    sb.check_output()['mpd', '--kill']
