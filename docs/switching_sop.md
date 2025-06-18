# Network Switching Standards

## Static Routes
- When creating a VLAN interface and the VLAN is 1, issue no shut command at end of stanza.
- Other VLANs are enabled by default and don't need to be no shut
- Example:
  ```
  interface Vlan1
   ip address a.b.c.d w.x.y.z
   no shut
  interface Vlan2
   ip address a.b.c.d w.x.y.z
  end
  ```

