#Define the server class
#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load_amount in self.connections.values():
            total += load_amount
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#
#Create a server and add a connection
server = Server()
server.add_connection("192.168.1.1")

print(server.load())
#Should output between 1 and 10

#close the connection 
server.close_connection("192.168.1.1")
print(server.load())
#Should output 0


#Begin Portion 2#
#Create the load balancer class
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server
        # Add the connection to the server
        server.connections[connection_id] = True

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # IE: find the server value connected with the connection_id key in self.connections
        connection_server = self.connections[connection_id]
        i = self.servers.index(connection_server)
        # Close the connection on the server
        del self.servers[i].connections[connection_id]
        # Remove the connection from the load balancer
        del self.connections[connection_id]
        

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total = 0
        for server in self.servers: 
            total += server.load()
        avg = total / len(self.servers)
        return avg

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#


    #Create a load balancer and add a connection
l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

#Add a server: the average load will be cut in half 
l.servers.append(Server())
print(l.avg_load())

#Close connection
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

# Add lots of connections! 
for connection in range(20):
    l.add_connection(connection)
print(l)
#Check that the average load does not exceed 50% 
print(l.avg_load())









