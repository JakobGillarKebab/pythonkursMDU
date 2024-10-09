import pinboard

def anslagstavla():
    h1 = 'Extrapris på mat!'
    h2 = 'Lägenhet sökes.'
    h3 = 'Gratis hälsorådgivning.'

    while True:
        pinboard.header(h1, h2, h3)

        post = input('Nytt anslag: ')

        if post == 'exit':
            break

        h1 = h2
        h2 = h3
        h3 = post

if __name__ == '__main__':
    main()