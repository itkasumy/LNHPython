def father(name):
    print('from father %s' %name)
    def son():
        print('from son')
        def grandson():
            print('from grandson...')
        grandson()
    son()

father('ksm')
