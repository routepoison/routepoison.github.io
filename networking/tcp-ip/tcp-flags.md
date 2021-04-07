# TCP Flags

__SYN__ - The synchronisation flag is used as a first step in establishing a three way handshake between two hosts. Only the first packet from both the sender and receiver should have this flag set. The following diagram illustrates a three way handshake process.

__ACK__ - The acknowledgment flag is used to acknowledge the successful receipt of a packet. As we can see from the diagram above, the receiver sends an ACK as well as a SYN in the second step of the three way handshake process to tell the sender that it received its initial packet.

__FIN__ - The finished flag means there is no more data from the sender. Therefore, it is used in the last packet sent from the sender.

__URG__ - The urgent flag is used to notify the receiver to process the urgent packets before processing all other packets. The receiver will be notified when all known urgent data has been received. See RFC 6093 for more details.

__PSH__ - The push flag is somewhat similar to the URG flag and tells the receiver to process these packets as they are received instead of buffering them.

__RST__ - The reset flag gets sent from the receiver to the sender when a packet is sent to a particular host that was not expecting it.
ECE - This flag is responsible for indicating if the TCP peer is ECN capable. See RFC 3168 for more details.

__CWR__ - The congestion window reduced flag is used by the sending host to indicate it received a packet with the ECE flag set. See RFC 3168 for more details.

__NS__ (experimental) - The nonce sum flag is still an experimental flag used to help protect against accidental malicious concealment of packets from the sender. See RFC 3540 for more details.

---

[Main Repository](../../README.md)