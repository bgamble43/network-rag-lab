# Network Routing Standards

## Static Routes
- Always specify next-hop IP.
- Primary static routes use AD 1.
- Backup static routes use AD 10.
- Example:
  ```
  ip route 0.0.0.0 0.0.0.0 10.1.1.1
  ip route 0.0.0.0 0.0.0.0 10.2.2.2 10
  ```
## Sticky Routes
 - Always add glue.
