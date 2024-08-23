# Record Start and End Time
import sys, os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from modal import Image, gpu
import modal
import sys, os
sys.path.append(os.path.abspath( '..'))
from modal import Image
import uaimodal
def main():
    import time

    startTime = time.time()


    from uaimodal.utils import rootPath
    from uaimodal.api import firebase
    it = rootPath
    print(it)
    print(firebase.db)
    # image = uaimodal.initUAIContainer("testToKill-01", "3.11", "usher.json")

    # mod = uaimodal.UAIModalImage()


    endTime = time.time()

    print("Time to StartUp: ", endTime - startTime)


if __name__ == "__main__":
    main()