# Lesson 3: Spanning Tree

## 3.1 Introduction to Spanning Tree Protocol (STP)

Spanning Tree Protocol (STP) is a Layer 2 protocol with multiple modes:

* 802.1D, which is the original specification
* Per-VLAN Spanning Tree (PVST)
* Per-VLAN Spanning Tree Plus (PVST+)
* 802.1W Rapid Spanning Tree Protocol (RSTP)
* 802.1S Multiple Spanning Tree Protocol (MST)

Catalyst Switches operate in PVST+, RSTP, and MST modes. All three of these modes are backward compatible with 802.1D.

__Bridge protocol data unit (BPDU)__: STP packets that are used by switches to identify a hierarchy and notify of changes in the STP topology

* A BPDU uses the destionation MAC address __01:80:c2:00:00:00__
* __Configuration BPDU__: Used to build the STP topology by identifying the root bridge, root ports, designated ports, and blocking ports. Contains the following fields:
    + STP type, root path cost, root bridge identifier, local bridge identifier, max age, hello time, and forward delay
* __Topology change notification (TCN) BPDU__: Used to communicate changes in the Layer 2 topology to other switches

### Key Terms

* __Root Bridge__: The root bridge is the top of the spanning tree for all path calculations by other switches. All ports art in a forwarding state.
* __Root Port (RP)__: The network port that connects directly to the root bridge or to a switch that conects to the root bridge.
* __Designated Port (DP)__: A network port that receives and forwards BPDU frames to other switches. A DP provides connectivity to downstream switches. All ports on the root bridge are categorized as designated ports. There should only be one DP on a link.
* __Blocking port__: A port that is not forwarding traffic because of STP calculations.

![STP Example](./img/stp.png)

### Key Terms Contd.

![Bridge Identifier](./img/bridge-identifier.png)

* __System priority__: This is a 4-bit value that indicates the preference for a switch to be the root bridge. The default value is 32,768. Increments in valued of 4,096
* __System ID extension__: This 12-bit value identifies the VLAN that the BPDU correlates to. The system priority and system ID extension are combined.
* __Local bridge identifier__: This is a combination of the local switch's bridge system MAC address, system ID extension, and system priority of the local bridge.
* __Root bridge identifier__: This is a combination of the root bridge system MAC address, system ID extension, and system priority of the root bridge.

#### 802.1D Port States

* __Disabled__: The port is shut down
* __Blocking__: The ports only receives BPDUs, but does not modify MAC table or forward packets
* __Listening__: The port can now send or receive BPDUs. It cannot forward any other network traffic.
    - Stays in this state for the duration of STP forwarding time (15s)
* __Learning__: The port can now modify the MAC address table with any network traffic that it receives.
    - Stays in this state for the duration of the STP forwarding time (15s)
* __Forwarding__: The switch port can forward all network traffic and can update the MAC address table as expected
* __Broken__: The switch has detected a configuration problem.

## 3.2 Building STP Topology

The STP Topology is calculated in the following fashion:

1. Elect the root bridge
2. Identify the Root Port (RP)
3. Locate designated ports (DP)
4. Identify which DP will change to a blocking state

### Root Bridge Election

* Upon initialization the switch thinks that it is the root bridge.
* Will receive configuration BPDUs from other switches and compare them against itself.
    + If the neighbor's BPDU is inferior, it ignores the BPDU.
    + If the neighbor's BPDU is preferred, it will advertise the neighbor's Bridge Identifier in the root bridge identifier of the BPDUs it will advertise
* The switch's system priority is compared first. Lower value is more preferred.
* If there is a tie, then the switch with lower system MAC address is preferred.
* Election process with a third switch.
* Election has already occurred between two switches. The root bridge MAC and priority is included in the BPDUs by all member switches.

### Root Port Selection

The downstream switches select their root port based on:

1. The interface associated to lowest root path cost is more preferred. The root path cost is the cost associated to the path taken to reach the root bridge.
2.The interface associated to the lowest system priority of the advertising switch is preferred next.
3. The interface associated to the lowest system MAC address of the advertising switch is preferred next.
4. When multiple links are associated to the same switch, the lowest port priority from the advertising switch is preferred.
5. When multiple link are associated to the same switch, the lower port number from the advertising switch is preferred.

### Locate Designated Ports

After the root bridge and RPs have been identified, all other ports are considered designated ports.

However, if two non-root switches are connected to each other on their designated ports, one of those switch ports must be set to a blocking state to prevent a forwarding loop

Blocking ports are identified based on the following logic:

1. The interface is a designated port and must not be considered a RP
2. The switch with the lower path cost to the root bridge forwards packets, and the one with the higher path cost blocks.
3. The system priority of the local switch is compared to the system priority of the remote switch. The local port is moved to a blocking state if the remote system priority is lower than that of the local switch.
4. The system MAC address of the local switch is compared to the system MAC of the remote switch. The local designated port is moved to a blocking state if the remote system MAC address is lower than that of the local switch.

## 3.3 Per VLAN Spanning Tree (PVST) and PVST+

### Limitations of 802.1D

* Original 802.1D supported only one STP topology for the entire switch network. Also referre to as Common Spanning Tree (CST).
* Does not allow the manipulation of the Layer 2 topology for specific VLANs that deviate from the CST. Prevents optimal flow or load-balancing based on traffic patterns.

### Per VLAN Spanning-Tree

* Per-VLAN Spanning Tree (PVST)
* Per-VLAN Spanning Tree Plus (PVST+)

> show spanning-tree

You can also add a VLAN ID:

> show spanning-tree [vlan _vlan-id_]

You can also get detailed output:

> show spanning-tree detail [vlan _vlan-id_]


## 3.4 STP Convergence

## 3.5 Rapid Spanning Tree Protocol (RSTP)

## 3.6 Tuning the STP Topology

## 3.8 Optimizing the Spanning Tree Topology

## Multiple Spanning Tree Protocool (MSTP)

---

[Back to main Repo](../../../README.md)

[Back to Safari Books](./../README.md)

[Previous Lesson: Switch Operations](./L2_switch-operations.md)

[Next Lesson: EtherChannel](./L4_Etherchannel.md)
