import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server


def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    print(ch1, ch2, ch3, ch4)
    print("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")
    parser.add_argument("--port",
                        type=int,
                        default=7000,
                        help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/debug", print)
    dispatcher.map("/elements/alpha_absolute", eeg_handler , "ALPHA_ABSOLUTE") 
    
    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
