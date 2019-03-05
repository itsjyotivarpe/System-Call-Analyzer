// socket problem
//http://stackoverflow.com/questions/3026858/segfault-possibly-due-to-casting/3026874#3026874
// basic setup
int sockfd;
char str[INET_ADDRSTRLEN];
sockaddr* sa;
socklen_t* sl;
struct addrinfo hints, *servinfo, *p;
int rv;
memset(&hints, 0, sizeof hints);
hints.ai_family = AF_UNSPEC;
hints.ai_socktype = SOCK_DGRAM;

// return string
string foundIP;

// setup the struct for a connection with selected IP
if ((rv = getaddrinfo("4.2.2.1", NULL, &hints, &servinfo)) != 0) {
    fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rv));
    return "1";
}

// loop through all the results and make a socket
for(p = servinfo; p != NULL; p = p->ai_next) {
    if ((sockfd = socket(p->ai_family, p->ai_socktype,
            p->ai_protocol)) == -1) {
        perror("talker: socket");
        continue;
    }

    break;
}

if (p == NULL) {
    fprintf(stderr, "talker: failed to bind socket\n");
    return "2";
}

// connect the UDP socket to something
connect(sockfd, p->ai_addr, p->ai_addrlen); // we need to connect to get the systems local IP

// get information on the local IP from the socket we created
getsockname(sockfd, sa, sl);

// convert the sockaddr to a sockaddr_in via casting
struct sockaddr_in *sa_ipv4 = (struct sockaddr_in *)sa;

// get the IP from the sockaddr_in and print it
inet_ntop(AF_INET, &(sa_ipv4->sin_addr), str, INET_ADDRSTRLEN);
printf("%s\n", str);

// return the IP
return foundIP;

}
