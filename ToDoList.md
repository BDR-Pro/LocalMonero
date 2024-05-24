# Bitcoin Testnet RPC Configuration

## ToDo List

### Step 1: Update `bitcoin.conf`

Use the following commands to open and edit the `bitcoin.conf` file:

```bash
mkdir -p ~/.bitcoin
nano ~/.bitcoin/bitcoin.conf
```

Add the following content to `bitcoin.conf`:

```conf
testnet=1
server=1
rpcuser=admin
rpcpassword=admin
rpcallowip=0.0.0.0/0
rpcbind=0.0.0.0
```

### Step 2: Create `requirements.txt`

Use the following commands to create a `requirements.txt` file:

```bash
nano requirements.txt
```

Add the following content to `requirements.txt`:

```txt
requests
```

### Step 3: Create `README.md`

Use the following commands to create a `README.md` file:

```bash
nano README.md
```

Add the following content to `README.md`:

```markdown
# Bitcoin Testnet RPC Configuration

This setup configures a Bitcoin testnet node to allow external RPC access.

## Steps to Setup

1. Update `bitcoin.conf` with the provided configuration.
2. Ensure the Bitcoin node is running and accessible.
3. Verify firewall rules to allow port `18332`.

## Requirements

Install required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Verify Monero RPC is Running

To verify if Monero RPC is running, use the following command:

```bash
curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
```

If you receive a valid JSON response, Monero RPC is running correctly.

### Summary Commands

1. **Edit `bitcoin.conf`:**

   ```bash
   mkdir -p ~/.bitcoin
   nano ~/.bitcoin/bitcoin.conf
   ```

   Add the following content:

   ```conf
   testnet=1
   server=1
   rpcuser=admin
   rpcpassword=admin
   rpcallowip=0.0.0.0/0
   rpcbind=0.0.0.0
   ```

2. **Create `requirements.txt`:**

   ```bash
   nano requirements.txt
   ```

   Add the following content:

   ```txt
   requests
   ```

3. **Create `README.md`:**

   ```bash
   nano README.md
   ```

   Add the following content:

   ```markdown
   # Bitcoin Testnet RPC Configuration

   This setup configures a Bitcoin testnet node to allow external RPC access.

   ## Steps to Setup

   1. Update `bitcoin.conf` with the provided configuration.
   2. Ensure the Bitcoin node is running and accessible.
   3. Verify firewall rules to allow port `18332`.

   ## Requirements

   Install required Python packages:

   ```bash
   pip install -r requirements.txt

   ```

4. **Verify Monero RPC is Running:**

   ```bash
   curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
   ```

By following these steps, you will have a properly configured Bitcoin testnet node, necessary dependencies listed in `requirements.txt`, and a concise `README.md` file with setup instructions.
