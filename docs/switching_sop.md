# Network Switching Standards

## Static Routes
- When creating a VLAN interface and the VLAN is 1, issue no shut command at end of stanza.
- Any VLAN other than VLAN 1 should have proxy arp disabled.
- Example:
  ```
  interface Vlan1
   ip address a.b.c.d w.x.y.z
   no shut
  interface Vlan2
   ip address a.b.c.d w.x.y.z
  end
  ```

