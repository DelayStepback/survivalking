from resources.game import Game
import resources.client_ as client

g = Game()

if __name__ == '__main__':
    while g.running:

        if not g.playing:
            g.curr_menu.display_menu()

        if g.playing:
            try:
                client.main(g.your_ip, int(g.your_port))
            except client.ClientExcept:
                g.lost_connection = True
                g.playing = False
            g.playing = False