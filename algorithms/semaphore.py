import threading
from enum import Enum
import time
from colorama import Fore


class SemaphoreState(Enum):
    GREEN = 5
    YELLOW = 3
    RED = 6


class Semaphore:
    _running: bool
    _current: SemaphoreState
    _name: str

    def __init__(self, name):
        self._name = name
        self._running = False

    def change_state(self, state: SemaphoreState):
        self._current = state
        color = Fore.GREEN if state == SemaphoreState.GREEN \
            else Fore.YELLOW if state == SemaphoreState.YELLOW \
            else Fore.RED
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} :: {color}{self._name} changed to {self._current.name}{Fore.RESET}")

    def start(self, config):
        self._running = True
        self._current = list(config.keys())[0]
        threading.Thread(target=self._run, args=(config,)).start()

    def _run(self, config):
        while self._running:
            for state, duration in config.items():
                self.change_state(state)
                time.sleep(duration)

    def stop(self):
        self._running = False


class SemaphoreCross:
    _cross: Semaphore
    _main: Semaphore

    def __init__(self):
        self._main = Semaphore('Main')
        self._cross = Semaphore('Cross')

    def start(self):
        print('Starting...')
        main_config = dict({
            SemaphoreState.GREEN: 5,
            SemaphoreState.YELLOW: 3,
            SemaphoreState.RED: 6,

        })
        cross_config = dict({
            SemaphoreState.RED: 6,
            SemaphoreState.GREEN: 5,
            SemaphoreState.YELLOW: 3
        })
        self._main.start(main_config)
        self._cross.start(cross_config)

    def stop(self):
        print('Stopping...')
        self._main.stop()
        self._cross.stop()
        print('Stopped')


if __name__ == '__main__':
    cross = SemaphoreCross()
    cross.start()
    time.sleep(30)
    cross.stop()
