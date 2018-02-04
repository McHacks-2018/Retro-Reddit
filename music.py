import subprocess as sb

def playMusic():
    try:
        print (sb.check_output(['mpd']))
    except sb.CalledProcessError as e:
        pass
    p = sb.Popen(['mpc','-q', 'load'], stdout=sb.PIPE, stdin=sb.PIPE, stderr=sb.STDOUT)    
    # Create m3u file and replace with mpc load
    # Come back to point file later
    sb.check_output(['mpc','clear'])
    grep_stdout = p.communicate(input=b'retro.m3u')[0]
    print (grep_stdout.decode())
    sb.check_output(['mpc','-q', 'shuffle'])
    sb.check_output(['mpc','-q', 'play'])

def stopMusic():
    print (sb.check_output(['mpc', 'clear']))
