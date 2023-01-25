import sshtunnel
import creds as creds

class SSHTunnel:
    def __enter__(self):
        if os.environ.get('ENV') == 'development':
            self.my_tunnel = sshtunnel.SSHTunnelForwarder((creds.ip, creds.port),
                                                            ssh_username=creds.username,
                                                            ssh_private_key=creds.private_key,
                                                            ssh_private_key_password=creds.passphrase,
                                                            remote_bind_address=('localhost', 3306))
            self.my_tunnel.start()
            self.local_bind_port = self.my_tunnel.local_bind_port
            return self
        elif os.environ.get('ENV') == 'production':
            self.my_tunnel = None
            self.local_bind_port = '3306'
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.environ.get('ENV') == 'development':
            self.my_tunnel.stop()


# In your code
with SSHTunnel() as tunnel:
  ...
  ...
