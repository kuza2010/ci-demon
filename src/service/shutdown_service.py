def close_service(pid_provider):
    print('Shutdown hook')
    pid_provider().kill_all()
    print('Shutdown hook completed!')
