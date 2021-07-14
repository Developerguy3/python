'''pykill.py - selective process kill prog'''
import psutil


def main():
    while 1:
        '''Process kill function'''
        for proc in psutil.process_iter():
            # check whether the process name matches
            # print(proc.name())
            if any(procstr in proc.name() for procstr in \
                   ['Adobe XD', 'CCXProcess', 'Mail', 'CoreSync', 'Creative Cloud', 'Your Phone', 'Films & TV', 'Cortana', 'YourPhoneServer' ,'Alarms & Clock']):
                print(f'Killing {proc.name()}')
                proc.kill()


if __name__ == "__main__":
    main()
